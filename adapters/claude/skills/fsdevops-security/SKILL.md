---
name: fsdevops-security
description: Security role skill of Full-Stack DevOps, always applied to builds and loaded by review. Covers secrets (never in the app bundle or repo), secure token storage, personal-data privacy and local encryption, input validation, platform permissions, network security, deep-link safety, logging hygiene, and dependency health and licence checks. Use when the user asks any security, privacy or dependency-licence question about an app.
---

# FSDevOps Security Engineer

## Rules (every build)
1. **No secrets in the client or the repo.** Anything shipped in an app can be extracted. API keys that must stay secret live on the server; public config uses `--dart-define-from-file` with a git-ignored file and a committed `*.example`.
2. **Tokens** in `flutter_secure_storage` (Windows Credential Manager, Android Keystore, iOS Keychain). Web has no true secure storage: short-lived tokens, refresh via HTTP-only cookies when the backend allows.
3. **Personal data:** collect the minimum; encrypt local databases holding personal data (SQLCipher for drift) when the PRD says so; clear on sign-out.
4. **Input:** validate at the UI for UX and again at the boundary; never build SQL by string concatenation (drift queries are parameterised).
5. **Network:** HTTPS only; certificate pinning only for your own API and only with a rotation plan.
6. **Deep links:** validate parameters; never act (delete, pay, send) from a link without a confirm screen.
7. **Logs:** no tokens, passwords or personal data; release builds log errors only.
8. **Permissions:** request at the moment of use with a reason; declare only what is used.

## Secure by default (every project; this is the single source, other skills link here)
1. **Threat model** in every PRD and change brief: assets, entry points, who can attack, top 3 abuse cases and the control for each. Update it when scope changes.
2. **Secret scanning:** gitleaks as a pre-commit hook (the scaffold recipe writes `.pre-commit-config.yaml` and a secret-safe `.gitignore`) and as a CI job. Check every diff for `github_pat_`, `ghp_`, `sk-`, `Bearer `, `password=` before commit; a hit stops the work.
3. **Least privilege:** CI `permissions: contents: read` by default, per-job escalation only; scoped, short-lived tokens; release secrets only in the release job.
4. **Supply chain:** pin and audit (`references/dependencies.md`); no install scripts from unreviewed packages.
5. **Signed releases:** sign with the user's own keys, publish SHA-256 checksums, never from an unverified build (`fsdevops-release`).
6. **Gate:** any Critical or Important security finding from `fsdevops-review` blocks release until fixed or explicitly accepted in writing by the user.
7. **Plugin and tooling code:** never run a shell with untrusted input (file paths, names); pass argument lists, quote `${CLAUDE_PLUGIN_ROOT}`, validate names with an allow-list pattern. Guards that protect security fail closed; formatting steps fail open.

## Dependencies (`references/dependencies.md`)
Health, licence, pinning and audit before adding any package.

## Review lens
When `fsdevops-review` runs the security lens, report findings with a weakness name (for example CWE-798 hard-coded credentials) and confidence.

Finish with a scratchpad: secrets found or ruled out, storage, dependency checks.
