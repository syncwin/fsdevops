# Recipe: documentation gate (Flutter and Dart)

Standard: `fsdevops/references/coding-standards.md` ("Documentation standard"). Use Read, Glob, Grep and `git` through Bash. Report `Check | Result | Detail` with PASS, FAIL or NOT RUN. Any FAIL fails the gate. NOT RUN (no git, no base branch) is never a pass.

## Static checks (always)
1. **Files exist:** `README.md`, `docs/setup.md`, `docs/architecture.md`, `docs/ops.md`. Missing = FAIL.
2. **CHANGELOG.md format (Keep a Changelog 1.1.0):** FAIL when the file is missing, has no `## [Unreleased]` heading, has a version heading that is not exactly `## [X.Y.Z] - YYYY-MM-DD` (SemVer, optional `-pre`/`+build`, optional ` [YANKED]` suffix), or a `### ` heading outside Added, Changed, Deprecated, Removed, Fixed, Security.
3. **`docs/features/README.md` index current:** the table header must be `| Feature | Status | Since | File |`. Every `docs/features/*.md` (except README.md) must have a row, and every row must name an existing file. The index must be ASCII only.
4. **Each `docs/features/*.md` valid:** ASCII only; a line `**Status:** <planned|beta|stable|deprecated> | **Since:** X.Y.Z | **Updated:** X.Y.Z`; sections `## Context`, `## Behaviour`, `## How it works`, `## UI`, `## Limits & known issues`, `## History`; Status and Since equal the index row; the Updated version appears under History; no `FILL IN:` left on a feature that is not `planned`.

## Diff checks (skip with "static only": report NOT RUN "--static")
1. Not a git repo: NOT RUN ("not a git repository").
2. Base: the given ref, else the first that exists of `origin/main`, `origin/master`, `main`, `master`; compare against `git merge-base <ref> HEAD`. None found: NOT RUN ("no base branch found").
3. Changed files = `git diff --name-only --relative <merge-base>` plus `git ls-files --others --exclude-standard`. Code = a `.dart` file under a `lib/` or `src/` folder, not `*.g.dart`, `*.freezed.dart`, `*.gr.dart`, not under `test/` or `docs/`. No code changed: PASS ("no changelog or feature entry needed") and stop.
4. **CHANGELOG [Unreleased] updated:** FAIL when there is no `[Unreleased]` section, or no new non-heading line under it compared with the base. PASS also when a release moved a non-empty Unreleased body into a new version heading.
5. **Feature docs for touched features:** map each changed code file to a feature slug: the first folder after `lib/` (skipping `src/` and `features/`), lower-case, `_` to `-`, needs a file below it; for `packages/<name>/...` use the package suffix matching an existing feature file, else drop the first `_` segment; ignore `*_core`, `*_ui` and generic names (core, shared, common, utils, util, l10n, generated, data, domain, presentation, ui, widgets, theme, models, services, helpers, lib, assets, admin, public). For each slug, `docs/features/<slug>.md` must exist and be among the changed files, else FAIL (missing or unchanged). Waiver: a new `### Changed` line or a new line containing `docs: none` under `[Unreleased]` passes this check for refactors. No feature-scoped code: PASS (shared code needs the changelog only).
6. **Index updated:** a feature file new against the base and `docs/features/README.md` unchanged = FAIL.
