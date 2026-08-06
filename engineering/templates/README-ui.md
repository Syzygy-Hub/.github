<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

[![Build](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-ui-{platform}/ci.yml?label=build&style=flat)](https://github.com/Syzygy-Hub/syzygy-ui-{platform}/actions)
[![Tests](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-ui-{platform}/ci.yml?label=tests&style=flat)](https://github.com/Syzygy-Hub/syzygy-ui-{platform}/actions)
[![Coverage](https://img.shields.io/badge/coverage-reported-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-ui-{platform}/actions)
[![Version](https://img.shields.io/badge/version-{VERSION}-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-ui-{platform}/releases)
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

# syzygy-ui-{platform}


Production-ready {PLATFORM_NAME} component library with design tokens, theming, and dark mode — zero third-party dependencies.

## What is it?

syzygy-ui-{platform} is a complete visual component library built on a shared design token system — colors, typography, spacing, radius, elevation, and animation — reproduced consistently with dark mode support from the ground up. {COMPONENT_COUNT} components ship ready to use.

The library has zero third-party runtime dependencies. All components are built directly on {NATIVE_FRAMEWORK}.

## Why would I use it?

Every component is production-ready: accessibility, dark mode, and dynamic type are handled, not left to the consumer. The token system ensures visual consistency across your entire app without coordination overhead.

The theming system lets you override any token at any level of the view hierarchy without modifying the library.

## Platform Support

**Requires:** {PLATFORM_REQUIREMENT}

## Installation

### {PACKAGE_MANAGER_NAME}

```{LANGUAGE}
{INSTALLATION_SNIPPET}
```

## What Does It Contain?

- **Components** — {COMPONENT_COUNT} production-ready components across Input, Display, Feedback, Overlay, Navigation, and Layout categories
- **Design Tokens** — `UIColorToken`, `UIFontToken`, `UISpacing`, `UIRadius`, `UIElevation`, `UIAnimation` — the shared visual language
- **Theming** — `SyzygyTheme`, `SyzygyThemeProvider` — override tokens at any level, three built-in themes (default, dark, high contrast)

## Architecture

**Depends on:** syzygy-foundation-{platform} (optional)

**Used by:** your app

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Example

```{LANGUAGE}
{THEME_PROVIDER_USAGE_EXAMPLE}
```

## Contributing & Releases

Release trigger: `release: vX.X.X — description` commit on `main`.
Tag format: `X.X.X` (no `v` prefix).
See [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md).

## License

MIT — see [LICENSE](LICENSE).

## Author

[Ayush Kumar Sethi](https://aks5686.github.io) — [github.com/aks5686](https://github.com/aks5686)
