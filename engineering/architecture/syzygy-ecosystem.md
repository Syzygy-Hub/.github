<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Ecosystem Architecture

## Overview

Syzygy is an AI-enabled cross-platform engineering framework for mobile, web and enterprise. It is organised as a layered ecosystem where every layer above Foundation is independently usable. No peer layer depends on another peer. Composition happens only at the Base layer, through dependency injection.

The ecosystem has 24 platform repositories (6 layers x 4 platforms: iOS, Android, React Native, Flutter), plus the `Syzygy-Hub/.github` Hub repository. All 24 platform repositories are at version **3.0.0**.

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

## Layers

### syzygy-foundation-*

- **Role**: Root layer. Provides cross-platform contracts and primitives consumed by every peer.
- **Shared contracts (iOS, verified in source)**: `NetworkClientProtocol`, `ConnectivityProvider`, `AuthProvider`, `StorageProvider`, `LoggerProtocol`, `AnalyticsProvider`. Typed error model: `SyzygyFoundationError` (present on Android, verified in source; the other platforms were not re-checked in this pass). Shared primitives include `SyzygyTimestamp` and `SyzygyVersion`.
- **Platforms**: iOS (SPM), Android (JitPack), React Native (npm), Flutter (pub.dev).
- **Status**: 3.0.0 shipped.

### syzygy-ui-*

- **Role**: Cross-platform design system.
- **Position**: Peer sibling. Depends only on Foundation.
- **Provides**: `SyzygyTheme` and runtime theme switching. Theme count and accessibility claims were not verified in this pass.
- **Status**: 3.0.0 shipped.

### syzygy-core-*

- **Role**: Business logic contracts and state management.
- **Position**: Peer sibling. Depends only on Foundation.
- **Provides**: Application-level abstractions, error handling patterns, testable business logic contracts.
- **Status**: 3.0.0 shipped.

### syzygy-services-*

- **Role**: Concrete service implementations.
- **Position**: Peer sibling. Depends only on Foundation.
- **Provides** (iOS, verified in source): `URLSessionNetworkClient` (an implementation of `NetworkClientProtocol`); `JWTAuthProvider` and `SyzygyAuthProvider` (implementations of `AuthProvider`); `KeychainStorageProvider` and `UserDefaultsStorageProvider` (implementations of `StorageProvider`). Other platforms follow the same pattern; they were not re-checked in this pass.
- **Status**: 3.0.0 shipped.

### syzygy-ai-*

- **Role**: AI abstraction layer. Contracts only; no concrete provider ships in these repositories.
- **Position**: Peer sibling. Depends only on Foundation contracts, **not** on Core or Services.
- **Provides** (the shipped surface is defined in [`ai-contract-spec.md`](../standards/ai-contract-spec.md)):
  - `LLMProvider`: `complete` and `stream`
  - `AgentProtocol`: a single `run` entry point. No agent loop ships in 3.0.0.
  - `RAGProvider`: `retrieve`
  - `EmbeddingProvider`: `embed`
  - `MemoryManager` and `NamespacedMemoryManager`: entry-based add, retrieve and clear, plus namespaced operations
  - Also: `ToolCall` and `ToolCallResult`, `AIError`, `JSONValue` (`JsonValue` in Dart), and `AgentRequest.maxSteps` (default 10, clamped to at least 1)
- **Tool and provider integration**: tools are passed on `LLMRequest.tools` and returned on `LLMResponse.toolCalls`. Concrete providers (for example OpenAI, Anthropic or Ollama adapters) are supplied by Services or the application layer, not by the AI repositories.
- **MCP**: MCP is a design goal. No MCP integration is present in the shipped AI code.
- **Status**: 3.0.0 shipped.

#### AI version history

The AI layer was released as `1.0.0` and `1.1.0`, then `3.0.0`. The 2.x line was skipped so that the AI layer matches the 3.0.0 ecosystem release. The sequence is confirmed by the git tags in `syzygy-ai-rn` and `syzygy-ai-ios`.

### syzygy-base-*

- **Role**: Opinionated scaffold and template. The only layer that composes peers.
- **Provides**: Ready-to-start application templates that wire Foundation, UI, Core, Services and AI through dependency injection.
- **Important distinction**: Base is not a library in the same sense as the peer layers. It is a template or scaffold that generates applications with the full Syzygy stack pre-configured.
- **Status**: 3.0.0 shipped.

### Syzygy Example App

- **Role**: Reference implementation of the complete Syzygy stack.
- **Demonstrates**: Networking, concurrency, security, testing and agentic AI patterns.
- **Status**: Planned.

## The Independence Principle

UI, Core, Services and AI may each depend on Foundation abstractions **only**. None of the peer layers depends on any other peer layer. Base is the only place where peer layers are composed, through dependency injection.

- **Consequence 1**: remove AI completely and the rest of Syzygy still compiles and runs.
- **Consequence 2**: take Foundation plus AI alone and build an AI application without adopting UI, Core or Services.

## How Base Wires the Stack

The dependency injection pattern used at the Base layer:

- **Base App** receives all layers.
- Foundation defines the contracts, for example `NetworkClientProtocol`.
- Services provides the concrete implementations, for example `URLSessionNetworkClient`, which satisfy the Foundation contracts.
- AI never imports Services directly.

The same pattern applies to `AuthProvider`, `StorageProvider` and `LoggerProtocol`: Foundation defines the contract, Services (or any consumer-supplied implementation) satisfies it, and every peer resolves the concrete instance through DI wired at Base.

## Platform Distribution

| Layer | iOS | Android | React Native | Flutter |
|---|---|---|---|---|
| Foundation | SPM | JitPack | npm | pub.dev |
| UI | SPM | JitPack | npm | pub.dev |
| Core | SPM | JitPack | npm | pub.dev |
| Services | SPM | JitPack | npm | pub.dev |
| AI | SPM | JitPack | npm | pub.dev |
| Base | Not published (app) | Not published (app) | Not published (app) | Not published (app) |

Registry publishing is platform-specific. Flutter publishes to pub.dev inside `flutter-release.yml`. React Native publishes to npm from each caller's own `publish-npm` job, because npm OIDC trusted publishing needs the caller's workflow file. iOS (SPM) and Android (JitPack) publish nothing beyond the GitHub Release, since the tag is the artefact. Apps (`app-release.yml`) publish nothing.

## Status summary

| Layer | Version | Status |
|---|---|---|
| Foundation | 3.0.0 | Shipped |
| UI | 3.0.0 | Shipped |
| Core | 3.0.0 | Shipped |
| Services | 3.0.0 | Shipped |
| AI | 3.0.0 | Shipped (1.0.0 and 1.1.0 earlier; 2.x skipped) |
| Base | 3.0.0 | Shipped |
| Example App | n/a | Planned |

## Version matrix (generated)

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

## Ecosystem feed and drift rule

The machine-readable feed is `ecosystem/feed.json`, generated from the `syzygy.yml` manifests of the 24 platform repositories plus the Hub entry. Its schema is `engineering/schema/ecosystem-feed.schema.json`, and the tooling is in `engineering/tooling/ecosystem-feed/`. Drift rule: the committed feed and the version matrix above must match what the manifests say. A weekly check (`.github/workflows/ecosystem-drift.yml`) reads the public raw manifests and fails on any difference. It never writes. To fix drift, a maintainer runs `check_drift.py --write` locally, reviews the diff and commits the result.

## Roadmap

- **Flagship Example App**: reference implementation of the full stack (Foundation, UI, Core, Services and AI, composed via Base). Planned.
- **Future AI items** (not in 3.0.0): embedding batching, tool-call completion as a separate method, a defined agent loop with step-budget exhaustion behaviour, and RAG ingestion. See [`ai-contract-spec.md`](../standards/ai-contract-spec.md), section 5.
