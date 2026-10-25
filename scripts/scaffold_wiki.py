#!/usr/bin/env python3
"""Scaffold a confirmed personal wiki from the bundled starter assets."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = SKILL_ROOT / "assets" / "starter-repo"
DOMAIN_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SCHEMA_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*\.md$")
RESERVED_SCHEMA_NAMES = {"README.md", "BLUEPRINT.md", "index.md", "log.md"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a personal wiki scaffold without initializing Git or publishing content."
    )
    parser.add_argument("--target", required=True, help="New or empty target directory")
    parser.add_argument("--name", required=True, help="Human-readable wiki name")
    parser.add_argument(
        "--domains",
        required=True,
        nargs="+",
        help="Domain slugs using lowercase letters, numbers, and hyphens",
    )
    parser.add_argument(
        "--blueprint",
        required=True,
        help="Path to the confirmed Markdown blueprint",
    )
    parser.add_argument(
        "--schema",
        default="AGENTS.md",
        help="Canonical schema filename (default: AGENTS.md)",
    )
    parser.add_argument(
        "--date",
        dest="scaffold_date",
        default=date.today().isoformat(),
        help="Initialization date in YYYY-MM-DD format",
    )
    return parser.parse_args()


def validate_inputs(args: argparse.Namespace) -> tuple[Path, Path, list[str], str]:
    target = Path(args.target).expanduser().resolve()
    blueprint = Path(args.blueprint).expanduser().resolve()
    name = args.name.strip()
    schema = args.schema.strip()
    domains = list(dict.fromkeys(args.domains))

    if not ASSET_ROOT.is_dir():
        raise ValueError(f"Starter assets not found: {ASSET_ROOT}")
    if not name:
        raise ValueError("Wiki name must not be empty")
    if target.exists() and not target.is_dir():
        raise ValueError(f"Target exists and is not a directory: {target}")
    if target.exists() and any(target.iterdir()):
        raise ValueError(f"Target must be new or empty: {target}")
    if not blueprint.is_file():
        raise ValueError(f"Confirmed blueprint not found: {blueprint}")
    if blueprint.stat().st_size < 200:
        raise ValueError("Blueprint is too short to be a confirmed design")
    if target == blueprint.parent or target in blueprint.parents:
        raise ValueError("Store the blueprint outside the target repository")
    if not domains:
        raise ValueError("At least one domain is required")
    for domain in domains:
        if not DOMAIN_PATTERN.fullmatch(domain):
            raise ValueError(
                f"Invalid domain slug '{domain}': use lowercase letters, numbers, and hyphens"
            )
    if not SCHEMA_PATTERN.fullmatch(schema) or schema in RESERVED_SCHEMA_NAMES:
        raise ValueError(f"Invalid or reserved schema filename: {schema}")
    try:
        date.fromisoformat(args.scaffold_date)
    except ValueError as exc:
        raise ValueError("Scaffold date must use YYYY-MM-DD") from exc

    return target, blueprint, domains, schema


def display_name(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def domain_list(domains: list[str]) -> str:
    return "\n".join(
        f"- [{display_name(domain)}](wiki/domains/{domain}/)" for domain in domains
    )


def domain_sections(domains: list[str]) -> str:
    sections = []
    for domain in domains:
        sections.append(
            f"""## {display_name(domain)}

Path: `wiki/domains/{domain}/`

### Long-Term Questions and Topics

None yet.

### Claims and Principles

None yet.

### Decisions and Reviews

None yet.

### Concepts and Supporting Records

None yet.
"""
        )
    return "\n".join(sections).rstrip() + "\n"


def replace_asset_placeholders(
    target: Path,
    schema: str,
    wiki_name: str,
    domains: list[str],
    scaffold_date: str,
) -> None:
    replacements = {
        "{{WIKI_NAME}}": wiki_name,
        "{{DOMAIN_LIST}}": domain_list(domains),
        "{{DOMAIN_SECTIONS}}": domain_sections(domains),
        "{{SCHEMA_FILE}}": schema,
        "{{DATE}}": scaffold_date,
    }
    for asset_file in ASSET_ROOT.rglob("*.md"):
        relative = asset_file.relative_to(ASSET_ROOT)
        if relative == Path("AGENTS.md") and schema != "AGENTS.md":
            relative = Path(schema)
        output_file = target / relative
        text = output_file.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            text = text.replace(placeholder, value)
        output_file.write_text(text, encoding="utf-8")


def scaffold(args: argparse.Namespace) -> tuple[Path, list[str], str]:
    target, blueprint, domains, schema = validate_inputs(args)
    wiki_name = args.name.strip()

    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ASSET_ROOT, target, dirs_exist_ok=True)

    if schema != "AGENTS.md":
        (target / "AGENTS.md").rename(target / schema)

    for domain in domains:
        domain_dir = target / "wiki" / "domains" / domain
        domain_dir.mkdir(parents=True, exist_ok=True)
        (domain_dir / ".gitkeep").touch()

    shutil.copy2(blueprint, target / "BLUEPRINT.md")
    replace_asset_placeholders(
        target, schema, wiki_name, domains, args.scaffold_date
    )
    return target, domains, schema


def main() -> int:
    args = parse_args()
    try:
        target, domains, schema = scaffold(args)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Created wiki scaffold: {target}")
    print(f"Domains: {', '.join(domains)}")
    print(f"Schema: {schema}")
    print("Next: review semantic alignment, then run verify_scaffold.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
