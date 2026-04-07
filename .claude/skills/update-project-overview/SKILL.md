---
name: update-project-overview
description: "Scan all projects in ~/projects/active/, update overview.md files with current info, remove stale projects, add new ones, and regenerate index.md. Triggers on 'update project overview', 'sync project docs', 'refresh overviews', or /update-project-overview."
argument-hint: "[project-name] (optional — update a single project instead of all)"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

# Update Project Overview

Scan all projects in `~/projects/active/`, update their `overview.md` files with current information, remove stale entries for deleted projects, add new projects, and regenerate `index.md`.

## Constants

- **PROJECTS_DIR**: `~/projects/active`
- **OVERVIEW_REPO**: `~/projects/active/my-projects-overview`
- **PROJECTS_SUBDIR**: `~/projects/active/my-projects-overview/projects`
- **INDEX_FILE**: `~/projects/active/my-projects-overview/index.md`
- **SKIP_SUFFIXES**: `-tests` (test directories)
- **SKIP_NAMES**: `my-projects-overview` (this repo itself)

## Execution

### Step 1: Discover Projects

Scan `PROJECTS_DIR` for all directories. Filter out:
- Directories ending with `-tests`
- `my-projects-overview` (this repo)

This produces the **live project list**.

### Step 2: Detect Changes

Compare the live project list against existing directories in `PROJECTS_SUBDIR`:

- **New projects**: exist in `PROJECTS_DIR` but not in `PROJECTS_SUBDIR`
- **Removed projects**: exist in `PROJECTS_SUBDIR` but not in `PROJECTS_DIR`
- **Existing projects**: exist in both (candidates for update)

Report the counts to the user:
```
Projects found: <N>
New: <list or "none">
Removed: <list or "none">
To update: <N>
```

### Step 3: Handle Removed Projects

For each removed project:
- Delete the directory from `PROJECTS_SUBDIR`
- Note it for removal from `index.md`

### Step 4: Analyze & Update Projects

If `$ARGUMENTS` specifies a single project name, only process that project. Otherwise process all new + existing projects.

For each project, dispatch a background **Agent** (subagent_type: `Explore`) to gather current information. Run agents in parallel batches for efficiency.

Each agent should gather:

1. **Git info**: `git remote -v`, `git branch --show-current`, `git status --short`, `git log --oneline -15`, `git log --format='%ai %s' -5`
2. **Directory structure**: `ls -la` at root, explore key subdirectories
3. **Project type detection**: Check for Package.swift (Swift/macOS), package.json (Node/web), pyproject.toml/requirements.txt (Python), Cargo.toml (Rust), build.gradle.kts (Kotlin/JVM), Makefile, docker-compose.yml, wrangler.jsonc (Cloudflare), railway.toml (Railway)
4. **Documentation**: Read CLAUDE.md, README.md, any markdown in docs/, research/, planning/, Roadmaps/
5. **Claude configuration**: Read .claude/ directory — settings.json, settings.local.json, rules/, skills/, commands/
6. **Tech stack details**: Read dependency/config files for versions and frameworks
7. **Build/test commands**: Extract from package.json scripts, Makefile targets, pyproject.toml, or CLAUDE.md

The agent should then **write** (not just return) the `overview.md` file at `PROJECTS_SUBDIR/<project-name>/overview.md`.

**Overview structure** — each file must include these sections:
```markdown
# <Project Name>

## Project Summary
(1-2 sentences: what it is, what it does)

## Type & Tech Stack
(Project type, languages, frameworks, key dependencies)

## GitHub URL
(git remote URL)

## Directory Structure
(tree-like view of key directories and files with annotations)

## Key Files & Components
(important files and what they do)

## Claude Configuration
(rules, skills, plugins, settings, commands from .claude/)

## Planning & Research Documents
(summarize any docs/, research/, planning/, Roadmaps/ content)

## Git History & Current State
(current branch, clean/dirty, recent commits, notable milestones)

## Build & Test Commands
(how to build, test, run, deploy)

## Notes
(anything else notable: architecture decisions, active work, blockers)
```

### Step 5: Regenerate index.md

After all project overviews are written, read every `overview.md` to extract:
- Project name
- One-line summary
- Primary tech stack
- GitHub organization (mikefullerton, agentic-cookbook, temporal-company, or other)
- Project status (active development, stable, planning, empty/placeholder)

Group projects into categories based on their type:
- **macOS Native Apps** — Swift/SwiftUI/AppKit projects
- **Cross-Platform Apps** — Kotlin Multiplatform or multi-platform projects
- **Agentic Cookbook Ecosystem** — Projects in the agentic-cookbook org
- **Web Applications & SaaS** — Web apps, websites, SaaS platforms
- **Claude Code Extensions & Tools** — Plugins, skills, CLI tools for Claude Code
- **Fun & Creative** — Side projects, experiments, creative tools
- **Infrastructure & Meta** — Setup, dashboards, meta-projects

Write `index.md` with:
- Header with generation date
- Category tables (Project | Summary | Tech)
- Quick Reference section: by organization, by status

### Step 6: Commit & Report

After all files are written, report a summary:
```
Update complete:
- Updated: <N> projects
- Added: <list or "none">
- Removed: <list or "none">
- Index regenerated
```

Do NOT automatically commit — let the user decide when to commit.

## Single-Project Mode

When `$ARGUMENTS` contains a project name:
- Only analyze and update that one project's `overview.md`
- Regenerate `index.md` (since the project summary may have changed)
- Skip steps 2-3 (discovery/removal)
- Report what changed

## Guidelines

- **Be thorough**: Read actual files, don't guess. Check git history, config files, dependency files.
- **Be current**: The overview should reflect the project's state RIGHT NOW, not what it was last time.
- **Remove stale info**: If a feature, file, or component no longer exists, remove it from the overview.
- **Preserve structure**: Always use the standard section headings so overviews are consistent and machine-readable.
- **Parallel execution**: Use background agents for speed. Batch all project analyses in parallel.
- **Keep summaries concise**: The index.md summary column should be one short sentence. Details go in overview.md.
