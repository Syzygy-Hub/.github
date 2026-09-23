<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# AI Contract Specification — v1.1.0

This document defines the canonical contract shape that all four Syzygy platforms (iOS, Android, React Native, Flutter) must satisfy for the v1.1.0 AI layer release.

---

## New Types in v1.1.0

All platforms must define the following types (exact spelling is platform-idiomatic):

### `JSONValue`

A recursive sum type representing any valid JSON value.

```
JSONValue =
  | null
  | bool
  | number   // double precision
  | string
  | [JSONValue]
  | { string: JSONValue }
```

### `AIError`

Structured error type for AI contract failures.

| Field | Type | Required | Notes |
|---|---|---|---|
| `code` | string | yes | Machine-readable error code, e.g. `"rate_limited"`, `"context_exceeded"` |
| `message` | string | yes | Human-readable description |
| `underlyingError` | Error / Throwable / unknown | no | Original error from the provider SDK |

### `ToolCallRequest`

Represents a tool/function call request emitted by an LLM.

| Field | Type | Required |
|---|---|---|
| `id` | string | yes |
| `name` | string | yes |
| `arguments` | JSONValue (object) | yes |

### `ToolCallResult`

The result returned to the model for a tool call.

| Field | Type | Required |
|---|---|---|
| `toolCallId` | string | yes — must match the originating `ToolCallRequest.id` |
| `content` | string | yes |
| `isError` | bool | no — defaults to `false` |

---

## Contract Modules

### 1. `LLMProvider`

Defines the interface for making completions requests to a language model backend.

**Required fields / properties**

| Name | Type | Notes |
|---|---|---|
| `modelId` | string | Identifies the active model |
| `maxTokens` | int | Upper bound on output tokens |
| `systemPrompt` | string? | Optional system-level instruction |

**Required methods**

```
complete(messages: [Message]) -> Result<String, AIError>
  // Blocking / async completion. Returns the model's text reply.

stream(messages: [Message]) -> AsyncSequence<String> / Flow<String> / Observable<String>
  // Streaming completion. Emits partial reply chunks.

completeWithTools(
  messages: [Message],
  tools: [ToolDefinition]
) -> Result<LLMResponse, AIError>
  // Completion that may return ToolCallRequests instead of or alongside text.
```

---

### 2. `AgentProtocol`

Defines the interface for a stateful agent that can execute multi-step reasoning loops.

**Required fields / properties**

| Name | Type | Notes |
|---|---|---|
| `agentId` | string | Stable identifier for the agent instance |
| `provider` | LLMProvider | The underlying model provider |

**Required methods**

```
run(input: String) -> Result<String, AIError>
  // Execute a full agent turn from a user input string.

runWithContext(input: String, context: [Message]) -> Result<String, AIError>
  // Execute with an explicit prior-message context.

reset() -> Void
  // Clear the agent's internal state and message history.
```

---

### 3. `EmbeddingProvider`

Defines the interface for computing dense vector embeddings from text.

**Required fields / properties**

| Name | Type | Notes |
|---|---|---|
| `modelId` | string | Identifies the embedding model |
| `dimensions` | int | Output vector dimensionality |

**Required methods**

```
embed(text: String) -> Result<[Float], AIError>
  // Returns the embedding vector for a single input string.

embedBatch(texts: [String]) -> Result<[[Float]], AIError>
  // Returns one embedding per input string.
```

---

### 4. `RAGProvider`

Defines the interface for retrieval-augmented generation: storing and querying document chunks alongside their embeddings.

**Required fields / properties**

| Name | Type | Notes |
|---|---|---|
| `embeddingProvider` | EmbeddingProvider | Used to embed queries and documents |

**Required methods**

```
add(documents: [Document]) -> Result<Void, AIError>
  // Embed and store one or more documents.

query(text: String, topK: Int) -> Result<[Document], AIError>
  // Embed the query and return the topK most-similar stored documents.

clear() -> Result<Void, AIError>
  // Remove all stored documents.
```

---

### 5. `MemoryManager`

Defines the interface for persistent or session-scoped memory that can be attached to an agent.

**Required fields / properties**

| Name | Type | Notes |
|---|---|---|
| `namespace` | string | Scopes memory to a user, session, or agent instance |

**Required methods**

```
store(key: String, value: JSONValue) -> Result<Void, AIError>
  // Persist a key/value pair under the namespace.

retrieve(key: String) -> Result<JSONValue?, AIError>
  // Look up a stored value. Returns nil/null when the key is absent.

delete(key: String) -> Result<Void, AIError>
  // Remove a stored key.

keys() -> Result<[String], AIError>
  // List all stored keys in the namespace.

clear() -> Result<Void, AIError>
  // Remove all keys in the namespace.
```

---

## Deprecations

### RN timestamp: `number` → `string` (bridge deprecation)

In React Native, timestamps that previously crossed the JS bridge as `number` (Unix milliseconds) are deprecated as of v1.1.0. Use `string` (ISO 8601) instead.

**Affected fields:** `Message.timestamp`, `MemoryManager` record metadata  
**Migration:** Accept both `number` and `string` at runtime; emit only `string` in new code.  
**Removal target:** v1.2.0

---

## Platform-Specific Deviations

### iOS — `Sendable` requirement

All contract types that cross actor boundaries must conform to `Sendable`. This applies to:

- `LLMProvider`, `AgentProtocol`, `EmbeddingProvider`, `RAGProvider`, `MemoryManager` (protocol itself)
- `AIError`, `ToolCallRequest`, `ToolCallResult`, `JSONValue` (value types)

Swift's `Sendable` constraint is an iOS/macOS compile-time requirement not present on other platforms. Implementations must not store mutable reference-type state visible across the protocol boundary without explicit concurrency protection.

### React Native — number timestamp bridge

React Native serialises `number` values across the JS–native bridge as double-precision floats. Unix millisecond timestamps near `Date.now()` (> 2^53 μs) are unaffected for the current epoch, but to avoid future truncation and align with the above deprecation, all new timestamp fields must use `string` (ISO 8601). See the deprecation note above.

---

## Related Documents

- [`repository-standard.md`](repository-standard.md) — repo structure and AI composition guidance
- [`release-standard.md`](release-standard.md) — versioning and release process
