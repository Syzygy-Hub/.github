[![iOS](https://img.shields.io/badge/iOS-Swift-FA7343?style=flat&logo=swift&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-ios)
[![Android](https://img.shields.io/badge/Android-Kotlin-7F52FF?style=flat&logo=kotlin&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-android)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-rn)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-0175C2?style=flat&logo=dart&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-flutter)
[![Repos](https://img.shields.io/badge/Repos-20-2F6FED?style=flat&logo=github&logoColor=white)](https://github.com/orgs/Syzygy-Hub/repositories)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](https://github.com/Syzygy-Hub/.github/blob/main/LICENSE)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Engineering Ecosystem for Intelligent Applications

Syzygy is an AI-enabled cross-platform engineering framework for mobile, web and enterprise — a layered ecosystem spanning iOS, Android, React Native and Flutter, with a first-class AI abstraction layer alongside UI, Core and Services. Every layer above Foundation is **independently usable**: adopt only what you need, in any combination, on any platform. Only the Base template composes the full stack.

The name comes from the astronomical term for when celestial bodies align — representing multiple platforms and disciplines coming together into one cohesive, aligned framework.

## Architecture

```
                         SYZYGY
                            │
                 ┌──────────▼──────────┐
                 │ SYZYGY FOUNDATION-* │
                 │                     │
                 │ Base protocols      │
                 │ SharedTypes         │
                 │ Shared contracts    │
                 └──────────┬──────────┘
                            │
        ┌──────────┬────────┼────────┬──────────┐
        │          │        │        │          │
        ▼          ▼        ▼        ▼          ▼
    ┌──────┐   ┌──────┐  ┌──────┐  ┌──────┐   
    │  UI  │   │ CORE │  │ SVCS │  │ AI ✦ │   
    │      │   │      │  │      │  │      │   
    │Design│   │ Biz  │  │ Net/ │  │ LLM/ │   
    │system│   │logic │  │ auth │  │ RAG/ │   
    │      │   │      │  │ /stor│  │agents│   
    └───┬──┘   └───┬──┘  └───┬──┘  └──┬───┘   
        │          │         │        │
        └──────────┴────┬────┴────────┘
                       │
                       ▼
             ┌──────────────────┐
             │  SYZYGY BASE-*   │
             │  (composer)      │
             └────────┬─────────┘
                      │
                      ▼
            ┌──────────────────┐
            │ Syzygy Example   │
            │ App              │
            └──────────────────┘
```

`✦` marks the new AI layer — the centrepiece of the framework's evolution.

## Layers

| Layer | Platforms | Status | Description |
|---|---|---|---|
| **Foundation** | iOS · Android · RN · Flutter | v1.0.0 ✅ | Base protocols, SharedTypes, shared contracts |
| **UI** | iOS · Android · RN · Flutter | v2.4.0 ✅ | Cross-platform design system, `SyzygyTheme`, runtime theme switching |
| **Core** | iOS · Android · RN · Flutter | In progress 🚧 | Business logic contracts, state management |
| **Services** | iOS · Android · RN · Flutter | In progress 🚧 | Networking, auth, storage implementations |
| **AI** ✦ | iOS · Android · RN · Flutter | Planned 📋 | `LLMProvider`, `AgentProtocol`, `RAGProvider`, `MemoryManager`, `StreamHandler` — MCP-native |
| **Base** | iOS · Android · RN · Flutter | Templates ✅ | Opinionated starter, composes all layers |

## Platform targets

- **iOS** — Swift Package Manager (SPM)
- **Android** — JitPack
- **React Native** — npm
- **Flutter** — pub.dev

## Design principles

- **Every layer above Foundation is independently usable** — adopt only what you need
- **No peer layer depends on another peer** — UI, Core, Services and AI each depend only on Foundation
- **Base is the only composer** — dependency injection happens at the application layer, not the library layer

## Roadmap

- **Core v1.0.0** — business-logic contracts and state management across all four platforms
- **Services v1.0.0** — networking, auth and storage implementations against Foundation contracts
- **AI v1.0.0** — `LLMProvider`, `AgentProtocol`, `RAGProvider`, `MemoryManager`, `StreamHandler`; MCP-native
- **Flagship Example App** — reference implementation of the full stack (Foundation + UI + Core + Services + AI, composed via Base)

## Repositories

### Foundation
- [syzygy-foundation-ios](https://github.com/Syzygy-Hub/syzygy-foundation-ios) — v1.0.0
- [syzygy-foundation-android](https://github.com/Syzygy-Hub/syzygy-foundation-android) — v1.0.0
- [syzygy-foundation-rn](https://github.com/Syzygy-Hub/syzygy-foundation-rn) — v1.0.0
- [syzygy-foundation-flutter](https://github.com/Syzygy-Hub/syzygy-foundation-flutter) — v1.0.0

### UI
- [syzygy-ui-ios](https://github.com/Syzygy-Hub/syzygy-ui-ios) — Swift 6 · SwiftUI · v2.4.0
- [syzygy-ui-android](https://github.com/Syzygy-Hub/syzygy-ui-android) — Kotlin · Jetpack Compose · v2.4.0
- [syzygy-ui-rn](https://github.com/Syzygy-Hub/syzygy-ui-rn) — React Native · TypeScript · v2.4.0
- [syzygy-ui-flutter](https://github.com/Syzygy-Hub/syzygy-ui-flutter) — Flutter · Dart · v2.4.0

### Core *(in progress)*
- syzygy-core-ios · syzygy-core-android · syzygy-core-rn · syzygy-core-flutter

### Services *(in progress)*
- syzygy-services-ios · syzygy-services-android · syzygy-services-rn · syzygy-services-flutter

### AI ✦ *(planned)*

- **syzygy-ai-ios** — AI abstraction layer for iOS — LLMProvider, AgentProtocol, RAGProvider, MemoryManager, StreamHandler. Coming soon. 📋 Planned
- **syzygy-ai-android** — AI abstraction layer for Android — LLMProvider, AgentProtocol, RAGProvider, MemoryManager, StreamHandler. Coming soon. 📋 Planned
- **syzygy-ai-rn** — AI abstraction layer for React Native — LLMProvider, AgentProtocol, RAGProvider, MemoryManager, StreamHandler. Coming soon. 📋 Planned
- **syzygy-ai-flutter** — AI abstraction layer for Flutter — LLMProvider, AgentProtocol, RAGProvider, MemoryManager, StreamHandler. Coming soon. 📋 Planned

### Base
- [syzygy-base-ios](https://github.com/Syzygy-Hub/syzygy-base-ios)
- [syzygy-base-android](https://github.com/Syzygy-Hub/syzygy-base-android)
- [syzygy-base-rn](https://github.com/Syzygy-Hub/syzygy-base-rn)
- [syzygy-base-flutter](https://github.com/Syzygy-Hub/syzygy-base-flutter)

Full architecture details: [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md)

## Brand

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-icon-512.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-icon-512.png" alt="Syzygy Icon" height="64">
</picture>

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
