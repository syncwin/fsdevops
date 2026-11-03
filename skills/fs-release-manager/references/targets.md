# Targets

## Windows (first)
- Build: `flutter build windows --release` → `build/windows/x64/runner/Release/` (exe + DLLs + `data/`). Ship the whole folder.
- Simple distribution: zip the Release folder (portable) or an installer built with a tool the user picks (for example Inno Setup).
- MSIX / Microsoft Store: follow the official "Build and release a Windows app" page (`official-docs.md`); the common route is the `msix` package (`dart run msix:create`) configured in `pubspec.yaml` (`msix_config`), signed with the user's certificate. Ask before adding the package.
- Unsigned builds trigger SmartScreen warnings; tell the user.

## Android
- `flutter build appbundle --release` for Play; `flutter build apk --release` for direct installs and F-Droid.
- Signing: `key.properties` (git-ignored) pointing at the user's keystore; `android/app/build.gradle(.kts)` reads it.
- Play internal testing track first. F-Droid: FOSS flavor without proprietary SDKs, reproducible build from a public repo.

## iOS
- Needs macOS: `flutter build ipa`, upload to TestFlight. On Windows use a cloud macOS service the user picks; mark local iOS steps NOT RUN.

## Web
- `flutter build web --wasm --release` → `build/web/`; deploy as static files (for example Cloudflare Pages). Set the base href if not served at `/`.
