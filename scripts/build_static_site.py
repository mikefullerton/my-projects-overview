#!/usr/bin/env python3
"""Bake projects.json into site/public/ so the Vite build picks it up.

Reads every projects/<name>/overview.md, cross-references which projects
still exist in ~/projects/, and emits a single projects.json in the shape
the React hook expects: a list of {id, folder, markdown}.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROJECTS_SUBDIR = REPO / "projects"
LIVE_PROJECTS = Path.home() / "projects"
OUTPUT = REPO / "site" / "public" / "projects.json"


def main() -> int:
    if not PROJECTS_SUBDIR.is_dir():
        print(f"error: {PROJECTS_SUBDIR} does not exist", file=sys.stderr)
        return 1

    live = set()
    if LIVE_PROJECTS.is_dir():
        live = {p.name for p in LIVE_PROJECTS.iterdir() if p.is_dir()}

    entries = []
    for project_dir in sorted(PROJECTS_SUBDIR.iterdir(), key=lambda p: p.name.lower()):
        if not project_dir.is_dir() or project_dir.name.startswith("."):
            continue
        overview = project_dir / "overview.md"
        if not overview.exists():
            continue
        entries.append({
            "id": project_dir.name,
            "folder": "active" if project_dir.name in live else "unknown",
            "markdown": overview.read_text(),
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(entries, indent=2) + "\n")
    print(f"wrote {len(entries)} projects to {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
