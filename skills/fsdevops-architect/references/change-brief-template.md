# Change brief: <title>

- **Why:** the problem or request, with evidence (error, issue, screenshot).
- **Files to change:** exact paths. Anything else is scope creep.
- **Parity list:** behaviour that must stay the same.
- **Risks:** migrations, data loss, builder-owned or generated paths, platform differences.
- **Tests:** new or changed tests that prove the fix.
- **Rollback:** how to undo (revert commit, migration down step).
- **Domains touched:**
- **Done when:** gate green, scenarios pass, reviewer clean.
