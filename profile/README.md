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

Syzygy is a cross-platform mobile ecosystem — production-ready Foundation, UI, Core and Service libraries, plus starter templates, spanning iOS, Android, React Native, and Flutter.

The name comes from the astronomical term for when celestial bodies align — representing multiple platforms coming together into one cohesive, aligned ecosystem.

## Why Syzygy

Every UI library ships with zero third-party dependencies and the same shared token system — colors, typography, spacing, radius — reproduced consistently across all four platforms, with full Dark Mode support built in from the start. Component naming and API shape stay deliberately consistent cross-platform (the same problem is solved the same way in SwiftUI, Jetpack Compose, React Native, and Flutter), and every repo shares the same CI pipeline and tag-gated release process.

## Ecosystem

Syzygy is a four-layer architecture. Each layer is independent and can be used without the others.

```
  syzygy-ui-*       syzygy-core-*    syzygy-services-*
  Presentation       App foundation   External world
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
               syzygy-foundation-*
               Contracts & primitives
```

- **Foundation** — contracts, primitives, shared types. Zero implementation. Every other layer depends on this.
- **UI** — visual component libraries with design tokens, theming, and dark mode. Zero business logic.
- **Core** — app foundation, navigation, DI, security, architecture utilities. *(in progress)*
- **Services** — networking, storage, analytics, OS integrations. *(in progress)*

Full architecture details: [syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md)

## Architecture

```
                         SYZYGY
                            │
                 ┌──────────▼──────────┐
                 │ SYZYGY FOUNDATION-* │
                 │                     │
                 │ Primitives          │
                 │ Contracts           │
                 │ Shared types        │
                 │ Errors              │
                 └──────────┬──────────┘
                            │
            ┌───────────────┼────────────────┐
            │               │                │
            ▼               ▼                ▼
       ┌─────────┐     ┌─────────┐     ┌──────────┐
       │   UI    │     │  CORE   │     │ SERVICES │
       │         │     │         │     │          │
       │ Visual  │     │ Business│     │ External │
       │ system  │     │ logic   │     │ world    │
       └────┬────┘     └────┬────┘     └─────┬────┘
            │               │                │
            └───────────────┼────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │  SYZYGY BASE APP │
                  └──────────────────┘
```

### Status

| Layer | iOS | Android | React Native | Flutter |
|---|:---:|:---:|:---:|:---:|
| UI | ✅ | ✅ | ✅ | ✅ |
| Foundation | ✅ | ✅ | ✅ | ✅ |
| Core | ⬜ | ⬜ | ⬜ | ⬜ |
| Services | ⬜ | ⬜ | ⬜ | ⬜ |
| Base App | 🚧 | 🚧 | 🚧 | 🚧 |

✅ Available &nbsp;·&nbsp; 🚧 In progress &nbsp;·&nbsp; ⬜ Not started

### Foundation
Primitives, contracts, shared types, errors — the base every other layer depends on.

- [syzygy-foundation-ios](https://github.com/Syzygy-Hub/syzygy-foundation-ios) — v1.0.0
- [syzygy-foundation-android](https://github.com/Syzygy-Hub/syzygy-foundation-android) — v1.0.0
- [syzygy-foundation-rn](https://github.com/Syzygy-Hub/syzygy-foundation-rn) — v1.0.0
- [syzygy-foundation-flutter](https://github.com/Syzygy-Hub/syzygy-foundation-flutter) — v1.0.0

### UI
Component libraries with design tokens, theming, and dark mode support.

- [syzygy-ui-ios](https://github.com/Syzygy-Hub/syzygy-ui-ios) — Swift 6 · SwiftUI · v2.4.0
- [syzygy-ui-android](https://github.com/Syzygy-Hub/syzygy-ui-android) — Kotlin · Jetpack Compose · v2.4.0
- [syzygy-ui-rn](https://github.com/Syzygy-Hub/syzygy-ui-rn) — React Native · TypeScript · v2.4.0
- [syzygy-ui-flutter](https://github.com/Syzygy-Hub/syzygy-ui-flutter) — Flutter · Dart · v2.4.0

### Core
App foundation — navigation, state management, dependency injection, and architecture utilities.

- syzygy-core-ios *(coming)*
- syzygy-core-android *(coming)*
- syzygy-core-rn *(coming)*
- syzygy-core-flutter *(coming)*

### Services
External world integrations — networking, storage, analytics, authentication, and OS services.

- syzygy-services-ios *(coming)*
- syzygy-services-android *(coming)*
- syzygy-services-rn *(coming)*
- syzygy-services-flutter *(coming)*

### Base App
Production-ready starter that composes all four layers — Clean Architecture, DI wiring, feature scaffolding, and CI/CD.

- [syzygy-base-ios](https://github.com/Syzygy-Hub/syzygy-base-ios)
- [syzygy-base-android](https://github.com/Syzygy-Hub/syzygy-base-android)
- [syzygy-base-rn](https://github.com/Syzygy-Hub/syzygy-base-rn)
- [syzygy-base-flutter](https://github.com/Syzygy-Hub/syzygy-base-flutter)

## Brand

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-icon-512.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-icon-512.png" alt="Syzygy Icon" height="64">
</picture>

Brand assets — logo, icon, banners, and color palette — are hosted in this repository under [`brand/`](https://github.com/Syzygy-Hub/.github/tree/main/brand). See [BRAND_GUIDE.md](https://github.com/Syzygy-Hub/.github/blob/main/brand/BRAND_GUIDE.md) for usage guidelines, clear space rules, minimum sizes, and correct/incorrect usage examples.

**Color palette:** Purple `#7F77DD` · Teal `#1D9E75` · Coral `#D85A30`

**Typography:** [Sora](https://fonts.google.com/specimen/Sora) for the wordmark and headings · [Inter](https://fonts.google.com/specimen/Inter) (or the platform system font — SF Pro on iOS, Roboto on Android) for body copy

**Available assets:**
- `syzygy-banner-dark/light` — SVG, PNG (1200 · 2400px), WebP
- `syzygy-icon` — SVG, PNG (32 · 192 · 512 · 1024px), WebP

## About

Built and maintained by [Ayush Kumar Sethi](https://github.com/aks5686) — Mobile Technical Architect with 15+ years across iOS, Android, React Native & Flutter.
