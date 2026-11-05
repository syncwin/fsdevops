#!/usr/bin/env python3
"""PostToolUse hook: run `dart format` on an edited .dart file. Silent no-op otherwise.

Skips generated files and does nothing when Dart is not installed. Never blocks the edit.
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

# Fail open (formatting is a convenience), but never via a shell: the path is untrusted input.
dart = shutil.which("dart")
if (isinstance(path, str) and path.endswith(".dart") and not path.endswith((".g.dart", ".freezed.dart"))
        and dart and os.path.isfile(path)):
    try:
        subprocess.run([dart, "format", "--", os.path.abspath(path)], capture_output=True, timeout=25)
    except Exception:
        pass
sys.exit(0)
