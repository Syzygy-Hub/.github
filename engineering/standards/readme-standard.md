<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy README Standard

Every Syzygy repository README follows the same structural rhythm. Each repository type has a canonical section order; sections that do not apply are omitted.

---

## Part 1 — Universal Rules

These rules apply to every Syzygy README regardless of repo type.

---

### Voice and Tone

- Written as if by one person — the same person wrote every README in the ecosystem
- Declarative, not promotional
- No "powerful", "elegant", "seamless", "robust", "best-in-class"
- Present tense throughout
- No internal notes, TODOs, or "coming soon" sections — if it's not done, it's not in the README

---

### Badge Format

Always shields.io. Always in this order:

```
Platform badge | Language badge | CI badge | Version badge | License badge
```

**Platform badge** — label is the platform name, message is the language or framework value. Color: `7F77DD` (Syzygy Purple). Replace `{PLATFORM}` and `{VALUE}` with real values before publishing:

```
[![{PLATFORM}](https://img.shields.io/badge/{PLATFORM}-{VALUE}-7F77DD?style=flat)](link)
```

Examples:
```
[![iOS](https://img.shields.io/badge/iOS-Swift-FA7343?style=flat&logo=apple&logoColor=white)](https://developer.apple.com/ios/)
[![Android](https://img.shields.io/badge/Android-Kotlin-7F52FF?style=flat&logo=android&logoColor=white)](https://developer.android.com/)
[![React Native](https://img.shields.io/badge/React%20Native-TypeScript-3178C6?style=flat&logo=react&logoColor=white)](https://reactnative.dev/)
[![Flutter](https://img.shields.io/badge/Flutter-Dart-0175C2?style=flat&logo=flutter&logoColor=white)](https://flutter.dev/)
```

**Language badge** — label is the language name, message is the version. Always includes logo. Color: `1D9E75` (Syzygy Teal). Replace `{LANGUAGE}` and `{VERSION}` before publishing:

```
[![{LANGUAGE}](https://img.shields.io/badge/{LANGUAGE}-{VERSION}-1D9E75?style=flat)](link)
```

Examples:
```
[![Swift](https://img.shields.io/badge/Swift-6.0-FA7343?logo=swift&logoColor=white)](https://swift.org)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Dart](https://img.shields.io/badge/Dart-3.0-0175C2?logo=dart&logoColor=white)](https://dart.dev)
```

**CI badge** — single badge covering build and tests. Replaces separate build and tests badges. Links to the GitHub Actions workflow:

```
[![CI](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/{repo}/ci.yml?label=ci&style=flat)](https://github.com/Syzygy-Hub/{repo}/actions/workflows/ci.yml)
```

All five badges must appear on a **single line** with no blank lines between them. The commented options block (platform/language/package manager alternatives) follows on the next line immediately after the badge line — no blank line between them.

**Version badge** — color `D85A30` (Syzygy Coral):

```
[![Version](https://img.shields.io/badge/version-{X.X.X}-D85A30?style=flat)](https://github.com/Syzygy-Hub/{repo}/releases)
```

**License badge** — always MIT, always color `green`:

```
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
```

---

### Banner Format

Always theme-aware. Always uses the `<picture>` element with light/dark srcset. Always links to `brand/` in the `.github` repo.

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>
```

---

### Heading Conventions

- H1 (`#`) — repository name only, exactly as it appears on GitHub. No tagline on the same line.
- H2 (`##`) — top-level sections only
- H3 (`###`) — subsections within a section (e.g. package manager variants inside Installation)
- No H4 or deeper in README files

---

### Link Conventions

- Link to the `.github` repo for engineering standards and architecture docs
- Never link to external docs that may go stale
- Relative links for files within the same repo (e.g. `[LICENSE](LICENSE)`)

---

### What Never Belongs in a README

- Walls of text in any section
- Architecture diagrams spanning multiple repos
- Implementation details — those belong in inline code comments
- Known limitations presented as permanent features
- Changelog content — that belongs in `CHANGELOG.md`
- An Author section
- Internal notes, judgment calls, or TODOs visible to readers

---

## Part 2 — Repository Templates

Canonical section order per repo type. Omit any section marked optional if it does not apply.

---

### Foundation Repos (`syzygy-foundation-*`)

```
1.  Badges (Platform | Language | CI | Version | License)
2.  Banner
3.  H1 — repo name
4.  One-sentence description
5.  About
6.  Platforms
7.  Requirements
8.  Installation
9.  Architecture
10. API
11. Usage
12. Platform Notes (optional — include only when platform APIs differ meaningfully)
13. Contributing
14. Releases
15. License
```

### UI Library Repos (`syzygy-ui-*`)

```
1.  Badges (Platform | Language | CI | Version | License)
2.  Banner
3.  H1 — repo name
4.  One-sentence description
5.  About
6.  Platforms
7.  Requirements
8.  Installation
9.  Architecture
10. Components
11. Usage
12. Contributing
13. Releases
14. License
```

### Core Repos (`syzygy-core-*`)

```
1.  Badges (Platform | Language | CI | Version | License)
2.  Banner
3.  H1 — repo name
4.  One-sentence description
5.  About
6.  Platforms
7.  Requirements
8.  Installation
9.  Architecture
10. Modules
11. Usage
12. Contributing
13. Releases
14. License
```

### Services Repos (`syzygy-services-*`)

```
1.  Badges (Platform | Language | CI | Version | License)
2.  Banner
3.  H1 — repo name
4.  One-sentence description
5.  About
6.  Platforms
7.  Requirements
8.  Installation
9.  Architecture
10. Modules
11. Usage
12. Contributing
13. Releases
14. License
```

### Base App Repos (`syzygy-base-*`)

```
1.  Badges (Platform | Language | CI | Version | License)
2.  Banner
3.  H1 — repo name
4.  One-sentence description
5.  About
6.  Platforms
7.  Requirements
8.  Installation
9.  Architecture
10. Contents
11. Usage
12. Contributing
13. Releases
14. License
```

---

## Section Rules

### About

One tight paragraph. 3–4 sentences. Covers what it is and why you would use it — both in the same block. No separate "What is it?" and "Why would I use it?" headings.

### Platforms

The table format depends on the repo scope:

**Platform-specific repos** (`syzygy-foundation-ios`, `syzygy-ui-android`, etc.) — single row for the repo's own platform only:

```markdown
## Platforms

| Platform | Min Version | Package Manager | Status |
|---|---|---|---|
| iOS | 16.0+ | SPM | ✅ Supported |
```

**Ecosystem-level repos** (org profile, `.github`, architecture docs) — full four-row matrix. Individual platform repos do not show the full matrix; that belongs in [syzygy-ecosystem.md](../architecture/syzygy-ecosystem.md).

**Status values:** `✅ Supported` | `⏳ Coming Soon` | `❌ Not Supported`

### Requirements

Bullet list. Covers platform version, language version, and tooling version for this specific platform repo.

```markdown
## Requirements

- iOS 16.0+
- Swift 6.0+
- Xcode 16.0+
```

### Installation

Platform-specific snippet. One block per package manager. No preamble.

### Architecture

Always before the contents section (API/Components/Modules/Contents). Documents only this repo's internal structure. No cross-repo diagrams.

```markdown
## Architecture

**Module structure:**
- SyzygyFoundation — runtime contracts and primitives
- SyzygyFoundationTesting — test support (separate import)

**Depends on:** nothing

**Used by:** syzygy-ui-*, syzygy-core-*, syzygy-services-*
```

### API / Components / Modules / Contents

Section heading depends on repo type:

| Repo type | Heading |
|---|---|
| Foundation repos | `## API` |
| UI repos | `## Components` |
| Core repos | `## Modules` |
| Services repos | `## Modules` |
| Base repos | `## Contents` |

Compact list. One line per module/group. No nested lists.

### Usage

One or more code blocks. The minimum to do something useful. No long explanation before the code — just the heading and the block(s).

### Platform Notes

Optional — include only when the implementation has meaningful platform-specific behavior that users need to know. Omit entirely when all platforms behave identically.

### Contributing

Brief. Links to Syzygy engineering standards.

```markdown
## Contributing

Contributions are welcome. Please follow the [Syzygy engineering standards](https://github.com/Syzygy-Hub/.github/tree/main/engineering/standards) when submitting pull requests.
```

### Releases

Documents the tag-based release flow. Links to the full release standard.

```markdown
## Releases

Releases follow a tag-based flow:

1. Create branch `release/X.X.X`
2. Bump version in manifest and `syzygy.yml`
3. Update `CHANGELOG.md`
4. Open PR → `main`, get approval and merge
5. Push the version tag: `git tag X.X.X && git push origin X.X.X`
6. CI validates the tag, publishes, and creates the GitHub Release automatically

See the [Syzygy Release Standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/release-standard.md) for full details.
```

### License

One line.

```markdown
## License

MIT — see [LICENSE](LICENSE).
```
