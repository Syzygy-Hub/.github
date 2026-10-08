#!/usr/bin/env python3
"""Read-only guard: every human-facing Markdown doc must open with the canonical Syzygy banner.

Run from the Hub root. Exits 1 and lists every failing file when a required doc does not start
with the canonical <picture> block. It never writes.
"""
import glob
import pathlib
import sys

CANONICAL = (
    '<picture>\n'
    '  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">\n'
    '  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">\n'
    '</picture>\n\n'
)

REQUIRED = [
    "README.md", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "profile/README.md", "brand/BRAND_GUIDE.md", ".github/workflows/README.md",
]
REQUIRED_GLOBS = ["docs/**/*.md", "engineering/**/*.md"]

# Deliberately exempt: GitHub issue/PR templates, YAML and other machine-read formats.
EXEMPT_PREFIXES = (".github/ISSUE_TEMPLATE/",)
EXEMPT_FILES = {".github/PULL_REQUEST_TEMPLATE.md"}


def required_files(root: pathlib.Path):
    found = set()
    for name in REQUIRED:
        if (root / name).exists():
            found.add(name)
    for pattern in REQUIRED_GLOBS:
        for path in glob.glob(str(root / pattern), recursive=True):
            found.add(str(pathlib.Path(path).relative_to(root)))
    return sorted(f for f in found if not f.startswith(EXEMPT_PREFIXES) and f not in EXEMPT_FILES)


def main() -> int:
    root = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path.cwd()
    failures = []
    files = required_files(root)
    for rel in files:
        text = (root / rel).read_text(encoding="utf-8")
        if not text.startswith(CANONICAL):
            failures.append(rel)
    for rel in failures:
        print(f"FAIL {rel}: does not open with the canonical banner")
    print(f"banner guard: {len(files) - len(failures)}/{len(files)} required docs pass")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
