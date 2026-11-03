#!/usr/bin/env python3
"""Detect the stack and shape of an app project. Standard library only.

Usage: python detect_project.py <dir> [--json]
"""
import json
import re
import sys
from pathlib import Path

SKIP = {".git", ".dart_tool", "build", "node_modules", ".fvm", "Pods"}
LIBS = {
    "state": ["flutter_riverpod", "riverpod", "hooks_riverpod", "flutter_bloc", "provider", "get", "signals", "mobx"],
    "routing": ["go_router", "auto_route", "beamer"],
    "models": ["freezed", "json_serializable", "built_value"],
    "database": ["drift", "sqflite", "isar", "hive", "objectbox", "shared_preferences"],
    "http": ["dio", "http", "chopper", "retrofit"],
    "codegen": ["build_runner", "riverpod_generator"],
    "lints": ["flutter_lints", "very_good_analysis", "lints"],
}
TARGETS = ["windows", "android", "ios", "web", "macos", "linux"]


def pubspecs(root):
    for p in root.rglob("pubspec.yaml"):
        if not SKIP.intersection(p.relative_to(root).parts):
            yield p


def deps(text):
    return set(re.findall(r"^\s{2}([a-z_][a-z0-9_]*):", text, re.M))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0] if args else ".").resolve()
    if not root.is_dir():
        print(f"Not a folder: {root}")
        return 2
    out = {"root": str(root), "stack": None, "packages": [], "libraries": {}, "targets": {},
           "workspace": False, "builder": None, "ownership_file": False, "tests": 0}
    files = list(pubspecs(root))
    if files:
        all_deps = set()
        for p in files:
            text = p.read_text(encoding="utf-8", errors="ignore")
            name = re.search(r"^name:\s*(\S+)", text, re.M)
            flutter = bool(re.search(r"^\s+flutter:\s*\n\s+sdk:\s*flutter", text, re.M))
            sdk = re.search(r"^\s+sdk:\s*['\"]?([^'\"\n]+)", text, re.M)
            if p.parent == root and re.search(r"^workspace:", text, re.M):
                out["workspace"] = True
            out["packages"].append({"path": str(p.parent.relative_to(root)) or ".",
                                    "name": name.group(1) if name else None,
                                    "flutter": flutter, "dart_sdk": sdk.group(1).strip() if sdk else None})
            all_deps |= deps(text)
            for t in TARGETS:
                if (p.parent / t).is_dir():
                    out["targets"].setdefault(t, []).append(str(p.parent.relative_to(root)) or ".")
        out["stack"] = "flutter" if any(x["flutter"] for x in out["packages"]) else "dart"
        out["libraries"] = {k: sorted(all_deps.intersection(v)) for k, v in LIBS.items()}
    elif (root / "package.json").exists():
        out["stack"] = "node (not supported yet)"
    elif any(root.iterdir()):
        out["stack"] = "unknown"
    else:
        out["stack"] = "empty"
    if any(root.rglob(".nowa")):
        out["builder"] = "nowa (visual builder: follow ownership rules)"
    out["ownership_file"] = (root / ".claude" / "ownership.md").exists()
    out["tests"] = sum(1 for p in root.rglob("*_test.dart") if not SKIP.intersection(p.parts))
    if "--json" in sys.argv:
        print(json.dumps(out, indent=2))
    else:
        for k, v in out.items():
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
