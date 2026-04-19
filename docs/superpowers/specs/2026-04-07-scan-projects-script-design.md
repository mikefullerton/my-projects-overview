# Scan Projects Script — Design Spec

## Goal

Replace the LLM-intensive data-gathering phase of the `update-project-overview` skill with a deterministic Python script. The script handles ~80% of the work (scanning, git queries, file reading, tech detection, template generation, index regeneration). The skill becomes a thin orchestrator that calls the script, then uses the LLM only for prose synthesis and site regeneration.

## Architecture

```
skill (update-project-overview)
  │
  ├─ calls: python3 scripts/scan_projects.py [--project <name>]
  │    └─ outputs JSON to stdout
  │
  ├─ LLM pass: fills <!-- LLM --> sections in each template_md
  │    └─ writes projects/<name>/overview.md
  │
  ├─ calls: python3 scripts/scan_projects.py --regenerate-index
  │    └─ reads all overview.md files, writes index.md
  │
  └─ site regeneration (existing skill logic, unchanged)
```

## Script: `scripts/scan_projects.py`

### Location

`scripts/scan_projects.py` in the `myprojectsoverview` repo.

### CLI Interface

```
python3 scripts/scan_projects.py                     # scan all projects
python3 scripts/scan_projects.py --project catnip    # scan one project
python3 scripts/scan_projects.py --regenerate-index  # regenerate index.md from existing overviews
```

### Constants

```python
PROJECTS_DIR = Path.home() / "projects" / "active"
OVERVIEW_REPO = PROJECTS_DIR / "myprojectsoverview"
PROJECTS_SUBDIR = OVERVIEW_REPO / "projects"
INDEX_FILE = OVERVIEW_REPO / "index.md"
SKIP_SUFFIXES = ["-tests"]
SKIP_NAMES = ["myprojectsoverview"]
```

### Output Format (scan mode)

JSON to stdout:

```json
{
  "projects": {
    "<name>": {
      "status": "new | existing | removed",
      "git": {
        "remote_url": "git@github.com:org/repo.git",
        "org": "mikefullerton",
        "branch": "main",
        "clean": true,
        "dirty_files": [],
        "recent_commits": [
          {"hash": "abc1234", "date": "2026-04-07", "message": "feat: add thing"}
        ],
        "last_commit_date": "2026-04-07"
      },
      "tech": {
        "type": "node | python | swift | kotlin | rust | unknown",
        "config_file": "package.json",
        "language": "TypeScript",
        "frameworks": ["React 19", "Vite"],
        "dependencies": {"react": "^19.2.4", "vite": "^8.0.5"},
        "scripts": {"build": "vite build", "dev": "vite", "test": "vitest"}
      },
      "structure": "tree-style string of key directories/files",
      "docs": {
        "README.md": "file contents or null",
        "CLAUDE.md": "file contents or null"
      },
      "planning_docs": {
        "docs/some-plan.md": "file contents",
        "research/topic.md": "file contents"
      },
      "claude_config": {
        "rules": [{"file": "rules/foo.md", "content": "..."}],
        "skills": [{"file": "skills/bar/SKILL.md", "content": "..."}],
        "settings": {},
        "commands": []
      },
      "template_md": "# Project Name\n\n## Project Summary\n<!-- LLM: ... -->\n\n## Type & Tech Stack\n..."
    }
  },
  "new": ["project-a"],
  "removed": ["project-b"],
  "existing": ["project-c", "project-d"]
}
```

### Data Gathering Per Project

All gathered via subprocess calls and file reads, parallelized across projects.

1. **Git info**
   - `git remote get-url origin` for remote URL
   - Parse org from remote URL (e.g., `mikefullerton`, `agentic-cookbook`, `temporal-company`)
   - `git branch --show-current` for current branch
   - `git status --porcelain` for clean/dirty state
   - `git log --format='%h|%ai|%s' -15` for recent commits

2. **Tech stack detection** — check for config files in priority order:
   - `Package.swift` → Swift/macOS
   - `package.json` → read and extract dependencies, scripts, detect frameworks (React, Vite, Hono, etc.)
   - `pyproject.toml` → Python, extract dependencies
   - `requirements.txt` → Python
   - `Cargo.toml` → Rust
   - `build.gradle.kts` → Kotlin/JVM
   - `wrangler.jsonc` / `wrangler.toml` → note Cloudflare deployment
   - `railway.toml` / `railway.json` → note Railway deployment

3. **Directory structure** — `find` limited to depth 3, excluding `node_modules`, `.git`, `__pycache__`, `.build`, `build`, `dist`. Format as indented tree.

4. **Documentation** — read contents of:
   - `README.md`, `CLAUDE.md` at root
   - Files in `docs/`, `research/`, `planning/`, `Roadmaps/` (first 200 lines each, skip binaries)

5. **Claude configuration** — read:
   - `.claude/settings.json`, `.claude/settings.local.json`
   - All files in `.claude/rules/`
   - All `SKILL.md` files in `.claude/skills/`
   - All files in `.claude/commands/`

### Template Generation

For each project, assemble a markdown template with all deterministic sections filled in. Sections that require LLM judgment get a `<!-- LLM -->` marker with context hints.

```markdown
# <Project Name>

## Project Summary
<!-- LLM: Write 1-2 sentences describing what this project is and does. Context: [raw data summary] -->

## Type & Tech Stack
- **Project Type:** <detected type>
- **Language:** <detected language>
- **Frameworks:** <detected frameworks>
- **Key Dependencies:** <from config file>
- **Deployment:** <Cloudflare/Railway/GitHub Pages/none detected>

## GitHub URL
`<remote_url>`

## Directory Structure
```
<tree output>
```

## Key Files & Components
<list of important files with annotations based on filename conventions>

## Claude Configuration
<rules, skills, settings, commands — or "None configured">

## Planning & Research Documents
<summaries of docs found, or "None found">

## Git History & Current State
- **Current Branch:** <branch>
- **Working Tree:** <clean/dirty>
- **Recent Commits:**
<formatted commit list>

## Build & Test Commands
<extracted from package.json scripts / Makefile / pyproject.toml>

## Notes
<!-- LLM: Note anything notable about architecture, active work, blockers, or status. Context: [raw data summary] -->
```

### Index Regeneration (`--regenerate-index`)

When called with `--regenerate-index`:

1. Read every `projects/<name>/overview.md`
2. Extract from each:
   - Project name (from `# H1`)
   - Summary (from `## Project Summary` section, first paragraph)
   - Tech (from `## Type & Tech Stack`, frameworks/language line)
   - GitHub org (parse from `## GitHub URL`)
3. Write `index.md` with:
   - Header with generation date
   - **Categories are NOT determined by the script.** The script outputs a flat list. The skill (or a separate LLM pass) assigns categories. However, if a previous `index.md` exists, the script preserves the existing category assignments for existing projects and marks new projects as `uncategorized`.
4. Quick Reference sections: by org, by status

The script reads the existing `index.md` to preserve category assignments. For new projects, it appends them to an "Uncategorized" section. The skill can then re-categorize if needed.

### Performance

- **Parallelism:** `concurrent.futures.ThreadPoolExecutor` with `max_workers=8` to gather data across projects simultaneously. Each project's data gathering is independent.
- **Subprocess batching:** Where possible, combine git commands (e.g., single `git log` call with format string rather than multiple calls).
- **File reads:** Use `pathlib` for direct reads, no subprocess overhead.
- **Early exit in single-project mode:** Skip discovery/diffing, go straight to gathering for the named project.

### Error Handling

- If a project directory has no `.git`, skip git fields (set to null) and still gather file data.
- If a config file is unreadable or malformed, set that field to null and continue.
- Errors are collected in a top-level `"errors"` array in the output JSON, not raised as exceptions.

## Skill Changes

The `update-project-overview` skill will be updated to:

1. **Step 1-3 (Discovery):** Call `python3 scripts/scan_projects.py` (or `--project <name>`). Parse JSON output. Handle removed projects (delete dirs/HTML).
2. **Step 4 (Analyze & Update):** For each project in the JSON, take the `template_md`, fill in `<!-- LLM -->` sections using the raw data as context. Write `overview.md`.
3. **Step 5 (Index):** Call `python3 scripts/scan_projects.py --regenerate-index`. If new projects need categorization, do a small LLM pass to assign categories, then re-run index generation.
4. **Step 5b (Site):** Unchanged — regenerate HTML site.
5. **Step 6 (Report):** Unchanged.

## What the LLM Still Does

- **Project Summary:** 1-2 sentence synthesis of what the project is and does
- **Notes:** Architecture decisions, active work, blockers, status assessment
- **Categorization:** Assigning new projects to index.md categories
- **Status classification:** active development / stable / planning / empty
- **Site HTML generation:** Converting overviews to styled HTML pages

## File Changes

| File | Change |
|------|--------|
| `scripts/scan_projects.py` | New — the script |
| `.claude/skills/update-project-overview/SKILL.md` | Updated — calls script instead of dispatching gather agents |
