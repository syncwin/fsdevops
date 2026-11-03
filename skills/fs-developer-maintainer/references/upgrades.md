# Upgrades

1. Branch. Baseline gate.
2. Read the official migration notes for every major version crossed (Flutter breaking changes page, package CHANGELOGs). Link them in the brief.
3. `flutter upgrade` (SDK) or `flutter pub outdated`, then `flutter pub upgrade --major-versions <package>` one package (or one tightly coupled group) at a time.
4. `dart fix --dry-run`, then `dart fix --apply`; review the diff.
5. Gate after each step; commit per step so a bad step reverts alone.
6. Platform folders: compare with a fresh `flutter create` of the same version (`windows/runner`, Gradle files) and port only needed changes.
7. Generated code: `dart run build_runner build --delete-conflicting-outputs`.
8. Builder-owned packages: confirm the builder supports the new SDK before upgrading them; otherwise pin and note it.
