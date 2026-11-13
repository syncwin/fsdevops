#!/usr/bin/env python3
"""PostToolUse hook: run `dart format` on an edited .dart file. Silent no-op otherwise.

Skips generated files and does nothing when Dart is not installed. Never blocks the edit.
On Windows, `dart` is usually a .bat shim and cmd.exe re-parses its arguments (BatBadBut), so we
resolve dart.exe directly and never run a .bat/.cmd; paths with cmd metacharacters are skipped.
"""
import json
import os
import shutil
import subprocess
import sys

try:
    data = json.load(sys.stdin)
    path = (data.get("tool_input") or {}).get("file_path", "")
except Exception:
    sys.exit(0)

UNSAFE = set('&|<>^%"')


def find_dart():
    """Return a real dart executable (never a .bat/.cmd), or None."""
    found = shutil.which("dart")
    if os.name != "nt":
        return found
    cands = []
    if found:
        if found.lower().endswith(".exe"):
            return found
        base = os.path.dirname(found)  # .../flutter/bin or .../dart-sdk/bin
        cands += [os.path.join(base, "cache", "dart-sdk", "bin", "dart.exe"), os.path.join(base, "dart.exe")]
    for env in ("DART_SDK", "FLUTTER_ROOT"):
        root = os.environ.get(env)
        if root:
            cands += [os.path.join(root, "bin", "dart.exe"), os.path.join(root, "bin", "cache", "dart-sdk", "bin", "dart.exe")]
    flutter = shutil.which("flutter")
    if flutter:
        cands.append(os.path.join(os.path.dirname(flutter), "cache", "dart-sdk", "bin", "dart.exe"))
    return next((c for c in cands if os.path.isfile(c)), None)


if isinstance(path, str) and path.endswith(".dart") and not path.endswith((".g.dart", ".freezed.dart")) and os.path.isfile(path):
    full = os.path.abspath(path)
    if os.name == "nt" and any(ch in UNSAFE for ch in full):
        print("format_dart: skipped, path contains a cmd metacharacter: " + full, file=sys.stderr)
        sys.exit(0)
    dart = find_dart()
    if dart:
        # Fail open (formatting is a convenience), but never via a shell: the path is untrusted input.
        try:
            subprocess.run([dart, "format", "--", full], capture_output=True, timeout=25)
        except Exception:
            pass
sys.exit(0)
