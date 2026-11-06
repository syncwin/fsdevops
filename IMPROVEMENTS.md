# Improvements

Log feedback and ideas here; move to Accepted when approved.

## Inbox
Format: date · idea · source

- 2026-11-04 · Add stacks for Web and Chrome extension (Mobile/Desktop already via Flutter) instead of separate plugins · user plan
- 2026-11-04 · Add ponytail's "need it? reuse? platform? dependency? one line? minimal" ladder to `references/lean-coding.md`; lite/full/ultra strictness setting; SessionStart hook that injects lean rules + model routing · github.com/DietrichGebert/ponytail (MIT)
- 2026-11-04 · Deterministic review: file list from git diff, bundle related files, one narrow check per lens, model only for judgement · Better Stack Short on "Open Code Review"
- 2026-11-04 · Use Anthropic security-guidance, pr-review-toolkit, code-simplifier, code-review and OWASP code-security-skills when installed (optional, fallback to own skills); trigger deep OWASP audit only for auth, payments, secrets, user input, new deps. Names/features unverified · personal notes
- 2026-11-04 · AGENTS.md model routing (Opus plans, Haiku/Sonnet execute) as a shipped default · all plugins (Claude plugins note)
- 2026-11-06 · Warm worktrees: copy git-ignored build caches (node_modules, .dart_tool, build) into new agent worktrees with copy-on-write clones (Worktrunk `wt step copy-ignored`). Windows needs a Dev Drive (ReFS block cloning). Test on lifeos-app first; then add a warm-worktree step · YouTube Short e03gppjLojw

## Accepted
- 2026-11-05 · AI+ contract adoption: when the plugin gets a contract.yaml, add evidence signals changelog_unreleased_updated, feature_docs_updated, feature_index_current, docs_gate_exit_code (rows of docs_gate.py) · User (docs standard)

## Done
- 2026-11-05 · Security first (enterprise level): secure-by-default baseline, threat model in each brief, secret scanning, supply-chain pinning/audit, signed releases, security findings block release · done in 0.3.2 (PR sec/baseline) · User
- 2026-11-05 · Documentation standard enforced (README + docs/, Keep a Changelog 0.0.1 start, docs/features/ index and template, docs_gate.py in the QA gate); 0.0.1 start and beta-until-1.0 rule · done in 0.3.3 (PR feat/docs-standard) · User
