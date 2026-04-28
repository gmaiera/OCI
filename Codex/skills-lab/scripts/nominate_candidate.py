#!/usr/bin/env python3
"""Move a sandbox skill into candidates after validation."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from validate_skill import validate_skill


LAB_ROOT = Path(__file__).resolve().parents[1]


def replace_tree(source: Path, target: Path) -> None:
    if target.exists() or target.is_symlink():
        if target.is_symlink():
            target.unlink()
        else:
            shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".gitkeep", "__pycache__"))


def ensure_eval_template(skill_name: str) -> None:
    eval_dir = LAB_ROOT / "evals" / skill_name
    eval_dir.mkdir(parents=True, exist_ok=True)
    prompts = eval_dir / "prompts.md"
    if not prompts.exists():
        template = (LAB_ROOT / "evals" / "TEMPLATE.md").read_text(encoding="utf-8")
        prompts.write_text(template.replace("<skill-name>", skill_name), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Nominate a sandbox skill as a candidate.")
    parser.add_argument("skill_name", help="Skill folder name in sandbox/")
    args = parser.parse_args()

    source = LAB_ROOT / "sandbox" / args.skill_name
    target = LAB_ROOT / "candidates" / args.skill_name

    errors, warnings = validate_skill(source)
    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print("Nomination aborted.")
        return 1

    replace_tree(source, target)
    ensure_eval_template(args.skill_name)
    print(f"Nominated {args.skill_name} as a candidate.")
    print(f"Eval notes: {LAB_ROOT / 'evals' / args.skill_name / 'prompts.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

