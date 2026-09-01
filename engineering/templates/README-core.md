[![{PLATFORM}](https://img.shields.io/badge/{PLATFORM}-{VALUE}-7F77DD?style=flat)](link) [![{LANGUAGE}](https://img.shields.io/badge/{LANGUAGE}-{VERSION}-1D9E75?style=flat)](link) [![CI](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-core-{platform}/ci.yml?label=ci&style=flat)](https://github.com/Syzygy-Hub/syzygy-core-{platform}/actions/workflows/ci.yml) [![Version](https://img.shields.io/badge/version-{VERSION}-D85A30?style=flat)](https://github.com/Syzygy-Hub/syzygy-core-{platform}/releases) [![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
<!-- Platform and Language badge options — replace the {PLATFORM}/{LANGUAGE} placeholders above with one of these:
[![iOS](https://img.shields.io/badge/iOS-Swift-FA7343?style=flat&logo=apple&logoColor=white)](https://developer.apple.com/ios/)
[![Android](https://img.shields.io/badge/Android-Kotlin-7F52FF?style=flat&logo=android&logoColor=white)](https://developer.android.com/)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-3178C6?style=flat&logo=react&logoColor=white)](https://reactnative.dev/)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-0175C2?style=flat&logo=flutter&logoColor=white)](https://flutter.dev/)
[![Swift](https://img.shields.io/badge/Swift-6.0-FA7343?logo=swift&logoColor=white)](https://swift.org)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Dart](https://img.shields.io/badge/Dart-3.0-0175C2?logo=dart&logoColor=white)](https://dart.dev)
Package manager badge options — uncomment the line for your platform:
[![SPM](https://img.shields.io/badge/SPM-compatible-FA7343?logo=swift&logoColor=white)](https://swift.org/package-manager)
[![JitPack](https://img.shields.io/badge/JitPack-compatible-4CAF50)](https://jitpack.io)
[![npm](https://img.shields.io/badge/npm-{PACKAGE_NAME}-CB3837?logo=npm&logoColor=white)](https://npmjs.com)
[![pub.dev](https://img.shields.io/badge/pub.dev-{PACKAGE_NAME}-0175C2?logo=dart&logoColor=white)](https://pub.dev)
-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# syzygy-core-{platform}

App foundation for {PLATFORM_NAME} — extensions, architecture utilities, security, and testing helpers you rebuild on every project.

## About

syzygy-core-{platform} is the app foundation layer — the collection of extensions, architecture patterns, DI utilities, security helpers, and testing infrastructure that every production {PLATFORM_NAME} app needs, extracted into one place. It implements Foundation contracts where applicable and provides the scaffolding your feature layers sit on top of. You rebuild the same DI container, the same navigation coordinator, the same keychain wrapper, and the same base test case on every project. Core gives you all of that, tested, consistent with the rest of the Syzygy ecosystem, and ready to extend.

## Platforms

| Platform | Min Version | Package Manager | Status |
|---|---|---|---|
| {platform} | {version}+ | {package_manager} | ⏳ Coming Soon |

> Replace `{platform}`, `{version}`, and `{package_manager}` with the values from your `syzygy.yml` manifest.

## Requirements

- {Platform} {version}+
- {Language} {version}+
- {Tooling} {version}+

> Fill in values from your `syzygy.yml` and platform documentation.

## Installation

### {PACKAGE_MANAGER_NAME}

```{LANGUAGE}
{INSTALLATION_SNIPPET}
```

## Architecture

**Depends on:** syzygy-foundation-{platform}

**Used by:** your app

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Modules

- **Extensions** — Standard library and platform type extensions (String, Date, Collection, etc.)
- **Architecture** — Base classes and protocols for MVVM, Clean Architecture, and DI
- **Security** — Keychain wrapper, encryption utilities, biometric helpers
- **Testing** — Base test cases, async test helpers, timeout utilities

## Usage

```{LANGUAGE}
{DI_AND_EXTENSION_USAGE_EXAMPLE}
```

<!-- ## Platform Notes -->
<!-- Include this section only when the implementation has meaningful platform-specific differences. -->
<!-- Remove this comment block entirely if not needed. -->

## Contributing

Contributions are welcome. Please follow the [Syzygy engineering standards](https://github.com/Syzygy-Hub/.github/tree/main/engineering/standards) when submitting pull requests.

## Releases

Releases follow a label-based PR flow:

1. Create branch `release/X.X.X`
2. Bump version in manifest and `syzygy.yml`
3. Update `CHANGELOG.md`
4. Open PR → `main` with label: `release`
5. Get approval and merge
6. CI tags `X.X.X`, publishes, and creates the GitHub Release automatically

See the [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md) for full details.

## License

MIT — see [LICENSE](LICENSE).
