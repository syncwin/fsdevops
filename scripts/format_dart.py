#!/usr/bin/env python3
"""PostToolUse hook: run `dart format` on an edited .dart file. Silent no-op otherwise.

Skips generated files and does nothing when Dart is not installed. Never blocks the edit.
"""
import json
import shutil
import subprocess
import sys

try:
    data = json.load(sys.stdin)
    path = (data.get("tool_input") or {}).get("file_path", "")
except Exception:
    sys.exit(0)

if (path.endswith(".dart") and not path.endswith((".g.dart", ".freezed.dart"))
        and shutil.which("dart")):
    subprocess.run(["dart", "format", path], capture_output=True, shell=sys.platform == "win32", timeout=25)
sys.exit(0)
