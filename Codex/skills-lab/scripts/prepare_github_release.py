#!/usr/bin/env python3
"""Prepare a GitHub-shareable copy of a production skill."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

from validate_skill import validate_skill


LAB_ROOT = Path(__file__).resolve().parents[1]
CODEX_ROOT = LAB_ROOT.parent
SHARED_ROOT = CODEX_ROOT / "skills"

SENSITIVE_PATTERNS = {
    "local home path": re.compile(r"/Users/gmaiera\b"),
    "private email": re.compile(r"[A-Za-z0-9._%+-]+@(oracle\.com|gmail\.com|icloud\.com)", re.I),
    "token-like value": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    "private ssh url": re.compile(r"git@github\.com:"),
}


def scan_sensitive(skill_dir: Path) -> list[str]:
    findings: list[str] = []
    for path in skill_dir.rglob("*"):
        if path.is_dir() or path.name == ".DS_Store":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        rel = path.relative_to(skill_dir)
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{rel}: possible {label}")

    return findings


def replace_tree(source: Path, target: Path) -> None:
    if target.exists() or target.is_symlink():
        if target.is_symlink():
            target.unlink()
        else:
            shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".gitkeep", "__pycache__"))


def append_registry(name: str, shared_path: Path) -> None:
    registry = LAB_ROOT / "registry.yaml"
    text = registry.read_text(encoding="utf-8") if registry.exists() else "skills: []\n"
    entry = (
        f"\n# shared {date.today().isoformat()}\n"
        f"- name: {name}\n"
        f"  status: github-ready\n"
        f"  shared_path: {shared_path.relative_to(CODEX_ROOT)}\n"
        f"  github_target: https://github.com/gmaiera/OCI/tree/main/Codex/skills/{name}\n"
    )

    if "skills: []" in text:
        text = text.replace("skills: []", "skills:\n" + entry)
    else:
        text = text.rstrip() + "\n" + entry

    registry.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare a skill package for GitHub sharing.")
    parser.add_argument("skill_name", help="Skill folder name in production/")
    parser.add_argument("--allow-findings", action="store_true", help="Copy even if privacy scan flags possible issues")
    args = parser.parse_args()

    source = LAB_ROOT / "production" / args.skill_name
    target = SHARED_ROOT / args.skill_name

    errors, warnings = validate_skill(source)
    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print("GitHub preparation aborted.")
        return 1

    findings = scan_sensitive(source)
    if findings and not args.allow_findings:
        print("Privacy scan found possible sensitive content:")
        for finding in findings:
            print(f"- {finding}")
        print("Review the skill or rerun with --allow-findings after manual approval.")
        return 1

    replace_tree(source, target)
    append_registry(args.skill_name, target)
    print(f"Prepared GitHub-shareable skill at {target}")
    print(f"Target URL: https://github.com/gmaiera/OCI/tree/main/Codex/skills/{args.skill_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
