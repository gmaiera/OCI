#!/usr/bin/env python3
"""Install a skill into ~/.codex/skills for local testing."""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

from validate_skill import validate_skill


DEFAULT_LOCAL_ROOT = Path.home() / ".codex" / "skills"


def backup_existing(target: Path) -> Path | None:
    if not target.exists() and not target.is_symlink():
        return None

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = target.with_name(f"{target.name}.backup-{timestamp}")
    target.rename(backup)
    return backup


def copy_skill(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    backup_existing(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".gitkeep", "__pycache__"))


def link_skill(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    backup_existing(target)
    target.symlink_to(source, target_is_directory=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install a skill locally for Codex testing.")
    parser.add_argument("skill_dir", type=Path, help="Path to skill folder")
    parser.add_argument("--local-root", type=Path, default=DEFAULT_LOCAL_ROOT)
    parser.add_argument("--mode", choices=["copy", "symlink"], default="copy")
    args = parser.parse_args()

    source = args.skill_dir.resolve()
    errors, warnings = validate_skill(source)

    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print("Install aborted.")
        return 1

    target = args.local_root.expanduser().resolve() / source.name

    if args.mode == "symlink":
        link_skill(source, target)
    else:
        copy_skill(source, target)

    print(f"Installed {source.name} to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

