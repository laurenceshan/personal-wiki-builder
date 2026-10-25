#!/usr/bin/env python3
"""Verify the structural integrity of a generated personal wiki scaffold."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOMAIN_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")
REQUIRED_DIRECTORIES = [
    "inbox/capture",
    "inbox/suggestions",
    "raw/external",
    "raw/personal",
    "raw/ai-conversations",
    "raw/research-data",
    "raw/assets",
    "wiki/domains",
    "wiki/sources",
    "wiki/synthesis",
    "templates",
    "exports/private",
    "exports/public",
]
REQUIRED_FILES = [
    "README.md",
    "BLUEPRINT.md",
    "index.md",
    "log.md",
    ".gitignore",
    "inbox/capture/README.md",
    "inbox/suggestions/README.md",
    "exports/public/README.md",
]
REQUIRED_TEMPLATES = [
    "source.md",
    "concept.md",
    "claim.md",
    "principle.md",
    "decision.md",
    "question.md",
    "entity.md",
    "review.md",
    "synthesis.md",
    "public-article.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Generated wiki directory")
    parser.add_argument(
        "--domains",
        nargs="*",
        help="Expected domain slugs; discovered from the scaffold when omitted",
    )
    parser.add_argument(
        "--schema",
        default="AGENTS.md",
        help="Expected canonical schema filename",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    errors: list[str] = []

    if not target.is_dir():
        print(f"ERROR: Target is not a directory: {target}", file=sys.stderr)
        return 1

    for relative in REQUIRED_DIRECTORIES:
        if not (target / relative).is_dir():
            errors.append(f"Missing directory: {relative}")

    required_files = REQUIRED_FILES + [args.schema]
    required_files += [f"templates/{name}" for name in REQUIRED_TEMPLATES]
    for relative in required_files:
        path = target / relative
        if not path.is_file():
            errors.append(f"Missing file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty required file: {relative}")

    domains = args.domains
    if domains:
        for domain in domains:
            if not DOMAIN_PATTERN.fullmatch(domain):
                errors.append(f"Invalid expected domain slug: {domain}")
            elif not (target / "wiki" / "domains" / domain).is_dir():
                errors.append(f"Missing domain directory: wiki/domains/{domain}")
    else:
        domains = sorted(
            path.name
            for path in (target / "wiki" / "domains").iterdir()
            if path.is_dir()
        ) if (target / "wiki" / "domains").is_dir() else []
        if not domains:
            errors.append("No domain directories found under wiki/domains")

    blueprint = target / "BLUEPRINT.md"
    if blueprint.is_file() and blueprint.stat().st_size < 400:
        errors.append("BLUEPRINT.md is too short to be substantive")

    for path in target.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".markdown", ".gitignore"} and path.name != ".gitignore":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Non-UTF-8 text file: {path.relative_to(target)}")
            continue
        if "{{" in text or "}}" in text:
            errors.append(f"Unresolved placeholder: {path.relative_to(target)}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} issue(s)", file=sys.stderr)
        return 1

    print(f"PASS: {target}")
    print(f"Domains: {', '.join(domains)}")
    print(f"Schema: {args.schema}")
    print(f"Templates: {len(REQUIRED_TEMPLATES)}")
    print("Structural validation passed; semantic review is still required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
