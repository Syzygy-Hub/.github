<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Release Standard

All Syzygy repositories follow this release process. Releases are triggered automatically by CI when a PR is merged to `main` with a commit message starting with `release:`.

---

## Release Flow

1. Create branch `release/X.X.X` from `main`
2. Bump the version number in the platform manifest:
   - iOS: no inline version field — the git tag is the version; bump `syzygy.yml` and CHANGELOG only
   - Android: `build.gradle.kts`
   - React Native: `package.json`
   - Flutter: `pubspec.yaml`
3. Bump the version in `syzygy.yml`
4. Update `CHANGELOG.md`: move the contents of `[Unreleased]` into a new `[X.X.X] - YYYY-MM-DD` section at the top, then reset `[Unreleased]` to empty above it. `[Unreleased]` always remains in the file — never delete it.
5. Ensure the README version badge reflects the new version
6. Open a Pull Request → `main`
7. Get review and approval — ensure the build job passes
8. Merge to `main` with a commit message starting with **`release:`** (e.g. `release: 1.0.1`)
9. CI detects the `release:` prefix on the push to `main` → reads version from `syzygy.yml` → creates git tag `X.X.X` → creates a GitHub Release using the `[X.X.X]` CHANGELOG entry as the release notes body

---

## Branch Naming

| Purpose | Format |
|---|---|
| Release | `release/X.X.X` |
| Feature | `feature/description` |
| Bug fix | `fix/description` |
| Chore / tooling | `chore/description` |

---

## Version Format

Semantic versioning: `major.minor.patch`. **No `v` prefix** — not in tags, not in `syzygy.yml`, not in CHANGELOG headers.

| Increment | When |
|---|---|
| `MAJOR` | Breaking API changes — consumers must update their code |
| `MINOR` | Backwards-compatible new features |
| `PATCH` | Backwards-compatible fixes only |

---

## The `release:` Commit Message Prefix

- The merge commit message **must start with `release:`** for CI to trigger the release pipeline
- Example: `release: 1.0.1 — CI improvements`
- Commits without the `release:` prefix merge normally — no release is created
- CI reads the version from `syzygy.yml` at the time of the push, not from the commit message

---

## CHANGELOG Rules

See [changelog-standard.md](changelog-standard.md) for full CHANGELOG formatting rules, including the `[Unreleased]` pattern, section order, entry format, and reference link format.

Summary:
- No `v` prefix in version headers — `[1.0.0]` not `[v1.0.0]`
- Date format: `YYYY-MM-DD`
- Include only sections with entries: `Added` | `Changed` | `Fixed` | `Removed`

---

## Tag Format

- No `v` prefix: `1.0.0` not `v1.0.0`
- Created automatically by CI after merge — **never create tags manually**

---

## Version Sync Checklist

All of the following must be updated and in sync before the release PR is merged:

- [ ] Platform manifest (`build.gradle.kts` / `package.json` / `pubspec.yaml`) where applicable
- [ ] `syzygy.yml` — `version:` field
- [ ] `CHANGELOG.md` — `[Unreleased]` contents moved into new `[X.X.X]` entry, `[Unreleased]` reset to empty
- [ ] `README.md` — version badge updated to `X.X.X`

### iOS-specific
- [ ] `Sources/SyzygyFoundation/SharedTypes/SyzygyVersion.swift` — bump `SyzygyVersion.current` to match the new version (e.g. `SyzygyVersion(1, 0, 2)`). This is a hardcoded value and must be bumped manually on every release. The test `currentVersionMatchesRelease` in `SyzygyVersionTests.swift` will fail CI if this is forgotten.

### Android-specific
- [ ] `build.gradle.kts` — version must be bumped in 3 places: project-level `version = "X.X.X"` and both `MavenPublication` blocks (`"release"` and `"testingSupport"`). All 3 must be in sync.

### RN-specific
- [ ] No additional version files beyond `package.json` — version is declared once and npm publish reads it directly.

### Flutter-specific
- [ ] `pubspec.yaml` — bump `version:` field to match the new version. This must be done manually on the release branch before opening the PR. The CI workflow patches `pubspec.yaml` at publish time as a safety net, but the repo file should always reflect the correct version from the start. `syzygy.yml` is the canonical version source — `pubspec.yaml` must be kept in sync with it.

---

## Multi-Platform Releases

Each platform releases independently. Synchronize releases only when there is an intentional cross-platform reason — for example when a Foundation version bump requires all consuming repos to update simultaneously.

---

## What CI Does on Release Merge

When a PR is merged to `main` with a commit message starting with `release:`, CI:

1. Detects the `release:` prefix on the push-to-main event
2. Reads the version from `syzygy.yml`
3. Creates git tag `X.X.X`
4. Creates a GitHub Release with the `[X.X.X]` CHANGELOG entry as the release notes body

> **Note:** Package registry publishing (JitPack / pub.dev / npm) is handled per-platform in each repo's CI workflow where applicable.
