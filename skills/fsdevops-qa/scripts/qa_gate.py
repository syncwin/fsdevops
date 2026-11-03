#!/usr/bin/env python3
"""Mechanical QA gate for Flutter/Dart projects. Standard library only.

Usage: python qa_gate.py <dir> [--target windows|apk|appbundle|web|ios|none] [--fix]
Prints a PASS / FAIL / NOT RUN table. Exit code 1 if any step FAILs.
"""
import argparse
import platform
import shutil
import subprocess
import sys
from pathlib import Path

WIN = sys.platform == "win32"


def run(cmd, cwd):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=WIN, timeout=1800)
        out = (p.stdout + p.stderr).strip().splitlines()
        return p.returncode, out[-15:]
    except subprocess.TimeoutExpired:
        return 124, ["timed out after 30 min"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--target", default="windows" if WIN else "none")
    ap.add_argument("--fix", action="store_true")
    a = ap.parse_args()
    root = Path(a.dir).resolve()
    if not (root / "pubspec.yaml").exists():
        sys.exit(f"No pubspec.yaml in {root}")
    results = []
    if not shutil.which("flutter"):
        for step in ["pub get", "format", "fix", "analyze", "test", "codegen", f"build {a.target}"]:
            results.append((step, "NOT RUN", "Flutter SDK not on PATH"))
        return report(results, None)
    _, ver = run(["flutter", "--version"], root)
    flutter_ver = ver[0] if ver else "unknown"
    pub = (root / "pubspec.yaml").read_text(encoding="utf-8", errors="ignore")

    if a.fix:
        run(["dart", "format", "."], root)
        run(["dart", "fix", "--apply"], root)

    steps = [
        ("pub get", ["flutter", "pub", "get"]),
        ("format", ["dart", "format", "--output=none", "--set-exit-if-changed", "."]),
        ("fix (dry run)", ["dart", "fix", "--dry-run"]),
        ("analyze", ["flutter", "analyze", "--fatal-infos"]),
    ]
    for name, cmd in steps:
        code, out = run(cmd, root)
        ok = code == 0
        if name == "fix (dry run)":
            ok = code == 0 and not any("proposed fixes" in l.lower() and not l.strip().startswith("0") for l in out)
        results.append((name, "PASS" if ok else "FAIL", "" if ok else " | ".join(out[-5:])))

    has_tests = any(p for p in root.rglob("*_test.dart") if ".dart_tool" not in p.parts)
    if has_tests:
        code, out = run(["flutter", "test"], root)
        results.append(("test", "PASS" if code == 0 else "FAIL", out[-1] if out else ""))
    else:
        results.append(("test", "FAIL", "no *_test.dart files"))

    if "build_runner" in pub or any("build_runner" in p.read_text(encoding="utf-8", errors="ignore")
                                    for p in root.rglob("pubspec.yaml") if ".dart_tool" not in p.parts):
        code, out = run(["dart", "run", "build_runner", "build", "--delete-conflicting-outputs"], root)
        results.append(("codegen", "PASS" if code == 0 else "FAIL", "" if code == 0 else out[-1]))
    else:
        results.append(("codegen", "PASS", "not used"))

    t = a.target
    if t == "none":
        results.append(("build", "NOT RUN", "--target none"))
    elif t == "ios" and platform.system() != "Darwin":
        results.append(("build ios", "NOT RUN", "needs macOS or a cloud macOS build"))
    elif t == "windows" and not WIN:
        results.append(("build windows", "NOT RUN", "needs Windows"))
    else:
        app = next((p.parent for p in sorted(root.rglob("pubspec.yaml"))
                    if (p.parent / "lib" / "main.dart").exists() and ".dart_tool" not in p.parts), root)
        args = ["flutter", "build", t, "--release"] + (["--wasm"] if t == "web" else [])
        code, out = run(args, app)
        results.append((f"build {t}", "PASS" if code == 0 else "FAIL", "" if code == 0 else " | ".join(out[-5:])))
    return report(results, flutter_ver)


def report(results, ver):
    print(f"Toolchain: {ver or 'not found'}")
    print(f"{'Step':<16} {'Result':<8} Detail")
    for s, r, d in results:
        print(f"{s:<16} {r:<8} {d}")
    return 1 if any(r == "FAIL" for _, r, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
