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

## flutter/

**File:** `analysis_options.yaml`

**Consumed by:** all `syzygy-*-flutter` repos (foundation, ui, core, services, base, and future Flutter libraries/apps).

**Fetched via:** the `org_config_sha` input in `flutter-ci.yml`. The workflow curls this file into the consuming repo's root as `analysis_options.yaml` before running `flutter analyze --fatal-warnings`.

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

---

## Updating Lint Rules

To update a lint rule, edit the relevant file in this folder and commit to `main`. All consuming repos pick up the change automatically on their next CI run, since configs are always fetched from `main`.

When a rule changes severity (e.g. from warning to error), note it in a commit message and check that it won't silently break currently-green CI runs in consuming repos.
