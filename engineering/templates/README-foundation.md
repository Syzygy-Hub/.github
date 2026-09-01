[![{PLATFORM}](https://img.shields.io/badge/{PLATFORM}-{VALUE}-7F77DD?style=flat)](link) [![{LANGUAGE}](https://img.shields.io/badge/{LANGUAGE}-{VERSION}-1D9E75?style=flat)](link) [![CI](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-foundation-{platform}/ci.yml?label=ci&style=flat)](https://github.com/Syzygy-Hub/syzygy-foundation-{platform}/actions/workflows/ci.yml) [![Version](https://img.shields.io/badge/version-{VERSION}-D85A30?style=flat)](https://github.com/Syzygy-Hub/syzygy-foundation-{platform}/releases) [![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
<!-- Platform and Language badge options — replace the {PLATFORM}/{LANGUAGE} placeholders above with one of these:
[![iOS](https://img.shields.io/badge/iOS-Swift-FA7343?style=flat&logo=apple&logoColor=white)](https://developer.apple.com/ios/)
[![Android](https://img.shields.io/badge/Android-Kotlin-7F52FF?style=flat&logo=android&logoColor=white)](https://developer.android.com/)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-3178C6?style=flat&logo=react&logoColor=white)](https://reactnative.dev/)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-0175C2?style=flat&logo=flutter&logoColor=white)](https://flutter.dev/)
[![Swift](https://img.shields.io/badge/Swift-6.0-FA7343?logo=swift&logoColor=white)](https://swift.org)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Dart](https://img.shields.io/badge/Dart-3.0-0175C2?logo=dart&logoColor=white)](https://dart.dev)
-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# syzygy-foundation-{platform}

Foundational contracts, primitives, and shared types for the Syzygy {PLATFORM_NAME} ecosystem.

## About

syzygy-foundation-{platform} defines the contracts every other Syzygy layer depends on — protocols, value types, enums, and error types only. There is zero implementation here: no business logic, no platform API calls. The Foundation layer is what makes UI, Core, and Services independently replaceable. Each layer imports Foundation and implements its contracts — nothing more. If you are building a custom implementation of a Syzygy contract, you import Foundation directly and conform to the relevant protocol.

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

> **Coming soon** — Foundation is not yet published to a package registry. To use it now, add it as a local path dependency or reference the GitHub repo directly.

### {PACKAGE_MANAGER_NAME}

```{LANGUAGE}
{INSTALLATION_SNIPPET}
```

## Architecture

**Module structure:**
- `{RUNTIME_MODULE}` — runtime contracts and primitives
- `{TESTING_MODULE}` — test support (separate import — never ship in production)

**Depends on:** nothing

**Used by:** syzygy-ui-{platform}, syzygy-core-{platform}, syzygy-services-{platform}

For the full ecosystem architecture see [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md).

## API

- **Primitives** — `SyzygyID<T>`, `Page<T>`, `PaginationRequest`, `SyzygyTimestamp`, `SyzygyDuration`, `TimeProvider`, `ValidationResult`, `ValidationRule`
- **Contracts** — `NetworkClientProtocol`, `StorageProvider`, `AuthProvider`, `AnalyticsProvider`, `LoggerProtocol`, `ConnectivityProvider`
- **Shared Types** — `SyzygyEnvironment`, `SyzygyConfiguration`, `SyzygyBuildInfo`, `SyzygyVersion`
- **Errors** — `SyzygyError`, `SyzygyErrorCode`, `SyzygyErrorSeverity`
- **Testing** — `MockNetworkClient`, `MockLogger`, `MockAuthProvider`, `MockStorageProvider`, `MockConnectivityProvider`, `SpyAnalyticsProvider`, `FixtureProvider`, `FixedTimeProvider` (separate import — test targets only)

## Usage

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

## Platform Notes

{PLATFORM_SPECIFIC_API_DIFFERENCES}

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
