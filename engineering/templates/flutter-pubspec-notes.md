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

**Standard Syzygy Flutter pubspec template:**

```yaml
name: syzygy_{type}_flutter
version: 1.0.0
description: "One-line description."
repository: https://github.com/Syzygy-Hub/syzygy-{type}-flutter

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  syzygy_foundation_flutter: ^1.0.0

dev_dependencies:
  flutter_lints: ^3.0.0
  test: ^1.24.0
```

Note: `publish_to` is absent — this is correct and intentional.
