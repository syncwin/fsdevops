# Stacks

## Detection order
1. `pubspec.yaml` containing a `flutter:` dependency → **Flutter**. A root `pubspec.yaml` with `workspace:` is a pub workspace; detect per package.
2. `pubspec.yaml` without Flutter → **Dart** package or CLI: use `fsdevops-flutter` rules that are not UI-specific.
3. `package.json` (React, Next.js, Node), `go.mod`, `Cargo.toml`, `pyproject.toml` → **not supported yet**. Say so, offer an architecture plan only, never guess the stack's standards.
4. Empty folder → ask which stack only if the user did not say; default to Flutter for "app", "desktop app", "mobile app".

## Supported
| Stack | Build skill | Gate | Release |
|---|---|---|---|
| Flutter (Windows, Android, iOS, web, macOS, Linux) | `fsdevops-flutter` | `fsdevops-qa` → Flutter gate | `fsdevops-release` → Flutter targets |

## Adding a stack (maintainers)
Add `skills/fsdevops-<stack>/` with its references, a gate section in `fsdevops-qa` (and `qa_gate.py`), a target section in `fsdevops-release`, links in `official-docs.md`, a row above, and evals. Shared skills (architect, maintainer, reviewer, security, performance, devops) gain only a short per-stack reference, never a rewrite.
