<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Pre-Push Hooks

## Overview̌

The `pre-push` hook runs linters before pushing code to catch lint violations locally before CI. It auto-detects your repo's platform (iOS / Android / React Native / Flutter), fetches the canonical lint config from this org-level `.github` repo, and runs the appropriate linter.

The hook **blocks pushes on lint failure** — lint must pass to complete the push.

## Installation

Run this once after cloning any Syzygy repo:

```bash
sh path/to/.github/engineering/hooks/setup-hooks.sh
```

If the `.github` repo is in your standard Syzygy folder layout, the setup script auto-locates it:

```bash
# From inside syzygy-ui-ios (or any repo at the standard depth)
sh ../../../.github/engineering/hooks/setup-hooks.sh
```

The setup script symlinks the hook into `.git/hooks/pre-push`. It's idempotent — safe to re-run.

## How It Works

### Platform Detection

The hook detects your platform by checking for platform-specific files (in priority order):
- **iOS:** `Package.swift` → runs SwiftLint
- **Flutter:** `pubspec.yaml` → runs `flutter analyze`
- **Android:** `build.gradle.kts` or `build.gradle` → runs `./gradlew ktlintCheck`
- **React Native:** `package.json` → runs ESLint (via npm or npx)

### Config Fetching

Lint configs are fetched from the org-level `.github` repo **on every push** (not cached locally):
- iOS: `.swiftlint.yml`
- Android: `.editorconfig`
- React Native: `.eslintrc.json` (or `.eslintrc.ts.json` for pure TS repos) + `.prettierrc`
- Flutter: `analysis_options.yaml`

This ensures you always lint against the latest org standards without manual updates.

### Lint Execution

The hook:
1. Backs up any local lint config file
2. Fetches the org config and installs it temporarily
3. Runs the linter
4. Restores the original config (or removes the temp file)
5. Returns the linter's exit code (push blocked on non-zero)

## Escape Hatches

### Bypass the hook entirely

```bash
git push --no-verify
```

Use when you need to push without linting (rare). This is a built-in git feature.

### Offline mode: use local config

```bash
SYZYGY_LINT_LOCAL=1 git push
```

Skips fetching from GitHub and uses whatever config is already in your repo (or the linter's built-in defaults if none exists). Useful for airplane/train work or when the internet is unavailable.

### Skip Android lint (Gradle cold start)

```bash
SYZYGY_SKIP_ANDROID_LINT=1 git push
```

Android's `./gradlew ktlintCheck` can take 10–20 seconds on first run (Gradle daemon startup). Use this to skip Android-specific linting when you've already run it manually.

**Note:** This only skips Android. Other platforms' linters still run.

## Supported Platforms

| Platform | Linter | Config File | Install Step |
|---|---|---|---|
| **iOS** | SwiftLint | `.swiftlint.yml` | `brew install swiftlint` |
| **Android** | ktlint (via Gradle) | `.editorconfig` | Included in `build.gradle.kts` |
| **React Native** | ESLint + Prettier | `.eslintrc.json` + `.prettierrc` | `npm install` |
| **Flutter** | Dart analyzer | `analysis_options.yaml` | Included with `flutter` SDK |

### Linter not installed?

If a linter isn't installed, the hook **warns but allows the push**:

```
⚠ pre-push: swiftlint is not installed — skipping lint.
  Install it and re-push to enforce lint locally.
```

This is intentional — developers on different platforms don't need every toolchain. CI will catch any lint errors.

## Troubleshooting

### "Could not fetch lint config from…"

The hook couldn't reach GitHub. Check:
- Internet connection
- GitHub status (https://status.github.com)
- Corporate firewall or proxy blocking `raw.githubusercontent.com`

**Workaround:** Use `SYZYGY_LINT_LOCAL=1` to lint offline.

### Lint command fails with "command not found"

Install the platform's toolchain:
- **iOS:** `brew install swiftlint`
- **Android:** Included; ensure `gradlew` exists
- **React Native:** `npm install`
- **Flutter:** `flutter pub get`

Re-push to run the hook again.

### Gradle / Xcode toolchain not configured

Android Gradle or iOS Xcode setup issues will show errors from the linter. Address those errors per your platform's standards.

**Workaround:** Use `SYZYGY_SKIP_ANDROID_LINT=1` (Android only) to skip while you fix setup.

### Symlink is broken or missing

The `.git/hooks/pre-push` symlink may break if the `.github` repo is moved. Reinstall:

```bash
sh path/to/.github/engineering/hooks/setup-hooks.sh
```

### Hook runs even though I moved the .github repo

The hook is a symlink to a fixed path. If you move the `.github` repo, re-run `setup-hooks.sh` to update the symlink.

## Development

To test the hook locally (without pushing):

```bash
# Simulate a pre-push event
.git/hooks/pre-push
```

For offline testing:

```bash
SYZYGY_LINT_LOCAL=1 .git/hooks/pre-push
```

For debugging, the hook prints each step (platform, fetches, linter output):

```
pre-push: fetching SwiftLint config…
pre-push: running swiftlint…
✓ pre-push lint passed (ios)
```

Linter output is not suppressed, so you'll see any lint errors in full detail.
