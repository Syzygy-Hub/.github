<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Contributing to Syzygy

Thank you for contributing. Syzygy is a layered, cross-platform engineering framework that runs on iOS, Android, React Native and Flutter. Read this file before you open a pull request. The detailed rules are in [`engineering/standards/`](engineering/standards/).

## The layers

Each platform repo belongs to one layer. Keep changes inside the layer they belong to.

| Layer | Role | May depend on |
|---|---|---|
| Foundation | Contracts and primitives | nothing above it |
| Core | Business logic contracts, state | Foundation only |
| Services | Concrete implementations (networking, auth, storage) | Foundation only |
| AI | AI contracts (LLM, agents, embeddings, RAG, memory) | Foundation only |
| UI | Design system | Foundation only |
| Base | Composes all layers into a starter app | every layer |

No peer layer depends on another peer. Only Base composes the stack. A change that makes Core depend on Services, or AI depend on Services, is not accepted.

## Before you start

1. Check the layer's manifest (`syzygy.yml`) for the current version.
2. Read the standards: [repository](engineering/standards/repository-standard.md), [release](engineering/standards/release-standard.md), [changelog](engineering/standards/changelog-standard.md), [readme](engineering/standards/readme-standard.md).
3. For AI work, read the [AI contract specification](engineering/standards/ai-contract-spec.md). The shipped code is the source of truth.
4. Install the pre-push lint hook: `sh path/to/.github/engineering/hooks/setup-hooks.sh`.

## Branches and commits

- Branch from `main`. Use `feature/...`, `fix/...` or `chore/...`. Release work uses `release/X.X.X`.
- Commit messages are imperative and present tense, for example `Add SyzygyID generic typed identifier`. Use `fix:`, `chore:` or `docs:` prefixes where they apply.

## Pull requests

1. Open a pull request into `main`.
2. CI must pass on the pull request. The CI workflow is the same one the release gate checks.
3. Update `CHANGELOG.md` under `[Unreleased]`. Do not edit released sections.
4. Use the pull request template. Describe the change, the layer, and any API impact.
5. A reviewer approves, then the pull request is merged.

## Releases

Each platform releases independently. The process:

1. Create `release/X.X.X` from `main`.
2. Bump the version in every place the release standard lists, including `syzygy.yml`.
3. Move `[Unreleased]` into `[X.X.X] - YYYY-MM-DD` in `CHANGELOG.md`.
4. Open a pull request into `main`, get it reviewed, and make sure CI passes.
5. Merge to `main`.
6. Push the bare tag `X.X.X` (no `v` prefix). The tag must point at a commit that has already passed CI. The release workflow validates the version and creates the GitHub Release. Registry publishing is platform-specific. Flutter publishes to pub.dev inside `flutter-release.yml`. React Native publishes to npm from each caller's own `publish-npm` job, because npm OIDC trusted publishing needs the caller's workflow file. iOS (SPM) and Android (JitPack) publish nothing beyond the GitHub Release, since the tag is the artefact. Apps (`app-release.yml`) publish nothing.

Versioning follows SemVer. CI-only and tooling-only changes are patch releases. Additive API is a minor release. Breaking changes are a major release and must be deprecated first. See the [release standard](engineering/standards/release-standard.md).

## Lint and tooling

- Shared lint configs live in [`engineering/tooling/`](engineering/tooling/). Do not add platform-local lint rules that contradict them.
- Do not commit lock files that the [lockfile policy](engineering/standards/repository-standard.md#lockfile-policy) forbids.

## Working with Claude Code

Claude Code is welcome for drafting code, tests and documentation, as long as the contributor reviews every change. Keep these rules when you use it:

- Let it read the standards first. Point it at the relevant file under `engineering/standards/`.
- Do not paste credentials, tokens or customer data into a prompt, a test or a fixture.
- Run the tests and the pre-push hook yourself before you push. Claude Code's output is not a substitute for CI.
- Confirm that any `CHANGELOG.md` entry describes what the code does, not what the assistant claimed.

## Code of conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions

Open an issue using the feature request or bug report template, or contact the maintainer. TODO: maintainer contact (to be provided by the owner).
