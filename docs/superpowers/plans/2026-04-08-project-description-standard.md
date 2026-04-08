# Standardized Project Description Rollout — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a standardized `docs/project/description.md` to every project in `~/projects/active/`, giving each project a consistent, human-curated description using progressive disclosure.

**Architecture:** A Python script (`scripts/generate_description_drafts.py`) in my-projects-overview gathers raw info from each project (README, CLAUDE.md, file structure, git remotes, tech detectors) and outputs a draft `description.md` per project. The drafts are then reviewed, refined, and committed into each project's own repo.

**Tech Stack:** Python 3.9+, git CLI

---

## Template Design

Every `docs/project/description.md` follows this progressive-disclosure structure:

```markdown
# {Project Name}

{One-line description — what it is and what it does.}

## Purpose

{1-2 paragraphs: why this project exists, who it's for, what problem it solves.}

## Key Features

- {Feature 1}
- {Feature 2}
- {Feature 3}

## Tech Stack

- **Language(s):** {e.g., Python 3.11, Swift 5.9}
- **Frameworks:** {e.g., React 19, SwiftUI}
- **Infrastructure:** {e.g., Railway, Cloudflare Workers}
- **Build/Test:** {e.g., pytest, vitest, xcodegen}

## Architecture

{Brief description of the high-level architecture — layers, key components, data flow.
Only include if the project is complex enough to warrant it. Omit for simple projects.}

## Status

{Current state: active development, stable, planning, archived, placeholder.}

## Related Projects

- {Links to related projects if any, e.g., "[Cookbook](../../cookbook/docs/project/description.md)"}
```

**Rules:**
- The file lives at `docs/project/description.md` inside each project's own repo
- The `# Title` MUST be the human-friendly project name (e.g., "Cat Herding", not "cat-herding")
- Sections that don't apply can be omitted (e.g., Architecture for trivial projects, Related Projects if none)
- Content should be curated, not auto-generated dumps — concise and useful for both humans and AI agents
- No directory trees, no git history, no build commands — those belong in README or overview.md

---

### Task 1: Create the draft-generation script

**Files:**
- Create: `scripts/generate_description_drafts.py`
- Test: `tests/test_generate_description_drafts.py`

- [ ] **Step 1: Write the failing test for project info gathering**

```python
# tests/test_generate_description_drafts.py
import json
import subprocess
import sys
from pathlib import Path

def test_gather_single_project():
    """Script gathers info for a known project and outputs valid JSON."""
    result = subprocess.run(
        [sys.executable, "scripts/generate_description_drafts.py",
         "--project", "my-projects-overview", "--json"],
        capture_output=True, text=True, cwd=str(Path(__file__).parent.parent)
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    data = json.loads(result.stdout)
    assert data["name"] == "my-projects-overview"
    assert "remote_url" in data
    assert "tech_stack" in data
    assert isinstance(data["tech_stack"], list)

def test_gather_all_projects():
    """Script gathers info for all projects."""
    result = subprocess.run(
        [sys.executable, "scripts/generate_description_drafts.py", "--json"],
        capture_output=True, text=True, cwd=str(Path(__file__).parent.parent)
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    data = json.loads(result.stdout)
    assert isinstance(data, list)
    assert len(data) >= 20  # we have ~27 projects
    names = [p["name"] for p in data]
    assert "cat-herding" in names
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/projects/active/my-projects-overview && python3 -m pytest tests/test_generate_description_drafts.py -v`
Expected: FAIL — script doesn't exist yet

- [ ] **Step 3: Implement the script**

```python
#!/usr/bin/env python3
"""Gather project info and generate draft description.md content.

Usage:
    python3 generate_description_drafts.py --json                    # all projects, raw JSON
    python3 generate_description_drafts.py --project NAME --json     # single project, raw JSON
    python3 generate_description_drafts.py --project NAME --draft    # single project, markdown draft
"""
import argparse
import json
import os
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
            capture_output=True, text=True, cwd=str(project_dir)
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None

def get_readme_content(project_dir: Path, max_lines: int = 50) -> Optional[str]:
    readme = project_dir / "README.md"
    if readme.exists():
        lines = readme.read_text().splitlines()[:max_lines]
        return "\n".join(lines)
    return None

def get_claude_md_content(project_dir: Path, max_lines: int = 30) -> Optional[str]:
    claude_md = project_dir / "CLAUDE.md"
    if claude_md.exists():
        lines = claude_md.read_text().splitlines()[:max_lines]
        return "\n".join(lines)
    return None

def detect_tech_stack(project_dir: Path) -> List[str]:
    found = []
    for filename, tech in TECH_DETECTORS:
        if (project_dir / filename).exists():
            if tech not in found:
                found.append(tech)
    return found

def has_existing_description(project_dir: Path) -> bool:
    return (project_dir / "docs" / "project" / "description.md").exists()

def gather_project_info(project_dir: Path) -> Dict[str, Any]:
    name = project_dir.name
    return {
        "name": name,
        "path": str(project_dir),
        "remote_url": get_remote_url(project_dir),
        "tech_stack": detect_tech_stack(project_dir),
        "has_readme": (project_dir / "README.md").exists(),
        "readme_excerpt": get_readme_content(project_dir),
        "has_claude_md": (project_dir / "CLAUDE.md").exists(),
        "claude_md_excerpt": get_claude_md_content(project_dir),
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
            print(f"Error: {project_dir} is not a directory", file=sys.stderr)
            sys.exit(1)
        return gather_project_info(project_dir)
    
    results = []
    for entry in sorted(PROJECTS_DIR.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            results.append(gather_project_info(entry))
    return results

def generate_draft(info: Dict[str, Any]) -> str:
    """Generate a markdown draft from gathered info."""
    name = info["name"]
    # Title-case the name, replacing hyphens with spaces
    title = name.replace("-", " ").title()
    
    lines = [f"# {title}", ""]
    lines.append("{One-line description — FILL IN}")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append("{Why this project exists — FILL IN}")
    lines.append("")
    
    if info["tech_stack"]:
        lines.append("## Tech Stack")
        lines.append("")
        for tech in info["tech_stack"]:
            lines.append(f"- {tech}")
        lines.append("")
    
    lines.append("## Status")
    lines.append("")
    lines.append("{Current status — FILL IN}")
    lines.append("")
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Gather project info for description.md generation")
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
        # Default: print summary
        if isinstance(data, list):
            for p in data:
                status = "HAS description" if p["has_existing_description"] else "NEEDS description"
                print(f"  {p['name']:40s} {status}  tech={p['tech_stack']}")
        else:
            print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ~/projects/active/my-projects-overview && python3 -m pytest tests/test_generate_description_drafts.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```
git add scripts/generate_description_drafts.py tests/test_generate_description_drafts.py
git commit -m "feat: add generate_description_drafts.py for project description rollout"
git push
```

---

### Task 2: Create description.md for my-projects-overview (this project)

This serves as the reference example for all other projects.

**Files:**
- Create: `docs/project/description.md` (in this repo)

- [ ] **Step 1: Create docs/project/ directory and write description.md**

```markdown
# My Projects Overview

A central index of all active projects, providing structured overviews and a browsable HTML site for Claude to reference.

## Purpose

This project keeps track of all the projects being worked on across `~/projects/active/` and provides a comprehensive index for Claude Code to reference. It auto-generates detailed overview files (tech stack, directory structure, git history, build commands) for each project and publishes them as a static HTML site.

It solves the problem of Claude needing context about the broader project ecosystem — which repos exist, what they do, how they relate, and what state they're in.

## Key Features

- Deterministic project scanner (`scripts/scan_projects.py`) that gathers tech stack, git info, docs, and directory structure
- Per-project `overview.md` files with structured, machine-readable content
- Static HTML site generation under `site/` for browsable project index
- Categorized index (`index.md`) grouping projects by domain (macOS apps, web apps, tools, etc.)

## Tech Stack

- **Language:** Python 3.9+
- **Build/Test:** pytest
- **Site:** Static HTML generated from markdown

## Status

Active development — index and overviews are regenerated regularly as projects evolve.

## Related Projects

- All projects in `~/projects/active/` are tracked by this project
- [My Projects](../my-projects/docs/project/description.md) — a separate web dashboard for project management
```

- [ ] **Step 2: Commit**

```
git add docs/project/description.md
git commit -m "feat: add standardized docs/project/description.md for my-projects-overview"
git push
```

---

### Task 3: Roll out description.md to all remaining projects

For each project in `~/projects/active/`, create `docs/project/description.md` using information from the overview files, READMEs, and CLAUDE.md files. Each description must follow the template from the plan.

**Projects to process (26 remaining, grouped by batch):**

**Batch A — macOS Native Apps (4 projects):**
- Hairball
- scratching-post (Scratching Post)
- catnip-terminal (Catnip Terminal)
- Whippet

**Batch B — Cross-Platform & Web Apps (6 projects):**
- temporal
- temporal-platform
- learntruefacts (Learn True Facts)
- myagenticprojects (MyAgenticProjects)
- mikefullerton.com
- catnip

**Batch C — Agentic Cookbook Ecosystem (8 projects):**
- cookbook
- cookbook-web
- dev-team
- roadmaps
- tools
- official-agent-registry
- agentic-auth-service
- agentic-kitchen

**Batch D — Claude Code Extensions & Tools (3 projects):**
- cat-herding
- code-review-pipline
- social-media-bot

**Batch E — Infrastructure, Fun & Meta (5 projects):**
- mysetup
- my-projects
- myagenticworkspace
- name-craft
- agentic-daemon

For each project:

- [ ] **Step 1: Read the overview file from `my-projects-overview/projects/{name}/overview.md`**

This is the richest source of structured info. Also check README.md and CLAUDE.md in the project repo itself.

- [ ] **Step 2: Write `docs/project/description.md` in the project's own repo**

Path: `~/projects/active/{name}/docs/project/description.md`

Follow the template. Use the overview data to write a concise, curated description. Do NOT copy the overview verbatim — distill it into the progressive-disclosure format.

- [ ] **Step 3: Commit and push in that project's repo**

```bash
cd ~/projects/active/{name}
mkdir -p docs/project
git add docs/project/description.md
git commit -m "docs: add standardized project description"
git push
```

**Special cases:**
- **agentic-kitchen** and **myagenticworkspace**: These are empty placeholders. Write a minimal description noting they are placeholder/empty repos.
- **Projects without overview files**: Use README.md, CLAUDE.md, and file structure inspection to write the description.

---

### Task 4: Update the scanner to detect and report description.md status

**Files:**
- Modify: `scripts/scan_projects.py`
- Modify: `scripts/generate_description_drafts.py`

- [ ] **Step 1: Add `has_description` field to scan_projects.py output**

In the `scan_project()` function, add detection of `docs/project/description.md` and include it in the JSON output.

- [ ] **Step 2: Update generate_description_drafts.py to report coverage**

Add a `--status` flag that shows which projects have descriptions and which don't.

Run: `python3 scripts/generate_description_drafts.py --status`
Expected output: list of all projects with HAS/NEEDS description status.

- [ ] **Step 3: Run tests**

Run: `cd ~/projects/active/my-projects-overview && python3 -m pytest tests/ -v`
Expected: all tests pass

- [ ] **Step 4: Commit**

```
git add scripts/scan_projects.py scripts/generate_description_drafts.py
git commit -m "feat: detect docs/project/description.md in project scanners"
git push
```
