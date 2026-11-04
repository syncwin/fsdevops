# Improvements

Log feedback and ideas here; move to Accepted when approved.

## Inbox
Format: date · idea · source

- 2026-11-04 · Add stacks for Web and Chrome extension (Mobile/Desktop already via Flutter) instead of separate plugins · user plan
- 2026-11-04 · Add ponytail's "need it? reuse? platform? dependency? one line? minimal" ladder to `references/lean-coding.md`; lite/full/ultra strictness setting; SessionStart hook that injects lean rules + model routing · github.com/DietrichGebert/ponytail (MIT)
- 2026-11-04 · Deterministic review: file list from git diff, bundle related files, one narrow check per lens, model only for judgement · Better Stack Short on "Open Code Review"
- 2026-11-04 · Use Anthropic security-guidance, pr-review-toolkit, code-simplifier, code-review and OWASP code-security-skills when installed (optional, fallback to own skills); trigger deep OWASP audit only for auth, payments, secrets, user input, new deps. Names/features unverified · A:\Downloads\Claude Plugins.md
- 2026-11-04 · AGENTS.md model routing (Opus plans, Haiku/Sonnet execute) as a shipped default · all plugins (Claude plugins note)
- 2026-11-04 · (web stack + LifeOS) Patterns from a Cloudflare Pages+Functions+D1 dashboard, patterns only. Auth: owner key in custom header + share key in URL path, owner magic link in hash then stripped; SHA-256 + constant-time compare, reject secrets <32 chars (fail closed); invalid share key returns 404. Handler skeleton: auth, write guard (same-origin, custom header, JSON type, body cap), validate, single DB module; one json() error helper `{error}` with no-store/noindex; idempotent writes via client UUID + ON CONFLICT DO NOTHING. D1: numbered additive-only migrations, insert-only event log with latest-row state, read via narrow views, static SQL allowlist, redact free text. Frontend: zero-build shell, blocking theme script (no flash), oklch tokens. Strict CSP (default-src 'none'), no-referrer, HTML no-cache + ?v= assets. Tests as policy linter (SQL allowlist, additive migrations, CSS rules, WCAG contrast pairs) + zero-dep preview server with fail/empty modes. Fix in our version: add rate limiting/lockout, key rotation/expiry, per-user share keys for audit, no keys in localStorage (prefer HttpOnly session), split monolith JS, self-host fonts, one shared view allowlist · reviewed dashboard pattern

## Accepted

## Done
