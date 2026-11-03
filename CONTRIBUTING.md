# Contributing

Questions and proposals: **support@syncwin.com**.

- By submitting a contribution you confirm you wrote it or have the right to submit it, and you license it under the MIT License in `LICENSE`.
- Write your own text and code. Do not paste in third-party skills, documentation text or code; link to official sources instead and add a line to `CREDITS.md` if an outside project shaped the idea.
- Keep each `SKILL.md` under 500 lines; move detail into `references/`.
- Update the root `CHANGELOG.md`; bump `version` in `.claude-plugin/plugin.json` and every skill's `metadata.version` together (breaking = major, new capability = minor, wording = patch).
- Test script changes: `python skills/fs-architect/scripts/detect_project.py <app>`, `python skills/fs-qa-engineer/scripts/qa_gate.py <app>`, and a throwaway `scaffold_app.py` run.
- A new stack follows `skills/fs-developer/references/stacks.md`.
- Run `claude plugin validate . --strict` before a pull request.
