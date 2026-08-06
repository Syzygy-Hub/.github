<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark.svg">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light.svg" alt="Syzygy" width="600">
</picture>

# Syzygy CHANGELOG Standard

Every Syzygy repository CHANGELOG follows the [Keep a Changelog](https://keepachangelog.com) format.

---

## File Format

```markdown
# Changelog

## [Unreleased]

## [X.X.X] - YYYY-MM-DD

### Added
- Add X to Y

### Changed
- Change X to use Y instead of Z

### Fixed
- Fix X crashing when Y is nil

### Removed
- Remove deprecated X
```

---

## Rules

### Version header
- Format: `[X.X.X]` — no `v` prefix
- Always followed by ` - YYYY-MM-DD`
- Most recent version at the top

### Unreleased section
- Always present at the top
- Accumulates changes since the last release
- Becomes the next version header on release — rename it, don't delete it

### Sections
Include only the sections that have entries. Standard sections in order:
1. **Added** — new features, new types, new modules
2. **Changed** — changes to existing behaviour
3. **Fixed** — bug fixes
4. **Removed** — removed features, deprecated items finally dropped

Do not add custom sections. Do not add a "Known Limitations" section — fix it, defer it to a future version, or document it as a code comment. It has no place in a CHANGELOG.

### Entry format
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

### Breaking changes
Mark clearly at the top of the version entry:

```markdown
## [2.0.0] - 2026-09-01

> **Breaking change:** `AuthProvider.state` is now a `AnyPublisher<AuthState, Never>` — replace direct property access with `.statePublisher`.

### Changed
- Changed `AuthProvider.state` from `AuthState` to `AnyPublisher<AuthState, Never>`
```

### What does not belong in a CHANGELOG
- Internal implementation notes
- Future plans or roadmap items
- Names of contributors (not a project convention here)
- PR or issue numbers (optional — include only if they add genuine context)
