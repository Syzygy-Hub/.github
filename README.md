[![Version](https://img.shields.io/badge/version-3.0.0-D85A30?style=flat)](profile/README.md)
[![iOS](https://img.shields.io/badge/iOS-Swift-FA7343?style=flat&logo=swift&logoColor=white)](profile/README.md#platform-targets)
[![Android](https://img.shields.io/badge/Android-Kotlin-7F52FF?style=flat&logo=kotlin&logoColor=white)](profile/README.md#platform-targets)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)](profile/README.md#platform-targets)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-0175C2?style=flat&logo=dart&logoColor=white)](profile/README.md#platform-targets)
[![Repos](https://img.shields.io/badge/repos-25-2F6FED?style=flat&logo=github&logoColor=white)](https://github.com/orgs/Syzygy-Hub/repositories)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Hub

Shared infrastructure for the Syzygy ecosystem: reusable CI and release workflows, engineering standards, lint tooling, templates and the ecosystem feed.

## What is Syzygy

Syzygy is a set of layered libraries shared across four platforms: iOS (Swift), Android (Kotlin), React Native (TypeScript) and Flutter (Dart). Foundation is the shared base of every layer. UI, Core, Services and AI each depend only on Foundation, never on each other. The organisation has 25 repositories: 24 platform repositories (6 layers x 4 platforms) and this Hub.

## Architecture at a glance

```
                                     syzygy-foundation-*
                                              |
      +-------------------+-------------------+-------------------+-------------------+
      |                   |                                       |                   |
      v                   v                                       v                   v
 syzygy-ui-*        syzygy-core-*                         syzygy-services-*      syzygy-ai-*
      |                   |                                       |                   |
      +-------------------+-------------------+-------------------+-------------------+
                                              |
                                              v
                              syzygy-base-* (composer/scaffold)
                                              |
                                              v
                                    Syzygy Example App
```

Base is the only composer of the full stack. The full dependency rules are in [`engineering/architecture/syzygy-ecosystem.md`](engineering/architecture/syzygy-ecosystem.md). The per-platform version matrix is in [`profile/README.md`](profile/README.md#version-matrix) and generated from [`ecosystem/feed.json`](ecosystem/feed.json).

## What's in this repo

| Path | Contents |
|---|---|
| [`.github/workflows/`](.github/workflows/) | Reusable CI, release and gate workflows, plus the drift and lint checks for this repo |
| [`engineering/standards/`](engineering/standards/) | Canonical rules: repository, release, changelog, README, AI contract and example-app standards |
| [`engineering/tooling/`](engineering/tooling/) | Lint configs (iOS, Android, RN, Dart and Flutter) and the `syzygy.yml` validator |
| [`engineering/templates/`](engineering/templates/) | README, `syzygy.yml`, CI and release caller templates |
| [`engineering/schema/`](engineering/schema/) | JSON Schemas for `syzygy.yml` and the ecosystem feed |
| [`ecosystem/`](ecosystem/) | The generated ecosystem feed and the repo list it is built from |
| [`brand/`](brand/) | Logo, icon, banners and the brand guide |
| [`docs/`](docs/) | Pinning policy and the GitHub settings checklist |

## Use the Hub workflows

Callers reference the workflows at `@main`. Copy a template from [`engineering/templates/`](engineering/templates/) and adjust the inputs. Minimal examples:

```yaml
# iOS library (Swift Package Manager)
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/ios-ci.yml@main

# Android library (JDK 17 is required for library repos)
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/android-ci.yml@main
    with:
      java_version: '17'
```

Input reference, library and app recipes for every platform, and the release rules are in [`.github/workflows/README.md`](.github/workflows/README.md).

## Engineering standards

- [`repository-standard.md`](engineering/standards/repository-standard.md): naming, the `syzygy.yml` manifest, branches and commits, lockfile policy
- [`release-standard.md`](engineering/standards/release-standard.md): SemVer, strict tags, release gating and the no-publish app mode
- [`changelog-standard.md`](engineering/standards/changelog-standard.md): Keep a Changelog format
- [`readme-standard.md`](engineering/standards/readme-standard.md): README structure and voice
- [`ai-contract-spec.md`](engineering/standards/ai-contract-spec.md): the AI contract shipped in v3.0.0
- [`example-apps-standard.md`](engineering/standards/example-apps-standard.md): example app repositories

## Contributing, security and conduct

- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- Changes: [CHANGELOG.md](CHANGELOG.md)

## Licence

TODO: licence holder is a pending decision. No licence is granted by this repository until the owner confirms the holder and licence text (see [`repository-standard.md`](engineering/standards/repository-standard.md)).
