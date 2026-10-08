<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# AI Contract Specification — v3.0.0

This document describes the AI contracts that the four `syzygy-ai-*` repositories (iOS, Android, React Native, Flutter) **actually ship** at 3.0.0. It replaces the v1.1.0 draft, which described a wider surface than any platform implements.

**Source of truth:** the code under `AI/{ios,android,rn,flutter}/src/syzygy-ai-*` in the local workspace. Where this document and the code disagree, the code wins and this document must be corrected.

**Version history:** the AI layer was released as 1.0.0 and 1.1.0, then 3.0.0. The 2.x line was skipped so that the AI layer version matches the 3.0.0 ecosystem release. Git tags in `syzygy-ai-rn` and `syzygy-ai-ios` confirm this sequence (`1.0.0`, `1.1.0`, `3.0.0`).

Conventions used below:

- **Present**: the item exists on that platform with the same semantics.
- **Differs**: the item exists but the name, shape or types differ from the other platforms. The difference is noted.
- **Absent**: the item is not in the shipped code.
- **Undefined**: the code does not specify the behaviour, so this spec does not define it either.

---

## 1. Shipped contract surface

### 1.1 Shared value types

| Type | iOS (Swift) | Android (Kotlin) | RN (TypeScript) | Flutter (Dart) |
|---|---|---|---|---|
| Message | `LLMMessage` (struct, `Role`: user/assistant/system/tool) | `LLMMessage` | `LLMMessage` (`MessageRole` union) | `LLMMessage` (`MessageRole` enum) |
| Request | `LLMRequest` (`messages`, `model`, `temperature?`, `maxTokens?`, `topP?`, `stopSequences`, `requestId?`, `correlationId?`, `tools?`) | `LLMRequest` data class (same fields) | `LLMRequest` interface (same fields) | `LLMRequest` class (same fields) |
| Response | `LLMResponse` (`content`, `tokenUsage?`, `finishReason?`, `providerName?`, `modelName?`, `toolCalls?`) | `LLMResponse` data class (same fields) | `LLMResponse` interface (same fields) | `LLMResponse` class (same fields) |
| Stream chunk | `LLMChunk` (`content?`, `toolCallDelta?`, `finishReason?`, `metadata`, `providerName?`, `modelName?`) | `LLMChunk` data class (same fields) | `LLMChunk` interface (same fields) | `LLMChunk` class (same fields) |
| Token usage | `TokenUsage` | `TokenUsage` | `TokenUsage` | `TokenUsage` |
| Finish reason | `FinishReason` (`stop`, `length`, `toolCall`, `contentFilter`, `error`) | `FinishReason` enum (`STOP`, `LENGTH`, `TOOL_CALL`, `CONTENT_FILTER`, `ERROR`) | `FinishReason` string union (`'tool_call'`, `'content_filter'` etc.) | `FinishReason` enum |
| Tool call | `ToolCall` (`id`, `name`, `arguments: JSONObject`) | `ToolCall` (`id`, `name`, `arguments: JSONObject`) | `ToolCall` | `ToolCall` (`arguments: JsonMap`) |
| Tool result | `ToolCallResult` | `ToolCallResult` | `ToolCallResult` | `ToolCallResult` |
| Tool definition | `AgentTool` | `AgentTool` | `AgentTool` | `AgentTool` |
| JSON value | `JSONValue` (`Types/JSONValue.swift`) | `JSONValue` (`types/JSONValue.kt`) | `JSONValue` type alias (`types/JSONValue.ts`) | `JsonValue` sealed class (`types/json_value.dart`), with `JsonMap` typedef |
| Error | `AIError` enum | `AIError` sealed class | `AIError` class with `code: AIErrorCode` | `AIError` sealed class |
| Embedding | `Embedding` (`values: [Float]`, `dimensions`, `metadata`) | `Embedding` (`values: FloatArray`, `dimensions`, `metadata`) | `Embedding` (`values: number[]`, `dimensions`, `metadata?`) | `Embedding` (`dimensions: int`) |
| Memory entry | `MemoryEntry` (`timestamp: SyzygyTimestamp`) | `MemoryEntry` (`timestamp: SyzygyTimestamp`) | `MemoryEntry` (`timestamp: SyzygyTimestamp`) | `MemoryEntry` (`timestamp: SyzygyTimestamp`) |
| Conversation turn | `ConversationTurn` | `ConversationTurn` | `ConversationTurn` | `ConversationTurn` |
| RAG chunk / options | `RAGChunk`, `RAGOptions` | `RAGChunk`, `RAGOptions` | `RAGChunk`, `RAGOptions` (`maxResults?`, `scoreThreshold?`, `metadata?`) | `RAGChunk`, `RAGOptions` |

### 1.2 `AIError`

The cases are the same six on every platform. Only the representation differs.

| Case | iOS | Android | RN (`code`) | Flutter |
|---|---|---|---|---|
| Authentication | `.authenticationFailure(String)` | `AuthenticationFailure` | `authentication_failure` | `AuthenticationFailure` |
| Rate limit | `.rateLimited(retryAfterMs: Int?)` | `RateLimited(retryAfterMs: Long?)` | `rate_limited` (`retryAfterMs?`) | `RateLimited(retryAfterMs: int?)` |
| Network | `.networkError(underlying: Error)` | `NetworkError(cause)` | `network_error` | `AINetworkError(message, cause?)` (**differs**: class name) |
| Invalid request | `.invalidRequest(String)` | `InvalidRequest` | `invalid_request` | `InvalidRequest` |
| Provider failure | `.providerFailure(String)` | `ProviderFailure` | `provider_failure` | `ProviderFailure` |
| Cancelled | `.cancelled` | `Cancelled` | `cancelled` | `Cancelled` |

Notes:

- The v1.1.0 `AIError` table (`code`, `message`, `underlyingError`) is **not** the shipped shape. iOS, Android and Flutter model errors as typed cases. RN uses a `code` string field. None of the platforms exposes a generic `underlyingError` field on every case.
- Flutter's `AIError` has a `message` field. It has no `code` field.

### 1.3 `JSONValue`

All platforms define a recursive JSON value type covering null, bool, number, string, array and object. The Dart type is named `JsonValue` (not `JSONValue`), which differs from the other three.

### 1.4 Tool calls

The v1.1.0 name `ToolCallRequest` is **absent**. The shipped type is `ToolCall` (`id`, `name`, `arguments`). `ToolCallResult` is present under the same name.

---

## 2. Contract modules

### 2.1 `LLMProvider`

| Method | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| Blocking completion | `complete(_ request: LLMRequest) async throws -> LLMResponse` | `suspend fun complete(request: LLMRequest): LLMResponse` | `complete(request: LLMRequest): Promise<LLMResponse>` | `Future<LLMResponse> complete(LLMRequest request)` |
| Streaming | `stream(_ request: LLMRequest) -> AsyncThrowingStream<LLMChunk, Error>` | `fun stream(request: LLMRequest): Flow<LLMChunk>` | `stream(request: LLMRequest): AsyncIterable<LLMChunk>` | `Stream<LLMChunk> stream(LLMRequest request)` |
| Tools in completion | **Absent** as a separate method. Tools are passed in `LLMRequest.tools`; tool calls come back in `LLMResponse.toolCalls`. | Same | Same | Same |

- `complete` takes an `LLMRequest`, not `messages: [Message]` as in v1.1.0.
- `completeWithTools` is **absent** on all platforms. See section 4.
- The v1.1.0 required fields `modelId`, `maxTokens` and `systemPrompt` on the provider are **absent**. Model and limits are per request (`LLMRequest.model`, `LLMRequest.maxTokens`).
- iOS `LLMProvider` conforms to `Sendable`.

### 2.2 `AgentProtocol`

| Item | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| Run | `run(_ request: AgentRequest) async throws -> AgentResult` | `suspend fun run(request: AgentRequest): AgentResult` | `run(request: AgentRequest): Promise<AgentResult>` | `Future<AgentResult> run(AgentRequest request)` |
| `run(input: String)` | **Absent** (input is on `AgentRequest.input`) | Absent | Absent | Absent |
| `runWithContext` | **Absent** | Absent | Absent | Absent |
| `reset()` | **Absent** | Absent | Absent | Absent |
| `agentId`, `provider` | **Absent** | Absent | Absent | Absent |

The v1.1.0 required properties and methods (`agentId`, `provider`, `runWithContext`, `reset`) are not shipped. `AgentProtocol` is a single-method interface on every platform. No concrete agent implementation exists in the four AI repositories. The only implementations found are test mocks.

### 2.3 `AgentRequest`, `AgentStep`, `AgentResult`

| Field | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| `input` | `String` | `String` | `string` | `String` |
| `tools` | `[AgentTool]`, default `[]` | `List<AgentTool>`, default empty | `AgentTool[]`, optional | `List<AgentTool>`, default `[]` |
| `maxSteps` | `Int`, default `10` | `Int`, default `10` (private `DEFAULT_MAX_STEPS`) | `number`, optional; default `DEFAULT_MAX_STEPS = 10` (exported) | `int`, default `10` |
| `metadata` | `[String: String]` | `Map<String, String>` | `Record<string, string>`, optional | `Map<String, String>` |

**`maxSteps` behaviour (verified in code):**

- **Default:** 10 on every platform.
  - iOS: `AgentRequest.swift` init default `maxSteps: Int = 10`.
  - Android: `AgentRequest.kt` `DEFAULT_MAX_STEPS = 10`.
  - RN: `AgentRequest.ts` `DEFAULT_MAX_STEPS = 10`, and `resolveMaxSteps()` maps `undefined` and non-finite values to the default.
  - Flutter: `agent_request.dart` init default `maxSteps = 10`.
- **Clamp:** values below 1 are raised to 1 on every platform.
  - iOS: `max(1, maxSteps)`.
  - Android: `maxSteps.coerceAtLeast(1)`.
  - RN: `Math.max(1, Math.floor(maxSteps))`.
  - Flutter: `maxSteps < 1 ? 1 : maxSteps`.
- **Behaviour when the step budget is exhausted:** **undefined**. No platform implements an agent loop in the shipped code, so no code path reads `maxSteps` to stop a loop. Consumers must not rely on any specific exhaustion behaviour until a loop is specified.

`AgentStep` fields: `action`, `input`, `output`, `metadata`. The types of `input` differ. iOS uses `[String: String]` plus an optional `structuredInput: JSONObject`. Android uses `Map<String, Any>`. RN uses `Record<string, unknown>`. Flutter follows the same pattern as the other platforms. The differences are not blocking, but the input type is a parity gap.

`AgentResult` fields: `finalAnswer`, `steps`, `tokenUsage?`.

### 2.4 `EmbeddingProvider`

| Item | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| Single embed | `embed(_ text: String) async throws -> Embedding` | `suspend fun embed(text: String): Embedding` | `embed(text: string): Promise<Embedding>` | `Future<Embedding> embed(String text)` |
| `embedBatch` | **Absent** | Absent | Absent | Absent |
| `modelId` on provider | **Absent** | Absent | Absent | Absent |
| `dimensions` on provider | **Absent** (value is on `Embedding.dimensions`) | Absent | Absent | Absent |

`embedBatch` and the provider-level `modelId` and `dimensions` are listed as **future** items in section 5. The v1.1.0 `embedBatch` requirement is withdrawn until a platform implements it.

### 2.5 `RAGProvider`

| Item | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| Retrieve | `retrieve(_ query: String, options: RAGOptions) async throws -> [RAGChunk]` (plus a convenience overload with default options) | `suspend fun retrieve(query: String, options: RAGOptions = RAGOptions()): List<RAGChunk>` | `retrieve(query: string, options?: RAGOptions): Promise<RAGChunk[]>` | `Future<List<RAGChunk>> retrieve(String query, {RAGOptions? options})` |
| `add(documents)` | **Absent** | Absent | Absent | Absent |
| `query(text, topK)` | **Absent** (use `retrieve`) | Absent | Absent | Absent |
| `clear()` | **Absent** | Absent | Absent | Absent |
| `embeddingProvider` property | **Absent** | Absent | Absent | Absent |

`RAGOptions.maxResults`: default 10, clamped to at least 1 (iOS `max(1, maxResults)`, Android `coerceAtLeast(1)`, RN `resolveMaxResults`, Flutter `maxResults < 1 ? 1 : maxResults`).

The v1.1.0 document-ingest API (`add`, `query`, `clear`) is **absent**. Ingestion is out of scope for the shipped RAG contract.

### 2.6 `MemoryManager`

| Item | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| Add | `add(_ entry: MemoryEntry) async throws` | `suspend fun add(entry: MemoryEntry)` | `add(entry: MemoryEntry): Promise<void>` | `Future<void> add(MemoryEntry entry)` |
| Retrieve | `retrieve(query: String, limit: Int)` | `retrieve(query: String, limit: Int)` | `retrieve(query: string, limit: number)` | `retrieve(String query, int limit)` |
| Clear | `clear()` | `clear()` | `clear()` | `clear()` |
| `namespace` property | **Absent** | Absent | Absent | Absent |
| `store(key, value)`, `retrieve(key)`, `delete(key)`, `keys()` | **Absent** | Absent | Absent | Absent |

The v1.1.0 key/value API (`store`, `retrieve(key)`, `delete`, `keys`) is **absent**. Shipped memory is entry-based (`MemoryEntry`), with query-based retrieval.

### 2.7 `NamespacedMemoryManager`

The method names are **the same on all four platforms**. Only the parameter signatures differ.

| Operation | iOS | Android | RN | Flutter |
|---|---|---|---|---|
| Add to namespace | `addToNamespace(entry:namespace:)` | `addToNamespace(entry, namespace)` | `addToNamespace(entry, namespace)` | `addToNamespace(entry, namespace)` |
| Retrieve from namespace | `retrieveFromNamespace(query:namespace:limit:)` (`limit: Int?`) | `retrieveFromNamespace(query, namespace, limit = null)` | `retrieveFromNamespace(query, namespace, limit?)` | `retrieveFromNamespace(query, namespace, {int? limit})` |
| Delete entry | `deleteEntry(id:namespace:)` | `deleteEntry(id, namespace)` | `deleteEntry(id, namespace)` | `deleteEntry(id, namespace)` |
| Clear namespace | `clearNamespace(namespace:)` | `clearNamespace(namespace)` | `clearNamespace(namespace)` | `clearNamespace(namespace)` |

The v1.1.0 table (`add(_:namespace:)`, `retrieve(query:namespace:limit:)`, `delete(id:namespace:)`, `clear(namespace:)`, and the Flutter variants `retrieveFromNamespace` and `clearNamespace`) is **superseded**. The shipped names are the same across platforms, so the earlier Dart-only rename rationale no longer applies to the namespaced methods.

`NamespacedMemoryManager` extends `MemoryManager` on every platform.

### 2.8 Streaming

| Platform | Shipped stream surface |
|---|---|
| iOS | `LLMProvider.stream` returns `AsyncThrowingStream<LLMChunk, Error>`. `StreamSemantics.swift` declares an empty `enum StreamContract`. |
| Android | `LLMProvider.stream` returns `Flow<LLMChunk>`. `StreamContract.kt` declares an empty `object StreamContract`. |
| RN | `LLMProvider.stream` returns `AsyncIterable<LLMChunk>`. `StreamContract.ts` declares `ChunkPhase` (`'chunk'`), `FinalPhase` (`'final'`) and `StreamPhase` types. Nothing in the contract uses them. |
| Flutter | `LLMProvider.stream` returns `Stream<LLMChunk>`. `stream_contract.dart` declares an abstract `StreamContract` class with a `stream` method. |

**Stream semantics are undefined.** The code does not specify whether a stream must end with a chunk whose `finishReason` is set, how errors are delivered mid-stream, or how cancellation works. The v1.1.0 phrase "stream semantics" describes an intent, not shipped behaviour.

### 2.9 Deprecations

- **RN timestamp `number` → `string` (v1.1.0, removal target v1.2.0): expired and removed.** The shipped `MemoryEntry.timestamp` and `ConversationTurn.timestamp` are typed `SyzygyTimestamp` on all four platforms. No `number`/`string` union exists in the code, so there is nothing to migrate. This deprecation is closed and must not appear in release notes as a pending removal.

---

## 3. Platform-specific deviations

- **iOS:** contract types that cross actor boundaries conform to `Sendable`. This applies to `LLMProvider`, `AgentProtocol`, `EmbeddingProvider`, `RAGProvider`, `MemoryManager`, `AIError`, `ToolCall`, `ToolCallResult` and `JSONValue`.
- **RN:** exposes `DEFAULT_MAX_STEPS`, `resolveMaxSteps` and `resolveMaxResults` as runtime helpers. Other platforms keep the defaults private or inside the options type.
- **Flutter:** the error class is `AINetworkError` and the JSON type is `JsonValue`. Both differ from the other platforms.
- **Android:** `Embedding.values` is a `FloatArray` with custom `equals`/`hashCode`.

---

## 4. Parity table (platform x API item)

Legend: **P** = present, **A** = absent, **D** = differs (present with a different name or shape; see note). File references are relative to `AI/{platform}/src/syzygy-ai-{platform}/`.

| API item | iOS | Android | RN | Flutter | Reference |
|---|---|---|---|---|---|
| `LLMProvider.complete` | P | P | P | P | iOS `Sources/SyzygyAI/Contracts/LLM/LLMProvider.swift`; Android `src/main/kotlin/com/syzygy/ai/contracts/llm/LLMProvider.kt`; RN `src/contracts/llm/LLMProvider.ts`; Flutter `lib/src/contracts/llm/llm_provider.dart` |
| `LLMProvider.stream` | P | P | P | P | same files |
| `LLMProvider.completeWithTools` | A (tools on `LLMRequest.tools`) | A | A | A | `LLMRequest.swift`, `LLMRequest.kt`, `LLMRequest.ts`, `llm_request.dart` |
| `LLMRequest` / `LLMResponse` | P | P | P | P | `contracts/llm/LLMRequest.*`, `LLMResponse.*` |
| `ToolCall` / `ToolCallResult` | P | P | P | P | `contracts/llm/ToolCall.*`, `ToolCallResult.*` |
| `ToolCallRequest` (v1.1.0 name) | A (`ToolCall`) | A | A | A | as above |
| `AIError` | P (enum) | P (sealed) | D (`code` field) | D (`AINetworkError`) | `contracts/AIError.*` (`ai_error.dart` on Flutter) |
| `JSONValue` | P | P | P | D (`JsonValue`) | `types/JSONValue.*`; Flutter `lib/src/types/json_value.dart` |
| `AgentProtocol.run` | P | P | P | P | `contracts/agent(s)/AgentProtocol.*` |
| `AgentProtocol.runWithContext` / `reset` / `agentId` / `provider` | A | A | A | A | as above |
| `AgentRequest.maxSteps` default 10, clamp ≥ 1 | P | P | P | P | `AgentRequest.swift`, `AgentRequest.kt`, `AgentRequest.ts`, `agent_request.dart` |
| `AgentStep.input` type | D (`[String:String]` + `structuredInput`) | D (`Map<String,Any>`) | D (`Record<string,unknown>`) | D | `AgentStep.*` |
| `EmbeddingProvider.embed` | P | P | P | P | `contracts/embeddings/EmbeddingProvider.*` |
| `EmbeddingProvider.embedBatch` | A | A | A | A | as above |
| `Embedding.dimensions` | P | P | P | P | `contracts/embeddings/Embedding.*` |
| `RAGProvider.retrieve` | P | P | P | P | `contracts/rag/RAGProvider.*` |
| `RAGProvider.add` / `query` / `clear` | A | A | A | A | as above |
| `RAGOptions.maxResults` default 10, clamp ≥ 1 | P | P | P | P | `contracts/rag/RAGOptions.*` (`rag_options.dart`) |
| `MemoryManager.add` / `retrieve(query,limit)` / `clear` | P | P | P | P | `contracts/memory/MemoryManager.*` |
| `MemoryManager.store/retrieve(key)/delete/keys` | A | A | A | A | as above |
| `NamespacedMemoryManager` (4 methods) | P | P | P | P | `contracts/memory/NamespacedMemoryManager.*` |
| Stream phase/semantics types | D (empty enum) | D (empty object) | D (type aliases only) | D (abstract class) | `StreamSemantics.swift`, `StreamContract.kt`, `StreamContract.ts`, `stream_contract.dart` |
| RN timestamp `number`→`string` deprecation | N/A (closed) | N/A | N/A (closed; `SyzygyTimestamp` on RN) | N/A | `contracts/memory/MemoryEntry.ts` |
| `Sendable` conformance | P (iOS only) | N/A | N/A | N/A | iOS contract files |

---

## 5. Future items (not implemented; not required for 3.0.0)

The following v1.1.0 requirements are **withdrawn from the 3.0.0 contract** because no platform implements them. They may return in a later minor release, with a new spec entry, once at least one platform ships them.

- `EmbeddingProvider.embedBatch(texts)`
- `EmbeddingProvider.modelId` and provider-level `dimensions`
- `LLMProvider.completeWithTools(messages, tools)` as a separate method
- `LLMProvider.modelId`, `maxTokens` and `systemPrompt` as provider-level fields
- `AgentProtocol.agentId`, `provider`, `runWithContext`, `reset`
- `RAGProvider.add`, `query`, `clear`, `embeddingProvider`
- `MemoryManager.namespace` and the key/value API (`store`, `retrieve(key)`, `delete`, `keys`)
- A defined stream end-of-stream and error contract
- An agent loop with defined exhaustion behaviour for `maxSteps`

---

## 6. Related documents

- [`repository-standard.md`](repository-standard.md): repo structure and AI composition guidance
- [`release-standard.md`](release-standard.md): versioning and release process
