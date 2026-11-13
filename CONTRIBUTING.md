# Contributing

Questions and proposals: **support@syncwin.com**.

- By submitting a contribution you confirm you wrote it or have the right to submit it, and you license it under the MIT License in `LICENSE`.
- Write your own text and code. Do not paste in third-party skills, documentation text or code; link to official sources instead and add a line to `CREDITS.md` if an outside project shaped the idea.
- The shipped plugin is text only: no hooks, scripts or non-text files under `adapters/claude`.
- Keep each `SKILL.md` under 500 lines; move detail into `references/`.
- Update the root `CHANGELOG.md`; bump `version` in `adapters/claude/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together (breaking = major, new capability = minor, wording = patch).
- Keep each recipe in `adapters/claude/skills/*/references/` in step with its maintainer script in `dev/`; test script changes with `python dev/fsdevops-plan/scripts/detect_project.py <app>`, `python dev/fsdevops-qa/scripts/qa_gate.py <app>` and a throwaway `scaffold_app.py` run.
- A new stack follows `adapters/claude/skills/fsdevops/references/stacks.md`.
- Run `claude plugin validate . --strict` before a pull request.
