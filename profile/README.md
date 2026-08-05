[![iOS](https://img.shields.io/badge/iOS-Swift%206%20%7C%20SwiftUI-blue?style=flat&logo=swift&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-ios)
[![Android](https://img.shields.io/badge/Android-Kotlin%20%7C%20Compose-brightgreen?style=flat&logo=android&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-android)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-61DAFB?style=flat&logo=react&logoColor=black)](https://github.com/Syzygy-Hub/syzygy-ui-rn)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-02569B?style=flat&logo=flutter&logoColor=white)](https://github.com/Syzygy-Hub/syzygy-ui-flutter)
[![Repos](https://img.shields.io/badge/Repos-12-orange?style=flat&logo=github&logoColor=white)](https://github.com/orgs/Syzygy-Hub/repositories)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Syzygy-Hub/syzygy-ui-ios/blob/main/LICENSE)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/Assets/syzygy-banner-dark-2400.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/Assets/syzygy-banner-light-2400.png" alt="Syzygy">
</picture>

Syzygy is a cross-platform mobile ecosystem — production-ready Foundation, UI, Core and Service libraries, plus starter templates, spanning iOS, Android, React Native, and Flutter.

The name comes from the astronomical term for when celestial bodies align — representing multiple platforms coming together into one cohesive, aligned ecosystem.

## Why Syzygy

Every UI library ships with zero third-party dependencies and the same shared token system — colors, typography, spacing, radius — reproduced consistently across all four platforms, with full Dark Mode support built in from the start. Component naming and API shape stay deliberately consistent cross-platform (the same problem is solved the same way in SwiftUI, Jetpack Compose, React Native, and Flutter), and every repo shares the same CI pipeline and tag-gated release process.

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
                 │ Constants           │
                 │ Lint / formatting   │
                 │ Build conventions   │
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
                  │                  │
                  │ Composition      │
                  │ Architecture     │
                  │ DI               │
                  │ Features         │
                  │ Configuration    │
                  └──────────────────┘
```

### Status

| Layer | iOS | Android | React Native | Flutter |
|---|:---:|:---:|:---:|:---:|
| UI | ✅ | ✅ | ✅ | ✅ |
| Foundation | 🚧 | 🚧 | 🚧 | 🚧 |
| Core | ⬜ | ⬜ | ⬜ | ⬜ |
| Services | ⬜ | ⬜ | ⬜ | ⬜ |
| Base App | 🚧 | 🚧 | 🚧 | 🚧 |

✅ Available &nbsp;·&nbsp; 🚧 In progress &nbsp;·&nbsp; ⬜ Not started

### Foundation
Primitives, contracts, shared types, errors, constants, lint and build conventions — the base every other layer depends on.

- [syzygy-foundation-ios](https://github.com/Syzygy-Hub/syzygy-foundation-ios)
- [syzygy-foundation-android](https://github.com/Syzygy-Hub/syzygy-foundation-android)
- [syzygy-foundation-rn](https://github.com/Syzygy-Hub/syzygy-foundation-rn)
- [syzygy-foundation-flutter](https://github.com/Syzygy-Hub/syzygy-foundation-flutter)

### UI
Component libraries with design tokens, theming, and dark mode support.

- [syzygy-ui-ios](https://github.com/Syzygy-Hub/syzygy-ui-ios) — Swift 6 · SwiftUI
- [syzygy-ui-android](https://github.com/Syzygy-Hub/syzygy-ui-android) — Kotlin · Jetpack Compose
- [syzygy-ui-rn](https://github.com/Syzygy-Hub/syzygy-ui-rn) — React Native · TypeScript
- [syzygy-ui-flutter](https://github.com/Syzygy-Hub/syzygy-ui-flutter) — Flutter · Dart

### Core
App Core — navigation, state management, dependency injection, and shared business logic.

- syzygy-core-ios
- syzygy-core-android
- syzygy-core-rn
- syzygy-core-flutter

### Services
External world integrations — networking, storage, analytics, authentication, and third-party SDKs.

- syzygy-services-ios
- syzygy-services-android
- syzygy-services-rn
- syzygy-services-flutter

### Base App
Production-ready starter that composes all four layers — Clean Architecture, DI wiring, feature scaffolding, and CI/CD.

- [syzygy-base-ios](https://github.com/Syzygy-Hub/syzygy-base-ios)
- [syzygy-base-android](https://github.com/Syzygy-Hub/syzygy-base-android)
- [syzygy-base-rn](https://github.com/Syzygy-Hub/syzygy-base-rn)
- [syzygy-base-flutter](https://github.com/Syzygy-Hub/syzygy-base-flutter)

## Brand

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/Assets/syzygy-icon.svg">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/Assets/syzygy-icon.svg" alt="Syzygy Icon" height="64">
</picture>

Brand assets — logo, icon, banners, and color palette — are hosted in this repository under [`Assets/`](https://github.com/Syzygy-Hub/.github/tree/main/Assets). See [BRAND_GUIDE.md](https://github.com/Syzygy-Hub/.github/blob/main/BRAND_GUIDE.md) for usage guidelines, clear space rules, minimum sizes, and correct/incorrect usage examples.

**Color palette:** Purple `#7F77DD` · Teal `#1D9E75` · Coral `#D85A30`

**Typography:** [Sora](https://fonts.google.com/specimen/Sora) for the wordmark and headings · [Inter](https://fonts.google.com/specimen/Inter) (or the platform system font — SF Pro on iOS, Roboto on Android) for body copy

**Available assets:**
- `syzygy-banner-dark/light` — SVG, PNG (1200 · 2400px), WebP
- `syzygy-icon` — SVG, PNG (32 · 192 · 512 · 1024px), WebP

## About

Built and maintained by [Ayush Kumar Sethi](https://github.com/aks5686) — Mobile Technical Architect with 15+ years across iOS, Android, React Native & Flutter.
