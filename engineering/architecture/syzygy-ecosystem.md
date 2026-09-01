<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Ecosystem Architecture

## Overview

Syzygy is an AI-enabled cross-platform engineering framework for mobile, web and enterprise. It is organised as a layered ecosystem where every layer above Foundation is independently usable. No peer layer depends on another peer — composition happens only at the Base layer through dependency injection.

## Architecture

```
                    syzygy-foundation-*
                            |
       +------------+----------------+------------+
       v            v                v            v
   syzygy-ui-*  syzygy-core-*  syzygy-services-*  syzygy-ai-*
       |            |                |            |
       +------------+----------------+------------+
                            |
                            v
                     syzygy-base-*
                     (composer/scaffold)
                            |
                            v
                  Syzygy Example App
```

## Layers

### syzygy-foundation-*

- **Role**: Root layer. Provides `SharedTypes`, `SyzygyVersion`, and shared contracts consumed by every peer.
- **Shared contracts**: `NetworkClientProtocol`, `AuthProvider`, `StorageProvider`, `LoggerProtocol`.
- **Platforms**: iOS (SPM), Android (JitPack), React Native (npm), Flutter (pub.dev).
- **Status**: v1.0.0 shipped.

### syzygy-ui-*

- **Role**: Cross-platform design system.
- **Position**: Peer sibling. Depends only on Foundation.
- **Provides**: `SyzygyTheme`, runtime theme switching, 3 built-in themes, accessibility-first components.
- **Status**: v2.4.0 shipped.

### syzygy-core-*

- **Role**: Business logic contracts and state management.
- **Position**: Peer sibling. Depends only on Foundation.
- **Provides**: Application-level abstractions, error handling patterns, testable business logic contracts.
- **Status**: In progress.

### syzygy-services-*

- **Role**: Concrete service implementations.
- **Position**: Peer sibling. Depends only on Foundation.
- **Provides**: `URLSession` / `OkHttp` / `Axios` / `Dio` implementations of `NetworkClientProtocol`; OAuth implementations of `AuthProvider`; Keychain / SharedPrefs / SecureStorage implementations of `StorageProvider`.
- **Status**: In progress.

### syzygy-ai-* (AI centrepiece)

- **Role**: AI abstraction layer.
- **Position**: Peer sibling. Depends only on Foundation contracts — **NOT** on Core or Services.
- **Provides**:
  - `LLMProvider` — provider-agnostic model interface
  - `AgentProtocol` — ReAct loop formalisation
  - `RAGProvider` — retrieval abstraction
  - `MemoryManager` — short- and long-term context
  - `StreamHandler` — streaming response handling
- **MCP-native**: designed to work with Model Context Protocol tool servers.
- **Provider-agnostic**: works with OpenAI, Anthropic Claude, Google Gemini, and local models via Ollama.
- **Status**: Planned — next major milestone.

### syzygy-base-*

- **Role**: Opinionated scaffold and template. The only layer that composes peers.
- **Provides**: Ready-to-start application templates that wire Foundation + UI + Core + Services + AI via dependency injection.
- **Important distinction**: Base is not a library in the same sense as the peer layers. It is a template/scaffold that generates applications with the full Syzygy stack pre-configured.
- **Status**: Templates available.

### Syzygy Example App

- **Role**: Reference implementation of the complete Syzygy stack.
- **Demonstrates**: Networking, Concurrency, Security, Testing, and Agentic AI patterns.
- **Status**: Planned.

## The Independence Principle

UI, Core, Services and AI may each depend on Foundation abstractions **only**. None of the peer layers depends on any other peer layer. Base is the only place where peer layers are composed — through dependency injection.

- **Consequence 1**: remove AI completely and the rest of Syzygy still compiles and runs.
- **Consequence 2**: take Foundation plus AI alone and build an AI application without adopting UI, Core or Services.

## How Base Wires the Stack

The dependency injection pattern used at the Base layer:

- **Base App** receives all layers.
- **syzygy-ai** receives `NetworkClientProtocol` from Foundation.
- **syzygy-services** provides `URLSessionNetworkClient` which implements `NetworkClientProtocol`.
- The concrete implementation from Services satisfies the abstract contract from Foundation.
- AI never imports Services directly.

The same pattern applies to `AuthProvider`, `StorageProvider`, and `LoggerProtocol`: Foundation defines the contract, Services (or any consumer-supplied implementation) satisfies it, and every peer resolves the concrete instance through DI wired at Base.

## Platform Distribution

| Layer | iOS | Android | React Native | Flutter |
|---|---|---|---|---|
| Foundation | SPM | JitPack | npm | pub.dev |
| UI | SPM | JitPack | npm | pub.dev |
| Core | SPM | JitPack | npm | pub.dev |
| Services | SPM | JitPack | npm | pub.dev |
| AI | SPM | JitPack | npm | pub.dev |

## Roadmap

- **Foundation v1.0.0** — shipped
- **UI v2.4.0** — shipped
- **Core v1.0.0** — in progress
- **Services v1.0.0** — in progress
- **AI v1.0.0** — planned (next major milestone)
- **Flagship Example App** — planned
