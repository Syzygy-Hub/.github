<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Release Standard

All Syzygy repositories follow this release process. Releases are triggered by pushing a version tag to the repo. The caller's `release.yml` runs on the tag push and calls the org release workflow, which validates the version and creates the GitHub Release. Registry publishing is platform-specific. Flutter publishes to pub.dev inside `flutter-release.yml`. React Native publishes to npm from each caller's own `publish-npm` job, because npm OIDC trusted publishing needs the caller's workflow file. iOS (SPM) and Android (JitPack) publish nothing beyond the GitHub Release, since the tag is the artefact. Apps (`app-release.yml`) publish nothing.

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
10. The caller's release workflow runs on the tag push → the org release workflow reads the version from `syzygy.yml` → validates it matches the tag → extracts the `## [X.X.X]` CHANGELOG section → creates a GitHub Release. Registry publishing, where applicable, is described under *What CI Does on Tag Push*.

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
| `MINOR` | Backwards-compatible new features (additive API) |
| `PATCH` | Backwards-compatible fixes only, including CI-only and tooling-only changes |

### SemVer and deprecation policy

- **CI-only or tooling-only changes are patch releases.** Changes to workflows, lint configs, templates, or hooks that do not change a published API are a `PATCH` bump.
- **Additive API is a minor release.** New public types, methods or options that do not break existing callers are a `MINOR` bump.
- **Breaking changes are a major release, and must go through a deprecation cycle first.** The API is marked deprecated in a minor release, with the replacement named in the CHANGELOG and in the code. It is removed only in the next major release. A deprecation must state its removal target version, and that version must be a future major. Deprecations with a past removal target must be closed in the next release, either by removing the item or by withdrawing the deprecation with a CHANGELOG entry.

Example: the AI layer's v1.1.0 deprecation of the RN timestamp type had a removal target of v1.2.0. That target expired without the code changing. Future deprecations must not repeat this pattern.

### Tag format history (legacy)

- **Current format:** bare strict semver, for example `3.0.0`. The release CI glob `[0-9]+.[0-9]+.[0-9]+` fires only on bare tags.
- **Legacy format:** `v`-prefixed tags exist in the UI Libraries repositories. Workspace snapshot of `.git/packed-refs` and `refs/tags`: `syzygy-ui-ios` has `v1.0.1` to `v1.0.4` (packed) alongside `1.0.0`, `2.3.0`, `2.4.0`, `2.5.0`, `3.0.0`, and `v2.0.0` to `v2.2.1` (loose). `syzygy-ui-android` and `syzygy-ui-rn` show the same mix. `syzygy-ui-flutter` has bare tags only (`1.0.0`, `1.0.1`, `2.x`, `3.0.0`).
- The `v`-prefixed tags are **legacy**. They are kept for history and must not be re-created or moved. They do not fire the release workflow, because the glob requires a digit at the start of the tag name.
- Do not delete legacy tags without an owner decision.

---

## Tag Format and Push

- No `v` prefix: `1.0.0` not `v1.0.0`
- Push the tag after merging to `main`: `git tag X.X.X && git push origin X.X.X`
- The tag push fires the caller's `release.yml`, which calls the org-level release workflow in `Syzygy-Hub/.github`
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
- [ ] `pubspec.yaml` — bump `version:` field to match the new version. This must be done manually on the release branch before opening the PR. The release workflow does not rewrite `pubspec.yaml`. It asserts that the file's `version:` equals `syzygy.yml` exactly and fails otherwise, so the repo file must be correct from the start. `syzygy.yml` is the canonical version source — `pubspec.yaml` must be kept in sync with it.

---

## Multi-Platform Releases

Each platform releases independently. Synchronize releases only when there is an intentional cross-platform reason — for example when a Foundation version bump requires all consuming repos to update simultaneously.

---

## What CI Does on Tag Push

When a tag matching `[0-9]+.[0-9]+.[0-9]+` is pushed to a repo, the caller's `release.yml` fires and calls the org-level release workflow (`Syzygy-Hub/.github/.github/workflows/{platform}-release.yml`), which:

1. Reads `version:` from `syzygy.yml` and validates it matches the pushed tag — fails the run if they differ
2. Extracts the `## [<version>]` section from `CHANGELOG.md` as release notes
3. Publishes to a registry only where the platform needs it. Flutter publishes to pub.dev inside `flutter-release.yml`. iOS (SPM) and Android (JitPack) need no publish step. React Native's npm publish is not in this workflow (see below).
4. Creates a GitHub Release with the extracted CHANGELOG entry as the release notes body

---

## Release gating

A release tag must point at a commit that has already passed CI. This section states exactly which parts of that requirement are live, which are opt-in, and which is the long-term primary control.

### What is live now

- **Release hardening only.** The org release workflows validate the tag and `version:`, extract the CHANGELOG entry and create the GitHub Release. Those checks are live.
- **No CI gate for existing callers.** The release workflows contain no CI check and no `ci_gate` or `skip_ci_gate` input. CI is checked for a release only when a caller adopts `ci-gate.yml` (see below).
- Any deliberate bypass of a CI check (for example a caller's `ci_gate: off` on the gate job) must be recorded in the CHANGELOG entry and the GitHub Release notes, with the reason.

### Opt-in: `ci-gate.yml` adoption

`.github/workflows/ci-gate.yml` in the Hub is a standalone reusable workflow (`workflow_call` only). Each repo adopts it explicitly. Adoption is a choice made per repo and is not automatic. This document does not adopt it for any caller.

Inputs:

| Input | Type | Default | Description |
|---|---|---|---|
| `sha` | string, required | none | Commit to verify. The caller passes `${{ github.sha }}`. |
| `ci_workflow_name` | string | `ci.yml` | Filename of the caller's CI workflow. |
| `ci_gate` | string | `enforce` | `off`, `warn` or `enforce`. |

`skip_ci_gate` is not declared in `ci-gate.yml`, so it cannot skip the gate. Use `ci_gate: off` instead.

Modes:

| Mode | Latest completed run succeeded | Any other result | Exit |
|---|---|---|---|
| `off` | not checked. `::notice::[off]` and a summary row | not checked | 0 |
| `warn` | `::notice::[success]` | `::warning::[category]`, release continues | 0 |
| `enforce` | `::notice::[success]` | `::error::[category]`, release stops | 1 |

Categories for a non-success result:

- `no-run`: no run of the CI workflow exists for the SHA.
- `in-progress`: runs exist for the SHA, but none has completed.
- `failed`: the newest completed run did not conclude `success`.
- `missing-permission`: the API returned HTTP 403, which means the caller lacks `actions: read`.
- `api-error`: any other API failure, or an unexpected response.

An invalid `ci_gate` value fails with `[invalid-mode]` and exit 1 in every case. Every mode writes a job-summary table.

Adoption pattern. The caller's existing tag trigger, inputs and secrets stay as they are. Only the two jobs below are added or changed:

```yaml
permissions:
  contents: read
  actions: read          # required: a called job cannot exceed the caller's top-level grant

jobs:
  gate:
    permissions:
      actions: read      # read CI runs for the tagged commit
      contents: read
    uses: Syzygy-Hub/.github/.github/workflows/ci-gate.yml@main
    with:
      sha: ${{ github.sha }}
      ci_workflow_name: ci.yml
      ci_gate: enforce

  release:
    needs: gate          # the release never starts unless the gate job passed
    permissions:
      contents: write    # as the release callee already requires
    uses: Syzygy-Hub/.github/.github/workflows/<platform>-release.yml@main
    with:
      ci_gate: off       # the gate job has already checked CI; do not check twice
      # existing release inputs and secrets, unchanged
```

Adoption rules:

- The caller's top-level `permissions` must include `actions: read`. A reusable workflow's job cannot exceed the caller's grant. Without it, `gate` gets HTTP 403, reported as `missing-permission`: `enforce` blocks the release, and `warn` passes with a warning.
- `sha` must be the tag event's `github.sha`. In a reusable workflow, `github.sha` belongs to the caller.
- `release` must set `ci_gate: off` only where the release callee accepts that input. Otherwise CI is checked twice.
- Adoption is complete only when the caller's top-level grant and the `gate` job's grant are both in its own workflow file, and `release` lists `needs: gate`.

### Long-term primary gate

The primary release gate is GitHub-native: required status checks on `main` and a tag ruleset that restricts tag creation to maintainers. The steps are in [`docs/github-settings-checklist.md`](../../docs/github-settings-checklist.md). None of them is enforced by Hub files. The `ci-gate.yml` reusable workflow is an interim, opt-in mechanism. It is not the primary gate.

## App release mode (no publish)

Apps and templates (`syzygy-base-*`, example apps) do not publish to a package registry. They use the no-publish release mode in `app-release.yml`. This mode:

- validates `version:` in `syzygy.yml` against the pushed tag,
- extracts the first versioned CHANGELOG section,
- creates a GitHub Release,
- never publishes to npm, pub.dev, JitPack or SPM.

Caller templates for apps are `release-app-{ios,android,rn,flutter}.yml.template` in [`engineering/templates/`](../templates/). Library callers use `release-library-*.yml.template`.

## React Native npm publish exception

React Native packages cannot use the standard reusable release workflow for npm publish due to npm OIDC trusted publishing constraints. npm validates the OIDC token `job_workflow_ref` claim against the trusted publisher configuration. When npm publish runs inside a reusable workflow hosted in `.github`, the claim points to `Syzygy-Hub/.github/.github/workflows/rn-release.yml`. npm's trusted publisher however expects the claim to match the individual repo's workflow file such as `Syzygy-Hub/syzygy-foundation-rn/.github/workflows/release.yml`.

To work around this each React Native repo uses a two-job release.yml: the first job delegates to the org-level `rn-release.yml` for version validation, CHANGELOG extraction and GitHub Release creation; the second job `publish-npm` runs directly in the repo's own `release.yml` and handles npm install and npm publish with provenance. This ensures the OIDC token `job_workflow_ref` matches the trusted publisher configuration on npmjs.com.

This exception applies to all RN repos: syzygy-foundation-rn, syzygy-ui-rn, syzygy-core-rn, syzygy-services-rn, syzygy-ai-rn.
