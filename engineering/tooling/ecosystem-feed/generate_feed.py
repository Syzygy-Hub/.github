#!/usr/bin/env python3
"""Build the Syzygy ecosystem feed (ecosystem/feed.json) from the syzygy.yml manifests.

Standard library only. The repo list is ecosystem/repos.json. Each manifest is read either
from a local checkout (--source local --local-root DIR) or from the public raw URL
https://raw.githubusercontent.com/<owner>/<repo>/<ref>/syzygy.yml (--source raw, the default).
Only manifest data plus the repo list are used. Nothing is inferred beyond that.

Output is deterministic: no timestamps, fixed key order, fixed list order.

Usage:
  generate_feed.py [--source raw|local] [--local-root DIR] [--repos FILE] [--output FILE]

Exit status: 0 on success, 2 if any repo could not be read or parsed, or the feed is invalid.
"""

import argparse
import importlib.util
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

HUB_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DEFAULT_REPOS = os.path.join(HUB_ROOT, "ecosystem", "repos.json")
DEFAULT_FEED = os.path.join(HUB_ROOT, "ecosystem", "feed.json")
VALIDATE_PY = os.path.join(HUB_ROOT, "engineering", "tooling", "validate-syzygy", "validate.py")

FEED_SCHEMA = "syzygy-ecosystem-feed/1"
GENERATED_FROM = "syzygy.yml files"
LAYER_ORDER = ["foundation", "ui", "core", "services", "ai", "base"]
PLATFORM_ORDER = ["ios", "android", "rn", "flutter"]
LAYER_LABEL = {"foundation": "Foundation", "ui": "UI", "core": "Core", "services": "Services",
               "ai": "AI", "base": "Base"}
PLATFORM_LABEL = {"ios": "iOS", "android": "Android", "rn": "React Native", "flutter": "Flutter"}
HUB_LAYER = "hub"
HUB_PLATFORM = "none"

SEMVER_RE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
NAME_RE = re.compile(r"^syzygy-([a-z]+)-([a-z]+)$")


class FetchError(Exception):
    pass


def _load_yaml_subset():
    """Reuse the subset YAML reader from the validator instead of copying it."""
    spec = importlib.util.spec_from_file_location("syzygy_validate", VALIDATE_PY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parse_manifest


parse_manifest = _load_yaml_subset()


def load_repo_list(path):
    with open(path, encoding="utf-8") as handle:
        doc = json.load(handle)
    for key in ("owner", "ref", "repos", "hub"):
        if key not in doc:
            raise ValueError("%s: missing key %r" % (path, key))
    return doc


def _http_get(url):
    last = "unknown error"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise FetchError("HTTP 404 at %s (missing, or the repo is private)" % url)
            last = "HTTP %d" % exc.code
        except (urllib.error.URLError, OSError) as exc:
            last = str(exc)
        if attempt < 2:
            time.sleep(2 * (attempt + 1))
    raise FetchError("%s: %s" % (url, last))


def read_manifest_text(item, source, local_root, owner, ref):
    if source == "local":
        if not local_root:
            raise FetchError("--local-root is required with --source local")
        path = os.path.join(local_root, item["path"], "syzygy.yml")
        try:
            with open(path, encoding="utf-8") as handle:
                return handle.read()
        except OSError as exc:
            raise FetchError("cannot read %s: %s" % (path, exc))
    url = "https://raw.githubusercontent.com/%s/%s/%s/syzygy.yml" % (owner, item["repo"], ref)
    return _http_get(url)


def _str_or_none(value, where, errors):
    if value is None or isinstance(value, str):
        return value
    errors.append("%s: expected a string, got %r" % (where, value))
    return None


def _repo_object(item, data, owner, errors):
    """Map one parsed manifest onto the feed repo object. Appends to errors on conflict."""
    repo = item["repo"]
    if not data:
        errors.append("%s: manifest parsed to no fields" % repo)
        return None

    name = data.get("name")
    if name is not None and name != repo:
        errors.append("%s: manifest name %r does not match repo list" % (repo, name))

    declared_type = data.get("type", data.get("layer"))  # legacy key "layer"
    if declared_type is not None and declared_type != item["layer"]:
        errors.append("%s: manifest type %r does not match repo list layer %r"
                      % (repo, declared_type, item["layer"]))

    platform = data.get("platform")
    if platform is not None and platform != item["platform"]:
        errors.append("%s: manifest platform %r does not match repo list platform %r"
                      % (repo, platform, item["platform"]))

    version = _str_or_none(data.get("version"), repo + ": version", errors)
    if version is not None and not SEMVER_RE.match(version):
        errors.append("%s: version %r is not bare strict semver" % (repo, version))
        version = None

    # Foundation constraint: canonical key, then legacy key "foundation", then a dependencies entry.
    syzygy_foundation = data.get("syzygy_foundation", data.get("foundation"))
    syzygy_foundation = _str_or_none(syzygy_foundation, repo + ": syzygy_foundation", errors)

    constraints = {}
    for key, value in data.items():
        if key.startswith("syzygy_") and key != "syzygy_foundation":
            constraints[key[len("syzygy_"):]] = value

    deps = data.get("dependencies")
    if isinstance(deps, list):
        for dep in deps:
            if not isinstance(dep, dict) or "name" not in dep:
                continue
            match = NAME_RE.match(str(dep["name"]))
            if not match:
                continue
            layer_key, value = match.group(1), dep.get("version")
            if layer_key == "foundation":
                syzygy_foundation = syzygy_foundation or _str_or_none(value, repo + ": dependency", errors)
            else:
                constraints[layer_key] = value
    elif isinstance(deps, dict):
        for layer_key, value in deps.items():
            if isinstance(value, dict):
                value = value.get("version")
            if layer_key == "foundation":
                syzygy_foundation = syzygy_foundation or _str_or_none(value, repo + ": dependency", errors)
            else:
                constraints[layer_key] = value

    clean = {}
    for layer_key, value in constraints.items():
        if layer_key not in LAYER_ORDER or layer_key == "foundation":
            errors.append("%s: unknown dependency constraint key %r" % (repo, layer_key))
            continue
        if value is None:
            continue
        if not isinstance(value, str):
            errors.append("%s: constraint for %s is not a string" % (repo, layer_key))
            continue
        clean[layer_key] = value
    ordered_constraints = {k: clean[k] for k in LAYER_ORDER if k in clean}

    return {
        "name": repo,
        "type": item["layer"],
        "version": version,
        "status": "shipped" if version is not None else "unknown",
        "language": _str_or_none(data.get("language"), repo + ": language", errors),
        "package_manager": _str_or_none(data.get("package_manager"), repo + ": package_manager", errors),
        "syzygy_foundation": syzygy_foundation,
        "dependency_constraints": ordered_constraints,
        "license": _str_or_none(data.get("license"), repo + ": license", errors),
        "repo_url": "https://github.com/%s/%s" % (owner, repo),
        "ci_workflow": None,
        "release_workflow": None,
    }


def build_feed(doc, source, local_root=None):
    """Return (feed, errors). feed is None when errors is non-empty."""
    errors = []
    owner, ref = doc["owner"], doc["ref"]

    entries = {}
    for item in doc["repos"]:
        layer, platform = item.get("layer"), item.get("platform")
        if layer not in LAYER_ORDER or platform not in PLATFORM_ORDER:
            errors.append("repo list: bad layer/platform for %r" % item.get("repo"))
            continue
        if (layer, platform) in entries:
            errors.append("repo list: duplicate %s/%s" % (layer, platform))
            continue
        entries[(layer, platform)] = item
    expected = len(LAYER_ORDER) * len(PLATFORM_ORDER)
    if len(entries) != expected:
        errors.append("repo list: expected %d platform repos, found %d" % (expected, len(entries)))

    repo_objects = {}
    for key, item in entries.items():
        try:
            text = read_manifest_text(item, source, local_root, owner, ref)
        except FetchError as exc:
            errors.append("%s: %s" % (item["repo"], exc))
            continue
        try:
            data = parse_manifest(text)
        except Exception as exc:  # the subset reader raises ValueError or IndexError on bad input
            errors.append("%s: syzygy.yml could not be parsed: %s" % (item["repo"], exc))
            continue
        obj = _repo_object(item, data, owner, errors)
        if obj is not None:
            repo_objects[key] = obj

    if errors:
        return None, errors

    layers = []
    for layer in LAYER_ORDER:
        platforms = []
        for platform in PLATFORM_ORDER:
            platforms.append({"platform": platform, "repos": [repo_objects[(layer, platform)]]})
        layers.append({"layer": layer, "platforms": platforms})

    hub_repo = doc["hub"]["repo"]
    hub = {
        "name": "hub",
        "type": HUB_LAYER,
        "version": None,
        "status": "unknown",
        "language": None,
        "package_manager": None,
        "syzygy_foundation": None,
        "dependency_constraints": {},
        "license": None,
        "repo_url": "https://github.com/%s/%s" % (owner, hub_repo),
        "ci_workflow": None,
        "release_workflow": None,
    }
    layers.append({"layer": HUB_LAYER, "platforms": [{"platform": HUB_PLATFORM, "repos": [hub]}]})

    feed = {"schema": FEED_SCHEMA, "generated_from": GENERATED_FROM, "layers": layers}
    return feed, []


def feed_text(feed):
    """Canonical serialisation. check_drift.py compares against this exact text."""
    return json.dumps(feed, indent=2, ensure_ascii=False) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", choices=["raw", "local"], default="raw")
    parser.add_argument("--local-root", help="directory containing the platform checkouts (local mode)")
    parser.add_argument("--repos", default=DEFAULT_REPOS)
    parser.add_argument("--output", help="write the feed here; default is stdout")
    args = parser.parse_args(argv)

    try:
        doc = load_repo_list(args.repos)
    except (OSError, ValueError) as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2

    feed, errors = build_feed(doc, args.source, args.local_root)
    if errors:
        print("ERROR: could not build feed (%d issue(s)):" % len(errors), file=sys.stderr)
        for err in errors:
            print("  - %s" % err, file=sys.stderr)
        return 2

    text = feed_text(feed)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
