<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Hub

This repository is the Syzygy-Hub organisation infrastructure. It is the single source of truth for brand assets, engineering standards, README templates, reusable CI workflows, and lint tooling across every Syzygy repo.

---

## Org Profile — [`profile/`](profile/)

[`profile/README.md`](profile/README.md) is the public-facing Syzygy-Hub GitHub organisation page — the page visitors see at [github.com/Syzygy-Hub](https://github.com/Syzygy-Hub).

---

## Brand — [`brand/`](brand/)

Logo, icon, banners, color palette, and typography guidelines.

- [`brand/`](brand/) — all asset files (SVG, PNG, WebP in all sizes)
- [`brand/BRAND_GUIDE.md`](brand/BRAND_GUIDE.md) — usage rules, clear space, do/don't

---

## Engineering Standards — [`engineering/standards/`](engineering/standards/)

The canonical rules every Syzygy repo follows.

- [`readme-standard.md`](engineering/standards/readme-standard.md) — the README rhythm, section order, badge format, voice rules
- [`changelog-standard.md`](engineering/standards/changelog-standard.md) — Keep a Changelog format, entry style, unreleased section
- [`release-standard.md`](engineering/standards/release-standard.md) — release trigger format, tag convention, pre-release checklist, multi-platform order
- [`repository-standard.md`](engineering/standards/repository-standard.md) — naming convention, syzygy.yml manifest, branch and commit format

---

## Ecosystem Architecture — [`engineering/architecture/`](engineering/architecture/)

The definitive description of how the Syzygy layers fit together.

- [`syzygy-ecosystem.md`](engineering/architecture/syzygy-ecosystem.md) — full layer diagram, dependency rules, what belongs (and doesn't) in each layer, platform support matrix

Individual repo READMEs do not reproduce the ecosystem diagram. They link here.

---

## README Templates — [`engineering/templates/`](engineering/templates/)

Copy the appropriate template when creating a new Syzygy repo.

- [`README-foundation.md`](engineering/templates/README-foundation.md) — for `syzygy-foundation-*`
- [`README-ui.md`](engineering/templates/README-ui.md) — for `syzygy-ui-*`
- [`README-core.md`](engineering/templates/README-core.md) — for `syzygy-core-*`
- [`README-services.md`](engineering/templates/README-services.md) — for `syzygy-services-*`
- [`README-base.md`](engineering/templates/README-base.md) — for `syzygy-base-*`
- [`syzygy.yml.template`](engineering/templates/syzygy.yml.template) — the repo manifest template

---

## Lint Tooling — [`engineering/tooling/`](engineering/tooling/)

Canonical lint and analysis configs. Consuming repos store a local copy under `tooling/{platform}/` and CI fetches the canonical version fresh on each run.

- [`engineering/tooling/ios/.swiftlint.yml`](engineering/tooling/ios/.swiftlint.yml)
- [`engineering/tooling/android/.editorconfig`](engineering/tooling/android/.editorconfig)
- [`engineering/tooling/rn/.eslintrc.json`](engineering/tooling/rn/.eslintrc.json) + [`.prettierrc`](engineering/tooling/rn/.prettierrc)
- [`engineering/tooling/flutter/analysis_options.yaml`](engineering/tooling/flutter/analysis_options.yaml)

---

## Developer Tools — [`engineering/hooks/`](engineering/hooks/)

Shared developer tools that improve the local development workflow.

- **Pre-push lint hook** — [`engineering/hooks/pre-push`](engineering/hooks/pre-push) — auto-detects repo platform, fetches canonical lint config, and runs linters before push. Blocks pushing on lint failure. See [`engineering/hooks/README.md`](engineering/hooks/README.md) for installation and usage.

---

## Reusable CI Workflows — [`.github/workflows/`](.github/workflows/)

Platform-specific GitHub Actions workflows called by individual repos via `workflow_call`.

**CI workflows** (triggered by `workflow_call` from consuming repos):

- [`ios-ci.yml`](.github/workflows/ios-ci.yml) — build, SwiftLint, test, optional coverage summary
- [`android-ci.yml`](.github/workflows/android-ci.yml) — build, ktlint, test, optional JaCoCo coverage summary
- [`rn-ci.yml`](.github/workflows/rn-ci.yml) — typecheck, lint, test, optional Jest coverage summary
- [`flutter-ci.yml`](.github/workflows/flutter-ci.yml) — analyze (--fatal-warnings), test, optional lcov coverage summary

**Release workflows** (triggered by tag push `[0-9]+.[0-9]+.[0-9]+` or `workflow_call`):

- [`ios-release.yml`](.github/workflows/ios-release.yml) — validate version, extract CHANGELOG, create GitHub Release (SPM publishes via the tag automatically)
- [`android-release.yml`](.github/workflows/android-release.yml) — validate version, extract CHANGELOG, create GitHub Release (JitPack auto-builds from the Release tag)
- [`rn-release.yml`](.github/workflows/rn-release.yml) — validate version, extract CHANGELOG, publish to npm, create GitHub Release
- [`flutter-release.yml`](.github/workflows/flutter-release.yml) — validate version, extract CHANGELOG, publish to pub.dev, create GitHub Release

Coverage is informational only — no threshold enforcement. Results appear in the GitHub Actions job summary.
