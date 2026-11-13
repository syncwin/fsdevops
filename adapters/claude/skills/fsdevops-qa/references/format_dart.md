# Recipe: format Dart files after every edit

This is a manual step, not automation. Do it yourself: it is a required step in the build skills (`fsdevops-flutter-build`, `fsdevops-maintain`) after each batch of edits, and in `fsdevops-qa` before the gate.

## Steps
1. List the `.dart` files you created or changed in this step. Skip generated files (`*.g.dart`, `*.freezed.dart`) and files that no longer exist.
2. Skip any path that contains a Windows cmd metacharacter (`& | < > ^ % "`). Say so in the report; never run a shell with untrusted paths.
3. Find Dart. Try `dart` on PATH. On Windows `dart` is often a `.bat` shim: do not run a `.bat` or `.cmd` with a path argument. Use the real `dart.exe` instead, looked up in this order: `dart.exe` next to the shim, `<flutter>\bin\cache\dart-sdk\bin\dart.exe` (from `flutter` on PATH), `%DART_SDK%\bin\dart.exe`, `%FLUTTER_ROOT%\bin\cache\dart-sdk\bin\dart.exe`. If the Dart MCP server is connected, its `dart_format` tool does the same job.
4. Run, with the paths as separate arguments and no shell string building:
   ```
   dart format -- <file1.dart> <file2.dart> ...
   ```
   Or `dart format .` at the package root when many files changed.
5. No Dart installed: report `format: NOT RUN (Dart not found)`. Never write "formatted" without having run it. Formatting problems never block the edit itself; the QA gate's format step (`dart format --output=none --set-exit-if-changed .`) is the check.
