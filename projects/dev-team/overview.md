# Dev Team - Project Overview

## Project Summary

The Agentic Cookbook Dev Team is a Claude Code plugin providing a multi-agent platform for product discovery, analysis, and project building. Distributed via the agentic-cookbook marketplace, it combines structured specialist expertise with flexible interview workflows to help users scope, plan, and build software through distributed AI team collaboration. Not yet ready for general use.

## Type & Tech Stack

- **Project Type:** Claude Code Plugin (multi-agent system orchestration)
- **Python 3.10+** -- Core logic: arbitrator, project-storage, scripts, observers, tests
- **Markdown** -- Agent definitions, specialist manifests, specialty-teams, workflows, skills
- **HTML/JavaScript** -- Web dashboard service, GitHub Pages site
- **SQLite 3** -- Shared database backend (v2 storage-provider unification in progress)
- **Testing:** pytest (122+ contract tests, deterministic test runner)

## GitHub URL

`git@github.com:agentic-cookbook/dev-team.git`
https://github.com/agentic-cookbook/dev-team

## Directory Structure

```
dev-team/
├── .claude/
│   ├── CLAUDE.md                      # Local workspace guide
│   ├── settings.json                  # SubagentStop hook (observer dispatch)
│   ├── rules/                         # 5 rules
│   │   ├── always-commit-and-push.md  # Non-negotiable: commit+push after every change
│   │   ├── bump-versions.md           # Increment version on skill/agent modification
│   │   ├── db-schema-design.md        # No blobs, no computed values, meaningful names
│   │   ├── optimize-subagent-dispatch.md  # Model selection, parallelism, progressive disclosure
│   │   └── use-project-directories.md # Plugin in plugins/dev-team/, dev tooling at root
│   └── skills/                        # create-specialist, lint-specialist
├── plugins/dev-team/                  # Self-contained plugin
│   ├── agents/                        # 20 agent definitions
│   │   ├── artifact-reviewer.md, build-runner.md, code-comparator.md
│   │   ├── code-generator.md, codebase-scanner.md, project-assembler.md
│   │   ├── project-scaffolder.md, recipe-reviewer.md, recipe-writer.md
│   │   ├── scope-matcher.md, smoke-tester.md, specialist-aligner.md
│   │   ├── specialist-analyst.md, specialist-code-pass.md
│   │   ├── specialist-interviewer.md, transcript-analyzer.md
│   │   ├── consulting-team-worker.md, consulting-team-verifier.md
│   │   ├── specialty-team-worker.md, specialty-team-verifier.md
│   │   └── _example.md
│   ├── specialists/                   # 20 specialists (13 domain + 6 platform + 1 PM)
│   │   ├── (domain) accessibility, claude-code, code-quality, data-persistence,
│   │   │   development-process, devops-observability, localization-i18n,
│   │   │   networking-api, reliability, security, software-architecture,
│   │   │   testing-qa, ui-ux-design
│   │   ├── (platform) platform-android, platform-database, platform-ios-apple,
│   │   │   platform-web-backend, platform-web-frontend, platform-windows
│   │   └── project-manager
│   ├── specialty-teams/               # 21 categories of specialty-team files
│   │   ├── accessibility/, claude-code/, code-quality/, data-persistence/
│   │   ├── development-process/, devops-observability/, localization-i18n/
│   │   ├── networking-api/, platform-android/, platform-database/
│   │   ├── platform-ios-apple/, platform-web-backend/, platform-web-frontend/
│   │   ├── platform-windows/, project-management/, reliability/
│   │   ├── security/, software-architecture/, testing-qa/, ui-ux-design/
│   │   └── _example/
│   ├── consulting-teams/              # Cross-cutting verification teams
│   │   ├── _example/
│   │   └── platform-database/
│   ├── skills/dev-team/
│   │   ├── SKILL.md                   # v0.7.0 -- Main skill router
│   │   └── workflows/                 # 8 workflows
│   ├── scripts/
│   │   ├── arbitrator.py              # Communication conduit (backend-swappable)
│   │   ├── arbitrator/                # Markdown backend resource scripts
│   │   ├── project_storage.py         # Project management storage
│   │   ├── project-storage/markdown/  # Project resource scripts
│   │   ├── storage-provider/markdown/ # Unified storage provider
│   │   ├── db/                        # SQLite database API
│   │   └── observers/                 # dispatch.py, stenographer.py, oslog.py
│   ├── services/dashboard/            # Web dashboard
│   ├── docs/                          # specialist-spec.md, specialist-guide.md
│   └── tests/
├── docs/
│   ├── architecture.md                # Single source of truth for system design
│   ├── planning/                      # 17+ design/implementation docs
│   │   ├── design-spec.md, todo.md, cookbook-requests.md
│   │   ├── 2026-04-02-shared-database-design.md
│   │   ├── 2026-04-03-system-architecture-v2.md
│   │   ├── 2026-04-04-specialty-team-extraction-plan.md
│   │   ├── unified-test-strategy-design.md, unified-test-strategy-plan.md
│   │   └── (12 more planning docs)
│   └── research/                      # 4+ research docs
│       ├── agent-patterns.md, conversational-patterns.md
│       ├── persona-design.md, database/
├── tests/
│   ├── run_tests.py                   # Deterministic test runner
│   ├── pyproject.toml                 # pytest config
│   ├── arbitrator/                    # 58 contract tests
│   ├── project-storage/               # 64 contract tests
│   ├── agents/, specialists/, specialty-teams/, consulting-teams/
│   ├── skills/, session/, dashboard/, observers/
│   ├── harness/, fixtures/, personas/
│   └── test-design.md, simulated-user.md
├── site/                              # GitHub Pages website assets
│   └── og.png
├── index.html                         # GitHub Pages main page (at root for GH Pages)
├── CNAME                              # Custom domain for GitHub Pages
├── README.md
└── .gitignore
```

## Key Files & Components

### Multi-Agent Pipeline
```
User invokes /dev-team <command>
  -> Skill router (SKILL.md) loads config, inits DB, routes to workflow
    -> Team-lead runs the workflow, talks to user
      -> Team-lead dispatches specialists via arbitrator
        -> Specialty-teams run (worker-verifier loop, max 3 retries)
        -> Consulting-teams review (cross-cutting concerns)
        [Observer hook fires on each subagent completion]
        -> Specialist-persona writes interpretations
      -> Specialist returns result via arbitrator
    -> Team-lead aggregates results, presents report
```

### Key Terminology
- **Team-Lead**: Runs a workflow, has a persona, talks to the user (5 types: interview, analysis, review, build, audit)
- **Specialist**: Self-enclosed domain expert with cookbook sources and specialty-team manifest (20 total)
- **Specialty-Team**: Worker-verifier pair focused on one cookbook artifact
- **Consulting-Team**: Worker-verifier pair for cross-cutting concern review
- **Observer**: Shell hook + Python script capturing subagent activity via SubagentStop
- **Session**: A playbook being executed with tracked state

### 20 Specialists
**Domain (13):** accessibility, claude-code, code-quality, data-persistence, development-process, devops-observability, localization-i18n, networking-api, reliability, security, software-architecture, testing-qa, ui-ux-design

**Platform (6):** platform-android, platform-database, platform-ios-apple, platform-web-backend, platform-web-frontend, platform-windows

**Management (1):** project-manager

### 8 Skill Workflows
interview, create-recipe-from-code, generate, create-code-from-recipe, lint, align-specialists, compare-code, view-recipe

### Pluggable Storage Backends
Arbitrator and project-storage APIs with swappable backends. Currently markdown-based. Storage-provider unification spec added (Apr 7) to consolidate arbitrator + project-storage into a single provider interface.

## Claude Configuration

### Rules (5)
1. **always-commit-and-push.md**: Non-negotiable. Commit + push after every change. No batching. No asking.
2. **bump-versions.md**: Increment version on skill/agent modification (patch/minor/major).
3. **db-schema-design.md**: No blobs, no computed values, no unstructured lists. Columns must be indexable. Use project vocabulary.
4. **optimize-subagent-dispatch.md**: Mechanical tasks use fast model. Judgment tasks use full model. Parallelize independent tasks.
5. **use-project-directories.md**: Plugin in `plugins/dev-team/`, dev tooling at repo root.

### Hook (settings.json)
`SubagentStop` -> `python3 plugins/dev-team/scripts/observers/dispatch.py` (auto-discovers observer modules: stenographer, oslog)

### Skills (2 dev skills)
- **create-specialist**: Scaffold new specialist definitions
- **lint-specialist**: Validate specialist files against spec

## Planning & Research Documents

### docs/architecture.md
Single source of truth for system design. Read first. Covers terminology, pipeline flow, components, file map, configuration.

### docs/planning/ (17+ docs)
- **design-spec.md**: Core system design
- **todo.md**: Current task tracking
- **2026-04-07 storage-provider unification**: Consolidate arbitrator + project-storage into single backend
- **2026-04-03 system-architecture-v2**: Next-gen architecture design
- **2026-04-02 shared-database-design/plan**: SQLite backend for sessions
- **2026-04-04 specialty-team-extraction-plan**: Refactoring specialty-teams
- **unified-test-strategy**: Design + implementation plan for test coverage
- **build-history.md**: Record of build changes

### docs/research/
- agent-patterns.md, conversational-patterns.md, persona-design.md, database/ research

## Git History & Current State

**Branch:** `main`
**Working Tree:** 2 deleted files (rules/.DS_Store, rules/.gitkeep)

**Recent Commits (all 2026-04-07):**
```
e04a6dc Add storage-provider unification and data model spec
f8d88f7 Move pyproject.toml into tests/ to keep repo root clean
6455e18 Move website assets to /site, keep CNAME and index.html at root for GH Pages
e19f7e9 Move planning docs into docs/planning, remove /planning
4fe827c Remove tracked .DS_Store file
```

**Key Recent Changes:**
- Storage-provider unification spec added (Apr 7)
- pyproject.toml moved into tests/ (Apr 7)
- Website assets moved to /site (Apr 7)
- Planning docs consolidated into docs/planning/ (Apr 7)
- Deterministic test runner added, all tests migrated from Vitest to pytest (Apr 6)
- Skill version: 0.7.0, Plugin version: 0.4.0

## Build & Test Commands

```bash
python3 tests/run_tests.py           # Run all tests (deterministic order)
pytest tests/ -q                     # Run all pytest tests
pytest tests/arbitrator/ -q          # Specific test area (58 contract tests)
pytest tests/project-storage/ -q     # Storage tests (64 contract tests)
/dev-team interview                  # Launch interview workflow
```

No build step -- plugin distributed as-is via marketplace.

## Notes

1. **Three-repo model**: agentic-cookbook (principles/guidelines), dev-team (plugin), workspace repo (per-user data: profiles, transcripts, analyses).

2. **Specialty-teams**: 21 categories across 20 specialists + consulting-teams for cross-cutting concerns. Worker-verifier loop with max 3 retries before escalation.

3. **Observer system**: SubagentStop hook auto-discovers observer modules (stenographer writes JSONL session log, oslog writes to macOS system log).

4. **Active development**: Storage-provider unification in progress. Tests migrated to pytest. Not ready for general use.

5. **GitHub Pages**: Website served from root `index.html` + `site/` directory with CNAME for custom domain.

6. **Commit discipline**: Must commit and push immediately after every change. Rule-enforced, non-negotiable.
