#!/usr/bin/env python3
"""Deterministic project scanner for update-project-overview skill.

Scans ~/projects/ for project directories, gathers git info,
tech stack, directory structure, docs, and Claude config. Outputs
structured JSON to stdout.

Usage:
    python3 scan_projects.py                     # scan all projects
    python3 scan_projects.py --project catnip    # scan one project
    python3 scan_projects.py --regenerate-index  # regenerate index.md
"""

import argparse
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

PROJECTS_DIR = Path.home() / "projects"
OVERVIEW_REPO = PROJECTS_DIR / "my-projects-overview"
PROJECTS_SUBDIR = OVERVIEW_REPO / "projects"
INDEX_FILE = OVERVIEW_REPO / "index.md"
SKIP_SUFFIXES = ["-tests"]
SKIP_NAMES = ["my-projects-overview"]
MAX_WORKERS = 8
MAX_DOC_LINES = 200

TREE_EXCLUDE = {
    "node_modules", ".git", "__pycache__", ".build", "build", "dist",
    ".venv", "venv", ".DS_Store", ".swiftpm",
}

TECH_DETECTORS = [
    ("Package.swift", "swift", "Swift"),
    ("package.json", "node", None),
    ("pyproject.toml", "python", "Python"),
    ("requirements.txt", "python", "Python"),
    ("Cargo.toml", "rust", "Rust"),
    ("build.gradle.kts", "kotlin", "Kotlin"),
]

DEPLOYMENT_FILES = {
    "wrangler.jsonc": "Cloudflare Workers",
    "wrangler.toml": "Cloudflare Workers",
    "railway.toml": "Railway",
    "railway.json": "Railway",
}

DOC_DIRS = ["docs", "research", "planning", "Roadmaps"]


def run_git(project_dir: Path, args: List[str], timeout: int = 10) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(project_dir)] + args,
            capture_output=True, text=True, timeout=timeout,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def gather_git(project_dir: Path) -> dict[str, Any]:
    info: Dict[str, Any] = {
        "remote_url": None, "org": None, "branch": None,
        "clean": None, "dirty_files": [], "recent_commits": [],
        "last_commit_date": None,
    }

    if not (project_dir / ".git").exists():
        return info

    info["remote_url"] = run_git(project_dir, ["remote", "get-url", "origin"])
    info["branch"] = run_git(project_dir, ["branch", "--show-current"])

    if info["remote_url"]:
        m = re.search(r"[:/]([^/]+)/[^/]+(?:\.git)?$", info["remote_url"])
        if m:
            info["org"] = m.group(1)

    status = run_git(project_dir, ["status", "--porcelain"])
    if status is not None:
        info["clean"] = len(status) == 0
        if status:
            info["dirty_files"] = status.splitlines()

    log = run_git(project_dir, ["log", "--format=%h|%ai|%s", "-15"])
    if log:
        for line in log.splitlines():
            parts = line.split("|", 2)
            if len(parts) == 3:
                date_str = parts[1].strip().split(" ")[0]
                info["recent_commits"].append({
                    "hash": parts[0].strip(),
                    "date": date_str,
                    "message": parts[2].strip(),
                })
        if info["recent_commits"]:
            info["last_commit_date"] = info["recent_commits"][0]["date"]

    return info


def read_file_safe(path: Path, max_lines: Optional[int] = None) -> Optional[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        if max_lines:
            lines = text.splitlines(keepends=True)
            text = "".join(lines[:max_lines])
        return text
    except (OSError, UnicodeDecodeError):
        return None


def detect_tech(project_dir: Path) -> dict[str, Any]:
    info: Dict[str, Any] = {
        "type": "unknown", "config_file": None, "language": None,
        "frameworks": [], "dependencies": {}, "scripts": {},
        "deployment": None,
    }

    for config_file, tech_type, language in TECH_DETECTORS:
        config_path = project_dir / config_file
        if config_path.exists():
            info["type"] = tech_type
            info["config_file"] = config_file
            if language:
                info["language"] = language

            if config_file == "package.json":
                _parse_package_json(config_path, info)
            elif config_file == "pyproject.toml":
                _parse_pyproject_toml(config_path, info)
            elif config_file == "Package.swift":
                info["language"] = "Swift"
                _detect_swift_frameworks(project_dir, info)
            break

    for deploy_file, deploy_name in DEPLOYMENT_FILES.items():
        if (project_dir / deploy_file).exists():
            info["deployment"] = deploy_name
            break

    return info


def _parse_package_json(path: Path, info: dict) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return

    deps = {}
    deps.update(data.get("dependencies", {}))
    deps.update(data.get("devDependencies", {}))
    info["dependencies"] = deps
    info["scripts"] = data.get("scripts", {})

    frameworks = []
    if "react" in deps:
        version = deps["react"].lstrip("^~")
        major = version.split(".")[0] if version else ""
        frameworks.append(f"React {major}" if major else "React")
    if "vite" in deps:
        frameworks.append("Vite")
    if "hono" in deps:
        frameworks.append("Hono")
    if "next" in deps:
        frameworks.append("Next.js")
    if "express" in deps:
        frameworks.append("Express")
    if "tailwindcss" in deps or "@tailwindcss/vite" in deps:
        frameworks.append("Tailwind CSS")

    info["frameworks"] = frameworks

    if "typescript" in deps or (path.parent / "tsconfig.json").exists():
        info["language"] = "TypeScript"
    else:
        info["language"] = "JavaScript"


def _parse_pyproject_toml(path: Path, info: dict) -> None:
    content = read_file_safe(path)
    if not content:
        return
    deps = {}
    in_deps = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("[") and "dependencies" in stripped:
            in_deps = True
            continue
        if stripped.startswith("[") and in_deps:
            break
        if in_deps and "=" in stripped:
            key = stripped.split("=")[0].strip().strip('"').strip("'")
            val = stripped.split("=", 1)[1].strip().strip('"').strip("'").strip(",")
            deps[key] = val
    if deps:
        info["dependencies"] = deps

    frameworks = []
    dep_names = {k.lower() for k in deps}
    if "flask" in dep_names:
        frameworks.append("Flask")
    if "django" in dep_names:
        frameworks.append("Django")
    if "fastapi" in dep_names:
        frameworks.append("FastAPI")
    if "pytest" in dep_names:
        frameworks.append("pytest")
    if "click" in dep_names:
        frameworks.append("Click")
    info["frameworks"] = frameworks


def _detect_swift_frameworks(project_dir: Path, info: dict) -> None:
    frameworks = []
    swift_files = list(project_dir.rglob("*.swift"))[:20]
    framework_keywords = {
        "SwiftUI": "import SwiftUI",
        "AppKit": "import AppKit",
        "SwiftTerm": "import SwiftTerm",
        "SQLite": "import SQLite",
    }
    found = set()
    for sf in swift_files:
        content = read_file_safe(sf, max_lines=30)
        if not content:
            continue
        for name, keyword in framework_keywords.items():
            if keyword in content and name not in found:
                frameworks.append(name)
                found.add(name)
    info["frameworks"] = frameworks


def build_tree(project_dir: Path, max_depth: int = 3) -> str:
    lines: List[str] = []
    _walk_tree(project_dir, "", 0, max_depth, lines)
    return "\n".join(lines)


def _walk_tree(
    directory: Path, prefix: str, depth: int, max_depth: int, lines: List[str],
) -> None:
    if depth >= max_depth:
        return
    try:
        entries = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        return

    entries = [e for e in entries if e.name not in TREE_EXCLUDE]
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "\u2514\u2500\u2500 " if is_last else "\u251c\u2500\u2500 "
        if entry.is_dir():
            lines.append(f"{prefix}{connector}{entry.name}/")
            extension = "    " if is_last else "\u2502   "
            _walk_tree(entry, prefix + extension, depth + 1, max_depth, lines)
        else:
            lines.append(f"{prefix}{connector}{entry.name}")


def gather_docs(project_dir: Path) -> Tuple[Dict[str, Optional[str]], Dict[str, str]]:
    root_docs: Dict[str, Optional[str]] = {
        "README.md": None,
        "CLAUDE.md": None,
    }
    for name in root_docs:
        path = project_dir / name
        if path.exists():
            root_docs[name] = read_file_safe(path, max_lines=MAX_DOC_LINES)

    planning_docs: Dict[str, str] = {}
    for doc_dir_name in DOC_DIRS:
        doc_dir = project_dir / doc_dir_name
        if not doc_dir.is_dir():
            continue
        for md_file in sorted(doc_dir.rglob("*.md")):
            rel = str(md_file.relative_to(project_dir))
            content = read_file_safe(md_file, max_lines=MAX_DOC_LINES)
            if content:
                planning_docs[rel] = content

    return root_docs, planning_docs


def gather_claude_config(project_dir: Path) -> dict[str, Any]:
    config: Dict[str, Any] = {
        "rules": [], "skills": [], "settings": {}, "commands": [],
    }
    claude_dir = project_dir / ".claude"
    if not claude_dir.is_dir():
        return config

    for settings_file in ["settings.json", "settings.local.json"]:
        path = claude_dir / settings_file
        if path.exists():
            content = read_file_safe(path)
            if content:
                try:
                    config["settings"][settings_file] = json.loads(content)
                except json.JSONDecodeError:
                    config["settings"][settings_file] = None

    rules_dir = claude_dir / "rules"
    if rules_dir.is_dir():
        for rule_file in sorted(rules_dir.rglob("*.md")):
            content = read_file_safe(rule_file, max_lines=MAX_DOC_LINES)
            if content:
                config["rules"].append({
                    "file": str(rule_file.relative_to(project_dir)),
                    "content": content,
                })

    skills_dir = claude_dir / "skills"
    if skills_dir.is_dir():
        for skill_file in sorted(skills_dir.rglob("SKILL.md")):
            content = read_file_safe(skill_file, max_lines=MAX_DOC_LINES)
            if content:
                config["skills"].append({
                    "file": str(skill_file.relative_to(project_dir)),
                    "content": content,
                })

    commands_dir = claude_dir / "commands"
    if commands_dir.is_dir():
        for cmd_file in sorted(commands_dir.rglob("*.md")):
            content = read_file_safe(cmd_file, max_lines=MAX_DOC_LINES)
            if content:
                config["commands"].append({
                    "file": str(cmd_file.relative_to(project_dir)),
                    "content": content,
                })

    return config


def generate_template(
    name: str, git: dict, tech: dict, structure: str,
    docs: dict, planning_docs: dict, claude_config: dict,
) -> str:
    lines: List[str] = []

    lines.append(f"# {name}")
    lines.append("")
    lines.append("## Project Summary")
    lines.append("<!-- LLM: Write 1-2 sentences describing what this project is and does. -->")
    lines.append("")

    lines.append("## Type & Tech Stack")
    lines.append(f"- **Project Type:** {tech['type']}")
    if tech["language"]:
        lines.append(f"- **Language:** {tech['language']}")
    if tech["frameworks"]:
        lines.append(f"- **Frameworks:** {', '.join(tech['frameworks'])}")
    if tech["dependencies"]:
        top_deps = dict(list(tech["dependencies"].items())[:15])
        dep_str = ", ".join(f"{k} {v}" for k, v in top_deps.items())
        lines.append(f"- **Key Dependencies:** {dep_str}")
    if tech["deployment"]:
        lines.append(f"- **Deployment:** {tech['deployment']}")
    lines.append("")

    lines.append("## GitHub URL")
    lines.append(f"`{git['remote_url'] or 'unknown'}`")
    lines.append("")

    lines.append("## Directory Structure")
    lines.append("```")
    lines.append(f"{name}/")
    lines.append(structure)
    lines.append("```")
    lines.append("")

    lines.append("## Key Files & Components")
    lines.append("<!-- LLM: List important files and what they do based on the structure and docs above. -->")
    lines.append("")

    lines.append("## Claude Configuration")
    if claude_config["rules"] or claude_config["skills"] or claude_config["settings"] or claude_config["commands"]:
        if claude_config["rules"]:
            lines.append("### Rules")
            for rule in claude_config["rules"]:
                lines.append(f"- `{rule['file']}`")
        if claude_config["skills"]:
            lines.append("### Skills")
            for skill in claude_config["skills"]:
                lines.append(f"- `{skill['file']}`")
        if claude_config["commands"]:
            lines.append("### Commands")
            for cmd in claude_config["commands"]:
                lines.append(f"- `{cmd['file']}`")
        if claude_config["settings"]:
            lines.append("### Settings")
            for fname in claude_config["settings"]:
                lines.append(f"- `{fname}`")
    else:
        lines.append("None configured.")
    lines.append("")

    lines.append("## Planning & Research Documents")
    if planning_docs:
        for doc_path in planning_docs:
            lines.append(f"- `{doc_path}`")
    else:
        lines.append("None found.")
    lines.append("")

    lines.append("## Git History & Current State")
    lines.append(f"- **Current Branch:** {git['branch'] or 'unknown'}")
    clean_str = "Clean" if git["clean"] else "Dirty" if git["clean"] is False else "Unknown"
    lines.append(f"- **Working Tree:** {clean_str}")
    lines.append(f"- **Last Commit:** {git['last_commit_date'] or 'unknown'}")
    lines.append("- **Recent Commits:**")
    if git["recent_commits"]:
        for commit in git["recent_commits"][:10]:
            lines.append(f"  - `{commit['hash']}` {commit['date']} — {commit['message']}")
    else:
        lines.append("  None")
    lines.append("")

    lines.append("## Build & Test Commands")
    if tech["scripts"]:
        for script_name, script_cmd in tech["scripts"].items():
            lines.append(f"- **{script_name}:** `{script_cmd}`")
    else:
        lines.append("No build scripts detected.")
    lines.append("")

    lines.append("## Notes")
    lines.append("<!-- LLM: Note anything notable about architecture, active work, blockers, or status. -->")
    lines.append("")

    return "\n".join(lines)


def scan_project(name: str, project_dir: Path) -> dict[str, Any]:
    git = gather_git(project_dir)
    tech = detect_tech(project_dir)
    structure = build_tree(project_dir)
    docs, planning_docs = gather_docs(project_dir)
    claude_config = gather_claude_config(project_dir)
    template = generate_template(name, git, tech, structure, docs, planning_docs, claude_config)

    return {
        "git": git,
        "tech": tech,
        "structure": structure,
        "docs": docs,
        "planning_docs": planning_docs,
        "claude_config": claude_config,
        "template_md": template,
        "has_description": (project_dir / "docs" / "project" / "description.md").exists(),
    }


def discover_projects(projects_dir: Path) -> List[str]:
    if not projects_dir.is_dir():
        return []
    names = []
    for entry in sorted(projects_dir.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name.startswith("."):
            continue
        if any(entry.name.endswith(suffix) for suffix in SKIP_SUFFIXES):
            continue
        if entry.name in SKIP_NAMES:
            continue
        names.append(entry.name)
    return names


def diff_projects(
    live: List[str], existing_dir: Path,
) -> Tuple[List[str], List[str], List[str]]:
    existing = set()
    if existing_dir.is_dir():
        existing = {
            e.name for e in existing_dir.iterdir()
            if e.is_dir() and not e.name.startswith(".")
        }
    live_set = set(live)
    new = sorted(live_set - existing)
    removed = sorted(existing - live_set)
    updated = sorted(live_set & existing)
    return new, removed, updated


def scan_all(
    projects_dir: Path, projects_subdir: Path, single_project: Optional[str] = None,
) -> Dict[str, Any]:
    errors: List[str] = []

    if single_project:
        project_dir = projects_dir / single_project
        if not project_dir.is_dir():
            return {"error": f"Project '{single_project}' not found in {projects_dir}"}
        data = scan_project(single_project, project_dir)
        existing_path = projects_subdir / single_project
        status = "existing" if existing_path.is_dir() else "new"
        data["status"] = status
        return {
            "projects": {single_project: data},
            "new": [single_project] if status == "new" else [],
            "removed": [],
            "existing": [single_project] if status == "existing" else [],
            "errors": errors,
        }

    live = discover_projects(projects_dir)
    new, removed, existing = diff_projects(live, projects_subdir)
    to_scan = new + existing
    projects: Dict[str, Any] = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {}
        for name in to_scan:
            project_dir = projects_dir / name
            futures[executor.submit(scan_project, name, project_dir)] = name

        for future in as_completed(futures):
            name = futures[future]
            try:
                data = future.result()
                data["status"] = "new" if name in new else "existing"
                projects[name] = data
            except Exception as e:
                errors.append(f"{name}: {e}")

    for name in removed:
        projects[name] = {"status": "removed"}

    return {
        "projects": projects,
        "new": new,
        "removed": removed,
        "existing": existing,
        "errors": errors,
    }


def regenerate_index(projects_subdir: Path, index_file: Path) -> None:
    entries: List[Dict[str, str]] = []

    if not projects_subdir.is_dir():
        return

    for project_dir in sorted(projects_subdir.iterdir()):
        if not project_dir.is_dir() or project_dir.name.startswith("."):
            continue
        overview = project_dir / "overview.md"
        if not overview.exists():
            continue

        content = read_file_safe(overview)
        if not content:
            continue

        name = project_dir.name
        summary = ""
        tech = ""
        org = ""

        # Extract name from H1
        h1_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        if h1_match:
            name = h1_match.group(1).strip()

        # Extract summary (first non-empty, non-marker line after ## Project Summary)
        sum_match = re.search(
            r"## Project Summary\n+(.+?)(?:\n\n|\n##)", content, re.DOTALL,
        )
        if sum_match:
            summary_text = sum_match.group(1).strip()
            if not summary_text.startswith("<!--"):
                summary = summary_text.split("\n")[0]

        # Extract tech
        tech_match = re.search(r"\*\*Frameworks?:\*\*\s*(.+)", content)
        if tech_match:
            tech = tech_match.group(1).strip()
        else:
            lang_match = re.search(r"\*\*Language:\*\*\s*(.+)", content)
            if lang_match:
                tech = lang_match.group(1).strip()

        # Extract org from GitHub URL (ssh, https, or plain forms)
        url_match = re.search(
            r"(?:git@github\.com:|https?://github\.com/)([^/\s`]+)/",
            content,
        )
        if url_match:
            org = url_match.group(1)

        entries.append({
            "dir_name": project_dir.name,
            "name": name,
            "summary": summary,
            "tech": tech,
            "org": org,
        })

    # Read existing index.md to preserve categories
    existing_categories = _parse_existing_categories(index_file)

    # Assign categories
    categorized: Dict[str, List[dict]] = {}
    uncategorized: List[dict] = []

    for entry in entries:
        found = False
        for cat, members in existing_categories.items():
            if entry["dir_name"] in members:
                categorized.setdefault(cat, []).append(entry)
                found = True
                break
        if not found:
            uncategorized.append(entry)

    # Build index.md
    lines = [
        "# My Projects Overview",
        "",
        "A comprehensive reference for all active projects in `~/projects/`."
        " Each project has a detailed `overview.md` with directory structure, tech stack,"
        " git history, Claude configuration, planning docs, and build commands.",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*",
        "",
        "---",
        "",
    ]

    for cat, cat_entries in categorized.items():
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| Project | Summary | Tech |")
        lines.append("|---------|---------|------|")
        for e in cat_entries:
            link = f"[{e['name']}](projects/{e['dir_name']}/overview.md)"
            lines.append(f"| {link} | {e['summary']} | {e['tech']} |")
        lines.append("")

    if uncategorized:
        lines.append("## Uncategorized")
        lines.append("")
        lines.append("| Project | Summary | Tech |")
        lines.append("|---------|---------|------|")
        for e in uncategorized:
            link = f"[{e['name']}](projects/{e['dir_name']}/overview.md)"
            lines.append(f"| {link} | {e['summary']} | {e['tech']} |")
        lines.append("")

    # Quick Reference
    by_org: Dict[str, List[str]] = {}
    for e in entries:
        org = e["org"] or "unknown"
        by_org.setdefault(org, []).append(e["name"])

    lines.append("---")
    lines.append("")
    lines.append("## Quick Reference")
    lines.append("")
    lines.append("### By Organization")
    lines.append("")
    for org, names in sorted(by_org.items()):
        lines.append(f"**{org}**: {', '.join(names)}")
    lines.append("")

    index_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_existing_categories(index_file: Path) -> dict[str, list[str]]:
    """Parse existing index.md to find which projects are in which categories."""
    categories: Dict[str, List[str]] = {}
    if not index_file.exists():
        return categories

    content = read_file_safe(index_file)
    if not content:
        return categories

    current_cat = None
    for line in content.splitlines():
        if line.startswith("## ") and line.strip() != "## Quick Reference":
            cat = line[3:].strip()
            if cat in ("Quick Reference",):
                current_cat = None
                continue
            current_cat = cat
            categories[current_cat] = []
        elif current_cat and "](projects/" in line:
            m = re.search(r"\]\(projects/([^/]+)/", line)
            if m:
                categories[current_cat].append(m.group(1))

    return categories


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan projects for overview generation")
    parser.add_argument("--project", help="Scan a single project by name")
    parser.add_argument(
        "--regenerate-index", action="store_true",
        help="Regenerate index.md from existing overviews",
    )
    parser.add_argument(
        "--projects-dir", type=Path, default=PROJECTS_DIR,
        help="Override projects directory",
    )
    parser.add_argument(
        "--overview-repo", type=Path, default=OVERVIEW_REPO,
        help="Override overview repo directory",
    )
    args = parser.parse_args()

    projects_dir = args.projects_dir
    overview_repo = args.overview_repo
    projects_subdir = overview_repo / "projects"
    index_file = overview_repo / "index.md"

    if args.regenerate_index:
        regenerate_index(projects_subdir, index_file)
        print(json.dumps({"status": "ok", "index_file": str(index_file)}))
        return

    result = scan_all(projects_dir, projects_subdir, args.project)
    json.dump(result, sys.stdout, indent=2, default=str)
    print()


if __name__ == "__main__":
    main()
