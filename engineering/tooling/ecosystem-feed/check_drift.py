#!/usr/bin/env python3
"""Check (or with --write, regenerate) the Syzygy ecosystem feed and its README tables.

Checks, in order:
  1. Regenerate the feed in memory from ecosystem/repos.json and the syzygy.yml manifests.
  2. Validate the regenerated feed against engineering/schema/ecosystem-feed.schema.json.
  3. Compare the regenerated feed with the committed ecosystem/feed.json (exact text).
  4. For each file in DOC_FILES, render the version table from the feed and compare it with
     the text between <!-- ECOSYSTEM:START --> and <!-- ECOSYSTEM:END -->.

--write rewrites ecosystem/feed.json and the marker blocks. The CI workflow never uses --write.
Run it locally, then review and commit the result.

Standard library only. Schema validation is a subset of JSON Schema draft 2020-12:
type, enum, const, pattern, required, properties, additionalProperties, propertyNames,
items, minItems and local $ref. Conditional keywords are not checked here; the
regeneration compare in step 3 covers the status/version rule.

Usage:
  check_drift.py [--source raw|local] [--local-root DIR] [--write]

Exit status: 0 in sync (or written), 1 drift found, 2 the feed could not be built or the
marker blocks are missing.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_feed as gf  # noqa: E402

SCHEMA_PATH = os.path.join(gf.HUB_ROOT, "engineering", "schema", "ecosystem-feed.schema.json")
DOC_FILES = ["profile/README.md", "engineering/architecture/syzygy-ecosystem.md"]
START = "<!-- ECOSYSTEM:START -->"
END = "<!-- ECOSYSTEM:END -->"


# ---------------------------------------------------------------- schema subset

def _is_type(instance, name):
    if name == "null":
        return instance is None
    if name == "object":
        return isinstance(instance, dict)
    if name == "array":
        return isinstance(instance, list)
    if name == "string":
        return isinstance(instance, str)
    if name == "boolean":
        return isinstance(instance, bool)
    if name == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if name == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    return False


def _resolve(root, ref):
    if not ref.startswith("#/"):
        raise ValueError("only local $ref is supported: %s" % ref)
    node = root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def schema_errors(instance, schema, root, path="$"):
    if "$ref" in schema:
        return schema_errors(instance, _resolve(root, schema["$ref"]), root, path)
    errors = []
    if "const" in schema and instance != schema["const"]:
        errors.append("%s: expected %r" % (path, schema["const"]))
    if "enum" in schema and instance not in schema["enum"]:
        errors.append("%s: %r is not one of %s" % (path, instance, schema["enum"]))
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_is_type(instance, t) for t in types):
            return errors + ["%s: expected type %s" % (path, "/".join(types))]
    if isinstance(instance, str) and "pattern" in schema:
        if not re.search(schema["pattern"], instance):
            errors.append("%s: %r does not match %s" % (path, instance, schema["pattern"]))
    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errors.append('%s: missing required key "%s"' % (path, req))
        props = schema.get("properties", {})
        for key, value in instance.items():
            if "propertyNames" in schema:
                errors.extend(schema_errors(key, schema["propertyNames"], root, path + " (key)"))
            if key in props:
                errors.extend(schema_errors(value, props[key], root, "%s.%s" % (path, key)))
            elif "additionalProperties" in schema:
                extra = schema["additionalProperties"]
                if extra is False:
                    errors.append('%s: unexpected key "%s"' % (path, key))
                elif isinstance(extra, dict):
                    errors.extend(schema_errors(value, extra, root, "%s.%s" % (path, key)))
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append("%s: fewer than %d items" % (path, schema["minItems"]))
        if "items" in schema:
            for idx, item in enumerate(instance):
                errors.extend(schema_errors(item, schema["items"], root, "%s[%d]" % (path, idx)))
    return errors


# ---------------------------------------------------------------- rendering

def render_block(feed):
    """Return the text placed between the markers (without the markers themselves)."""
    lines = [
        "<!-- Generated from ecosystem/feed.json by engineering/tooling/ecosystem-feed/check_drift.py. Do not edit by hand. -->",
        "| Layer | " + " | ".join(gf.PLATFORM_LABEL[p] for p in gf.PLATFORM_ORDER) + " |",
        "|---|" + "---|" * len(gf.PLATFORM_ORDER),
    ]
    hub = None
    for layer in feed["layers"]:
        if layer["layer"] == gf.HUB_LAYER:
            hub = layer["platforms"][0]["repos"][0]
            continue
        cells = {}
        for plat in layer["platforms"]:
            repo = plat["repos"][0]
            cells[plat["platform"]] = "%s (%s)" % (repo["version"], repo["status"])
        row = [gf.LAYER_LABEL[layer["layer"]]] + [cells[p] for p in gf.PLATFORM_ORDER]
        lines.append("| " + " | ".join(row) + " |")
    if hub is not None:
        version = hub["version"] if hub["version"] is not None else "not recorded"
        lines.append("")
        lines.append("Hub repository (`%s`): version %s, status %s." % (hub["repo_url"].split("/")[-1], version, hub["status"]))
    return "\n".join(lines)


def block_region(text):
    """Return (start, end) character offsets of the marker pair, or (None, message)."""
    starts = [m.start() for m in re.finditer(re.escape(START), text)]
    ends = [m.start() for m in re.finditer(re.escape(END), text)]
    if len(starts) != 1 or len(ends) != 1 or ends[0] < starts[0]:
        return None, "expected exactly one %s followed by one %s" % (START, END)
    return (starts[0], ends[0] + len(END)), None


def expected_region(feed):
    return START + "\n" + render_block(feed) + "\n" + END


# ---------------------------------------------------------------- drift detail

def _flatten(feed):
    out = {}
    for layer in feed.get("layers", []):
        for plat in layer.get("platforms", []):
            for repo in plat.get("repos", []):
                out[repo.get("name")] = repo
    return out


def feed_drift_summary(committed_text, fresh):
    try:
        committed = json.loads(committed_text)
    except ValueError:
        return ["committed ecosystem/feed.json is not valid JSON"]
    old, new = _flatten(committed), _flatten(fresh)
    notes = []
    for name in sorted(set(old) | set(new)):
        if name not in old:
            notes.append("%s: added to the repo list" % name)
        elif name not in new:
            notes.append("%s: removed from the repo list" % name)
        elif old[name] != new[name]:
            changed = [k for k in new[name] if old[name].get(k) != new[name].get(k)]
            notes.append("%s: %s differ" % (name, ", ".join(changed)))
    if not notes:
        notes.append("layer ordering or top-level fields differ")
    return notes


# ---------------------------------------------------------------- main

def _read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def _write(path, text):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", choices=["raw", "local"], default="raw",
                        help="raw: public raw URLs (CI). local: checkouts under --local-root.")
    parser.add_argument("--local-root", help="directory containing the platform checkouts (local mode)")
    parser.add_argument("--repos", default=gf.DEFAULT_REPOS)
    parser.add_argument("--feed", default=gf.DEFAULT_FEED)
    parser.add_argument("--write", action="store_true",
                        help="rewrite ecosystem/feed.json and the marker blocks (local use only)")
    args = parser.parse_args(argv)

    try:
        doc = gf.load_repo_list(args.repos)
        feed, errors = gf.build_feed(doc, args.source, args.local_root)
    except (OSError, ValueError) as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    if errors:
        print("ERROR: could not build the feed from the manifests (%d issue(s)):" % len(errors))
        for err in errors:
            print("  - %s" % err)
        print("No files were checked or written.")
        return 2

    with open(SCHEMA_PATH, encoding="utf-8") as handle:
        schema = json.load(handle)
    schema_problems = schema_errors(feed, schema, schema)
    if schema_problems:
        print("ERROR: regenerated feed fails %s:" % os.path.relpath(SCHEMA_PATH, gf.HUB_ROOT))
        for problem in schema_problems:
            print("  - %s" % problem)
        return 2

    fresh_text = gf.feed_text(feed)
    drift = []
    committed_text = _read(args.feed) if os.path.exists(args.feed) else None
    feed_rel = os.path.relpath(args.feed, gf.HUB_ROOT)
    if committed_text is None:
        drift.append("%s is missing" % feed_rel)
    elif committed_text != fresh_text:
        drift.append("%s differs from regeneration: %s" % (feed_rel, "; ".join(feed_drift_summary(committed_text, feed))))

    region_text = expected_region(feed)
    doc_status = {}
    doc_texts = {}
    for rel in DOC_FILES:
        path = os.path.join(gf.HUB_ROOT, rel)
        text = _read(path)
        region, problem = block_region(text)
        if region is None:
            doc_status[rel] = "ERROR: " + problem
            continue
        doc_texts[rel] = (path, text, region)
        if text[region[0]:region[1]] != region_text:
            doc_status[rel] = "DRIFT: marker block differs from the feed"
            drift.append("%s marker block differs from the feed" % rel)
        else:
            doc_status[rel] = "OK"

    marker_errors = [rel for rel, state in doc_status.items() if state.startswith("ERROR")]

    if args.write:
        if marker_errors:
            for rel in marker_errors:
                print("%s: %s" % (rel, doc_status[rel]))
            print("Add the markers by hand once, then run --write again. Nothing was written.")
            return 2
        if committed_text != fresh_text:
            _write(args.feed, fresh_text)
            print("WROTE %s" % feed_rel)
        for rel, (path, text, region) in doc_texts.items():
            updated = text[:region[0]] + region_text + text[region[1]:]
            if updated != text:
                _write(path, updated)
                print("WROTE marker block in %s" % rel)
        print("Done. Review the diff and commit the result.")
        return 0

    if marker_errors:
        for rel in marker_errors:
            print("%s: %s" % (rel, doc_status[rel]))
        return 2

    for rel in DOC_FILES:
        print("%s: %s" % (rel, doc_status[rel]))
    print("%s: %s" % (feed_rel, "OK" if committed_text == fresh_text else "DRIFT"))

    if drift:
        print("")
        print("ECOSYSTEM DRIFT DETECTED. The committed feed or README tables do not match the syzygy.yml manifests.")
        for item in drift:
            print("  - %s" % item)
        print("Fix: run `python3 engineering/tooling/ecosystem-feed/check_drift.py --source local --local-root <Syzygy dir> --write` locally, review the diff, and commit.")
        if os.environ.get("GITHUB_ACTIONS") == "true":
            print("::error title=Ecosystem drift::Run check_drift.py --write locally and commit the result.")
        return 1

    print("OK: feed and README tables match the manifests (%s source, %d repos)." %
          (args.source, sum(len(p["repos"]) for lay in feed["layers"] for p in lay["platforms"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
