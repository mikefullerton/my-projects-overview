#!/usr/bin/env python3
"""Gather project info and generate draft description.md content.

Usage:
    python3 generate_description_drafts.py --json                    # all projects, raw JSON
    python3 generate_description_drafts.py --project NAME --json     # single project, raw JSON
    python3 generate_description_drafts.py --project NAME --draft    # single project, markdown draft
    python3 generate_description_drafts.py                           # default: print status summary
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

PROJECTS_DIR = Path.home() / "projects" / "active"

TECH_DETECTORS = [
    ("Package.swift", "Swift"),
    ("build.gradle.kts", "Kotlin"),
    ("pyproject.toml", "Python"),
    ("requirements.txt", "Python"),
    ("package.json", "Node.js/TypeScript"),
    ("tsconfig.json", "TypeScript"),
    ("Cargo.toml", "Rust"),
    ("go.mod", "Go"),
    ("Gemfile", "Ruby"),
    ("Dockerfile", "Docker"),
    ("railway.toml", "Railway"),
    ("wrangler.toml", "Cloudflare Workers"),
]


def get_remote_url(project_dir: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True, cwd=str(project_dir),
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def get_file_excerpt(filepath: Path, max_lines: int = 50) -> Optional[str]:
    if filepath.exists():
        lines = filepath.read_text().splitlines()[:max_lines]
        return "\n".join(lines)
    return None


def detect_tech_stack(project_dir: Path) -> List[str]:
    found = []  # type: List[str]
    for filename, tech in TECH_DETECTORS:
        if (project_dir / filename).exists():
            if tech not in found:
                found.append(tech)
    return found


def has_existing_description(project_dir: Path) -> bool:
    return (project_dir / "docs" / "project" / "description.md").exists()


def gather_project_info(project_dir: Path) -> Dict[str, Any]:
    return {
        "name": project_dir.name,
        "path": str(project_dir),
        "remote_url": get_remote_url(project_dir),
        "tech_stack": detect_tech_stack(project_dir),
        "has_readme": (project_dir / "README.md").exists(),
        "readme_excerpt": get_file_excerpt(project_dir / "README.md"),
        "has_claude_md": (project_dir / "CLAUDE.md").exists(),
        "claude_md_excerpt": get_file_excerpt(project_dir / "CLAUDE.md", 30),
        "has_existing_description": has_existing_description(project_dir),
        "top_level_entries": sorted([
            e.name for e in project_dir.iterdir()
            if not e.name.startswith(".") and e.name != "node_modules"
        ]) if project_dir.exists() else [],
    }


def gather_all(project_name: Optional[str] = None) -> Any:
    if project_name:
        project_dir = PROJECTS_DIR / project_name
        if not project_dir.is_dir():
            print("Error: %s is not a directory" % project_dir, file=sys.stderr)
            sys.exit(1)
        return gather_project_info(project_dir)

    results = []  # type: List[Dict[str, Any]]
    for entry in sorted(PROJECTS_DIR.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            results.append(gather_project_info(entry))
    return results


def generate_draft(info: Dict[str, Any]) -> str:
    """Generate a markdown draft from gathered info."""
    name = info["name"]
    title = name.replace("-", " ").title()

    lines = [
        "# %s" % title, "",
        "{One-line description -- FILL IN}", "",
        "## Purpose", "",
        "{Why this project exists -- FILL IN}", "",
    ]

    if info["tech_stack"]:
        lines.extend(["## Tech Stack", ""])
        for tech in info["tech_stack"]:
            lines.append("- %s" % tech)
        lines.append("")

    lines.extend(["## Status", "", "{Current status -- FILL IN}", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gather project info for description.md generation",
    )
    parser.add_argument("--project", help="Single project name to scan")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("--draft", action="store_true", help="Output markdown draft")
    args = parser.parse_args()

    data = gather_all(args.project)

    if args.json:
        print(json.dumps(data, indent=2))
    elif args.draft:
        if isinstance(data, list):
            print("Error: --draft requires --project", file=sys.stderr)
            sys.exit(1)
        print(generate_draft(data))
    else:
        if isinstance(data, list):
            for p in data:
                status = "HAS description" if p["has_existing_description"] else "NEEDS description"
                print("  %-40s %s  tech=%s" % (p["name"], status, p["tech_stack"]))
        else:
            print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
