<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

<!--
How to add an entry (for future changes; this comment is not rendered):
1. Add a line under [Unreleased] in the section that fits: Added, Changed, Deprecated, Removed, Fixed or Security.
2. Start the line with the verb in past tense ("Added", "Changed", "Fixed") and name the file or input touched.
3. For any change to a reusable workflow, add a sub-bullet "Callers affected: ..." saying whether callers must edit anything, and what.
4. Do not add custom sections, PR numbers, contributor names or a "Known limitations" section.
5. A deprecation must state its removal target as a future major version.
-->

# Changelog

All notable changes to the Syzygy Hub (`Syzygy-Hub/.github`) are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The Hub is not tagged yet, so all changes sit under `[Unreleased]`.

---

## [Unreleased]

### Added

- Added `engineering/tooling/banner-guard/check_banner.py`, a read-only check of the canonical banner. README-type files (root `README.md`, `profile/README.md`, `engineering/templates/README-*.md`) must have badge lines, then the banner, then the H1. Other required docs must open with the banner. It runs as an extra step in `ecosystem-drift.yml`; the workflow's triggers and permissions are unchanged.
- Added `.github/workflows/lint-workflows.yml`, which runs actionlint (pinned 1.7.7, checksum-verified) on Hub workflows, and `.github/dependabot.yml` for GitHub Actions updates in this repo. Neither affects callers.
- Added `app-release.yml`, the release workflow for apps and templates. It validates the tag and `syzygy.yml`, extracts the CHANGELOG section and creates a GitHub Release. It never publishes to a registry.
  - Callers affected: none. New app repositories use `release-app-{ios,android,rn,flutter}.yml.template`.
- Added `ci-gate.yml`, an opt-in reusable workflow that checks the tagged commit has a successful CI run. Modes `off`, `warn` and `enforce` (default `enforce` for adopters). Reports missing permission, API error, no completed run and failed run separately. No caller uses it yet.
  - Callers affected: none. Only a caller that adopts `ci-gate.yml` needs `actions: read` at workflow top level.
  - Callers affected: none. Adoption is a caller choice (see `docs/github-settings-checklist.md` and `engineering/standards/release-standard.md`).
- Added an optional release notification to a website repository (`notify_website_repo`, default off, needs `WEBSITE_DISPATCH_TOKEN`). Silently skipped when unset.
- Added the ecosystem feed `ecosystem/feed.json`, generated from each repo's `syzygy.yml` by `engineering/tooling/ecosystem-feed/`, with a JSON Schema, and a weekly drift check `.github/workflows/ecosystem-drift.yml` (read-only).
- Added iOS CI inputs `xcodebuild_extra_args`, `ios_simulator_device` and `ios_simulator_os`. Empty simulator fields auto-detect the newest iOS runtime and the newest iPhone on it.
  - Callers affected: none. Existing `project_type: xcode` callers keep working.
- Added a Swift Testing summary to the iOS CI job summary.
- Added `use_local_analysis_options` to `flutter-ci.yml` (default `false`, see Changed).
  - Callers affected: Flutter callers with a repo-root `analysis_options.yaml` that they want to keep must set `use_local_analysis_options: true`.
- Added `project_type` to `android-ci.yml` (`library` or `app`).
  - Callers affected: callers on an application module must set `project_type: app` and `module: ':app'`.
- Added the optional `demonstrates` and `depends_on` fields to `syzygy.schema.json`, for example repositories only. The schema rejects them on any other `type`.
- Added `engineering/standards/example-apps-standard.md`, `engineering/templates/README-example.md` and an example-type comment block in `engineering/templates/syzygy.yml.template`.
- Added the lockfile policy to `engineering/standards/repository-standard.md`.
- Added `docs/pinning-policy.md`, which describes the current `@main` policy and a possible later move to Hub release tags.
- Added `docs/ecosystem-fragment.md`, the ecosystem fragment.
- Added community health files: `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, issue templates and a pull request template.

### Changed

- Changed the Markdown docs to use the same canonical `<picture>` banner (width 600). README-type files open with their badge row, then the banner, matching the readme standard's section order. Other docs open with the banner. Exempt: issue and pull request templates, YAML, CODEOWNERS and dependabot templates.
- Changed the root `README.md` architecture section to the ASCII diagram used in `profile/README.md`. Removed the AI-layer legend line and the `✦` markers that only supported it.
- Changed the root `README.md` to a shorter, repo-focused structure. Its release description now matches the workflows: release workflows create GitHub Releases and do not publish; callers publish.
- Changed the caller templates: iOS templates use `project_type` `spm` or `xcode` (not `library` or `app`); the RN app template uses `node_version_from_engines` with `22` as fallback; undeclared inputs were removed.
  - Callers affected: none. Templates are not live callers.
- Changed release workflows to be compatible by default. Their `verify-ci` job and the `ci_gate` and `skip_ci_gate` inputs are removed. The release jobs run a read-only validation job (`contents: read`) and the release job (`contents: write`, `id-token: write` on Flutter only).
  - Callers affected: none. Every existing release caller grants `contents: write` and `id-token: write` and uses `secrets: inherit`, which the new workflows satisfy.
  - Callers affected: none required.
- Changed the release tag filter to strict bare semver, `'[0-9]+.[0-9]+.[0-9]+'`. Tags with a `v` prefix or a pre-release suffix are rejected.
  - Callers affected: callers must use the strict filter in `on.push.tags`.
- Changed CI workflows so that no build, lint, analysis or test failure is masked. There is no `|| true`, `continue-on-error` or output pipe. Only coverage and summary steps tolerate missing output, and they emit `::warning::`.
  - Callers affected: none.
- Changed CI concurrency so that superseded runs are cancelled on every ref except the default branch.
  - Callers affected: none.
- Changed `rn-ci.yml` to cache npm when a `package-lock.json` exists. Without a lockfile it runs `npm install` and writes a warning that the install is not reproducible.
  - Callers affected: none.
- Changed `flutter-ci.yml` to cache pub packages.
  - Callers affected: none.
- Changed `flutter-ci.yml` so the Hub analysis options overwrite a repo-root `analysis_options.yaml` by default. Set `use_local_analysis_options: true` to keep a local file.
  - Callers affected: Flutter callers with a local `analysis_options.yaml` that they want to keep must set `use_local_analysis_options: true`.
- Changed `android-ci.yml` so `project_type` defaults to `library`.
  - Callers affected: application-module callers must set `project_type: app`.
- Changed `ai-contract-spec.md` to v3.0.0. It describes the contracts the four AI platform repositories ship, and replaces the v1.1.0 draft.
- Changed `release-standard.md` to add the SemVer and deprecation policy, the tag format history, and the no-publish app release mode.
- Changed `syzygy.yml` to the canonical schema, where `type` replaces `layer`. The reference validator still accepts legacy keys with a warning.

### Deprecated

- Deprecated the `skip_ci_gate` input of `ci-gate.yml`. It is not declared there. Use `ci_gate: off` instead. The release workflows no longer have it.
  - Callers affected: none required. Removal target: not set. It must be a future major version (owner decision).

### Security

- Changed CI workflows to least-privilege permissions: CI jobs use `contents: read`. The release validation job uses `contents: read`. Release jobs use `contents: write`. Only `ci-gate.yml` requests `actions: read`.
  - Callers affected: none.
- Changed `rn-release` template to Node 24 with no `registry-url`, matching the npm OIDC publish constraint used by real callers.
  - Callers affected: none.

---

[Unreleased]: https://github.com/Syzygy-Hub/.github/commits/main
