[![Build](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-base-{platform}/ci.yml?label=build&style=flat)](https://github.com/Syzygy-Hub/syzygy-base-{platform}/actions)
[![Tests](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-base-{platform}/ci.yml?label=tests&style=flat)](https://github.com/Syzygy-Hub/syzygy-base-{platform}/actions)
[![Coverage](https://img.shields.io/badge/coverage-reported-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-base-{platform}/actions)
[![Version](https://img.shields.io/badge/version-{VERSION}-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-base-{platform}/releases)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
<!-- Language badge — uncomment the line for your platform:
[![Swift](https://img.shields.io/badge/Swift-6.0-FA7343?logo=swift&logoColor=white)](https://swift.org)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Dart](https://img.shields.io/badge/Dart-3.0-0175C2?logo=dart&logoColor=white)](https://dart.dev)
-->
<!-- Package manager badge — uncomment the line for your platform:
[![SPM](https://img.shields.io/badge/SPM-compatible-FA7343?logo=swift&logoColor=white)](https://swift.org/package-manager)
[![JitPack](https://img.shields.io/badge/JitPack-compatible-4CAF50)](https://jitpack.io)
[![npm](https://img.shields.io/badge/npm-{PACKAGE_NAME}-CB3837?logo=npm&logoColor=white)](https://npmjs.com)
[![pub.dev](https://img.shields.io/badge/pub.dev-{PACKAGE_NAME}-0175C2?logo=dart&logoColor=white)](https://pub.dev)
-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# syzygy-base-{platform}


Production-ready {PLATFORM_NAME} app scaffold with all four Syzygy layers pre-wired — fork it and start building features on day one.

## What is it?

syzygy-base-{platform} is a complete, production-ready mobile app scaffold that composes syzygy-foundation-{platform}, syzygy-ui-{platform}, syzygy-core-{platform}, and syzygy-services-{platform} into a working app. The architecture is already wired: DI container, navigation, theming, auth flow, and a home screen are all in place.

It is not a library — it is a template repository. Fork it, rename it, and start adding features without writing any of the scaffolding yourself.

## Why would I use it?

Every production app needs the same plumbing: DI wiring, navigation setup, theme application, a login flow, and a home screen. Base gives you all of that, already connected to the Syzygy ecosystem and following the same architecture patterns across all four platforms.

## Platform Support

**Requires:** {PLATFORM_REQUIREMENT}

## Installation

This is a **template repository** — do not add it as a package dependency. To use it:

1. Click **Use this template** on GitHub (or fork it)
2. Clone your new repo
3. Rename the app target, bundle identifier, and package name to match your project
4. Run `{DEPENDENCY_INSTALL_COMMAND}` to resolve the Syzygy layer dependencies

## What Does It Contain?

- **Login flow** — authentication screen wired to `AuthProvider` from syzygy-foundation-{platform}
- **Home screen** — entry point after authentication, themed via syzygy-ui-{platform}
- **Navigation setup** — platform-appropriate navigation pattern pre-configured
- **DI wiring** — dependency injection container registering all four Syzygy layers
- **Theme wiring** — `SyzygyThemeProvider` applied at root, dark mode and high contrast supported
- **Full layer integration** — syzygy-foundation-{platform}, syzygy-ui-{platform}, syzygy-core-{platform}, and syzygy-services-{platform} all connected

## Architecture

**Depends on:**
- syzygy-foundation-{platform}
- syzygy-ui-{platform}
- syzygy-core-{platform}
- syzygy-services-{platform}

**Used by:** your production app (fork this repo — do not add it as a dependency)

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Example

### App entry point — all four layers wired

```{LANGUAGE}
{APP_ENTRY_POINT_WIRING_EXAMPLE}
```

## Contributing & Releases

This is a **template repository** — fork it to start a new app. Do not open pull requests into this repo with app-specific code.

Changes that improve the scaffold itself (architecture wiring, tooling, CI setup) are welcome. To propose one, open an issue first.

Release trigger: `release: vX.X.X — description` commit on `main`.
Tag format: `X.X.X` (no `v` prefix).
See [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md).

## License

MIT — see [LICENSE](LICENSE).

## Author

[Ayush Kumar Sethi](https://aks5686.github.io) — [github.com/aks5686](https://github.com/aks5686)
