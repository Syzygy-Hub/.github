<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy README Standard

Every Syzygy repository README follows this standard exactly. Same rhythm, same voice, same depth — regardless of platform or layer.

---

## The README Rhythm

Every Syzygy README has these sections in this exact order. No exceptions.

```
1.  Badges
2.  Repository name (H1)
3.  Banner (theme-aware)
4.  One-sentence description
5.  What is it?
6.  Why would I use it?
7.  Platform support
8.  Installation
9.  What does it contain?
10. Simplest working example
11. Contributing & Releases
12. License
13. Author
```

---

## Section Rules

### 1. Badges

Always first. Always shields.io. Always in this order:

```
[![Build](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/{repo}/ci.yml?label=build&style=flat)](...)
[![Tests](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/{repo}/ci.yml?label=tests&style=flat)](...)
[![Version](https://img.shields.io/badge/version-{X.X.X}-blue?style=flat)](...)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](...)
```

Coverage badge is optional — include only if the repo generates a coverage report in CI.

### 2. Repository Name (H1)

The repo name exactly as it appears on GitHub. No tagline on the same line.

```markdown
# syzygy-foundation-ios
```

### 3. Banner

Always theme-aware. Always uses the `<picture>` element with light/dark srcset. Always links to `brand/` in the `.github` repo.

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/syzygy-banner-light-1200.png" alt="Syzygy">
</picture>
```

### 4. One-Sentence Description

One sentence only. What it is and what platform. No adjectives like "powerful" or "elegant".

```
Foundational contracts, primitives, and shared types for the Syzygy iOS ecosystem.
```

### 5. What is it?

2–3 sentences. No more. Focus on what it contains, not what it enables.

### 6. Why would I use it?

2–3 sentences. No more. Focus on the problem it solves, not its features.

### 7. Platform Support

Compact. One line per platform or a small table if multi-platform.

```markdown
**Requires:** iOS 16.0+ · Swift 6 · Xcode 16+
```

### 8. Installation

Platform-specific snippet. One block per package manager. No preamble.

```markdown
## Installation

### Swift Package Manager
...
```

### 9. What Does It Contain?

Compact list. One line per module/group. No nested lists.

```markdown
- **Primitives** — SyzygyID, Page, SyzygyTimestamp, SyzygyDuration, ValidationResult
- **Contracts** — NetworkClientProtocol, StorageProvider, AuthProvider, AnalyticsProvider, LoggerProtocol, ConnectivityProvider
- **Shared Types** — SyzygyEnvironment, SyzygyConfiguration, SyzygyBuildInfo, SyzygyVersion
- **Errors** — SyzygyError, SyzygyErrorCode, SyzygyErrorSeverity
- **Testing** — MockNetworkClient, MockLogger, SpyAnalyticsProvider, FixtureProvider (separate import)
```

### 10. Simplest Working Example

One code block. The absolute minimum to do something useful. No explanation before the code — just a heading and the block.

### 11. Contributing & Releases

Brief. Link to `engineering/standards/release-standard.md` in the `.github` repo. Include the release commit format.

```markdown
## Contributing & Releases

Release trigger: `release: vX.X.X — description` commit on `main`.
Tag format: `X.X.X` (no `v` prefix).
See [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md).
```

### 12. License

One line.

```markdown
## License

MIT — see [LICENSE](LICENSE).
```

### 13. Author

Always last. Always this exact format.

```markdown
## Author

[Ayush Kumar Sethi](https://aks5686.github.io) — [github.com/aks5686](https://github.com/aks5686)
```

---

## Architecture Section Rule

Each repo documents only its own internal structure. The ecosystem-wide architecture diagram lives exclusively in [`engineering/architecture/syzygy-ecosystem.md`](../architecture/syzygy-ecosystem.md).

In each repo's README, the architecture section covers:

```markdown
## Architecture

**Module structure:**
- SyzygyFoundation — runtime contracts and primitives
- SyzygyFoundationTesting — test support (separate import)

**Depends on:** nothing

**Used by:** syzygy-ui-*, syzygy-core-*, syzygy-services-*
```

No cross-repo diagrams. No ecosystem maps. No arrows pointing to other repos.

---

## Voice and Tone

- Written as if by one person — the same person wrote every README in the ecosystem
- Declarative, not promotional
- No "powerful", "elegant", "seamless", "robust", "best-in-class"
- Present tense throughout
- No internal notes, TODOs, or "coming soon" sections — if it's not done, it's not in the README

---

## What Does Not Belong in a README

- Walls of text in any section
- Architecture diagrams spanning multiple repos
- Implementation details (those belong in inline code comments)
- Known limitations presented as permanent features
- Contribution workflow beyond the release trigger format
- Changelog content — that belongs in CHANGELOG.md
