#!/usr/bin/env python3
"""Read-only guard for the canonical Syzygy banner in Hub Markdown docs.

Two layouts are enforced:
- README-type files (root README.md, profile/README.md, engineering/templates/README-*.md):
  a header of badge lines (markdown badge images, blank lines, HTML comments such as the
  badge-options block), then the canonical banner, then the H1.
- Every other required doc: the canonical banner is the first content.

Run from the Hub root. Exits 1 and lists each failing file. It never writes.
"""
import glob
import pathlib
import sys

CANONICAL = (
    '<picture>\n'
    '  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">\n'
    '  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">\n'
    '</picture>\n'
)

README_TYPE = ["README.md", "profile/README.md"]

REQUIRED = [
    "README.md", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "profile/README.md", "brand/BRAND_GUIDE.md", ".github/workflows/README.md",
]
REQUIRED_GLOBS = ["docs/**/*.md", "engineering/**/*.md"]

# Deliberately exempt: GitHub issue/PR templates, YAML and other machine-read formats.
EXEMPT_PREFIXES = (".github/ISSUE_TEMPLATE/",)
EXEMPT_FILES = {".github/PULL_REQUEST_TEMPLATE.md"}


def required_files(root: pathlib.Path):
    found = {n for n in REQUIRED if (root / n).exists()}
    for pattern in REQUIRED_GLOBS:
        for path in glob.glob(str(root / pattern), recursive=True):
            found.add(str(pathlib.Path(path).relative_to(root)))
    return sorted(f for f in found if not f.startswith(EXEMPT_PREFIXES) and f not in EXEMPT_FILES)


def is_readme_type(rel: str, root: pathlib.Path) -> bool:
    return rel in README_TYPE or (rel.startswith("engineering/templates/README-") and rel.endswith(".md"))


def badge_header_ok(prefix: str) -> bool:
    """Prefix before the banner: badge lines, blanks and HTML comments only, with at least one badge."""
    in_comment = False
    badges = 0
    for line in prefix.split("\n"):
        s = line.strip()
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if not s:
            continue
        if s.startswith("<!--"):
            if "-->" not in s:
                in_comment = True
            continue
        if s.startswith("[![") or s.startswith("[!["):
            badges += 1
            continue
        return False
    return badges >= 1 and not in_comment


def check(rel: str, text: str, root: pathlib.Path):
    if is_readme_type(rel, root):
        idx = text.find(CANONICAL)
        if idx < 0:
            return "README-type file lacks the canonical banner"
        prefix = text[:idx]
        after = text[idx + len(CANONICAL):]
        if not badge_header_ok(prefix):
            return "README-type header must be badge lines (and comments) before the banner"
        if after.strip() == "" or not after.lstrip().startswith("#"):
            return "README-type file must have the H1 directly after the banner"
        return None
    if not text.startswith(CANONICAL):
        return "does not open with the canonical banner"
    return None


def main() -> int:
    root = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path.cwd()
    files = required_files(root)
    failures = []
    for rel in files:
        reason = check(rel, (root / rel).read_text(encoding="utf-8"), root)
        if reason:
            failures.append((rel, reason))
    for rel, reason in failures:
        print(f"FAIL {rel}: {reason}")
    print(f"banner guard: {len(files) - len(failures)}/{len(files)} required docs pass")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
