<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="600">
</picture>

# Ecosystem feed

`ecosystem/feed.json` is a machine-readable inventory of the Syzygy ecosystem. It has one entry for each of the 24 platform repositories (6 layers x 4 platforms) and one entry for the Hub. A website can consume it directly.

- **Schema:** `engineering/schema/ecosystem-feed.schema.json` (JSON Schema draft 2020-12). The `schema` key in the feed is `syzygy-ecosystem-feed/1`.
- **Repo list:** `ecosystem/repos.json` maps each layer and platform to its GitHub repository and local checkout path.
- **Source data:** only each repo's `syzygy.yml` and the repo list. Nothing else is inferred.

## Fields

Each repo object has the same keys: `name`, `type`, `version`, `status`, `language`, `package_manager`, `syzygy_foundation`, `dependency_constraints`, `license`, `repo_url`, `ci_workflow` and `release_workflow`. Missing values are `null`.

- `version` is the manifest version, bare strict semver. It is `null` when the manifest has no version.
- `status` is `shipped` when `version` is semver, and `unknown` otherwise. The Hub has no manifest, so its status is `unknown`.
- `syzygy_foundation` is the foundation constraint. It is read from `syzygy_foundation`, from the legacy `foundation` key, or from a `dependencies` entry.
- `dependency_constraints` maps other layers to constraints, for example `{"core": "3.0.0"}`. It is empty for repos that declare none.
- `ci_workflow` and `release_workflow` are always `null` in version 1. Manifests do not declare them.
- `language`, `package_manager` and `license` are `null` when the manifest omits them. Several AI and Base manifests omit them.

The feed is deterministic. It has no timestamps, and keys and lists are in a fixed order. Regenerating from the same manifests gives byte-identical output.

## Scripts

Both scripts use only the Python standard library. They reuse the subset YAML reader in `engineering/tooling/validate-syzygy/validate.py`.

**`generate_feed.py`** builds the feed and prints it, or writes it with `--output`.

```bash
# Public raw URLs (default)
python3 engineering/tooling/ecosystem-feed/generate_feed.py

# Local checkouts
python3 engineering/tooling/ecosystem-feed/generate_feed.py --source local --local-root /path/to/Syzygy
```

**`check_drift.py`** is the drift check. It regenerates the feed in memory and checks four things:

1. The feed validates against the schema.
2. The committed `ecosystem/feed.json` equals the regenerated text.
3. The marker block in each file listed in `DOC_FILES` equals the table rendered from the feed. The files are `profile/README.md` and `engineering/architecture/syzygy-ecosystem.md`.
4. The files contain exactly one `<!-- ECOSYSTEM:START -->` and one `<!-- ECOSYSTEM:END -->` pair.

```bash
# Check, raw URLs (what CI runs)
python3 engineering/tooling/ecosystem-feed/check_drift.py

# Check, local checkouts
python3 engineering/tooling/ecosystem-feed/check_drift.py --source local --local-root /path/to/Syzygy

# Regenerate the feed and marker blocks (local use only), then review and commit
python3 engineering/tooling/ecosystem-feed/check_drift.py --source local --local-root /path/to/Syzygy --write
```

Exit codes: `0` in sync or written, `1` drift found, `2` the feed could not be built (a manifest is missing, unreadable, unparseable or conflicts with the repo list), or the marker pairs are missing.

## Limits

- **Schema validation is a subset.** The stdlib validator supports `type`, `enum`, `const`, `pattern`, `required`, `properties`, `additionalProperties`, `propertyNames`, `items`, `minItems` and local `$ref`. It does not check conditional keywords, so the status and version rule is covered by the regeneration compare instead.
- **Raw mode needs public repos.** `--source raw` reads `https://raw.githubusercontent.com/Syzygy-Hub/<repo>/<ref>/syzygy.yml` with no token. A private repo returns HTTP 404, and the check fails. A token would then be needed, and the workflow does not have one.
- **Raw mode reads `ref` (`main`).** Local mode reads the working tree, which may contain unpushed changes. The two modes can disagree.
- **The YAML reader is a subset.** It covers the manifest forms used in the org. Anchors, multi-line scalars and flow mappings are not supported.
