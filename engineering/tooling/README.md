<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Shared Lint Configuration

This folder contains the canonical shared lint configuration files for all Syzygy platform repos. All repos consume these configs via curl fetch in their CI workflows, always from the latest `main`.

---

## ios/

**File:** `.swiftlint.yml`

**Consumed by:** all `syzygy-*-ios` repos (foundation, ui, core, services, base, and future iOS libraries/apps).

**Fetched via:** the `org_config_sha` input in `ios-ci.yml`. The workflow curls this file into the consuming repo's root as `.swiftlint.yml` before running `swiftlint --config .swiftlint.yml`.

**Key rules enforced:**

- **Opt-in rules enabled:** `empty_count` (prefer `.isEmpty` over `.count == 0`), `closure_spacing`, `explicit_init`, `redundant_type_annotation`
- **Disabled rules:** `todo` — TODO/FIXME comments are allowed during active development
- **Force unwrapping / casting:** `warning` severity (not error) — intentional force-unwraps in tests and static assets are acceptable
- **Line length:** warning at 120, error at 200; comments and URLs are excluded
- **File length:** warning at 400 lines, error at 600 — accounts for SwiftUI view bodies that mix view, preview, and helper code
- **Type body length:** warning at 250, error at 400
- **Function body length:** warning at 60, error at 100
- **Identifier name:** minimum length 2; `id` is explicitly allowed
- **Included paths:** `Sources/`, `Tests/` — targets the standard SPM layout of consuming repos

---

## android/

**File:** `.editorconfig`

**Consumed by:** all `syzygy-*-android` repos (foundation, ui, core, services, base, and future Android libraries/apps).

**Fetched via:** the `org_config_sha` input in `android-ci.yml`. The workflow curls this file into the consuming repo's root as `.editorconfig`; ktlint reads it automatically alongside the standard EditorConfig properties.

**Key rules enforced:**

- **Global:** UTF-8 charset, LF line endings, final newline required, trailing whitespace trimmed, 4-space indent
- **Kotlin files (`*.{kt,kts}`):** 4-space indent, 120-char max line length, final newline
- **ktlint standard rules enabled:** `no-wildcard-imports`, `import-ordering`, `max-line-length`, `final-newline`, `no-trailing-spaces`
- **Trailing commas:** disabled on both call sites and declaration sites — optional stylistic preference, not enforced
- **YAML/JSON files:** 2-space indent
- **Markdown files:** trailing whitespace trimmed disabled (allows intentional trailing spaces for line breaks)

---

## rn/

**Files:** `.eslintrc.json` (app repos), `.eslintrc.ts.json` (pure TypeScript library repos), `.prettierrc` (all RN repos)

**Consumed by:** all `syzygy-*-rn` repos (foundation, ui, core, services, base, and future RN libraries/apps).

**Fetched via:** the `org_config_sha` and `eslint_config` inputs in `rn-ci.yml`. The workflow curls the chosen ESLint config and saves it as `.eslintrc.json` at the repo root. It also removes any local `.eslintrc.js` / `.eslintrc.cjs` to prevent precedence conflicts.

### When to use each ESLint config

| Config file | Use when |
|---|---|
| `.eslintrc.json` | The repo contains React Native components, screens, hooks, or any JSX/TSX. Default for app repos (`syzygy-base-rn`, `syzygy-ui-rn`). |
| `.eslintrc.ts.json` | The repo is a pure TypeScript library with no React or JSX (e.g. `syzygy-foundation-rn`, `syzygy-core-rn`). |

Pass the config filename via the `eslint_config` input to `rn-ci.yml`. The fetched file is always saved as `.eslintrc.json` so ESLint auto-discovers it without extra configuration.

### `.eslintrc.json` — React Native app config

**Key rules enforced:**
- Parser: `@typescript-eslint/parser` with JSX enabled (`ecmaFeatures.jsx: true`)
- Plugins: `@typescript-eslint`, `react`, `react-hooks`, `react-native`, `import`
- Extends: `eslint:recommended`, `plugin:@typescript-eslint/recommended`, `plugin:react/recommended`, `plugin:react-hooks/recommended`, `eslint-config-prettier` (last — disables formatting rules conflicting with Prettier)
- `@typescript-eslint/no-unused-vars`: warn (ignores underscore-prefixed args and vars)
- `@typescript-eslint/no-explicit-any`: warn
- `react/prop-types`: off (TypeScript provides type safety)
- `react/react-in-jsx-scope`: off (React 17+ JSX transform)
- `react-native/no-inline-styles`: warn
- `react-native/no-unused-styles`: warn
- `import/order`: warn — enforces import group ordering with alphabetical sort and blank lines between groups
- Ignore patterns: `dist`, `node_modules`, `lib`, `build`

### `.eslintrc.ts.json` — Pure TypeScript library config

**Key rules enforced:**
- Parser: `@typescript-eslint/parser` — no JSX
- Plugins: `@typescript-eslint` only
- Extends: `eslint:recommended`, `plugin:@typescript-eslint/recommended`
- `@typescript-eslint/no-explicit-any`: **error** (stricter than the app config)
- `@typescript-eslint/explicit-function-return-type`: warn (off in test files via override)
- `@typescript-eslint/no-unused-vars`: error with `argsIgnorePattern: "^_"` — function parameters prefixed with `_` are treated as intentionally unused and will not trigger the rule (e.g. `_reason`, `_token`, `_key`). Use this convention in mocks and interface implementations where a parameter is required by the contract but not used.
- `no-console`: warn
- Env: `node`, `es2020`
- Test override: `explicit-function-return-type` disabled for `**/*.test.ts` and `**/__tests__/**/*.ts`

### `.prettierrc` — Shared Prettier config (all RN repos)

```json
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "all",
  "tabWidth": 2,
  "useTabs": false,
  "printWidth": 100,
  "arrowParens": "always"
}
```

---

## dart/

**File:** `analysis_options.yaml`

**Consumed by:** pure-Dart library repos (`syzygy-foundation-flutter`, `syzygy-core-flutter`, `syzygy-services-flutter`, `syzygy-ai-flutter`) — repos that have **no** Flutter SDK dependency and must remain publishable with `dart pub`.

**Fetched via:** the pre-push hook and CI for pure-Dart repos. The hook auto-detects that `pubspec.yaml` has no `sdk: flutter` dependency and fetches this config instead of `flutter/analysis_options.yaml`.

**Key rules enforced:**

- **Base:** extends `package:lints/recommended.yaml` (the Dart-standard lint set, not `flutter_lints`)
- `avoid_print`: true — prefer a real logger over `print()` in production code
- `prefer_single_quotes`: true — matches the single-quote convention used in the shared ESLint/Prettier config
- `always_declare_return_types`: true
- `unnecessary_this`: true
- **Excluded from analysis:** `**/*.g.dart`, `**/*.freezed.dart`, `build/**`

**Why `lints` and not `flutter_lints`?** Pure-Dart packages have no Flutter SDK dependency. Using `flutter_lints` would require the Flutter SDK to be installed to run `dart analyze`, preventing these packages from being published and tested with `dart pub` alone.

---

## flutter/

**File:** `analysis_options.yaml`

**Consumed by:** Flutter app and package repos (`syzygy-base-flutter`, `syzygy-ui-flutter`, and Flutter example apps) — repos that declare `sdk: flutter` as a dependency.

**Fetched via:** the `org_config_sha` input in `flutter-ci.yml`. The workflow curls this file into the consuming repo's root as `analysis_options.yaml` before running `flutter analyze --fatal-warnings`. The pre-push hook auto-detects Flutter repos (via `sdk: flutter` in `pubspec.yaml`) and fetches this config.

**Key rules enforced:**

- **Base:** extends `package:flutter_lints/flutter.yaml` (Flutter's recommended lint set)
- `prefer_const_constructors`: true — lets Flutter skip subtree rebuilds for const widgets
- `prefer_const_constructors_in_immutables`: true
- `prefer_const_literals_to_create_immutables`: true
- `avoid_print`: true — prefer a real logger over `print()` in production code
- `prefer_single_quotes`: true — matches the single-quote convention used in the shared ESLint/Prettier config
- `always_declare_return_types`: true
- `avoid_unnecessary_containers`: true — a `Container` with no styling is wasted nesting
- `sized_box_for_whitespace`: true — `SizedBox` is cheaper than `Container` for pure spacing
- `unnecessary_this`: true
- **Excluded from analysis:** `**/*.g.dart`, `**/*.freezed.dart`, `build/**`

### Dart/Flutter config split summary

| Repo type | Example repos | Config used | Analyze command |
|---|---|---|---|
| Pure-Dart library | `syzygy-foundation-flutter`, `syzygy-core-flutter`, `syzygy-services-flutter`, `syzygy-ai-flutter` | `tooling/dart/analysis_options.yaml` (`lints`) | `dart analyze` |
| Flutter app/package | `syzygy-base-flutter`, example apps | `tooling/flutter/analysis_options.yaml` (`flutter_lints`) | `flutter analyze` |

The pre-push hook auto-detects which config applies (see [`engineering/hooks/README.md`](../hooks/README.md)). The `dart/` config path was introduced in Foundation v2.0.0.

---

## Local Linting

To catch lint violations **before pushing**, developers can install the pre-push hook from the Syzygy-Hub/.github repo:

```bash
sh path/to/.github/engineering/hooks/setup-hooks.sh
```

The hook runs locally on every push, using the same lint configs and rules documented here. This catches violations at dev time rather than CI time. See [`engineering/hooks/README.md`](../hooks/README.md) for installation, usage, and escape hatches (offline mode, platform-specific skips).

---

## Updating Lint Rules

To update a lint rule, edit the relevant file in this folder and commit to `main`. All consuming repos pick up the change automatically on their next CI run, since configs are always fetched from `main`.

When a rule changes severity (e.g. from warning to error), note it in a commit message and check that it won't silently break currently-green CI runs in consuming repos.
