# Platforms (desktop first)

## Order
Windows desktop → Android → iOS → web (unless the PRD says otherwise). Scaffold every target at the start (`flutter create --platforms=windows,android,ios,web .`) so platform folders exist, but verify only the current target; later targets are NOT RUN until their turn.

## Windows desktop
- Toolchain: Visual Studio with "Desktop development with C++" (`Microsoft.VisualStudio.Workload.NativeDesktop`), then `flutter doctor -v` and `flutter devices` must list `windows` (official setup page).
- Run `flutter run -d windows`; build `flutter build windows --release` (output under `build/windows/x64/runner/Release/`).
- Desktop UX: keyboard shortcuts (`Shortcuts`/`Actions`), hover states, right-click menus (`MenuAnchor`), resizable layouts down to a minimum width, scroll bars visible, text selectable where useful.
- Window title, size and minimum size: set in `windows/runner/main.cpp` and `win32_window.cpp`; add a window-management package only when runtime control is required (user's OK).
- System tray, auto-start and file associations: only when the PRD asks; each needs a package or native code and the user's OK.
- Packaging and release: `fsdevops-release`.

## Release-only differences (check before every release build)
Debug builds hide some platform settings; a feature that works in `flutter run` can fail in a release build. Source: docs.flutter.dev deployment and platform setup pages.
| Target | Check | Where |
|---|---|---|
| Android | `android.permission.INTERNET` (and every other permission the app uses) is in the main manifest; `flutter create` puts INTERNET only in the debug and profile manifests | `android/app/src/main/AndroidManifest.xml` |
| Android | release signing config set from env or CI secrets, not the debug key; minify or shrink rules keep reflected classes | `android/app/build.gradle(.kts)` |
| iOS | a usage description string for every protected API used (camera, photos, location, microphone and others) | `ios/Runner/Info.plist` |
| macOS | network client (and any other) entitlement in both Debug and Release entitlement files; the sandbox blocks network calls otherwise | `macos/Runner/*.entitlements` |
| Windows | when packaging as MSIX, declare the capabilities the app uses (for example internetClient) | packaging config |
| Web | API hosts allow the app origin (CORS); `--base-href` matches the hosting path | server config, build command |

- Prefer a physical phone over USB or wireless debugging on low-end PCs; the emulator needs a capable GPU.
- Flavors for store builds versus FOSS builds when the PRD needs both (`fsdevops-ci`).

## iOS
- Needs a Mac or a cloud macOS build service; on Windows mark iOS builds NOT RUN and name the service the user chose.

## Web
- `flutter build web --wasm --release` (skwasm with CanvasKit fallback). Expect a multi-MB first load and no real SEO; keep marketing pages separate.
