<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Hub Pinning Policy

This document describes how platform repositories reference the Hub's reusable workflows, and how that could change later to Hub release tags.

**Current policy: callers stay on the floating `@main` ref.** This document does not change that policy. **No caller is affected by this document.** No caller needs to edit anything because of it.

---

## 1. Today

Every caller references the Hub by branch:

```yaml
uses: Syzygy-Hub/.github/.github/workflows/ios-ci.yml@main
```

Two consequences, both as documented in [`.github/workflows/README.md`](../.github/workflows/README.md):

- Every caller receives Hub changes on the next run, without a caller edit.
- Action references inside the Hub workflows use floating major tags (`@v4`, `@v2`, `@v1`). That is a separate question and is not changed here.

The `org_config_sha` input (default `main`) is the ref used to fetch shared tooling configs such as SwiftLint, ESLint and analysis options. It is independent of the `uses:` ref.

---

## 2. Possible future: pinning to a Hub release tag

A caller could later pin to a Hub release instead of `main`:

```yaml
uses: Syzygy-Hub/.github/.github/workflows/ios-ci.yml@3.1.0
```

### Tag format

| Option | Example | Assessment |
|---|---|---|
| Bare strict semver (recommended) | `3.1.0` | Matches the rule for every Syzygy repository in [`release-standard.md`](../engineering/standards/release-standard.md): no `v` prefix. |
| `v`-prefixed | `v3.1.0` | Not used. The `v` prefix is legacy for the UI Libraries repositories only and is not a Hub convention. |

Hub tags would be bare semver, so one format applies everywhere. Hub tags do not trigger any workflow: the Hub has no `push: tags` trigger, and every workflow in it is reusable only.

### Tag rules (proposed, applied when the first Hub tag is made)

- One tag per Hub release, on a commit on `main` that has been reviewed and merged.
- Tags are never moved or re-created once pushed.
- Tag and CHANGELOG version match: the `## [X.Y.Z]` section of `CHANGELOG.md` at the tagged commit is the release record for that tag.

---

## 3. What changes

### For the Hub

- A tag is created per Hub release. Hub changes accumulate on `main` until a release is cut.
- `CHANGELOG.md` is the source of truth for release notes. At release time the `[Unreleased]` entries move into a new `## [X.Y.Z] - YYYY-MM-DD` section, as set out in [`changelog-standard.md`](../engineering/standards/changelog-standard.md). The `[Unreleased]` compare link then points at the new tag.
- Until the first tag exists, the `[Unreleased]` link in `CHANGELOG.md` points to the commit history of `main`.
- Callers that pin to a tag keep receiving that tag's behaviour. A fix on `main` reaches them only when they move their ref, so each Hub release must be described fully in its CHANGELOG section for callers to decide.

### For callers

- A caller that moves to a tag changes one line per workflow: the `@main` ref in `uses:`.
- The caller should also set `org_config_sha` to the same tag. Otherwise the reusable workflow runs the tag's logic but fetches tooling configs from `main`. This applies to every workflow input that takes a Hub ref.
- Release workflows are not affected by the ref choice in a different way: the tag filter in the caller's `release.yml` is independent of the Hub ref. The strict bare-semver filter stays as it is.
- Rollback is a one-line change back to `@main`, or to the previous tag.

---

## 4. Migration (future, not started)

1. The Hub owner creates the first Hub tag from a reviewed `main` commit, after a CHANGELOG section for it exists.
2. Callers move one repository at a time. Each caller changes `uses:` and `org_config_sha` together, and runs CI before merging.
3. Nothing is required of a caller that stays on `@main`. Staying there remains valid until the owner decides otherwise.

No step in this list has been taken. The Hub has no tags today.

---

## 5. Status

| Item | State |
|---|---|
| Caller ref | `@main`, unchanged |
| Hub tags | None exist |
| Caller action required | None |
