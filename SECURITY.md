<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Security Policy

## Supported versions

Security fixes are applied to the latest release of each Syzygy repository, on each platform (iOS, Android, React Native, Flutter). Older major versions are not patched unless the maintainer says otherwise in a release note.

| Layer | Supported |
|---|---|
| Foundation, UI, Core, Services, AI, Base | Latest release (3.0.0 line) |

## Reporting a vulnerability

Do not open a public issue, pull request or discussion for a security problem.

Report it privately by one of these routes:

- Use GitHub's private vulnerability reporting on the affected repository (Security tab, "Report a vulnerability"), if it is enabled there.
- Otherwise contact the maintainer directly. TODO: maintainer security contact address (to be provided by the owner).

Include:

- the repository and version (the tag, for example `3.0.0`) and the platform,
- the steps to reproduce, or a minimal sample,
- the impact as you understand it,
- whether you have shared the details anywhere else.

## What to expect

- Acknowledgement within 5 working days. TODO: confirm the response target with the owner.
- A severity assessment and a plan. Fixes ship as a patch release under the release standard, with a CHANGELOG entry that names the issue without exploit detail.
- Credit in the release notes if you want it.

## Scope notes for this ecosystem

- AI contracts (`syzygy-ai-*`) must not accept or store raw API keys. Credentials are supplied through a credential provider. A report that shows a key or token stored in a contract, a manifest or a template is in scope and high priority.
- Never include real credentials, tokens or personal data in a report or in a test fixture.
- The reusable CI workflows in this repo run with the permissions the callers grant. A report about excessive workflow permissions or unpinned third-party actions is in scope.
