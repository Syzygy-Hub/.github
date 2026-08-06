<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark.svg">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light.svg" alt="Syzygy" width="600">
</picture>

# Syzygy Release Standard

---

## Release Trigger

A release is triggered by a commit on `main` whose message starts with:

```
release: vX.X.X — description
```

The `v` prefix appears in the commit message for readability. It is stripped from the actual git tag.

**Examples:**
```
release: v1.0.0 — initial release
release: v2.4.0 — theming system across all platforms
release: v2.4.1 — fix overlayAlpha on Android ModalDialog
```

---

## Tag Format

```
X.X.X
```

No `v` prefix. The tag `1.0.0` is correct. The tag `v1.0.0` is wrong.

---

## Version Format

Semantic versioning: `major.minor.patch`

| Increment | When |
|---|---|
| `patch` | Fixes and non-breaking additions only |
| `minor` | Any breaking change, minimum — also new modules or significant additions |
| `major` | Reserved for fundamental architectural changes |

---

## Pre-Release Checklist

Complete all of these before committing the release trigger:

1. **Bump the version** in the package manifest (Package.swift / build.gradle.kts / package.json / pubspec.yaml). Never leave this to CI.
2. **Move Unreleased entries** to the new version header in CHANGELOG.md with today's date.
3. **Verify the build passes** locally before pushing.
4. **Verify tests pass** locally before pushing.

---

## CI Gate

Tag creation and GitHub Release happen only after CI passes on `main`. The CI workflow:
1. Builds and tests on push to `main`
2. If triggered by a tag matching `[0-9]+.[0-9]+.[0-9]+`, creates a GitHub Release with auto-generated release notes

---

## Multi-Platform Release Order

When releasing across all four platforms simultaneously:

```
1. Android
2. Flutter
3. React Native
4. iOS
```

Each platform release is a separate commit and tag. Stagger by a few minutes to keep the CI queues manageable.

---

## Breaking Changes

- Increment `minor` version at minimum
- Add a `> **Breaking change:**` callout at the top of the CHANGELOG version entry
- Document the migration path in the CHANGELOG entry, not just what changed

---

## What CI Does (and Does Not Do)

| CI does | CI does not do |
|---|---|
| Build on every push/PR | Bump the version |
| Test on every push/PR | Update CHANGELOG |
| Lint on every push/PR | Create tags |
| Create GitHub Release on tag | Push to registries (Foundation layer — future) |

The developer owns the version, CHANGELOG, and tag. CI validates and publishes.
