#!/bin/sh
# ─────────────────────────────────────────────────────────────────────
# Syzygy hook installer
# ─────────────────────────────────────────────────────────────────────
# Run this once inside any Syzygy repo to install the shared pre-push
# lint hook.  Safe to re-run (idempotent).
#
# Usage:
#   cd /path/to/syzygy-ui-ios     # any cloned Syzygy repo
#   sh /path/to/.github/engineering/hooks/setup-hooks.sh
#
# The script auto-locates the .github repo by resolving its own path
# (it lives at <.github>/engineering/hooks/setup-hooks.sh) and by
# walking up the filesystem looking for the standard Syzygy layout.
# ─────────────────────────────────────────────────────────────────────

set -e

# ── Helpers ──────────────────────────────────────────────────────────
red()   { printf '\033[1;31m%s\033[0m\n' "$1"; }
green() { printf '\033[1;32m%s\033[0m\n' "$1"; }
dim()   { printf '\033[2m%s\033[0m\n' "$1"; }

die() {
  red "✗ setup-hooks: $1"
  exit 1
}

# ── Verify we're inside a git repo ──────────────────────────────────
if [ ! -d ".git" ]; then
  die "Not a git repository root. Run this from the top level of a Syzygy repo."
fi

REPO_ROOT="$(pwd)"

# ── Locate the .github repo ─────────────────────────────────────────
# Strategy 1: resolve from this script's own location.
#   setup-hooks.sh lives at <.github>/engineering/hooks/setup-hooks.sh
#   so the pre-push file is a sibling in the same directory.
SCRIPT_DIR=""
if [ -n "$0" ] && [ "$0" != "sh" ] && [ "$0" != "-sh" ]; then
  _script="$0"
  # Follow symlinks if readlink is available.
  if command -v readlink >/dev/null 2>&1; then
    _resolved=$(readlink -f "$_script" 2>/dev/null || readlink "$_script" 2>/dev/null || echo "$_script")
    if [ -n "$_resolved" ]; then
      _script="$_resolved"
    fi
  fi
  case "$_script" in
    /*) SCRIPT_DIR=$(dirname "$_script") ;;
    *)  SCRIPT_DIR=$(dirname "$(pwd)/$_script") ;;
  esac
fi

HOOK_SOURCE=""

if [ -n "$SCRIPT_DIR" ] && [ -f "${SCRIPT_DIR}/pre-push" ]; then
  HOOK_SOURCE="${SCRIPT_DIR}/pre-push"
fi

# Strategy 2: walk up the filesystem looking for the standard Syzygy
# folder layout.  The .github repo is typically nested under Org/src/.
if [ -z "$HOOK_SOURCE" ]; then
  _search="$REPO_ROOT"
  _max_depth=6
  _depth=0
  while [ "$_depth" -lt "$_max_depth" ]; do
    _parent=$(dirname "$_search")
    for _candidate in \
      "${_parent}/.github/engineering/hooks/pre-push" \
      "${_parent}/Org/src/.github/engineering/hooks/pre-push"; do
      if [ -f "$_candidate" ]; then
        HOOK_SOURCE="$_candidate"
        break 2
      fi
    done
    _search="$_parent"
    _depth=$((_depth + 1))
  done
fi

if [ -z "$HOOK_SOURCE" ]; then
  die "Could not find .github/engineering/hooks/pre-push.
  Make sure the Syzygy .github repo is cloned in the standard layout,
  or create the symlink manually:
    ln -sf /absolute/path/to/.github/engineering/hooks/pre-push .git/hooks/pre-push"
fi

# Resolve to absolute path for a stable symlink.
HOOK_SOURCE=$(cd "$(dirname "$HOOK_SOURCE")" && pwd)/$(basename "$HOOK_SOURCE")

dim "Found hook source: ${HOOK_SOURCE}"

# ── Install the symlink ─────────────────────────────────────────────
HOOKS_DIR="${REPO_ROOT}/.git/hooks"
TARGET="${HOOKS_DIR}/pre-push"

# Create hooks dir if absent (bare clone edge case).
mkdir -p "$HOOKS_DIR"

# Idempotency: if the symlink already points to the right place, done.
if [ -L "$TARGET" ]; then
  _existing=$(readlink "$TARGET" 2>/dev/null || true)
  if [ "$_existing" = "$HOOK_SOURCE" ]; then
    green "✓ pre-push hook already installed (${TARGET} → ${HOOK_SOURCE})"
    exit 0
  fi
  dim "Replacing existing pre-push symlink (was: ${_existing})"
fi

# If there's an existing non-symlink pre-push, back it up.
if [ -f "$TARGET" ] && [ ! -L "$TARGET" ]; then
  _backup="${TARGET}.backup.$(date +%Y%m%d%H%M%S)"
  cp "$TARGET" "$_backup"
  dim "Backed up existing pre-push hook to ${_backup}"
fi

# Ensure the hook source is executable.
chmod +x "$HOOK_SOURCE"

# Create (or replace) the symlink.
ln -sf "$HOOK_SOURCE" "$TARGET"

# ── Confirm ──────────────────────────────────────────────────────────
if [ -L "$TARGET" ]; then
  green "✓ pre-push hook installed: ${TARGET} → ${HOOK_SOURCE}"
else
  die "Failed to create symlink at ${TARGET}"
fi
