# Recipe: mechanical QA gate (Flutter and Dart)

Do these steps with Bash and the Dart MCP server (`analyze_files`, `pub`, tests) when connected. Run at the workspace root (the folder with the root `pubspec.yaml`). Report a table: `Step | Result | Detail`, with the Flutter version line on top. Every step is PASS, FAIL or NOT RUN; NOT RUN is never a pass.

## Inputs
- `<dir>`: the project folder. Stop with "No pubspec.yaml in <dir>" when it has none.
- `target`: `windows`, `apk`, `appbundle`, `web`, `ios` or `none`. Default `windows` on Windows, otherwise `none`.
- `fix` (optional): before the steps run `dart format .` then `dart fix --apply`, and review the diff.

## Steps
Each command runs in `<dir>` with a 30 minute limit, as an argument list (no shell strings with untrusted input). Keep the last 15 output lines.

0. `flutter` not on PATH: mark `pub get`, `format`, `fix`, `analyze`, `test`, `codegen`, `build <target>` all NOT RUN ("Flutter SDK not on PATH"), still run the `docs` step (see `docs_gate.md`), and stop. Otherwise note `flutter --version` (first line).
1. `pub get`: `flutter pub get`. PASS when exit 0.
2. `format`: `dart format --output=none --set-exit-if-changed .`. PASS when exit 0.
3. `fix (dry run)`: `dart fix --dry-run`. FAIL when exit is not 0, or when the output has a "proposed fixes" line whose count does not start with `0`.
4. `analyze`: `flutter analyze --fatal-infos`. PASS when exit 0.
5. `test`: look for `*_test.dart` files (ignore `.dart_tool`). None: FAIL ("no *_test.dart files"). Otherwise `flutter test`; PASS when exit 0.
6. `codegen`: if the root `pubspec.yaml` or any workspace `pubspec.yaml` (ignore `.dart_tool`) mentions `build_runner`, run `dart run build_runner build --delete-conflicting-outputs`; PASS when exit 0. Otherwise PASS with "not used".
7. `docs`: follow `docs_gate.md` (same folder). Its FAIL lines make this step FAIL (show up to 3). All static checks pass but the diff checks are NOT RUN: report NOT RUN with "(static checks passed)".
8. `build <target>`:
   - `none`: NOT RUN ("--target none").
   - `ios` not on macOS: NOT RUN ("needs macOS or a cloud macOS build").
   - `windows` not on Windows: NOT RUN ("needs Windows").
   - Otherwise find the app folder: the first `pubspec.yaml` (sorted, ignoring `.dart_tool`) whose folder has `lib/main.dart`; else the root. There run `flutter build <target> --release` (add `--wasm` for `web`). PASS when exit 0; FAIL shows the last 5 lines.

Overall: FAIL if any step FAILs. A failed run is reported as is; never fix while gating (fixes happen in the router's fix loop). Prefer the Dart MCP tools when connected, with the same reporting rules.
