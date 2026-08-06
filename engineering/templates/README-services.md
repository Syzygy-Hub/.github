[![Build](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-services-{platform}/ci.yml?label=build&style=flat)](https://github.com/Syzygy-Hub/syzygy-services-{platform}/actions)
[![Tests](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-services-{platform}/ci.yml?label=tests&style=flat)](https://github.com/Syzygy-Hub/syzygy-services-{platform}/actions)
[![Coverage](https://img.shields.io/badge/coverage-reported-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-services-{platform}/actions)
[![Version](https://img.shields.io/badge/version-{VERSION}-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-services-{platform}/releases)
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

# syzygy-services-{platform}


External world infrastructure for {PLATFORM_NAME} — concrete implementations of Foundation contracts for networking, storage, analytics, and OS services.

## What is it?

syzygy-services-{platform} implements the contracts defined in syzygy-foundation-{platform} using real platform APIs. Networking uses {NETWORK_FRAMEWORK}, storage uses {STORAGE_FRAMEWORK}, connectivity monitoring uses {CONNECTIVITY_FRAMEWORK}.

Every service is a plug-and-play drop-in. Swap any of them for a custom implementation by conforming to the Foundation contract.

## Why would I use it?

You need a networking layer, a storage layer, and an analytics adapter on every project. Services gives you production-ready implementations of all of them, with the Foundation contracts guaranteeing you can replace any one without touching the rest of your code.

## Platform Support

**Requires:** {PLATFORM_REQUIREMENT}

## Installation

### {PACKAGE_MANAGER_NAME}

```{LANGUAGE}
{INSTALLATION_SNIPPET}
```

## What Does It Contain?

- **Networking** — `{NETWORK_CLIENT_CLASS}` implementing `NetworkClientProtocol` — {NETWORK_DESCRIPTION}
- **Storage** — `{STORAGE_CLASS}` implementing `StorageProvider` — {STORAGE_DESCRIPTION}
- **Analytics** — `{ANALYTICS_CLASS}` implementing `AnalyticsProvider` — {ANALYTICS_DESCRIPTION}
- **Media** — {MEDIA_DESCRIPTION}
- **OS Services** — `{CONNECTIVITY_CLASS}` implementing `ConnectivityProvider`, {OTHER_OS_SERVICES}

## Architecture

**Depends on:** syzygy-foundation-{platform}

**Used by:** your app

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Example

```{LANGUAGE}
{NETWORK_CLIENT_REGISTRATION_AND_USAGE_EXAMPLE}
```

## Contributing & Releases

Release trigger: `release: vX.X.X — description` commit on `main`.
Tag format: `X.X.X` (no `v` prefix).
See [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md).

## License

MIT — see [LICENSE](LICENSE).

## Author

[Ayush Kumar Sethi](https://aks5686.github.io) — [github.com/aks5686](https://github.com/aks5686)
