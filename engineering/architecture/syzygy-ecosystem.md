<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Ecosystem Architecture

This is the single authoritative description of the Syzygy ecosystem architecture. Individual repo READMEs describe only their own internal structure and link here for the full picture.

---

## The Ecosystem

```
                         SYZYGY ECOSYSTEM

     ┌─────────────────────────────────────────────────┐
     │                   Your App                      │
     └────────────────────┬────────────────────────────┘
                          │ consumes
                          ▼
     ┌─────────────────────────────────────────────────┐
     │              syzygy-base-{platform}             │
     │                                                 │
     │  Composition · Architecture · DI · Features     │
     └───────┬────────────────┬────────────────┬───────┘
             │                │                │
             ▼                ▼                ▼
     ┌───────────┐   ┌────────────┐   ┌──────────────┐
     │ syzygy-   │   │  syzygy-   │   │   syzygy-    │
     │  ui-*     │   │  core-*    │   │ services-*   │
     │           │   │            │   │              │
     │ Visual    │   │ App infra- │   │ External     │
     │ system    │   │ structure  │   │ world        │
     └─────┬─────┘   └─────┬──────┘   └──────┬───────┘
           │               │                  │
           └───────────────┼──────────────────┘
                           │ all depend on (independently)
                           ▼
     ┌─────────────────────────────────────────────────┐
     │          syzygy-foundation-{platform}           │
     │                                                 │
     │  Contracts · Primitives · Shared Types · Errors │
     └─────────────────────────────────────────────────┘
```

---

## Dependency Rules

These are laws. They are never broken.

| Layer | Depends on | Must never depend on |
|---|---|---|
| Foundation | Nothing | Anything |
| UI | Foundation (optional) | Core, Services |
| Core | Foundation | Services |
| Services | Foundation | Core |
| Base App | All four | — |

**UI must never depend on Core or Services.** Visual components have no business logic and no knowledge of external systems.

**Core must never depend on Services.** The app foundation layer does not call external APIs directly — it coordinates through contracts defined in Foundation.

**Services must never depend on Core.** External integrations implement Foundation contracts and are consumed by Core and Base App, not the other way around.

---

## Layer Responsibilities

### Foundation — `syzygy-foundation-{platform}`

**What it is:** Contracts, primitives, and shared types. Zero implementation.

**What belongs here:**
- Protocols and interfaces (NetworkClientProtocol, StorageProvider, AuthProvider, etc.)
- Generic value types (SyzygyID, Page, SyzygyTimestamp, SyzygyDuration)
- Shared enums and error types (SyzygyEnvironment, SyzygyError, LogLevel)
- Test support contracts (FixtureProvider, TimeProvider)

**What does NOT belong here:**
- Any class with behaviour beyond property storage
- Any reference to platform APIs (UIKit, Android SDK, React Native APIs, Flutter widgets)
- Network implementations
- Storage implementations
- Authentication logic
- Business logic of any kind
- Pagination state (belongs in Core)
- Specific error types (NetworkError, AuthError — belong in Services)
- ValidationRule implementations (belong in the consuming layer)

---

### UI — `syzygy-ui-{platform}`

**What it is:** Visual component library with design tokens and theming. Zero business logic.

**What belongs here:**
- SwiftUI views, Composables, React Native components, Flutter widgets
- Design tokens (colors, typography, spacing, radius, elevation, animation)
- Theme system (SyzygyTheme, SyzygyThemeProvider)
- Layout components

**What does NOT belong here:**
- Network calls
- Local storage
- Authentication logic
- Navigation logic (belongs in Core)
- Analytics tracking beyond UI events
- Any import of syzygy-core-* or syzygy-services-*

---

### Core — `syzygy-core-{platform}`

**What it is:** App infrastructure — the utilities and architecture scaffolding every app rebuilds from scratch.

**What belongs here:**
- Extensions on standard library types
- DI container / service locator
- Navigation framework
- State management utilities
- Security utilities (keychain, encryption)
- Architecture patterns (MVVM, Clean Architecture base classes)
- Testing helpers for app-layer testing

**What does NOT belong here:**
- External API calls (belongs in Services)
- Visual components (belongs in UI)
- Fundamental contracts (belongs in Foundation)
- Business-domain logic (belongs in the consuming app)

---

### Services — `syzygy-services-{platform}`

**What it is:** Concrete implementations of Foundation contracts for the external world.

**What belongs here:**
- Network client implementation (URLSession, OkHttp, fetch, Dio)
- Storage implementations (UserDefaults/Keychain, SharedPrefs, AsyncStorage, SharedPreferences)
- Analytics providers (Firebase, Segment, custom)
- Push notification handling
- Media and camera services
- OS-level integrations (connectivity monitoring, biometrics, location)

**What does NOT belong here:**
- Business logic
- UI components
- Navigation
- Domain-specific models (belongs in the consuming app)

---

### Base App — `syzygy-base-{platform}`

**What it is:** A production-ready starter that wires all four layers together.

**What belongs here:**
- DI setup and module registration
- Feature scaffolding
- App entry point and configuration
- CI/CD pipeline

**What does NOT belong here:**
- Reusable library code (if it's reusable, it belongs in one of the four layers above)

---

## Platform Support Matrix

| Package | iOS | Android | React Native | Flutter |
|---|:---:|:---:|:---:|:---:|
| syzygy-foundation-* | ✅ v1.0.0 | ✅ v1.0.0 | ✅ v1.0.0 | ✅ v1.0.0 |
| syzygy-ui-* | ✅ v2.4.0 | ✅ v2.4.0 | ✅ v2.4.0 | ✅ v2.4.0 |
| syzygy-core-* | ⏳ | ⏳ | ⏳ | ⏳ |
| syzygy-services-* | ⏳ | ⏳ | ⏳ | ⏳ |
| syzygy-base-* | ✅ | ✅ | ✅ | ✅ |

✅ Available · ⏳ In progress · ⬜ Not started

---

## Package Identifiers

| Repo | iOS (SPM) | Android (JitPack) | RN (npm) | Flutter (pub.dev) |
|---|---|---|---|---|
| Foundation | `syzygy-foundation-ios` | `com.syzygyhub:foundation-android` | `syzygy-foundation-rn` | `syzygy_foundation_flutter` |
| UI | `syzygy-ui-ios` | `com.syzygyhub:ui-android` | `syzygy-ui-rn` | `syzygy_ui_flutter` |
| Core | `syzygy-core-ios` | `com.syzygyhub:core-android` | `syzygy-core-rn` | `syzygy_core_flutter` |
| Services | `syzygy-services-ios` | `com.syzygyhub:services-android` | `syzygy-services-rn` | `syzygy_services_flutter` |
