<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

[![Build](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-core-{platform}/ci.yml?label=build&style=flat)](https://github.com/Syzygy-Hub/syzygy-core-{platform}/actions)
[![Tests](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-core-{platform}/ci.yml?label=tests&style=flat)](https://github.com/Syzygy-Hub/syzygy-core-{platform}/actions)
[![Coverage](https://img.shields.io/badge/coverage-reported-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-core-{platform}/actions)
[![Version](https://img.shields.io/badge/version-{VERSION}-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-core-{platform}/releases)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
<!-- Language badge — replace {LANGUAGE_BADGE} with one of:
     iOS:     [![Swift](https://img.shields.io/badge/Swift-6.0-FA7343?style=flat&logo=swift&logoColor=white)](https://swift.org)
     Android: [![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?style=flat&logo=kotlin&logoColor=white)](https://kotlinlang.org)
     RN:      [![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
     Flutter: [![Dart](https://img.shields.io/badge/Dart-3.0-0175C2?style=flat&logo=dart&logoColor=white)](https://dart.dev)
-->
{LANGUAGE_BADGE}
<!-- Package manager badge — replace {PACKAGE_MANAGER_BADGE} with one of:
     iOS:     [![SPM](https://img.shields.io/badge/SPM-compatible-FA7343?style=flat)](https://swift.org/package-manager)
     Android: [![JitPack](https://img.shields.io/badge/JitPack-compatible-4CAF50?style=flat)](https://jitpack.io)
     RN:      [![npm](https://img.shields.io/badge/npm-{PACKAGE_NAME}-CB3837?style=flat&logo=npm&logoColor=white)](https://www.npmjs.com/package/{PACKAGE_NAME})
     Flutter: [![pub.dev](https://img.shields.io/badge/pub.dev-{PACKAGE_NAME}-0175C2?style=flat&logo=dart&logoColor=white)](https://pub.dev/packages/{PACKAGE_NAME})
-->
{PACKAGE_MANAGER_BADGE}

# syzygy-core-{platform}


App foundation for {PLATFORM_NAME} — extensions, architecture utilities, security, and testing helpers you rebuild on every project.

## What is it?

syzygy-core-{platform} is the app foundation layer — the collection of extensions, architecture patterns, DI utilities, security helpers, and testing infrastructure that every production {PLATFORM_NAME} app needs, extracted into one place.

It implements Foundation contracts where applicable and provides the scaffolding your feature layers sit on top of.

## Why would I use it?

You rebuild the same DI container, the same navigation coordinator, the same keychain wrapper, and the same base test case on every project. Core gives you all of that, tested, consistent with the rest of the Syzygy ecosystem, and ready to extend.

## Platform Support

**Requires:** {PLATFORM_REQUIREMENT}

## Installation

### {PACKAGE_MANAGER_NAME}

```{LANGUAGE}
{INSTALLATION_SNIPPET}
```

## What Does It Contain?

- **Extensions** — Standard library and platform type extensions (String, Date, Collection, etc.)
- **Architecture** — Base classes and protocols for MVVM, Clean Architecture, and DI
- **Security** — Keychain wrapper, encryption utilities, biometric helpers
- **Testing** — Base test cases, async test helpers, timeout utilities

## Architecture

**Depends on:** syzygy-foundation-{platform}

**Used by:** your app

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Example

```{LANGUAGE}
{DI_AND_EXTENSION_USAGE_EXAMPLE}
```

## Contributing & Releases

Release trigger: `release: vX.X.X — description` commit on `main`.
Tag format: `X.X.X` (no `v` prefix).
See [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md).

## License

MIT — see [LICENSE](LICENSE).

## Author

[Ayush Kumar Sethi](https://aks5686.github.io) — [github.com/aks5686](https://github.com/aks5686)
