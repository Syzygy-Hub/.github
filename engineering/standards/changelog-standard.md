<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy CHANGELOG Standard

Every Syzygy repository CHANGELOG follows the [Keep a Changelog](https://keepachangelog.com) format.

---

## File Format

```markdown
# Changelog

All notable changes to `{repo-name}` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

## [1.0.0] - YYYY-MM-DD

### Added
- Added X to Y

### Changed
- Changed X to use Y instead of Z

### Fixed
- Fixed X crashing when Y is nil

### Removed
- Removed deprecated X

[Unreleased]: https://github.com/Syzygy-Hub/{repo}/compare/1.0.0...HEAD
[1.0.0]: https://github.com/Syzygy-Hub/{repo}/releases/tag/1.0.0
```

---

## Rules

### Version Header

- Format: `[X.X.X]` — no `v` prefix
- Always followed by ` - YYYY-MM-DD`
- Most recent version at the top, below `[Unreleased]`

### [Unreleased] Section

- **Always present** at the top of the file, above all version entries — never delete it
- All in-progress changes are added here during development, before a version is assigned
- **On release:** move the contents of `[Unreleased]` into a new `[X.X.X] - YYYY-MM-DD` section, then reset `[Unreleased]` to empty above it

```markdown
## [Unreleased]

## [1.1.0] - 2026-09-01

### Added
- Added `SyzygyLogger` — structured logging contract with level filtering
```

### Sections

Include only the sections that have entries. Standard sections in order:

1. **Added** — new features, new types, new modules
2. **Changed** — changes to existing behaviour
3. **Fixed** — bug fixes
4. **Removed** — removed features, deprecated items finally dropped

Do not add custom sections. Do not add a "Known Limitations" section — fix it, defer it to a future version, or document it as a code comment. It has no place in a CHANGELOG.

### Entry Format

- One line per change
- Past tense: "Added X", "Fixed Y crashing when Z", "Removed deprecated X"
- Imperative is also acceptable for consistency with commit messages: "Add X", "Fix Y"
- Pick one style per repo and be consistent — do not mix in the same CHANGELOG

**Preferred style (Syzygy standard): past tense**

```markdown
### Added
- Added `SyzygyID<T>` — generic typed identifier wrapping a UUID-based String
- Added `NetworkClientProtocol` — async network execution contract
```

### Breaking Changes

Mark clearly at the top of the version entry:

```markdown
## [2.0.0] - 2026-09-01

> **Breaking change:** `AuthProvider.state` is now a `AnyPublisher<AuthState, Never>` — replace direct property access with `.statePublisher`.

### Changed
- Changed `AuthProvider.state` from `AuthState` to `AnyPublisher<AuthState, Never>`
```

### Reference Links

Every version entry and the `[Unreleased]` section must have a corresponding reference link at the bottom of the file. Links enable clickable version headers in rendered Markdown.

Format:

```markdown
[Unreleased]: https://github.com/Syzygy-Hub/{repo}/compare/{latest-tag}...HEAD
[1.1.0]: https://github.com/Syzygy-Hub/{repo}/releases/tag/1.1.0
[1.0.0]: https://github.com/Syzygy-Hub/{repo}/releases/tag/1.0.0
```

Rules:
- `[Unreleased]` always points to `compare/{latest-tag}...HEAD` — update the tag each time a new version is released
- Each version link points to its GitHub Release tag
- Links appear in descending version order at the bottom of the file
- No `v` prefix in tag URLs — `releases/tag/1.0.0` not `releases/tag/v1.0.0`

### What Does Not Belong in a CHANGELOG

- Internal implementation notes
- Future plans or roadmap items
- Names of contributors (not a project convention here)
- PR or issue numbers (optional — include only if they add genuine context)
