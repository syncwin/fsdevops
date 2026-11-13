# Recipe: detect the project

Use Glob, Read and Grep (or Bash) in the project folder `<dir>` (default: the current folder). Stop with "Not a folder" if it is not one. Ignore these folders everywhere: `.git`, `.dart_tool`, `build`, `node_modules`, `.fvm`, `Pods`. Report the facts below as a short list.

1. **Stack.**
   - Any `pubspec.yaml` found: `flutter` if any of them has `dependencies:` with `flutter:` and `sdk: flutter`, else `dart`.
   - No pubspec but a `package.json`: "node (not supported yet)".
   - Folder has files but none of the above: `unknown`. Empty folder: `empty`.
2. **Packages:** for every `pubspec.yaml`: relative folder (`.` for the root), `name:`, whether it is a Flutter package, its Dart `sdk:` constraint.
3. **Workspace:** true when the root `pubspec.yaml` has a top-level `workspace:` key.
4. **Targets:** for each package folder, which of `windows`, `android`, `ios`, `web`, `macos`, `linux` exist as subfolders, listed per target.
5. **Libraries:** collect the dependency names (two-space-indented `name:` keys) from all pubspecs, then list the ones present in each group:
   - state: flutter_riverpod, riverpod, hooks_riverpod, flutter_bloc, provider, get, signals, mobx
   - routing: go_router, auto_route, beamer
   - models: freezed, json_serializable, built_value
   - database: drift, sqflite, isar, hive, objectbox, shared_preferences
   - http: dio, http, chopper, retrofit
   - codegen: build_runner, riverpod_generator
   - lints: flutter_lints, very_good_analysis, lints
6. **Builder:** a `.nowa` file or folder anywhere means a visual builder (Nowa): follow the ownership rules (`fsdevops/references/ownership.md`).
7. **Ownership file:** whether `.claude/ownership.md` exists.
8. **Tests:** the number of `*_test.dart` files.

Never invent a fact that these checks did not show.
