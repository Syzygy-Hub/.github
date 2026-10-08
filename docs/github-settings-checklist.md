<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# GitHub settings checklist (manual)

These settings cannot be enforced by files in the Hub repository. Each item must be applied by a
maintainer in the GitHub UI or API. Every item below is marked **Status: not applied by Hub files**.
Nothing in this checklist is enabled by the Step 1c change.

This checklist is the long-term primary release gate. It is GitHub-native: required status checks on
`main` plus a tag ruleset. The opt-in `ci-gate.yml` reusable workflow is a transition mechanism only
(see [release-standard.md](../engineering/standards/release-standard.md#release-gating)).

## Repo scope

| Group | Repos (`syzygy-<group>-<platform>`) | Platforms | Published? |
|---|---|---|---|
| Foundation | `syzygy-foundation-{android,flutter,ios,rn}` | 4 | Yes |
| Core | `syzygy-core-{android,flutter,ios,rn}` | 4 | Yes |
| Services | `syzygy-services-{android,flutter,ios,rn}` | 4 | Yes |
| AI | `syzygy-ai-{android,flutter,ios,rn}` | 4 | Yes |
| UI Libraries | `syzygy-ui-{android,flutter,ios,rn}` | 4 | Yes |
| Base | `syzygy-base-{android,flutter,ios,rn}` | 4 | No (apps and templates, no registry publish) |

Total: 24 repositories, plus the Hub repository `Syzygy-Hub/.github`.

CI workflow file in every platform repo: `.github/workflows/ci.yml` (display name `CI`). Every
repo's release workflow, where present, is `.github/workflows/release.yml`. Base repos have no release
workflow.

---

## 1. Required status checks on `main`

**Scope:** all 24 platform repos, plus the Hub repo.
**Status: not applied by Hub files.**

- [ ] For each repo, add a branch ruleset or branch protection on `main` that requires status checks.
- [ ] Require the CI check names that GitHub shows for the latest successful `ci.yml` run on `main`
      (the check names are the job names in `ci.yml`, as GitHub displays them). Select them from the
      checks list. Do not type them from memory.
- [ ] Require pull requests before merging to `main`, and require the branch to be up to date
      if that is the team's policy.
- [ ] Block force-pushes and deletion of `main`.

Release tags point at commits that were merged to `main`, so this rule is what stops an unchecked
commit from reaching a tag.

## 2. Tag ruleset (release tags)

**Scope:** all 24 platform repos.
**Status: not applied by Hub files.**

- [ ] Create a tag ruleset in each repo: Settings, Rules, Rulesets, New tag ruleset.
- [ ] Target: all tags, or the narrowest pattern the UI allows for bare semver tags. Legacy tags with a
      `v` prefix (for example in `syzygy-ui-ios`) must not be re-created or moved. Do not delete them
      without an owner decision (release-standard, Version format).
- [ ] Restrict creations to maintainers. Set the bypass list to the maintainers team only.
- [ ] Restrict updates and deletions of matching tags.
- [ ] Verify with a test tag in a sandbox repo, or with the ruleset's evaluate view, before relying on it.

**Release merges (where feasible):** the release PR merges into `main`, so the required check in
item 1 is the required check for release merges. Add a separate ruleset for `release/*` branches only
if the team actually merges into them. Confirm the plan supports the ruleset type before relying on it.

## 3. Secret scanning and push protection

**Scope:** all 24 platform repos and the Hub repo. An org-wide code security configuration is an option.
**Status: not applied by Hub files.**

- [ ] Enable secret scanning on every repo.
- [ ] Enable push protection on every repo, so pushes with detected secrets are blocked.
- [ ] Review the existing alert list for each repo after enabling.

## 4. Dependabot alerts and security updates

**Scope:** all 24 platform repos and the Hub repo.
**Status: not applied by Hub files.**

- [ ] Enable Dependabot alerts on every repo.
- [ ] Enable Dependabot security updates on every repo.
- [ ] Note: `engineering/templates/dependabot.yml.template` covers version updates in caller repos. It is
      a separate file and is not enabled by this item.

## 5. GitHub Pages (website, if used)

**Scope:** to be confirmed by the owner. No website source is present in the Hub files.
**Status: not applied by Hub files.**

- [ ] Confirm whether a website is used, and which repo serves it.
- [ ] If it is used, set Pages to deploy from GitHub Actions or from the chosen branch, and set the
      custom domain and HTTPS enforcement in the same place.
- [ ] If it is not used, record that in the owner's notes and skip this item.

## 6. pub.dev automated publishing (per Flutter package)

**Scope:** Flutter packages only: `syzygy-foundation-flutter`, `syzygy-core-flutter`,
`syzygy-services-flutter`, `syzygy-ai-flutter`, `syzygy-ui-flutter`. Base is not published.
**Status: not applied by Hub files. User action. Not enabled here.**

- [ ] For each package, on pub.dev open the package admin page, then Automated publishing.
- [ ] Set the repository to `Syzygy-Hub/<repo>` and the tag pattern to match bare semver tags
      (for example `{{version}}`, matching the tag format in release-standard).
- [ ] Until enabled, `flutter-release.yml` keeps its default `pub_auth: credentials` path. Do not
      change the caller input until this item is done and verified.

## 7. npm trusted publishing (per React Native package)

**Scope:** `syzygy-foundation-rn`, `syzygy-ui-rn`, `syzygy-core-rn`, `syzygy-services-rn`,
`syzygy-ai-rn`.
**Status: not applied by Hub files. User action. Not enabled here.**

- [ ] For each package, on npmjs.com open the package settings and add a trusted publisher.
- [ ] Set the repository to `Syzygy-Hub/<repo>` and the workflow file to `release.yml`. The npm
      publish job runs in the repo's own `release.yml`, not in the org workflow
      (release-standard, React Native npm publish exception). The claim must match that file exactly.
- [ ] Confirm that the publish job in each repo's `release.yml` still runs with provenance after
      the trusted publisher is set.

## 8. Default branch name

**Scope:** all 24 platform repos and the Hub repo.
**Status: not applied by Hub files. Verify only.**

- [ ] For each repo, confirm that Settings, General, Default branch is `main`.
- [ ] Release tags, required checks and the pub.dev and npm configuration above assume `main`.
      If a repo uses another default branch, fix it before enabling items 1 to 7 there.

---

## Sign-off

| Item | Scope | Applied by | Date |
|---|---|---|---|
| 1. Required checks on `main` | 24 + Hub | | |
| 2. Tag ruleset | 24 | | |
| 3. Secret scanning and push protection | 24 + Hub | | |
| 4. Dependabot alerts and security updates | 24 + Hub | | |
| 5. GitHub Pages (if used) | to confirm | | |
| 6. pub.dev automated publishing | 5 Flutter packages | | |
| 7. npm trusted publishing | 5 RN packages | | |
| 8. Default branch `main` | 24 + Hub | | |
