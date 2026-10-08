<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Syzygy Example Apps Standard

This standard defines the Syzygy Example App: one reference application per platform that composes the Syzygy layers and shows how they fit together.

**Status:** planned. The four example repositories are **not created** by this document. Creating them is a separate owner decision.

---

## 1. Scope

| Repository | Platform | Language | Package manager (how the example consumes libraries) |
|---|---|---|---|
| `syzygy-example-ios` | iOS | swift | `spm` |
| `syzygy-example-android` | Android | kotlin | `jitpack` |
| `syzygy-example-rn` | React Native | typescript | `npm` |
| `syzygy-example-flutter` | Flutter | dart | `pub.dev` |

Repository names follow the pattern `syzygy-example-{platform}` in [`syzygy.schema.json`](../schema/syzygy.schema.json).

An example is an application, not a library. It has no public API for consumers to depend on.

---

## 2. Not published to package registries

Example apps are **never published** to a package registry. They are not published to npm, pub.dev, JitPack or SPM. Their only release artefact is a GitHub Release, created by the no-publish mode of `app-release.yml`. See section 8.

---

## 3. Versioning

Examples version **independently** of the libraries. An example at `2.1.0` may consume libraries at `3.0.0`. Its version does not have to match any library version.

- **Strict SemVer, bare tags.** Tags are `MAJOR.MINOR.PATCH` with no `v` prefix and no pre-release suffix, for example `1.0.0`. The tag must match `^[0-9]+\.[0-9]+\.[0-9]+$`. This is the same rule as [release-standard.md](release-standard.md).
- **`syzygy.yml` `version:` must equal the tag** and the CHANGELOG must contain a `## [X.X.X]` section for it.
- **MAJOR:** a change that forces readers or forks to rewrite how they wire layers, for example a different composition or DI pattern.
- **MINOR:** a new demonstrated flow or layer, or a new library version range in `depends_on`.
- **PATCH:** fixes, documentation, and tooling changes that do not change the demonstrated patterns.

Whether an example version works with a given library version is recorded only in the compatibility table (section 4).

---

## 4. Compatibility table

Each example release is mapped to the library versions it was built and tested against. The table is maintained by the owner as versions ship. **No rows are defined by this standard.** Do not add rows for versions that have not shipped.

Format, one table per example repository (kept in that repository's README, which links to this section):

| Example version | syzygy-foundation | syzygy-core | syzygy-services | syzygy-ai | syzygy-ui | syzygy-base (if consumed) |
|---|---|---|---|---|---|---|

Rules:

- Each cell is the library version (bare semver) the example release was built against. Use `n/a` if the layer is not consumed.
- Rows are added in descending example-version order, one row per example release.
- A row is added in the same change as the example's release PR, and only after the release is tagged.

---

## 5. Required `syzygy.yml` shape

Every example repository has a `syzygy.yml` at the repo root. Template: [`syzygy.yml.template`](../templates/syzygy.yml.template) (example variant, commented).

```yaml
name: syzygy-example-ios                 # syzygy-example-{platform}
type: example                            # required value for example repos
platform: ios
language: swift
package_manager: spm                     # how the example consumes libraries (section 1)
license: MIT
version: 0.0.0                           # placeholder. Bare strict semver; the owner sets the real value at first release and it equals the tag.
syzygy_foundation: ">=3.0.0"             # required for every type except foundation
description: "One sentence, no emoji"
demonstrates: [foundation, ui, core, services, ai, base]
depends_on:
  - name: syzygy-foundation-ios
    version_constraint: ">=3.0.0"
  - name: syzygy-ui-ios
    version_constraint: ">=3.0.0"
```

Field rules:

- `type: example` is required.
- `demonstrates` is a list of canonical layer identifiers: `foundation`, `ui`, `core`, `services`, `ai`, `base`. It must list every layer in section 6 for the platform.
- `depends_on` is a list of mappings with `name` (a library repository name) and `version_constraint` (a version range with bare semver operands). It lists the library repositories the example consumes. `syzygy-base-*` is a template, not a library, so it appears in `depends_on` only if the example consumes its code.
- The schema accepts `demonstrates` and `depends_on` **only** on `type: example`. Any other type that sets them fails validation.
- Validate with `engineering/tooling/validate-syzygy/validate.py`. The validator is report-only by default.

---

## 6. Layers each example must demonstrate

Each example must demonstrate **all six layers** on its platform. A layer is demonstrated when at least one user-visible flow exercises that layer's public API.

Every cell below is currently **to be implemented**. No example repository exists yet, so no cell is complete.

| Layer | iOS (`syzygy-example-ios`) | Android (`syzygy-example-android`) | RN (`syzygy-example-rn`) | Flutter (`syzygy-example-flutter`) |
|---|---|---|---|---|
| Foundation (`foundation`) | to be implemented | to be implemented | to be implemented | to be implemented |
| UI (`ui`) | to be implemented | to be implemented | to be implemented | to be implemented |
| Core (`core`) | to be implemented | to be implemented | to be implemented | to be implemented |
| Services (`services`) | to be implemented | to be implemented | to be implemented | to be implemented |
| AI (`ai`) | to be implemented | to be implemented | to be implemented | to be implemented |
| Base (`base`) | to be implemented | to be implemented | to be implemented | to be implemented |

Base is demonstrated through its composition role: the example's dependency injection and wiring follow the Base pattern for that platform.

---

## 7. README

Each example repository README follows [`README-example.md`](../templates/README-example.md). It covers purpose, layers demonstrated (linked to section 6), how to run, a reference to the compatibility table, and the CI badge and licence placeholders.

---

## 8. CI and release recipes

An example uses the **app** templates. It does not use the library templates.

| Purpose | Template (copy to `.github/workflows/`) | Calls |
|---|---|---|
| CI | `ci-app-{platform}.yml.template` as `ci.yml` | `{platform}-ci.yml` at `@main` |
| Release | `release-app-{platform}.yml.template` as `release.yml` | `app-release.yml` at `@main` |

- **Release:** the tag filter is the strict bare-semver glob `'[0-9]+.[0-9]+.[0-9]+'`. `app-release.yml` validates the tag against `syzygy.yml`, extracts the CHANGELOG section, and creates the GitHub Release. It has **no publish step** and no CI-gate input.
- **CI gate:** examples adopt the opt-in `ci-gate.yml` through the commented `gate` job in the app release template, the same as libraries. The release workflows themselves check no CI. See [`.github/workflows/README.md`](../../.github/workflows/README.md).
- **Android:** `project_type: app` with `module: ':app'`. Required, because the library path is the default.
- **iOS:** `project_type: xcode` with the app's workspace or project and scheme.

---

## 9. Owner decisions outstanding

- Creation of the four repositories.
- The first example version and its `syzygy.yml` `version:` value.
- The licence holder (see [repository-standard.md](repository-standard.md)).
- Completion of each cell in section 6.
