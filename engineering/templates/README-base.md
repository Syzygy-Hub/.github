[![{PLATFORM}](https://img.shields.io/badge/{PLATFORM}-{VALUE}-7F77DD?style=flat)](link) [![{LANGUAGE}](https://img.shields.io/badge/{LANGUAGE}-{VERSION}-1D9E75?style=flat)](link) [![CI](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-base-{platform}/ci.yml?label=ci&style=flat)](https://github.com/Syzygy-Hub/syzygy-base-{platform}/actions/workflows/ci.yml) [![Version](https://img.shields.io/badge/version-{VERSION}-D85A30?style=flat)](https://github.com/Syzygy-Hub/syzygy-base-{platform}/releases) [![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
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

# syzygy-base-{platform}

Production-ready {PLATFORM_NAME} app scaffold with all four Syzygy layers pre-wired — fork it and start building features on day one.

## About

syzygy-base-{platform} is a complete, production-ready mobile app scaffold that composes syzygy-foundation-{platform}, syzygy-ui-{platform}, syzygy-core-{platform}, and syzygy-services-{platform} into a working app. The architecture is already wired: DI container, navigation, theming, auth flow, and a home screen are all in place. It is not a library — it is a template repository. Fork it, rename it, and start adding features without writing any of the scaffolding yourself.

## Platforms

| Platform | Min Version | Package Manager | Status |
|---|---|---|---|
| {platform} | {version}+ | {package_manager} | ✅ Supported |

> Replace `{platform}`, `{version}`, and `{package_manager}` with the values from your `syzygy.yml` manifest.

## Requirements

- {Platform} {version}+
- {Language} {version}+
- {Tooling} {version}+

> Fill in values from your `syzygy.yml` and platform documentation.

## Installation

This is a **template repository** — do not add it as a package dependency. To use it:

1. Click **Use this template** on GitHub (or fork it)
2. Clone your new repo
3. Rename the app target, bundle identifier, and package name to match your project
4. Run `{DEPENDENCY_INSTALL_COMMAND}` to resolve the Syzygy layer dependencies

## Architecture

**Depends on:**
- syzygy-foundation-{platform}
- syzygy-ui-{platform}
- syzygy-core-{platform}
- syzygy-services-{platform}

**Used by:** your production app (fork this repo — do not add it as a dependency)

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Contents

- **Login flow** — authentication screen wired to `AuthProvider` from syzygy-foundation-{platform}
- **Home screen** — entry point after authentication, themed via syzygy-ui-{platform}
- **Navigation setup** — platform-appropriate navigation pattern pre-configured
- **DI wiring** — dependency injection container registering all four Syzygy layers
- **Theme wiring** — `SyzygyThemeProvider` applied at root, dark mode and high contrast supported
- **Full layer integration** — syzygy-foundation-{platform}, syzygy-ui-{platform}, syzygy-core-{platform}, and syzygy-services-{platform} all connected

## Usage

### App entry point — all four layers wired

```{LANGUAGE}
{APP_ENTRY_POINT_WIRING_EXAMPLE}
```

<!-- ## Platform Notes -->
<!-- Include this section only when the implementation has meaningful platform-specific differences. -->
<!-- Remove this comment block entirely if not needed. -->

## Contributing

This is a **template repository** — fork it to start a new app. Do not open pull requests into this repo with app-specific code.

Changes that improve the scaffold itself (architecture wiring, tooling, CI setup) are welcome. To propose one, open an issue first.

## Releases

Releases follow a tag-based flow:

1. Create branch `release/X.X.X`
2. Bump version in manifest and `syzygy.yml`
3. Update `CHANGELOG.md`
4. Open PR → `main`, get approval and merge
5. Push the version tag: `git tag X.X.X && git push origin X.X.X`
6. CI validates the tag, publishes, and creates the GitHub Release automatically

See the [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md) for full details.

## License

MIT — see [LICENSE](LICENSE).
