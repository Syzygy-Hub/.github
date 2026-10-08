<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

[![iOS](https://img.shields.io/badge/iOS-Swift-FA7343?style=flat&logo=swift&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-ios)
[![Android](https://img.shields.io/badge/Android-Kotlin-7F52FF?style=flat&logo=kotlin&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-android)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-rn)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-0175C2?style=flat&logo=dart&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-flutter)
[![Repos](https://img.shields.io/badge/Repos-25-2F6FED?style=flat&logo=github&logoColor=white)](https://github.com/orgs/Syzygy-Hub/repositories)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](https://github.com/Syzygy-Hub/.github/blob/main/LICENSE)

# Engineering Ecosystem for Intelligent Applications

Syzygy is an AI-enabled cross-platform engineering framework for mobile, web and enterprise — a layered ecosystem spanning iOS, Android, React Native and Flutter, with a first-class AI abstraction layer alongside UI, Core and Services. Every layer above Foundation is **independently usable**: adopt only what you need, in any combination, on any platform. Only the Base template composes the full stack.

The name comes from the astronomical term for when celestial bodies align — representing multiple platforms and disciplines coming together into one cohesive, aligned framework.

## Architecture

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

`✦` marks the new AI layer — the centrepiece of the framework's evolution.

## Layers

| Layer | Platforms | Status | Description |
|---|---|---|---|
| **Foundation** | iOS · Android · RN · Flutter | v3.0.0 ✅ | Cross-platform contracts, shared primitives and typed error model |
| **UI** | iOS · Android · RN · Flutter | v3.0.0 ✅ | Cross-platform design system, `SyzygyTheme`, runtime theme switching |
| **Core** | iOS · Android · RN · Flutter | v3.0.0 ✅ | Business logic contracts, state management |
| **Services** | iOS · Android · RN · Flutter | v3.0.0 ✅ | Networking, auth, storage implementations |
| **AI** ✦ | iOS · Android · RN · Flutter | v3.0.0 ✅ | LLMProvider, AgentProtocol, RAGProvider, EmbeddingProvider, MemoryManager — contracts only |
| **Base** | iOS · Android · RN · Flutter | v3.0.0 ✅ | Opinionated starter that composes all layers |
| **Examples** | iOS · Android · RN · Flutter | Planned 🔲 | Reference implementation of the full stack |

### Version matrix

<!-- ECOSYSTEM:START -->
<!-- Generated from ecosystem/feed.json by engineering/tooling/ecosystem-feed/check_drift.py. Do not edit by hand. -->
| Layer | iOS | Android | React Native | Flutter |
|---|---|---|---|---|
| Foundation | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) |
| UI | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) |
| Core | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) |
| Services | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) |
| AI | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) |
| Base | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) | 3.0.0 (shipped) |

Hub repository (`.github`): version not recorded, status unknown.
<!-- ECOSYSTEM:END -->

## Platform targets

- **iOS** — Swift Package Manager (SPM)
- **Android** — JitPack
- **React Native** — npm
- **Flutter** — pub.dev

Registry publishing is platform-specific. Flutter publishes to pub.dev inside `flutter-release.yml`. React Native publishes to npm from each caller's own `publish-npm` job, because npm OIDC trusted publishing needs the caller's workflow file. iOS (SPM) and Android (JitPack) publish nothing beyond the GitHub Release, since the tag is the artefact. Apps (`app-release.yml`) publish nothing.

## Design principles

- **Every layer above Foundation is independently usable** — adopt only what you need
- **No peer layer depends on another peer** — UI, Core, Services and AI each depend only on Foundation
- **Base is the only composer** — dependency injection happens at the application layer, not the library layer

## Roadmap

- **Flagship Example App** — reference implementation of the full stack (Foundation + UI + Core + Services + AI, composed via Base)

## Repositories

### Foundation
- [syzygy-foundation-ios](https://github.com/Syzygy-Hub/syzygy-foundation-ios) — Base protocols and shared contracts · v3.0.0
- [syzygy-foundation-android](https://github.com/Syzygy-Hub/syzygy-foundation-android) — Base protocols and shared contracts · v3.0.0
- [syzygy-foundation-rn](https://github.com/Syzygy-Hub/syzygy-foundation-rn) — Base protocols and shared contracts · v3.0.0
- [syzygy-foundation-flutter](https://github.com/Syzygy-Hub/syzygy-foundation-flutter) — Base protocols and shared contracts · v3.0.0

### UI
- [syzygy-ui-ios](https://github.com/Syzygy-Hub/syzygy-ui-ios) — Swift 6 · SwiftUI · v3.0.0
- [syzygy-ui-android](https://github.com/Syzygy-Hub/syzygy-ui-android) — Kotlin · Jetpack Compose · v3.0.0
- [syzygy-ui-rn](https://github.com/Syzygy-Hub/syzygy-ui-rn) — React Native · TypeScript · v3.0.0
- [syzygy-ui-flutter](https://github.com/Syzygy-Hub/syzygy-ui-flutter) — Flutter · Dart · v3.0.0

### Core
- [syzygy-core-ios](https://github.com/Syzygy-Hub/syzygy-core-ios) — Business logic contracts · v3.0.0
- [syzygy-core-android](https://github.com/Syzygy-Hub/syzygy-core-android) — Business logic contracts · v3.0.0
- [syzygy-core-rn](https://github.com/Syzygy-Hub/syzygy-core-rn) — Business logic contracts · v3.0.0
- [syzygy-core-flutter](https://github.com/Syzygy-Hub/syzygy-core-flutter) — Business logic contracts · v3.0.0

### Services
- [syzygy-services-ios](https://github.com/Syzygy-Hub/syzygy-services-ios) — Networking, auth and storage implementations · v3.0.0
- [syzygy-services-android](https://github.com/Syzygy-Hub/syzygy-services-android) — Networking, auth and storage implementations · v3.0.0
- [syzygy-services-rn](https://github.com/Syzygy-Hub/syzygy-services-rn) — Networking, auth and storage implementations · v3.0.0
- [syzygy-services-flutter](https://github.com/Syzygy-Hub/syzygy-services-flutter) — Networking, auth and storage implementations · v3.0.0

### AI ✦
- [syzygy-ai-ios](https://github.com/Syzygy-Hub/syzygy-ai-ios) — AI contracts for iOS — LLMProvider, AgentProtocol, RAGProvider, EmbeddingProvider, MemoryManager · v3.0.0
- [syzygy-ai-android](https://github.com/Syzygy-Hub/syzygy-ai-android) — AI contracts for Android — LLMProvider, AgentProtocol, RAGProvider, EmbeddingProvider, MemoryManager · v3.0.0
- [syzygy-ai-rn](https://github.com/Syzygy-Hub/syzygy-ai-rn) — AI contracts for React Native — LLMProvider, AgentProtocol, RAGProvider, EmbeddingProvider, MemoryManager · v3.0.0
- [syzygy-ai-flutter](https://github.com/Syzygy-Hub/syzygy-ai-flutter) — AI contracts for Flutter — LLMProvider, AgentProtocol, RAGProvider, EmbeddingProvider, MemoryManager · v3.0.0

### Base
- [syzygy-base-ios](https://github.com/Syzygy-Hub/syzygy-base-ios) — Opinionated starter that composes all layers · v3.0.0
- [syzygy-base-android](https://github.com/Syzygy-Hub/syzygy-base-android) — Opinionated starter that composes all layers · v3.0.0
- [syzygy-base-rn](https://github.com/Syzygy-Hub/syzygy-base-rn) — Opinionated starter that composes all layers · v3.0.0
- [syzygy-base-flutter](https://github.com/Syzygy-Hub/syzygy-base-flutter) — Opinionated starter that composes all layers · v3.0.0

Full architecture details: [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md)

## Brand

Brand assets — logo, icon, banners, and color palette — are hosted in this repository under [`brand/`](https://github.com/Syzygy-Hub/.github/tree/main/brand). See [BRAND_GUIDE.md](https://github.com/Syzygy-Hub/.github/blob/main/brand/BRAND_GUIDE.md) for usage guidelines, clear space rules, minimum sizes, and correct/incorrect usage examples.

**Color palette:** Purple ![7F77DD](https://img.shields.io/badge/-%237F77DD-7F77DD?style=flat-square) `#7F77DD` · Teal ![1D9E75](https://img.shields.io/badge/-%231D9E75-1D9E75?style=flat-square) `#1D9E75` · Coral ![D85A30](https://img.shields.io/badge/-%23D85A30-D85A30?style=flat-square) `#D85A30`

**Typography:** [Sora](https://fonts.google.com/specimen/Sora) for the wordmark and headings · [Inter](https://fonts.google.com/specimen/Inter) (or the platform system font — SF Pro on iOS, Roboto on Android) for body copy

## Org links

- [All Syzygy-Hub repositories](https://github.com/orgs/Syzygy-Hub/repositories)
- [Engineering standards](https://github.com/Syzygy-Hub/.github/tree/main/engineering/standards)
- [Architecture overview](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md)
- [Brand guide](https://github.com/Syzygy-Hub/.github/blob/main/brand/BRAND_GUIDE.md)
- [License](https://github.com/Syzygy-Hub/.github/blob/main/LICENSE)

## About

Built and maintained by [Ayush Kumar Sethi](https://github.com/aks5686) — Mobile Technical Architect with 15+ years across iOS, Android, React Native & Flutter.
