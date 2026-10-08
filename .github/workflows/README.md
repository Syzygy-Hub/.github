<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Reusable Workflows

Reusable GitHub Actions workflows called by platform repos through `workflow_call`. All nine files are reusable only. None has its own trigger.

| File | Purpose |
|---|---|
| `ios-ci.yml` | SwiftLint, build, test. SPM (`project_type: spm`) or Xcode (`project_type: xcode`). |
| `android-ci.yml` | Gradle build or assemble, ktlint, test. Library or app mode. Optional lint, publishing check, coverage, emulator tests. |
| `rn-ci.yml` | npm typecheck, lint, test. Optional native Android and iOS smoke builds. |
| `flutter-ci.yml` | Analyze and test. Flutter or pure Dart (auto-detected). Optional build smoke tests. |
| `ios-release.yml` | Tag and version check, CI gate, CHANGELOG, GitHub Release. SPM: no publish step. |
| `android-release.yml` | As iOS release. JitPack builds from the GitHub Release tag. |
| `rn-release.yml` | As iOS release. npm is published by the caller (see Releases). |
| `flutter-release.yml` | As iOS release, plus pub.dev publish. |
| `app-release.yml` | As iOS release, with no registry publish. For apps and templates. |

Callers pin the Hub ref in `uses:`, for example `uses: Syzygy-Hub/.github/.github/workflows/ios-ci.yml@main`. Action references inside these workflows use floating major tags (`@v4`, `@v2`, `@v1`).

---

## Common conventions

- **Failure policy (CI):** no build, lint, analysis or test failure is masked. There is no `|| true`, `continue-on-error` or `xcpretty` pipe. Only the coverage and summary steps tolerate missing output, and they emit `::warning::` annotations.
- **Concurrency (CI):** each CI workflow cancels superseded runs for the same workflow and ref.
- **Permissions:** CI workflows use `contents: read`. Release `validate` jobs use `contents: read`. Release jobs use `contents: write` (`id-token: write` on Flutter only). Only `ci-gate.yml` requests `actions: read`, and only when a caller adopts it.
- **Common inputs:** every CI workflow accepts `working_directory` (default `.`), `runner`, `org_config_sha` (default `main`), `coverage` and `upload_artifacts`. Release workflows have no `working_directory` or `runner` input. Their jobs run on fixed labels: `ubuntu-latest` for `validate` and most release jobs, `macos-latest` for the `ios-release.yml` release job.

---

## Inputs reference

### ios-ci.yml

| Input | Type | Default | Applies to | Description |
|---|---|---|---|---|
| `project_type` | string | `spm` | all | `spm` runs `swift build` / `swift test`. `xcode` runs `xcodebuild` against `xcode_project` or `xcode_workspace`. |
| `working_directory` | string | `.` | all | Directory containing `Package.swift` or the Xcode project. |
| `runner` | string | `macos-latest` | all | Must be a macOS runner. See the high-deployment-target note. |
| `org_config_sha` | string | `main` | all | Ref of `Syzygy-Hub/.github` used to fetch tooling configs. |
| `coverage` | boolean | `true` | all | Coverage report in the job summary. |
| `upload_artifacts` | boolean | `true` | all | Upload `<working_directory>/.build/reports/`. |
| `xcode_project` | string | `''` | `project_type: xcode` | `.xcodeproj` path, relative to `working_directory`. Set this or `xcode_workspace`, not both. |
| `xcode_workspace` | string | `''` | `project_type: xcode` | `.xcworkspace` path, relative to `working_directory`. Set this or `xcode_project`, not both. |
| `scheme` | string | `''` | `project_type: xcode` (required) | Xcode scheme to build and test. |
| `xcode_version` | string | `''` | all | Xcode `major.minor` (e.g. `16.2`). Empty keeps the runner default. Otherwise the step selects `/Applications/Xcode_<version>.app` and checks it with `xcodebuild -version`. The job fails if that Xcode is not installed on the image. |
| `ios_simulator_device` | string | `''` | `project_type: xcode` | Simulator device name. Empty means auto-detect. |
| `ios_simulator_os` | string | `''` | `project_type: xcode` | Simulator iOS version. Empty means auto-detect. Must be installed on the runner image. |
| `swiftlint_version` | string | `0.59.1` | all | SwiftLint release downloaded from GitHub Releases (`portable_swiftlint.zip`). The installed `swiftlint version` must equal this value. The release publishes no checksum asset, so the pin is by version only. |

**Simulator auto-detect (`project_type: xcode`, both fields empty):** the step selects the newest iOS runtime available to the chosen Xcode, then the newest iPhone on that runtime (highest generation, then Pro Max > Pro > Plus > base). Setting one field keeps the other on auto. Explicit values must be installed on the image. The resolved destination is written to the job summary. The job fails with `::error::` if no matching iPhone is found. With `project_type: spm`, no simulator is selected.

**SwiftLint config:** in `spm` mode the org config is fetched to `./.swiftlint.yml` and overwrites any local file. Its included paths assume `Sources/` and `Tests/`. In `xcode` mode the org config is fetched only when the repo has no `.swiftlint.yml`. App repos should copy the org config to the repo root and adapt its included paths.

### android-ci.yml

| Input | Type | Default | Applies to | Description |
|---|---|---|---|---|
| `project_type` | string | `library` | all | `library`: `build` (includes `assembleRelease`, `check`, `lint`) plus `test` and `ktlintCheck`. `app`: `assembleDebug`, `test`, `ktlintCheck`. **Callers on an application module must set `app`.** |
| `module` | string | `:` | all | Gradle project path. `:` is the root project. Otherwise a path such as `:app` or `:feature:login`. Task names are prefixed with it. |
| `java_version` | string | `21` | all | JDK for `setup-java` (Temurin). Must match the repo's `jvmToolchain()`. Library repos pass `'17'`. |
| `working_directory` | string | `.` | all | Directory containing `gradlew`. |
| `runner` | string | `ubuntu-latest` | all | Linux runner. Required for `instrumented_tests`. |
| `org_config_sha` | string | `main` | all | As above. |
| `coverage` | boolean | `true` | all | Runs `jacocoTestReport` and posts a summary. The consuming repo must define the task. |
| `upload_artifacts` | boolean | `true` | all | Upload test reports. |
| `run_lint` | boolean | `false` | all | Runs `lint`. Opt-in because it can surface new failures. The repo must define `lint`. |
| `validate_publishing` | boolean | `false` | `project_type: library` | Runs `publishToMavenLocal`. Setting it with `app` fails the job early. |
| `instrumented_tests` | boolean | `false` | all | Separate job running `connectedDebugAndroidTest` on an emulator. Requires a Linux runner with KVM. |
| `emulator_api_level` | number | `34` | `instrumented_tests` | Emulator API level. |
| `gradle_cache_read_only` | boolean | `false` | all | Passes `cache-read-only` to `setup-gradle`. Useful on non-default branches. |

The ktlint editorconfig is fetched to `<repo root>/.editorconfig` only when the repo has none. An existing `.editorconfig` is never overwritten.

### rn-ci.yml

| Input | Type | Default | Applies to | Description |
|---|---|---|---|---|
| `working_directory` | string | `.` | all | Directory containing `package.json`. |
| `runner` | string | `ubuntu-latest` | all | Runner for the library checks and the Android smoke job. |
| `org_config_sha` | string | `main` | all | As above. |
| `coverage` | boolean | `true` | all | Jest with coverage and a summary. When false, plain `npm test`. |
| `upload_artifacts` | boolean | `true` | all | Upload `coverage/`. |
| `node_version` | string | `22` | all | Node major. Ignored when `node_version_from_engines` is true. |
| `node_version_from_engines` | boolean | `false` | app repos | Read the minimum major from `package.json` `engines.node`. See the range rule below. |
| `eslint_config` | string | `.eslintrc.json` | all | Config fetched from `engineering/tooling/rn/`. Use `.eslintrc.ts.json` for pure TypeScript libraries. |
| `native_smoke_android` | boolean | `false` | app repos | Runs `./gradlew assembleDebug` in `<working_directory>/android`. |
| `native_java_version` | string | `17` | `native_smoke_android` | JDK for the Android smoke build (`17` or `21`). |
| `native_smoke_ios` | boolean | `false` | app repos | Runs `pod install` and an `iphonesimulator` `xcodebuild` in `<working_directory>/ios` on `macos-latest`. |
| `native_ios_scheme` | string | `''` | `native_smoke_ios` (required) | Xcode scheme to build. |

**Dependency install:** `npm ci` when `package-lock.json` exists. Without a lockfile the job falls back to `npm install`, writes a warning, and notes that the install is not reproducible. The required `typecheck`, `lint` and `test` scripts are checked up front.

**Node range rule (only when `node_version_from_engines: true`):** each `||` alternative contributes its `>=X` lower bound, or else its first number. The result is the minimum across alternatives. Examples: `>= 22.11.0` gives 22. `^22.13.0 || ^24.3.0 || >= 26.0.0` gives 22. `<=22 >=20` gives 20. `20 || >=22` gives 20. If `engines.node` is absent, the job fails.

### flutter-ci.yml

| Input | Type | Default | Applies to | Description |
|---|---|---|---|---|
| `working_directory` | string | `.` | all | Directory containing `pubspec.yaml`. |
| `runner` | string | `ubuntu-latest` | all | Runner for the analysis and test job and the Android build smoke job. |
| `org_config_sha` | string | `main` | all | As above. |
| `coverage` | boolean | `true` | all | Tests with coverage and a summary. |
| `upload_artifacts` | boolean | `true` | all | Upload `coverage/`. |
| `flutter_version` | string | `stable` | Flutter repos | Channel (`stable`, `beta`, `master`) or a pinned version such as `3.35.0`. Ignored for pure-Dart repos. |
| `dart_sdk_version` | string | `''` | pure-Dart repos | Pinned Dart SDK (e.g. `3.9.0`). Empty means latest stable. Ignored for Flutter repos. |
| `use_local_analysis_options` | boolean | `false` | all | Default `false`: the Hub config overwrites any repo-root `analysis_options.yaml`. `true`: keep a local file, and fetch the Hub config only when none exists. |
| `build_smoke_android` | boolean | `false` | Flutter repos | Runs `flutter build apk --debug` (requires `android/`). |
| `build_smoke_ios` | boolean | `false` | Flutter repos | Runs `flutter build ios --debug --no-codesign` on `macos-latest` (requires `ios/`). |

Repo type is detected from `sdk: flutter` in `pubspec.yaml`. Flutter repos use `tooling/flutter` and pure-Dart repos use `tooling/dart` (variant chosen per repo).

---

## Library and app recipes

Caller files live in each repo at `.github/workflows/ci.yml` (CI) and `.github/workflows/release.yml` (release). Use `@main`, or a branch ref while testing.

### iOS

**Library (SPM):**

```yaml
name: CI
on:
  push:
    branches: ['**']
    tags-ignore: ['*']
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/ios-ci.yml@main
    with:
      project_type: spm
      coverage: true
```

**App (Xcode):**

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/ios-ci.yml@main
    with:
      project_type: xcode
      xcode_project: SyzygyBase.xcodeproj   # or xcode_workspace: <App>.xcworkspace
      scheme: SyzygyBase
      coverage: false
      # runner / xcode_version: set for high deployment targets (see below)
      # ios_simulator_device / ios_simulator_os: leave empty to auto-detect
```

### Android

**Library:** library mode is the default. Pass the JDK the repo's `jvmToolchain()` uses.

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/android-ci.yml@main
    with:
      java_version: '17'
      project_type: library
      coverage: true   # requires jacocoTestReport in the repo
```

**App (application module):** set `project_type: app` and `module: ':app'`.

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/android-ci.yml@main
    with:
      java_version: '21'
      project_type: app
      module: ':app'
      coverage: false
      run_lint: true   # optional; the repo must define lint
```

### React Native

**Library (TypeScript only):**

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/rn-ci.yml@main
    with:
      node_version: '22'
      eslint_config: '.eslintrc.ts.json'
      coverage: true
```

**App:** read the Node major from `engines.node`, and opt in to native smoke builds if needed.

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/rn-ci.yml@main
    with:
      node_version_from_engines: true
      eslint_config: '.eslintrc.json'
      native_smoke_android: true
      native_smoke_ios: true
      native_ios_scheme: <Scheme>
```

Repos whose `engines.node` is missing must set `node_version` explicitly, because `node_version_from_engines: true` fails in that case.

### Flutter

**Library (pure Dart):**

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/flutter-ci.yml@main
    with:
      coverage: true
```

**App (Flutter):**

```yaml
jobs:
  ci:
    uses: Syzygy-Hub/.github/.github/workflows/flutter-ci.yml@main
    with:
      flutter_version: '3.35.0'   # or 'stable'
      build_smoke_android: true
      build_smoke_ios: true
```

Pure-Dart libraries that need a repo-local analysis file should pass `use_local_analysis_options: true`.

---

## Releases

Callers float on `@main`, so these changes reach a caller as soon as they merge to `main`.

All five release workflows share one flow:

1. **`validate`** checks the tag and `syzygy.yml`, and for Flutter also `pub_auth`. It requests `contents: read` only and never receives secrets.
2. **`release`** (`needs: validate`) extracts the CHANGELOG entry, asserts `pubspec.yaml` (Flutter), publishes where applicable, creates the GitHub Release and, if configured, notifies a website repo. It requests `contents: write`. Flutter also requests `id-token: write`, which is inert unless `pub_auth: oidc`. The other workflows request no `id-token`.

Each caller's own `release.yml` owns the `push: tags` trigger and calls the Hub workflow with `secrets: inherit`. The caller grants `contents: write` (and `id-token: write` for Flutter) at workflow level. All 20 release callers already do. The audit is in `_audit/step1/RELEASE-PERMISSIONS.md`.

**Compatibility.** The release workflows have no `ci_gate` or `skip_ci_gate` input and do not check CI. `ci_workflow_name` is still accepted and ignored, so existing callers do not break. Any input not listed in the table below is rejected by GitHub when the workflow starts, so callers must pass only listed inputs.

**The CI gate is opt-in and sits in the caller.** To gate a release on CI, the caller adds a `gate` job that calls `ci-gate.yml` with `permissions: actions: read` at job level, and makes `release` depend on it (`needs: gate`). The release templates in `engineering/templates/` show this block commented out. The gate policy itself is in the gate section of `engineering/standards/release-standard.md`.

**Who publishes.** Registry publishing is platform-specific. Flutter publishes to pub.dev inside `flutter-release.yml`. React Native publishes to npm from each caller's own `publish-npm` job, because npm OIDC trusted publishing needs the caller's workflow file. iOS (SPM) and Android (JitPack) publish nothing beyond the GitHub Release, since the tag is the artefact. Apps (`app-release.yml`) publish nothing.

### Tag and version rules

- **Strict semver tags.** The tag must match `^[0-9]+\.[0-9]+\.[0-9]+$`, for example `3.0.0`. Tags with a `v` prefix are rejected, and so are pre-release or build-metadata tags such as `3.0.0-rc1`. Callers should use the strict tag filter `'[0-9]+.[0-9]+.[0-9]+'` in `on.push.tags`. The loose filter `'*'` lets through tags the Hub then rejects.
- **Reading `syzygy.yml`.** The value after `version:` is read, then any `#` comment, whitespace, and single or double quotes are removed. `3.0.0`, `"3.0.0"`, `'3.0.0'` and `3.0.0 # comment` all read as `3.0.0`.
- **Standard releases** (iOS, Android, RN, Flutter): the `syzygy.yml` version must equal the tag exactly.
- **`flutter-release`:** the release job also asserts that `pubspec.yaml` `version:` equals `syzygy.yml` exactly, including any `+build` suffix. The release does not rewrite `pubspec.yaml`. Example: `pubspec 3.0.0+1` against `syzygy.yml 3.0.0` fails.
- **`app-release`:** compares the MAJOR.MINOR.PATCH core only. Build metadata after `+` is ignored, but must contain only `[0-9A-Za-z.-]`. Example: `syzygy.yml 3.0.0+1` with tag `3.0.0` passes. `3.0.0-rc1` fails.

### CHANGELOG

The release notes are the body of the `## [<version>]` section, excluding the heading. The release fails if the section is missing or empty. `allow_empty_notes: true` uses generic notes and warns.

### Website notification (optional, off by default)

- **Inputs:** `notify_website_repo` (string, default `''`, meaning off). Secret: `WEBSITE_DISPATCH_TOKEN`, optional, declared with `required: false`. It reaches the workflow only through `secrets: inherit`.
- **When it runs:** only after the GitHub Release is created, and only if `notify_website_repo` is set and the token is passed. The step sends `POST https://api.github.com/repos/<notify_website_repo>/dispatches` with `event_type: syzygy-release` and `client_payload: { repo, tag, version }`. `repo` is the caller's `owner/repo`. `tag` and `version` are the bare semver.
- **Failure handling:** a missing token skips the step silently. An invalid repo name, a response other than HTTP 204, or a network error emits `::warning::` and the release still succeeds.
- **Permissions:** the step runs inside the existing `release` job and adds none. The token needs permission to create repository dispatch events on the target repo (for a fine-grained token, `contents: write` on that repo).
- **Caller example:**

```yaml
jobs:
  release:
    permissions:
      contents: write
    uses: Syzygy-Hub/.github/.github/workflows/ios-release.yml@main
    with:
      notify_website_repo: Syzygy-Hub/website
    secrets: inherit
```

### Per-workflow release inputs

| Workflow | Inputs | Secrets | Publish |
|---|---|---|---|
| `ios-release.yml` | `allow_empty_notes`, `notify_website_repo`, `ci_workflow_name` (accepted, ignored) | `WEBSITE_DISPATCH_TOKEN` (optional) | None. The git tag is the release. |
| `android-release.yml` | as above | as above | None. JitPack builds from the tag. |
| `rn-release.yml` | as above; output `version` | as above | None in this workflow. npm is published from the caller's own `publish-npm` job, because npm OIDC trusted publishing requires the caller's workflow file as `job_workflow_ref`. This workflow requests no `id-token`. |
| `flutter-release.yml` | as above, plus `pub_auth` (`credentials` default, or `oidc`) | `PUB_CREDENTIALS` (credentials mode), `WEBSITE_DISPATCH_TOKEN` (optional) | pub.dev. `credentials` runs `flutter pub publish --force`. `oidc` runs `dart pub publish --force` and needs `id-token: write`. `oidc` is prepared but no caller enables it. |
| `app-release.yml` | `allow_empty_notes`, `notify_website_repo`, `ci_workflow_name` (accepted, ignored) | `WEBSITE_DISPATCH_TOKEN` (optional) | None. |

For `pub_auth: oidc`, automated publishing must be enabled per package on pub.dev first. Verify that pub.dev accepts the reusable-workflow token before any caller switches. The propagation check after publish is a warning, not a failure.

---
## High deployment targets (iOS)

Projects whose deployment target is newer than the default runner's SDK and simulator runtimes need both `runner` and `xcode_version` set. Example: `syzygy-base-ios` deploys to iOS 26.5.

- The runner image must ship an iOS 26.x SDK and simulator runtime.
- `xcode_version` must name an Xcode installed at `/Applications/Xcode_<version>.app` on that image.
- Illustrative caller inputs (not applied to any repo here):

```yaml
with:
  project_type: xcode
  xcode_workspace: <App>.xcworkspace
  scheme: <Scheme>
  runner: macos-26        # example label, not confirmed as offered
  xcode_version: '26.0'   # example, not confirmed on that image
```

Before use, confirm that the runner label is offered on GitHub-hosted runners and that the Xcode version is installed on that image. Leave the simulator fields empty to auto-detect.
