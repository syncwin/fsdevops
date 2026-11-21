# Credits

Full-Stack DevOps is one MIT-licensed package. Every skill, script and reference in it was written for this plugin. No third-party skill is forked, bundled or copied. The projects below shaped ideas or are linked as sources of truth; their licences are named for reference only and do not apply to this package.

| Project | What we learned from it | Licence (reference) |
|---|---|---|
| Flutter and Dart documentation (docs.flutter.dev, dart.dev) | Source of truth for architecture, platforms, standards and release. Linked from `skills/fsdevops/references/official-docs.md`, not copied | See each site |
| [flutter/agent-plugins](https://github.com/flutter/agent-plugins) | Which Flutter tasks an agent skill set should cover (architecture, routing, responsive layout, tests, localization, JSON) | BSD-3-Clause |
| [Dart and Flutter MCP server](https://docs.flutter.dev/ai/mcp-server) | Declared in `.mcp.json` and used for analyze, format and tests when present; not bundled | BSD-3-Clause |
| [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) | The minimal-code order of operations (the lean ladder in `skills/fsdevops/references/lean-coding.md`, rewritten in our own words) and reviewing for over-engineering | MIT |
| [Anthropic claude-plugins-official](https://github.com/anthropics/claude-plugins-official) (pr-review-toolkit) | The idea of confidence-scored review that reports only high-certainty findings | Apache-2.0 |
| [anthropics/skills](https://github.com/anthropics/skills) `frontend-design` | A short design plan before code (colour roles, typefaces with roles, a layout idea) and checking it against generic generated-app defaults (`fsdevops-design/references/design-direction.md`) | Apache-2.0 |
| [anthropics/skills](https://github.com/anthropics/skills) `webapp-testing` | Look before acting: capture screenshots, inspect, then act (the shoot, fix, re-shoot loop in `fsdevops-design/references/visual-qa.md`; Playwright kept for the web target only) | Apache-2.0 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | A design-system master file kept in the repo and anti-patterns chosen by product type (`DESIGN.md`, `anti-patterns.md`); its style database and search scripts were not adopted | MIT |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Lens scores 0 to 4 and narrow focused passes (bolder, quieter, typeset, layout, polish) (`fsdevops-critic/references/focused-passes.md`); its 40-point total and launcher binary were not adopted | Apache-2.0 |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) `baseline-ui` | Strict baseline rules: tabular figures, real confirm or undo, no tracking changes, short motion (`fsdevops-design/references/baseline-ui.md`) | MIT |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Accessibility checks mapped to Flutter: visible focus, roles for toggles, labelled fields, target spacing (`fsdevops/references/accessibility.md`) | MIT |
| Full-Stack WP DevOps (same author) | The lifecycle: router, architect, build, QA gate, independent reviewer, release | MIT |

Flutter and the related logo are trademarks of Google LLC. Claude and Anthropic are trademarks of Anthropic, PBC. This project is independent and not affiliated with or endorsed by either. See `docs/trademarks.md`.
