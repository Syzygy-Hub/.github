<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Reusable CI Workflows

These are reusable GitHub Actions workflows called by individual Syzygy repos via `workflow_call`. Each workflow is parameterised via inputs so the same workflow serves all repos of that platform type. All action references use floating version tags (`@v4`, `@v2`, `@main`).

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

## ios-release.yml

Validates the pushed tag against `syzygy.yml`, extracts the CHANGELOG entry, and creates a GitHub Release. SPM publishing is automatic — no explicit publish step needed (the git tag is the SPM release).

| Trigger | Runner | Key inputs |
|---|---|---|
| `push: tags '[0-9]+.[0-9]+.[0-9]+'`, `workflow_call` | `macos-latest` | _(none beyond the tag)_ |

**Steps:**
1. Checkout (`actions/checkout`, `fetch-depth: 0`)
2. Read and validate version (reads `version:` from `syzygy.yml`; fails if it does not match the pushed tag)
3. Extract CHANGELOG entry (`awk` — extracts the first versioned section from `CHANGELOG.md` into `release_notes.txt`)
4. SPM note (echo confirming the tag is the SPM release)
5. Create GitHub Release (`gh release create` with `--notes-file release_notes.txt` and `--target` set to the commit SHA)

---

## android-release.yml

Validates the pushed tag against `syzygy.yml`, extracts the CHANGELOG entry, and creates a GitHub Release. JitPack auto-builds from the GitHub Release tag — no explicit publish step needed.

| Trigger | Runner | Key inputs |
|---|---|---|
| `push: tags '[0-9]+.[0-9]+.[0-9]+'`, `workflow_call` | `ubuntu-latest` | _(none beyond the tag)_ |

**Steps:**
1. Checkout (`actions/checkout`, `fetch-depth: 0`)
2. Read and validate version (reads `version:` from `syzygy.yml`; fails if it does not match the pushed tag)
3. Extract CHANGELOG entry (`awk` — extracts the first versioned section from `CHANGELOG.md` into `release_notes.txt`)
4. JitPack note (echo confirming JitPack will auto-build from the tag)
5. Create GitHub Release (`gh release create` with `--notes-file release_notes.txt` and `--target` set to the commit SHA)

---

## rn-release.yml

Validates the pushed tag against `syzygy.yml`, publishes the npm package, and creates a GitHub Release.

| Trigger | Runner | Key inputs |
|---|---|---|
| `push: tags '[0-9]+.[0-9]+.[0-9]+'`, `workflow_call` | `ubuntu-latest` | `NPM_TOKEN` (secret) |

**Steps:**
1. Checkout (`actions/checkout`, `fetch-depth: 0`)
2. Read and validate version (reads `version:` from `syzygy.yml`; fails if it does not match the pushed tag)
3. Extract CHANGELOG entry (`awk` — extracts the first versioned section from `CHANGELOG.md` into `release_notes.txt`)
4. Set up Node (`actions/setup-node@v4`, Node 18, registry `https://registry.npmjs.org`)
5. Install dependencies (`npm ci`)
6. Publish to npm (`npm publish --access=public --provenance`, authenticated via `NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}`)
7. Create GitHub Release (`gh release create` with `--notes-file release_notes.txt` and `--target` set to the commit SHA)

---

## flutter-release.yml

Validates the pushed tag against `syzygy.yml`, publishes the Dart package to pub.dev, waits for propagation, and creates a GitHub Release.

| Trigger | Runner | Key inputs |
|---|---|---|
| `push: tags '[0-9]+.[0-9]+.[0-9]+'`, `workflow_call` | `ubuntu-latest` | `PUB_CREDENTIALS` (secret) |

**Steps:**
1. Checkout (`actions/checkout`, `fetch-depth: 0`)
2. Read and validate version (reads `version:` from `syzygy.yml`; fails if it does not match the pushed tag)
3. Extract CHANGELOG entry (`awk` — extracts the first versioned section from `CHANGELOG.md` into `release_notes.txt`)
4. Set up Flutter (`subosito/flutter-action@v2`, stable channel)
5. Setup pub credentials (writes `${{ secrets.PUB_CREDENTIALS }}` to `$HOME/.config/dart/pub-credentials.json`)
6. Install dependencies (`flutter pub get`)
7. Sync pubspec.yaml version (`sed` patches `pubspec.yaml` version to match the validated tag)
8. Publish to pub.dev (`flutter pub publish --force`)
9. Wait for pub.dev propagation (polls `https://pub.dev/api/packages/$PACKAGE_NAME` every 10 s for up to 30 attempts; emits a warning rather than failing if the version is not confirmed after 300 s)
10. Create GitHub Release (`gh release create` with `--notes-file release_notes.txt` and `--target` set to the commit SHA)

---

## Coverage

Coverage is informational only — no threshold enforcement. Results appear in the GitHub Actions job summary. Coverage upload uses `if-no-files-found: warn` so missing coverage paths produce a warning rather than a failure, and the upload step runs with `if: always()` so artifacts are captured even when tests fail.

---

## Floating Action Refs

All action references in these workflows use floating version tags (`@v4`, `@v2`, `@main`) rather than SHA-pinned commits. This is a deliberate decision for a solo-maintained organisation where maintenance overhead outweighs supply chain risk. When a new major version of an action is released, update the floating tag across all workflows in a single pass. Do not add SHA pins — they are not used in this ecosystem.
