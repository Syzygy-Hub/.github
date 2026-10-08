<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Flutter pubspec.yaml — Scaffolding Notes

## `publish_to` blocklist

**INVALID — do not use:**

```yaml
publish_to: https://pub.dev
```

`pub.dev` rejects packages that set `publish_to` to `https://pub.dev`. The field is intended to redirect publishing to a *different* host, not to re-specify the default. Setting it to `https://pub.dev` causes `dart pub publish` to fail with a validation error.

**Correct options:**

| Scenario | `publish_to` value | Notes |
|---|---|---|
| Public package on pub.dev | *(omit the field entirely)* | Defaults to pub.dev — this is the standard for all Syzygy Flutter packages |
| Private / internal package | `publish_to: none` | Prevents accidental publishing; use for packages that should never be released publicly |
| Private registry | `publish_to: https://your-registry.example.com` | Only when targeting an internal pub server |

**Standard Syzygy Flutter pubspec template (pure-Dart library):**

```yaml
name: syzygy_{type}_flutter
version: 1.0.0
description: "One-line description."
repository: https://github.com/Syzygy-Hub/syzygy-{type}-flutter

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  syzygy_foundation_flutter: ^2.0.0

dev_dependencies:
  lints: ^3.0.0
  test: ^1.24.0
```

Note: `publish_to` is absent — this is correct and intentional.

> **`lints` not `flutter_lints`:** Foundation, Core, Services, and AI Flutter repos are pure-Dart libraries with no Flutter SDK dependency. They use `lints` (from `package:lints`) so they can be analysed and published with `dart pub` without requiring the Flutter SDK. Use `flutter_lints` only in Flutter app/package repos that declare `sdk: flutter` (e.g. `syzygy-base-flutter`, example apps). See `tooling/dart/analysis_options.yaml` and `tooling/flutter/analysis_options.yaml` for the canonical configs.
