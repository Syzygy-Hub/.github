<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark.svg">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light.svg" alt="Syzygy" width="600">
</picture>

[![Build](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-foundation-{platform}/ci.yml?label=build&style=flat)](https://github.com/Syzygy-Hub/syzygy-foundation-{platform}/actions)
[![Tests](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-foundation-{platform}/ci.yml?label=tests&style=flat)](https://github.com/Syzygy-Hub/syzygy-foundation-{platform}/actions)
[![Coverage](https://img.shields.io/badge/coverage-reported-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-foundation-{platform}/actions)
[![Version](https://img.shields.io/badge/version-{VERSION}-2F6FED?style=flat)](https://github.com/Syzygy-Hub/syzygy-foundation-{platform}/releases)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
<!-- Language badge — replace {LANGUAGE_BADGE} with one of:
     iOS:     [![Swift](https://img.shields.io/badge/Swift-6.0-FA7343?style=flat&logo=swift&logoColor=white)](https://swift.org)
     Android: [![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?style=flat&logo=kotlin&logoColor=white)](https://kotlinlang.org)
     RN:      [![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
     Flutter: [![Dart](https://img.shields.io/badge/Dart-3.0-0175C2?style=flat&logo=dart&logoColor=white)](https://dart.dev)
-->
{LANGUAGE_BADGE}

# syzygy-foundation-{platform}

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-2400.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-2400.png" alt="Syzygy">
</picture>

Foundational contracts, primitives, and shared types for the Syzygy {PLATFORM_NAME} ecosystem.

## What is it?

syzygy-foundation-{platform} defines the contracts that every other Syzygy layer depends on — protocols, value types, enums, and error types only. There is zero implementation here. No business logic. No platform API calls.

The Foundation layer is what makes UI, Core, and Services independently replaceable. Each layer imports Foundation and implements its contracts — nothing more.

## Why would I use it?

You use it by depending on it from syzygy-ui-{platform}, syzygy-core-{platform}, or syzygy-services-{platform}. You don't import Foundation directly in your app — your app imports the layer that implements the contracts you need.

If you are building a custom implementation of a Syzygy contract — say, a custom analytics provider — you import Foundation directly and conform to `AnalyticsProvider`.

## Platform Support

**Requires:** {PLATFORM_REQUIREMENT}

## Installation

> **Coming soon** — Foundation is not yet published to a package registry. To use it now, add it as a local path dependency or reference the GitHub repo directly.

### {PACKAGE_MANAGER_NAME}

```{LANGUAGE}
{INSTALLATION_SNIPPET}
```

## What Does It Contain?

- **Primitives** — `SyzygyID<T>`, `Page<T>`, `PaginationRequest`, `SyzygyTimestamp`, `SyzygyDuration`, `TimeProvider`, `ValidationResult`, `ValidationRule`
- **Contracts** — `NetworkClientProtocol`, `StorageProvider`, `AuthProvider`, `AnalyticsProvider`, `LoggerProtocol`, `ConnectivityProvider`
- **Shared Types** — `SyzygyEnvironment`, `SyzygyConfiguration`, `SyzygyBuildInfo`, `SyzygyVersion`
- **Errors** — `SyzygyError`, `SyzygyErrorCode`, `SyzygyErrorSeverity`
- **Testing** — `MockNetworkClient`, `MockLogger`, `MockAuthProvider`, `MockStorageProvider`, `MockConnectivityProvider`, `SpyAnalyticsProvider`, `FixtureProvider`, `FixedTimeProvider` (separate import — test targets only)

## Architecture

**Module structure:**
- `{RUNTIME_MODULE}` — runtime contracts and primitives
- `{TESTING_MODULE}` — test support (separate import — never ship in production)

**Depends on:** nothing

**Used by:** syzygy-ui-{platform}, syzygy-core-{platform}, syzygy-services-{platform}

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## Examples

### Implementing a contract

```{LANGUAGE}
{NETWORK_CLIENT_IMPLEMENTATION_EXAMPLE}
```

### Using a primitive

```{LANGUAGE}
{SYZYGY_ID_USAGE_EXAMPLE}
```

### Using test support

```{LANGUAGE}
{MOCK_NETWORK_CLIENT_TEST_EXAMPLE}
```

## Contributing & Releases

Release trigger: `release: vX.X.X — description` commit on `main`.
Tag format: `X.X.X` (no `v` prefix).
See [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md).

## License

MIT — see [LICENSE](LICENSE).

## Author

[Ayush Kumar Sethi](https://aks5686.github.io) — [github.com/aks5686](https://github.com/aks5686)
