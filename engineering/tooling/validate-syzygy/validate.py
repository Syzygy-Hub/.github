#!/usr/bin/env python3
"""Validate syzygy.yml manifests against engineering/schema/syzygy.schema.json.

Standard library only. PyYAML is NOT required. Limitation: the built-in YAML reader
handles the subset used by Syzygy manifests (top-level keys, one level of nested
mappings, block lists of scalars or mappings, inline [a, b] lists, quoted or plain
scalars, and trailing comments). Anchors, multi-line scalars and flow mappings are
not supported and will be read as plain strings or raise a parse error.

Schema support is a subset of JSON Schema draft 2020-12: type, enum, const, pattern,
required, properties, not, allOf, if/then/else, items.

Example apps (type: example) are validated by the same schema. The example-only
fields `demonstrates` (list of layer names) and `depends_on` (list of mappings with
`name` and `version_constraint`) are declared in the schema, so they are checked
without special-case code here. The schema forbids them on any non-example type.

Usage:
  validate.py [--report-only] [--schema PATH] FILE [FILE ...]

Exit status:
  --report-only: always 0 (prints PASS / WARN / FAIL).
  otherwise:     1 if any file is FAIL, else 0.
"""

import argparse
import json
import os
import re
import sys

DEFAULT_SCHEMA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "schema", "syzygy.schema.json"
)

# Legacy keys accepted with a warning, mapped to the canonical key.
LEGACY_KEY_MAP = {"layer": "type", "foundation": "syzygy_foundation"}
LEGACY_DEPENDENCY_PREFIX = "syzygy_"  # syzygy_core, syzygy_ui, ... (not syzygy_foundation)


# ---------------------------------------------------------------- YAML subset

_KV_RE = re.compile(r"^[A-Za-z_][\w-]*\s*:(\s|$)")


def _strip_comment(line):
    out = []
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _scalar(text):
    text = text.strip()
    if text == "":
        return None
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    if text in ("true", "false"):
        return text == "true"
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_scalar(part) for part in inner.split(",")]
    return text


def _lines(text):
    out = []
    for raw in text.splitlines():
        if raw.strip() in ("", "---", "..."):
            continue
        stripped = _strip_comment(raw)
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        out.append([indent, stripped.strip()])
    return out


def _parse_block(lines, i, indent):
    if i >= len(lines):
        return None, i
    first = lines[i][1]
    if first == "-" or first.startswith("- "):
        result = []
        while i < len(lines):
            ind, txt = lines[i]
            if ind != indent or not (txt == "-" or txt.startswith("- ")):
                break
            item = txt[1:].strip()
            if item == "":
                i += 1
                sub, i = _parse_block(lines, i, lines[i][0] if i < len(lines) and lines[i][0] > indent else indent + 2)
                result.append(sub)
            elif _KV_RE.match(item):
                lines[i] = [indent + 2, item]
                sub, i = _parse_block(lines, i, indent + 2)
                result.append(sub)
            else:
                result.append(_scalar(item))
                i += 1
        return result, i
    result = {}
    while i < len(lines):
        ind, txt = lines[i]
        if ind != indent or txt == "-" or txt.startswith("- "):
            break
        key, _, rest = txt.partition(":")
        key = key.strip()
        rest = rest.strip()
        i += 1
        if rest == "":
            if i < len(lines) and lines[i][0] > indent:
                sub, i = _parse_block(lines, i, lines[i][0])
                result[key] = sub
            else:
                result[key] = None
        else:
            result[key] = _scalar(rest)
    return result, i


def parse_manifest(text):
    lines = _lines(text)
    if not lines:
        return {}
    data, _ = _parse_block(lines, 0, lines[0][0])
    if not isinstance(data, dict):
        raise ValueError("manifest root is not a mapping")
    return data


# ---------------------------------------------------------------- schema check

def _check(instance, schema, path="$"):
    errors = []
    if "const" in schema and instance != schema["const"]:
        errors.append("%s: expected %r" % (path, schema["const"]))
    t = schema.get("type")
    if t:
        checks = {
            "object": isinstance(instance, dict),
            "array": isinstance(instance, list),
            "string": isinstance(instance, str),
            "boolean": isinstance(instance, bool),
        }
        if not checks.get(t, True):
            return ["%s: expected type %s" % (path, t)]
    if "enum" in schema and instance not in schema["enum"]:
        errors.append("%s: %r is not one of %s" % (path, instance, schema["enum"]))
    if "pattern" in schema and isinstance(instance, str):
        if not re.search(schema["pattern"], instance):
            errors.append("%s: %r does not match pattern %s" % (path, instance, schema["pattern"]))
    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errors.append('%s: missing required field "%s"' % (path, req))
        for key, sub in schema.get("properties", {}).items():
            if key in instance:
                errors.extend(_check(instance[key], sub, "%s.%s" % (path, key)))
    if isinstance(instance, list) and "items" in schema:
        for idx, item in enumerate(instance):
            errors.extend(_check(item, schema["items"], "%s[%d]" % (path, idx)))
    if "not" in schema and not _check(instance, schema["not"], path):
        errors.append("%s: must not match %s" % (path, json.dumps(schema["not"])))
    for sub in schema.get("allOf", []):
        errors.extend(_check(instance, sub, path))
    if "if" in schema:
        matched = not _check(instance, schema["if"], path)
        branch = "then" if matched else "else"
        if branch in schema:
            errors.extend(_check(instance, schema[branch], path))
    return errors


# ---------------------------------------------------------------- normalise

def normalise(data):
    """Return (data, warnings). Maps legacy keys to canonical keys and reports them."""
    warnings = []
    data = dict(data)
    for legacy, canonical in LEGACY_KEY_MAP.items():
        if legacy in data:
            warnings.append('legacy key "%s": use "%s"' % (legacy, canonical))
            if canonical not in data:
                data[canonical] = data[legacy]
    for key in list(data):
        if key.startswith(LEGACY_DEPENDENCY_PREFIX) and key != "syzygy_foundation":
            warnings.append('legacy dependency key "%s": use dependencies list' % key)
    deps = data.get("dependencies")
    if "syzygy_foundation" not in data and isinstance(deps, list):
        for dep in deps:
            if isinstance(dep, dict) and str(dep.get("name", "")).startswith("syzygy-foundation-"):
                data["syzygy_foundation"] = dep.get("version")
                warnings.append("foundation constraint given in dependencies; use syzygy_foundation")
                break
    if "contracts" in data and isinstance(data["contracts"], list) and data["contracts"] and \
            isinstance(data["contracts"][0], dict):
        warnings.append("contracts uses name/version objects; the canonical form is a list of names")
    return data, warnings


def validate_file(path, schema):
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as exc:
        return "FAIL", ["cannot read file: %s" % exc]
    try:
        data = parse_manifest(text)
    except ValueError as exc:
        return "FAIL", ["parse error: %s" % exc]
    data, warnings = normalise(data)
    errors = _check(data, schema)
    if errors:
        return "FAIL", errors + warnings
    if warnings:
        return "WARN", warnings
    return "PASS", []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report-only", action="store_true",
                        help="print results and always exit 0 (use in CI)")
    parser.add_argument("--schema", default=DEFAULT_SCHEMA, help="path to syzygy.schema.json")
    parser.add_argument("files", nargs="+", help="syzygy.yml paths (quote paths containing spaces)")
    args = parser.parse_args(argv)

    with open(args.schema, encoding="utf-8") as handle:
        schema = json.load(handle)

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for path in args.files:
        status, issues = validate_file(path, schema)
        counts[status] += 1
        print("%s  %s" % (status, path))
        for issue in issues:
            print("      - %s" % issue)
    print("SUMMARY PASS=%d WARN=%d FAIL=%d" % (counts["PASS"], counts["WARN"], counts["FAIL"]))

    if args.report_only:
        return 0
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
