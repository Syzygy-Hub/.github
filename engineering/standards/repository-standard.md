<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Repository Standard

---

## Naming Convention

```
syzygy-{type}-{platform}
```

**Types:** `foundation` | `ui` | `core` | `services` | `base`

**Platforms:** `ios` | `android` | `rn` | `flutter`

**Examples:**
```
syzygy-foundation-ios
syzygy-ui-android
syzygy-core-rn
syzygy-services-flutter
syzygy-base-ios
```

---

## syzygy.yml Manifest

Every Syzygy repo must have a `syzygy.yml` at its root.

```yaml
# Syzygy Repository Manifest
name: syzygy-ui-ios
type: ui                       # foundation | ui | core | services | ai | base | app | example
platform: ios                  # ios | android | rn | flutter
language: swift                # swift | kotlin | typescript | dart
package_manager: spm           # spm | jitpack | npm | pub.dev
license: MIT
version: 3.0.0                 # bare semver, no v prefix
syzygy_foundation: ">=3.0.0"  # omit for foundation repos
```

See the template at [`engineering/templates/syzygy.yml.template`](../templates/syzygy.yml.template).

### Canonical schema and validator

The canonical schema is [`engineering/schema/syzygy.schema.json`](../schema/syzygy.schema.json) (JSON Schema draft 2020-12). It covers all layers, including `ai`, `base`, `app` and `example`. The legacy keys `layer`, `foundation` and the `syzygy_<layer>` keys are accepted by the validator and reported as warnings. The canonical key is `type`.

The reference validator is [`engineering/tooling/validate-syzygy/validate.py`](../tooling/validate-syzygy/validate.py). It uses only the Python standard library. A minimal YAML subset parser is used because PyYAML is not guaranteed on runners, so the validator accepts only the flat and one-level-nested manifest forms used in the org. Usage:

```bash
python3 path/to/.github/engineering/tooling/validate-syzygy/validate.py --report-only path/to/repo/syzygy.yml
```

- `--report-only` (the default when run from CI) prints PASS, WARN or FAIL for each file and exits 0.
- Without `--report-only`, the script exits non-zero when any file is FAIL.
- Callers pass one or more manifest paths. Quote paths that contain spaces (for example `"UI Libraries/ios/src/syzygy-ui-ios/syzygy.yml"`).

**Planned for 3.0.1:** a Hub input `syzygy_validation: report-only` on the release workflows, so that every release runs the validator and records the result without blocking. This is a planned item only. It is not in 3.0.0 and no workflow implements it yet.

---

## Lockfile Policy

Lockfiles follow the kind of artefact the repo produces.

| Repo kind | `package-lock.json` (RN) | `Package.resolved` (SwiftPM) | `pubspec.lock` (Dart/Flutter) | `Podfile.lock` (iOS app) | `gradle` lock files |
|---|---|---|---|---|---|
| RN library | **Commit** (release CI needs it for `npm ci`) | n/a | n/a | n/a | n/a |
| SwiftPM library | n/a | **Do not commit** (add to `.gitignore`) | n/a | n/a | n/a |
| Dart / Flutter library | n/a | n/a | **Do not commit** (add to `.gitignore`) | n/a | n/a |
| App (any platform) | Commit | Commit | Commit | **Commit** | Commit where the build uses lock files |

Rules:

- RN libraries keep `package-lock.json` committed. The release CI runs `npm ci`, which requires the lock file.
- SwiftPM libraries and Dart/Flutter libraries do **not** commit `Package.resolved` or `pubspec.lock`. Libraries are consumed through version ranges, so a committed lock file only adds noise and can mask resolution problems in consumers.
- Apps commit every lock file, including `Podfile.lock`, so builds are reproducible.

Audit note (workspace snapshot): `UI Libraries/ios/src/syzygy-ui-ios/Package.resolved` and `UI Libraries/flutter/src/syzygy-ui-flutter/pubspec.lock` are present in the working trees of two library repos. They do not match this policy and need removal from the tracked files in those repos. This document does not change those repos; the owners must act on it.

---

## Required CI recipes: library versus app

Caller workflows for each platform are provided as templates in [`engineering/templates/`](../templates/):

- Libraries: `ci-library-{ios,android,rn,flutter}.yml.template` and `release-library-{ios,android,rn,flutter}.yml.template`
- Apps: `ci-app-{ios,android,rn,flutter}.yml.template` and `release-app-{ios,android,rn,flutter}.yml.template`

Differences:

- **Library** CI runs the build, lint, unit tests and coverage. It does not run device or simulator smoke tests unless the library explicitly needs them. Release creates the GitHub Release. Registry publishing is platform-specific. Flutter publishes to pub.dev inside `flutter-release.yml`. React Native publishes to npm from each caller's own `publish-npm` job, because npm OIDC trusted publishing needs the caller's workflow file. iOS (SPM) and Android (JitPack) publish nothing beyond the GitHub Release, since the tag is the artefact. Apps (`app-release.yml`) publish nothing.
- **App** CI additionally runs build smoke tests and may run native smoke tests (`build_smoke_*`, `native_smoke_*`). Release uses the no-publish mode (`app-release.yml`): it validates the version, extracts the CHANGELOG and creates a GitHub Release, but never publishes to a registry.

The input names used by the templates are listed in [`engineering/templates/`](../templates/) and documented in [`.github/workflows/README.md`](../../.github/workflows/README.md), which the workflow owners maintain. Do not copy input descriptions from this document; read them from the workflows README.

---

## Licence holder (PENDING DECISION)

The legal holder named in the licence text is **not yet chosen**. This is an explicit open decision. Until the owner decides, the MIT licence text is not changed, and no repo should add a LICENSE file that names a holder. The decision belongs to the Syzygy-Hub owner. Record the outcome in this section once made.

---

## Semantic version tags

Tags are bare strict semver: `MAJOR.MINOR.PATCH`, for example `3.0.0`. Do not use a `v` prefix for new tags. The release CI glob `[0-9]+.[0-9]+.[0-9]+` matches only bare tags. The full policy is in [`release-standard.md`](release-standard.md).

---

## Repository Settings

| Setting | Value |
|---|---|
| Visibility | Public |
| License | MIT |
| Default branch | `main` |
| README | Enabled |
| .gitignore | Platform-appropriate |
| Description | One sentence, no emoji |

**GitHub Topics — follow this convention:**

| Type | Topics |
|---|---|
| `syzygy-foundation-ios` | `syzygy`, `ios`, `swift`, `foundation`, `mobile` |
| `syzygy-ui-android` | `syzygy`, `android`, `kotlin`, `ui`, `jetpack-compose`, `mobile` |
| `syzygy-core-rn` | `syzygy`, `react-native`, `typescript`, `core`, `mobile` |
| `syzygy-services-flutter` | `syzygy`, `flutter`, `dart`, `services`, `mobile` |

---

## Required Files

Every Syzygy repo must contain:

```
{repo}/
├── syzygy.yml          ← manifest
├── README.md           ← follows readme-standard.md
├── CHANGELOG.md        ← follows changelog-standard.md
├── LICENSE             ← MIT
└── tooling/            ← platform lint config (fetched from .github)
    └── {platform}/
        └── .swiftlint.yml | .editorconfig | .eslintrc.json | .eslintrc.ts.json | analysis_options.yaml
```

> **RN repos:** Use `.eslintrc.json` for React Native app repos; use `.eslintrc.ts.json` for pure TypeScript library repos (e.g. `syzygy-foundation-rn`). See the [Tooling](#tooling) section for details.

---

## Branch and Commit Conventions

**Default branch:** `main`

**Commit message format:** imperative mood, present tense

```
Add SyzygyID generic typed identifier
Fix overlayAlpha not applied on Android ModalDialog
Remove deprecated UIColorToken.separator
```

**Prefixed commits:**

| Prefix | When |
|---|---|
| `release: X.X.X — description` | Merge commit for a release branch (convention only — releases are triggered by pushing the version tag, not by this prefix) |
| `fix: description` | Bug fixes |
| `chore: description` | Maintenance, dependency updates, tooling |
| `docs: description` | Documentation only changes |

No prefix needed for feature additions — the commit message describes what was added.

---

## .gitignore

Use the platform-appropriate GitHub .gitignore template:
- iOS: `Swift.gitignore`
- Android: `Android.gitignore`
- RN: `Node.gitignore`
- Flutter: `Dart.gitignore`

Add repo-specific entries below the template block.

---

## Required .gitignore Entries

Every Syzygy repo must include the following entries regardless of platform. These are the global minimum — the platform CI templates may add further entries on top.

### macOS artifacts

```
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
```

These are generated by macOS Finder and Spotlight. Never commit them.

### Editor artifacts

```
.vscode/
.idea/
*.swp
*.swo
*~
```

These cover VS Code, JetBrains IDEs, and Vim/Neovim temporary files. Never commit editor-local settings into a shared repo.

### Platform-specific entries

Platform-specific build outputs, dependency caches, and generated files are **not standardised here** — they are handled per-repo via the platform GitHub .gitignore template above.

Common examples (not exhaustive):

| Platform | Typical entries |
|---|---|
| iOS | `.build/`, `*.xcuserstate`, `DerivedData/` |
| Android | `build/`, `.gradle/`, `local.properties` |
| RN | `node_modules/`, `ios/Pods/`, `android/build/` |
| Flutter | `.dart_tool/`, `build/`, `.flutter-plugins` |

Add whatever your repo generates. The rule is: if it's generated locally and not needed by CI or other contributors, it goes in `.gitignore`.

---

## Tooling

Each repo fetches its lint config from the canonical source in this repo:

| Platform | Source |
|---|---|
| iOS | `engineering/tooling/ios/.swiftlint.yml` |
| Android | `engineering/tooling/android/.editorconfig` |
| RN (app) | `engineering/tooling/rn/.eslintrc.json` + `.prettierrc` |
| RN (TS library) | `engineering/tooling/rn/.eslintrc.ts.json` + `.prettierrc` |
| Flutter app/package | `engineering/tooling/flutter/analysis_options.yaml` (`flutter_lints`) |
| Pure-Dart library | `engineering/tooling/dart/analysis_options.yaml` (`lints`) |

Foundation, Core, Services, and AI Flutter repos are pure-Dart libraries (no Flutter SDK dependency) and must use the `dart/` config. Flutter app/package repos (Base Flutter, example apps) use the `flutter/` config. The pre-push hook auto-detects which applies. See [`engineering/hooks/README.md`](../hooks/README.md) for details.

Store a local copy under `tooling/{platform}/` in each repo. CI fetches the canonical version fresh on each run.

### Local Development — Pre-Push Lint Hook

To catch lint violations before CI, install the pre-push hook:

```bash
sh path/to/.github/engineering/hooks/setup-hooks.sh
```

The hook auto-detects your repo platform and runs the same lint checks that CI runs, using the same canonical configs. It blocks pushes on lint failure. See [`engineering/hooks/README.md`](../hooks/README.md) for full details, escape hatches, and troubleshooting.

### RN ESLint config variants

There are two ESLint configs for RN repos — choose based on what the repo contains:

| Config | File | Use when |
|---|---|---|
| React Native app | `.eslintrc.json` | The repo contains React Native components, screens, hooks, or any JSX/TSX. Includes `react`, `react-hooks`, `react-native`, and `import` plugins. |
| TypeScript library | `.eslintrc.ts.json` | The repo is a pure TypeScript library with no React or JSX (e.g. `syzygy-foundation-rn`, `syzygy-core-rn`). Requires only `@typescript-eslint`. |

**CI fetch — React Native app repo:**
```yaml
- name: Lint
  run: |
    curl -fsSL https://raw.githubusercontent.com/Syzygy-Hub/.github/main/engineering/tooling/rn/.eslintrc.json \
      -o .eslintrc.json
    curl -fsSL https://raw.githubusercontent.com/Syzygy-Hub/.github/main/engineering/tooling/rn/.prettierrc \
      -o .prettierrc
    npm run lint
```

**CI fetch — Pure TypeScript library repo:**
```yaml
- name: Lint
  run: |
    curl -fsSL https://raw.githubusercontent.com/Syzygy-Hub/.github/main/engineering/tooling/rn/.eslintrc.ts.json \
      -o .eslintrc.json
    curl -fsSL https://raw.githubusercontent.com/Syzygy-Hub/.github/main/engineering/tooling/rn/.prettierrc \
      -o .prettierrc
    npm run lint
```

> The `.eslintrc.ts.json` is fetched and saved as `.eslintrc.json` at the root so ESLint auto-discovers it without any extra configuration. Both variants share the same `.prettierrc`.

### Shared Lint Configuration

All Syzygy repos consume shared lint rules from the `Syzygy-Hub/.github` repository under `engineering/tooling/`. This is the canonical source for all platform lint configuration files.

| Platform | Path in `.github` | Config |
|---|---|---|
| iOS | `engineering/tooling/ios/.swiftlint.yml` | SwiftLint rules |
| Android | `engineering/tooling/android/.editorconfig` | ktlint config and EditorConfig |
| React Native | `engineering/tooling/rn/.eslintrc.json` + `.prettierrc` | ESLint and Prettier |
| React Native (TS library) | `engineering/tooling/rn/.eslintrc.ts.json` + `.prettierrc` | ESLint (TypeScript-only, no JSX) |
| Flutter app/package | `engineering/tooling/flutter/analysis_options.yaml` | Dart analyzer rules (`flutter_lints`) |
| Pure-Dart library | `engineering/tooling/dart/analysis_options.yaml` | Dart analyzer rules (`lints`) |

Consume the shared config in CI by fetching directly from this repo. Configs are always fetched from the latest `main`.

---

## Reusable Workflow Inputs Reference

All four platform CI workflows (`ios-ci.yml`, `android-ci.yml`, `rn-ci.yml`, `flutter-ci.yml`) are reusable via `workflow_call`. This section documents the shared and platform-specific inputs.

### Shared inputs (all platforms)

#### `org_config_sha`

```yaml
org_config_sha:
  required: false
  type: string
  default: 'main'
```

`org_config_sha` is the ref used to fetch tooling configs (SwiftLint, editorconfig, ESLint, analysis options) from `Syzygy-Hub/.github`. The default is `main` and this is the standard value for all repos — configs are always fetched from the latest `main`. There is no requirement to pin this to a commit SHA.

### Calling org-level reusable workflows

Syzygy workflows use floating version tags (`@v4`, `@v2`, `@main`) throughout. Do not SHA-pin action refs. When calling org-level reusable workflows use `@main` as the ref. The `org_config_sha` input always uses its default value of `main` — do not override it with a commit SHA.

#### `upload_artifacts`

```yaml
upload_artifacts:
  required: false
  type: boolean
  default: true
```

Controls whether the workflow uploads build artifacts (test results / coverage) to GitHub Actions. Defaults to `true`. Set to `false` to opt out (e.g. for matrix jobs where only one leg should upload, or to reduce storage usage).

Artifact upload paths per platform:

| Platform | Artifact name | Path uploaded |
|---|---|---|
| iOS | `test-artifacts` | `.build/reports/` |
| Android | `test-results` | `build/reports/tests/test` |
| RN | `coverage` | `coverage/` |
| Flutter | `coverage` | `coverage/` |

All uploads use `if-no-files-found: warn` — missing paths produce a warning, not a failure. The upload step runs with `if: always()` so artifacts are captured even when tests fail.

#### `coverage`

```yaml
coverage:
  required: false
  type: boolean
  default: true
```

Whether to run coverage-enabled tests and post a summary to the job summary. When `false`, the plain test command runs instead.

### Platform-specific inputs

#### Android — `java_version`

```yaml
java_version:
  required: false
  type: string
  default: '21'
```

JDK version passed to `actions/setup-java`. Must match the `jvmToolchain()` value in the repo's `build.gradle.kts`:

| Repo type | Value |
|---|---|
| Library (`syzygy-foundation-android`) | `'17'` |
| App / UI repos | `'21'` (default) |

#### Flutter — `flutter_version`

```yaml
flutter_version:
  required: false
  type: string
  default: 'stable'
```

Flutter version or channel passed to `subosito/flutter-action`. Pass a specific version string (e.g. `'3.22.0'`) to pin, or a channel name (`stable`, `beta`).

#### RN — `node_version`

```yaml
node_version:
  required: false
  type: string
  default: '22'
```

Node.js version passed to `actions/setup-node`.

#### RN — `eslint_config`

```yaml
eslint_config:
  required: false
  type: string
  default: '.eslintrc.json'
```

ESLint config filename to fetch from `engineering/tooling/rn/`. See [RN ESLint config variants](#rn-eslint-config-variants) above for when to use each value.

---

## AI Composition Guidance

This section covers how AI contracts (defined in [`ai-contract-spec.md`](ai-contract-spec.md)) should be consumed per platform, how API credentials must be handled, and how to wire implementations with the standard DI pattern.

### Declaring the AI contract dependency

Each platform's AI layer package (`syzygy-ai-{platform}`) is a separate library. Depend on it using the platform's standard package manager:

| Platform | Package manager | Dependency declaration |
|---|---|---|
| iOS | Swift Package Manager (SPM) | Add `syzygy-ai-ios` as a `.package` in `Package.swift`; import the `SyzygyAI` product |
| Android | Gradle (JitPack) | `implementation("com.github.Syzygy-Hub:syzygy-ai-android:{version}")` in `build.gradle.kts` |
| React Native | npm | `"syzygy-ai-rn": "^{version}"` in `package.json` |
| Flutter | pub | `syzygy_ai_flutter: ^{version}` in `pubspec.yaml` |

Depend only on the AI contracts package — never on a concrete provider SDK directly from `Base`, `Core`, or `Foundation`. Provider SDKs (Anthropic, OpenAI, etc.) are implementation details that live in `Services` or the application layer.

### API keys must never appear in contracts or Base

AI contract protocols (`LLMProvider`, `EmbeddingProvider`, etc.) must not accept or store raw API keys. The correct pattern:

- The protocol accepts a **credential provider** or **token provider** interface defined in `Foundation` or `Services`.
- The credential provider is responsible for fetching, refreshing, and supplying tokens at call time.
- Concrete values (API keys, bearer tokens) are injected by `Services` or the application layer — never hardcoded, never stored in a contract protocol, and never committed to source control.

```
// WRONG — never do this
protocol LLMProvider {
  var apiKey: String { get }  // ← exposes credential in contract
}

// CORRECT
protocol LLMProvider {
  var credentialProvider: CredentialProvider { get }  // ← provider supplies the token
}
```

### DI binding pattern

The standard layering is:

1. **`syzygy-ai-{platform}`** (AI contracts) — declares the protocol slots (`LLMProvider`, `AgentProtocol`, etc.). No implementations here.
2. **`syzygy-services-{platform}`** — provides concrete implementations (e.g. `AnthropicLLMProvider`) and wires them to the protocol slots via the DI container.
3. **App layer** — calls into `Services` to resolve the AI protocols; never constructs provider instances directly.

`Base` may reference AI contract protocols for shared UI/logic that needs to call AI, but `Base` must never instantiate or depend on a concrete provider. The implementation is always injected from `Services` or above.

---

### Example caller — full production usage

```yaml
# .github/workflows/ci.yml in a consuming repo
name: CI
on:
  push:
    branches: ['**']
  pull_request:
    branches: [main]

jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/rn-ci.yml@main
    with:
      eslint_config: '.eslintrc.ts.json'   # pure TS library
      node_version: '20'
      coverage: true
      upload_artifacts: true
```