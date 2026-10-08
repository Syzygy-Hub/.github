<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

<!-- TEMPLATE. Copy to the root of syzygy-example-{platform} as README.md and replace every {placeholder}. Standard: engineering/standards/example-apps-standard.md -->

# syzygy-example-{platform}

<!-- TODO: CI badge. Replace the workflow file name and owner once the repository exists. -->
[![CI](https://img.shields.io/github/actions/workflow/status/Syzygy-Hub/syzygy-example-{platform}/ci.yml?label=ci&style=flat)](https://github.com/Syzygy-Hub/syzygy-example-{platform}/actions/workflows/ci.yml)

{One sentence: what this example app shows, no emoji.}

> This is an example application. It is **not published** to any package registry. Its only release artefact is a GitHub Release.

## Purpose

{Two or three sentences: who the example is for and what it demonstrates about composing the Syzygy layers on {PLATFORM_NAME}.}

## Layers demonstrated

| Layer | Where it is shown | Status |
|---|---|---|
| Foundation | {screen or flow} | {status} |
| UI | {screen or flow} | {status} |
| Core | {screen or flow} | {status} |
| Services | {screen or flow} | {status} |
| AI | {screen or flow} | {status} |
| Base | {composition root and wiring} | {status} |

Status values come from the requirement table in `example-apps-standard.md`, section 6. Until the example is built, each row is `to be implemented`.

## Requirements

- {PLATFORM_NAME} {minimum version}
- {LANGUAGE} {version}
- {Tooling} {version}

## How to run

1. Clone the repository.
2. {Install step, for example `npm install`, `flutter pub get`, `pod install`, or Gradle sync.}
3. {Run step, for example `npx react-native run-ios` or `flutter run`.}
4. {Any configuration the app needs, and where to put it. Do not commit secrets.}

## Library compatibility

Library versions this example was built against are listed per release in the compatibility table: {link to the table, in this README or in the standard}.

Versions in `syzygy.yml` (`depends_on`) are the version ranges the example consumes.

## Versioning and release

This example versions independently of the Syzygy libraries. Releases are tagged with bare strict semver, for example `1.0.0`, with no `v` prefix. Each tag creates a GitHub Release from the matching CHANGELOG section. Nothing is published to a registry.

## Contributing

{Link to CONTRIBUTING.md in the Syzygy Hub, or a short note.}

## Security

{Link to SECURITY.md in the Syzygy Hub.}

## License

<!-- TODO: licence holder is a pending decision. See engineering/standards/repository-standard.md. Replace with the confirmed licence text and holder. -->
MIT. {TODO: copyright holder.} See [LICENSE](LICENSE).
