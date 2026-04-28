#!/usr/bin/env python3
"""Validate a Codex skill folder before local install or promotion."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN_FILES = {
    "README.md",
    "CHANGELOG.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    raw = text[4:end].strip()
    body = text[end + 4 :].lstrip()
    data: dict[str, str] = {}

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            data[key] = value.strip().strip("\"'")

    return data, body


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not skill_dir.exists():
        return [f"Skill folder does not exist: {skill_dir}"], warnings
    if not skill_dir.is_dir():
        return [f"Skill path is not a folder: {skill_dir}"], warnings

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"Missing required file: {skill_md}"], warnings

    text = skill_md.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        errors.append("SKILL.md frontmatter is missing required field: name")
    if not description:
        errors.append("SKILL.md frontmatter is missing required field: description")

    if name and name != skill_dir.name:
        warnings.append(f"Frontmatter name '{name}' differs from folder name '{skill_dir.name}'")

    if description and len(description.split()) < 12:
        warnings.append("Description is short; make trigger conditions more explicit")

    body_lines = body.splitlines()
    if len(body_lines) > 500:
        warnings.append(f"SKILL.md body is {len(body_lines)} lines; consider moving details to references/")

    found_forbidden = sorted(p.name for p in skill_dir.iterdir() if p.name in FORBIDDEN_FILES)
    if found_forbidden:
        warnings.append("Skill folder contains auxiliary docs that skills should avoid: " + ", ".join(found_forbidden))

    references_dir = skill_dir / "references"
    if references_dir.exists():
        for ref in references_dir.iterdir():
            if ref.is_file() and ref.name not in text:
                warnings.append(f"references/{ref.name} is not mentioned from SKILL.md")

    agents_yaml = skill_dir / "agents" / "openai.yaml"
    if not agents_yaml.exists():
        warnings.append("Missing agents/openai.yaml; optional, but recommended for UI metadata")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Codex skill folder.")
    parser.add_argument("skill_dir", type=Path, help="Path to a skill folder")
    args = parser.parse_args()

    errors, warnings = validate_skill(args.skill_dir.resolve())

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print("FAILED")
        return 1

    print("PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())

