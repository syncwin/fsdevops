# Platforms (desktop first)

## Order
Windows desktop → Android → iOS → web (unless the PRD says otherwise). Scaffold every target at the start (`flutter create --platforms=windows,android,ios,web .`) so platform folders exist, but verify only the current target; later targets are NOT RUN until their turn.

## Windows desktop
- Toolchain: Visual Studio with "Desktop development with C++" (`Microsoft.VisualStudio.Workload.NativeDesktop`), then `flutter doctor -v` and `flutter devices` must list `windows` (official setup page).
- Run `flutter run -d windows`; build `flutter build windows --release` (output under `build/windows/x64/runner/Release/`).
- Desktop UX: keyboard shortcuts (`Shortcuts`/`Actions`), hover states, right-click menus (`MenuAnchor`), resizable layouts down to a minimum width, scroll bars visible, text selectable where useful.
- Window title, size and minimum size: set in `windows/runner/main.cpp` and `win32_window.cpp`; add a window-management package only when runtime control is required (user's OK).
- System tray, auto-start and file associations: only when the PRD asks; each needs a package or native code and the user's OK.
- Packaging and release: `fs-release-manager`.

## Android
- Prefer a physical phone over USB or wireless debugging on low-end PCs; the emulator needs a capable GPU.
- Flavors for store builds versus FOSS builds when the PRD needs both (`fs-devops-engineer`).

## iOS
- Needs a Mac or a cloud macOS build service; on Windows mark iOS builds NOT RUN and name the service the user chose.

## Web
- `flutter build web --wasm --release` (skwasm with CanvasKit fallback). Expect a multi-MB first load and no real SEO; keep marketing pages separate.
