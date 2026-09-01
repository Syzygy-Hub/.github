<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Reusable CI Workflows

These are reusable GitHub Actions workflows called by individual Syzygy repos via `workflow_call`. Each workflow is parameterised via inputs so the same workflow serves all repos of that platform type. All action references are SHA-pinned for supply chain security.

---

## ios-ci.yml

Runs SwiftLint, builds, and tests an iOS Swift Package Manager library or app.

| Trigger | Runner | Key inputs |
|---|---|---|
| `workflow_call` | `macos-latest` | `scheme`, `coverage`, `upload_artifacts`, `org_config_sha` |

**Steps:**
1. Checkout (`actions/checkout`)
2. Fetch SwiftLint config (curl `.swiftlint.yml` from `org_config_sha`)
3. Install SwiftLint (`brew install swiftlint`)
4. Lint (`swiftlint --config .swiftlint.yml`)
5. Build (`swift build`)
6. Test with coverage (`swift test --enable-code-coverage` + `xcrun llvm-cov report`) — when `coverage: true`
7. Test without coverage (`swift test`) — when `coverage: false`
8. Upload test artifacts (`actions/upload-artifact`, `build/reports/`) — when `upload_artifacts: true`

---

## android-ci.yml

Builds, lints with ktlint, tests, and optionally reports JaCoCo coverage for an Android Kotlin project.

| Trigger | Runner | Key inputs |
|---|---|---|
| `workflow_call` | `ubuntu-latest` | `coverage`, `java_version`, `upload_artifacts`, `org_config_sha` |

**Steps:**
1. Checkout (`actions/checkout`)
2. Set up JDK (`actions/setup-java`, version from `java_version` input, Temurin distribution)
3. Fetch ktlint config (curl `.editorconfig` from `org_config_sha`)
4. Build (`./gradlew build`)
5. ktlint check (`./gradlew ktlintCheck`)
6. Test (`./gradlew test`)
7. Upload test results (`actions/upload-artifact`, `build/reports/tests/test`) — when `upload_artifacts: true`
8. Coverage report (`./gradlew jacocoTestReport` + summary) — when `coverage: true`

> **Note:** `java_version` defaults to `'21'` for app repos. Library repos (e.g. `syzygy-foundation-android`) should pass `'17'` to match their `jvmToolchain()` setting.

---

## rn-ci.yml

Typechecks, lints, and tests a React Native or pure TypeScript library repo.

| Trigger | Runner | Key inputs |
|---|---|---|
| `workflow_call` | `ubuntu-latest` | `coverage`, `node_version`, `eslint_config`, `upload_artifacts`, `org_config_sha` |

**Steps:**
1. Checkout (`actions/checkout`)
2. Set up Node (`actions/setup-node`, version from `node_version` input)
3. Fetch ESLint and Prettier configs (curl from `org_config_sha`; removes any local `.eslintrc.js` / `.eslintrc.cjs` to prevent precedence conflicts)
4. Install dependencies (`npm install`)
5. Typecheck (`npm run typecheck`)
6. Lint (`npm run lint`)
7. Test with coverage (`npm test -- --coverage --coverageReporters=text-summary` + summary) — when `coverage: true`
8. Test without coverage (`npm test`) — when `coverage: false`
9. Upload coverage (`actions/upload-artifact`, `coverage/`) — when `upload_artifacts: true`

> **`eslint_config` input:** Pass `.eslintrc.json` (default) for React Native app repos that contain JSX/TSX components, screens, or hooks. Pass `.eslintrc.ts.json` for pure TypeScript library repos with no React or JSX (e.g. `syzygy-foundation-rn`, `syzygy-core-rn`). The fetched config is always saved as `.eslintrc.json` at the repo root so ESLint auto-discovers it.

---

## flutter-ci.yml

Analyzes and tests a Flutter Dart project with strict warnings enforcement.

| Trigger | Runner | Key inputs |
|---|---|---|
| `workflow_call` | `ubuntu-latest` | `coverage`, `flutter_version`, `upload_artifacts`, `org_config_sha` |

**Steps:**
1. Checkout (`actions/checkout`)
2. Set up Flutter (`subosito/flutter-action`, version from `flutter_version` input)
3. Fetch analysis config (curl `analysis_options.yaml` from `org_config_sha`)
4. Install dependencies (`flutter pub get`)
5. Analyze (`flutter analyze --fatal-warnings`)
6. Test with coverage (`flutter test --coverage` + lcov summary if available) — when `coverage: true`
7. Test without coverage (`flutter test`) — when `coverage: false`
8. Upload coverage (`actions/upload-artifact`, `coverage/`) — when `upload_artifacts: true`

---

## Coverage

Coverage is informational only — no threshold enforcement. Results appear in the GitHub Actions job summary. Coverage upload uses `if-no-files-found: warn` so missing coverage paths produce a warning rather than a failure, and the upload step runs with `if: always()` so artifacts are captured even when tests fail.

---

## SHA Pinning

All action references in these workflows are pinned to specific commit SHAs for supply chain security. Never replace SHA pins with floating version tags like `v3` or `v4`.

Both the `uses:` ref and the `org_config_sha` input should be pinned to the same commit SHA so the workflow file and the tooling configs it fetches are always in sync. See the [repository standard](https://github.com/Syzygy-Hub/.github/blob/main/engineering/standards/repository-standard.md#pinning-the-uses-ref) for the pinning pattern.
