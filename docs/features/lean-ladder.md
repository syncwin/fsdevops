# Lean ladder

Status: shipped in 0.4.0.

## Context
Over-building is the commonest waste in agent-written code. The plugin needed one shared rule for planning, building and reviewing.

## Behaviour
- Read the touched code and list every touch point before planning.
- Climb six rungs and stop at the first that works: skip it, reuse, Dart/Flutter built-in, installed dependency, one line, minimum code.
- Never cut: trust-boundary validation, data-loss handling, security, accessibility.
- Shortcuts are recorded as `// shortcut: <limit>, upgrade when <condition>`.
- Modes: review, audit, debt.

## How it works
Single source: `skills/fsdevops/references/lean-coding.md`. Used by `fsdevops-plan` (touch points), `fsdevops-flutter-build` and `fsdevops-maintain` (apply), `fsdevops-review` (lean and debt lenses).

## Limits
Guidance for the model; no script enforces it.

## History
- 0.4.0: merged into the existing lean-coding reference.

Method adapted from [Ponytail](https://github.com/dietrichgebert/ponytail) by Dietrich Gebert (MIT); text is original.
