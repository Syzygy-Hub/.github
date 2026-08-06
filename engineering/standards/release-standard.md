<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Release Standard

All Syzygy repositories follow this release process. Releases are triggered automatically by CI when a pull request carrying the `release` label is merged to `main`.

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
7. Add the label **`release`** to the PR
8. Get review and approval
9. Merge to `main`
10. CI detects the `release` label on the merged PR → creates git tag `X.X.X` → publishes the package to the registry → creates a GitHub Release using the `[X.X.X]` CHANGELOG entry as the release notes body

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

## The `release` PR Label

- Label name: **`release`**
- Must be added to the PR **before merge** for CI to trigger the release pipeline
- PRs without the `release` label merge normally — no release is created
- The label is not removed after merge; CI reads it from the merged PR event

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

---

## Multi-Platform Releases

Each platform releases independently. Synchronize releases only when there is an intentional cross-platform reason — for example when a Foundation version bump requires all consuming repos to update simultaneously.

---

## What CI Does on Release PR Merge

When a PR with the `release` label is merged to `main`, CI:

1. Detects the `release` label on the merged PR event
2. Reads the version from the platform manifest
3. Creates git tag `X.X.X`
4. Publishes the package to the registry (JitPack / pub.dev / npm / SPM via the tag)
5. Creates a GitHub Release with the `[X.X.X]` CHANGELOG entry as the release notes body
