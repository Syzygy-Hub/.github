<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Release Standard

All Syzygy repositories follow this release process. Releases are triggered by pushing a version tag to the repo — CI fires on the tag push, validates the version, publishes, and creates the GitHub Release.

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
8. Merge to `main`
9. Push the version tag: `git tag X.X.X && git push origin X.X.X`
10. CI detects the tag push → reads version from `syzygy.yml` → validates it matches the tag → extracts the `[X.X.X]` CHANGELOG entry → publishes to the platform registry (where applicable) → creates a GitHub Release

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

## Tag Format and Push

- No `v` prefix: `1.0.0` not `v1.0.0`
- Push the tag after merging to `main`: `git tag X.X.X && git push origin X.X.X`
- The tag push fires the org-level release workflow in `Syzygy-Hub/.github`
- CI validates that `syzygy.yml`'s `version:` field matches the pushed tag — if they differ, the release fails before publishing anything
- Use a conventional commit message on the merge commit (e.g. `release: 1.0.1 — CI improvements`) for a clear history, but the commit message does not trigger CI

---

## CHANGELOG Rules

See [changelog-standard.md](changelog-standard.md) for full CHANGELOG formatting rules, including the `[Unreleased]` pattern, section order, entry format, and reference link format.

Summary:
- No `v` prefix in version headers — `[1.0.0]` not `[v1.0.0]`
- Date format: `YYYY-MM-DD`
- Include only sections with entries: `Added` | `Changed` | `Fixed` | `Removed`
- The release workflow extracts the first versioned section from `CHANGELOG.md` — the `[X.X.X]` section must exist and be populated before pushing the tag

---

## Version Tag Rules

- No `v` prefix: `1.0.0` not `v1.0.0`
- Tags are pushed manually by the developer after the release PR is merged — `git tag X.X.X && git push origin X.X.X`
- The tag pattern `[0-9]+.[0-9]+.[0-9]+` is what fires the org-level release workflow

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

## What CI Does on Tag Push

When a tag matching `[0-9]+.[0-9]+.[0-9]+` is pushed to a repo, the org-level release workflow (`Syzygy-Hub/.github/.github/workflows/{platform}-release.yml`) fires and:

1. Reads `version:` from `syzygy.yml` and validates it matches the pushed tag — fails the run if they differ
2. Extracts the first versioned section from `CHANGELOG.md` as release notes
3. Publishes to the platform package registry (where applicable — npm for RN, pub.dev for Flutter; SPM is implicit on the tag, JitPack auto-builds from the GitHub Release) — **except React Native** (see below)
4. Creates a GitHub Release with the extracted CHANGELOG entry as the release notes body

---

## React Native npm publish exception

React Native packages cannot use the standard reusable release workflow for npm publish due to npm OIDC trusted publishing constraints. npm validates the OIDC token `job_workflow_ref` claim against the trusted publisher configuration. When npm publish runs inside a reusable workflow hosted in `.github`, the claim points to `Syzygy-Hub/.github/.github/workflows/rn-release.yml`. npm's trusted publisher however expects the claim to match the individual repo's workflow file such as `Syzygy-Hub/syzygy-foundation-rn/.github/workflows/release.yml`.

To work around this each React Native repo uses a two-job release.yml: the first job delegates to the org-level `rn-release.yml` for version validation, CHANGELOG extraction and GitHub Release creation; the second job `publish-npm` runs directly in the repo's own `release.yml` and handles npm install and npm publish with provenance. This ensures the OIDC token `job_workflow_ref` matches the trusted publisher configuration on npmjs.com.

This exception applies to all RN repos: syzygy-foundation-rn, syzygy-ui-rn, syzygy-core-rn, syzygy-services-rn, syzygy-ai-rn.
