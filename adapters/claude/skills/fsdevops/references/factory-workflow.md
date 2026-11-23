# Factory workflow

Use when an agent builds the change and automated gates decide. Start small: one agent, small well-described issues. Never run it without review.

1. **Issue first.** Every change starts as a written issue: the problem plus acceptance criteria (how we know it is fixed). No issue, no work.
2. **Tests first.** Write or name the tests that prove each criterion before any code. The merge gate only knows what the tests know, so a criterion with no test is not covered.
3. **Own worktree and branch.** The building agent works in its own worktree and branch, then opens a PR that links the issue.
4. **CI loop.** CI runs the tests. On failure the result goes back to the agent to fix. Set a limit (for example 3 tries); after that, stop and report what failed.
5. **Merge gate.** All three must be true: tests passed, review approved, scope matches the issue. Only then merge.
6. **Human review on every PR.** Whoever requested the change is not the one who approves it.
7. **Holdout scenarios (larger work, optional).** Acceptance tests the building agent never sees, run by the reviewer after the build.
8. **Do not** use a no-review setup, widen scope mid-PR, or let the building agent edit the tests to make them pass.
