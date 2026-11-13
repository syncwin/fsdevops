# Security policy

## Reporting a vulnerability in this plugin

The package is text only: instructions and recipes that tell Claude which commands to run (project detection, scaffold, QA and docs gates, Dart formatting). The matching Python tools in `dev/` are maintainer tooling and are not shipped. If you find a flaw in a recipe, or guidance that would steer generated code toward an insecure pattern, email **support@syncwin.com** with the subject "Security". Include the file, what you saw, and how to reproduce it. Please do not open a public issue first. Expect an acknowledgement, then a fix and a CHANGELOG entry.

## Vulnerabilities in Flutter or Dart

Report them through the Flutter and Dart projects' own security processes, not here.

## What this plugin does not guarantee

The plugin plans, builds, verifies and reviews app code with an AI model. Its gate and review reduce risk; they do not prove code is secure, correct or fit for your use. Read generated code before shipping, test on real devices, keep backups, and get a professional security review for anything handling payments, personal data or authentication. A check that could not run is reported NOT RUN, never as a pass.
