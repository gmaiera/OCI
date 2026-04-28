#!/usr/bin/env python3
"""Promote a candidate skill into local production and install it."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

from validate_skill import validate_skill


LAB_ROOT = Path(__file__).resolve().parents[1]
CODEX_ROOT = LAB_ROOT.parent
LOCAL_ROOT = Path.home() / ".codex" / "skills"


def replace_tree(source: Path, target: Path) -> None:
    if target.exists() or target.is_symlink():
        if target.is_symlink():
            target.unlink()
        else:
            shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".gitkeep", "__pycache__"))


def append_registry(name: str, production_path: Path, local_path: Path) -> None:
    registry = LAB_ROOT / "registry.yaml"
    text = registry.read_text(encoding="utf-8") if registry.exists() else "skills: []\n"
    entry = (
        f"\n# promoted {date.today().isoformat()}\n"
        f"- name: {name}\n"
        f"  status: production-local\n"
        f"  production_path: {production_path.relative_to(CODEX_ROOT)}\n"
        f"  local_path: {local_path}\n"
        f"  github_shared: false\n"
    )

    if "skills: []" in text:
        text = text.replace("skills: []", "skills:\n" + entry)
    else:
        text = text.rstrip() + "\n" + entry

    registry.write_text(text, encoding="utf-8")


def install_local(production_path: Path, local_path: Path) -> int:
    command = [
        sys.executable,
        str(LAB_ROOT / "scripts" / "install_local.py"),
        str(production_path),
        "--local-root",
        str(local_path.parent),
    ]
    return subprocess.call(command)


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote a candidate skill to local production.")
    parser.add_argument("skill_name", help="Skill folder name in candidates/")
    args = parser.parse_args()

    candidate = LAB_ROOT / "candidates" / args.skill_name
    production = LAB_ROOT / "production" / args.skill_name
    local = LOCAL_ROOT / args.skill_name

    errors, warnings = validate_skill(candidate)
    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print("Promotion aborted.")
        return 1

    replace_tree(candidate, production)
    install_code = install_local(production, local)
    if install_code != 0:
        return install_code

    append_registry(args.skill_name, production, local)
    print(f"Promoted {args.skill_name} to local production.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
