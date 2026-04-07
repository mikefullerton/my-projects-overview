# Dev Team

## Project Summary

dev-team is a Claude Code plugin providing a multi-agent platform for product discovery, analysis, and project building. Distributed via the agentic-cookbook marketplace, it combines structured specialist expertise with flexible interview workflows to help users scope, plan, and build software through distributed AI team collaboration.

## Type & Tech Stack

- **Project Type:** Claude Code Plugin (multi-agent system orchestration)
- **Python 3.10+** — Core logic: arbitrator, project-storage, scripts, tests
- **Markdown** — Agent definitions, specialist manifests, specialty-teams, workflows
- **HTML/JavaScript** — Web dashboard service
- **SQLite 3** — Shared database backend (v2 in progress)
- **Testing:** pytest

## GitHub URL

`git@github.com:agentic-cookbook/dev-team.git`

## Directory Structure

```
dev-team/
├── .claude/
│   ├── CLAUDE.md                      # Local workspace guide
│   ├── rules/                         # 5 rules: always-commit-and-push, bump-versions, db-schema-design, optimize-subagent-dispatch, use-project-directories
│   ├── settings.json                  # SubagentStop hook (observer dispatch)
│   └── skills/                        # create-specialist, lint-specialist
├── plugins/dev-team/                  # Main plugin (self-contained)
│   ├── .claude-plugin/plugin.json     # v0.4.0
│   ├── agents/                        # 20 agent definitions
│   ├── specialists/                   # 20 specialists (13 domain + 6 platform + 1 PM)
│   ├── specialty-teams/               # 232 specialty-team files across 20 categories
│   ├── consulting-teams/              # Cross-cutting verification teams
│   ├── skills/dev-team/
│   │   ├── SKILL.md                   # v0.7.0 — Main skill router
│   │   └── workflows/                 # 8 workflows: interview, create-recipe-from-code, generate, create-code-from-recipe, lint, align-specialists, compare-code, view-recipe
│   ├── scripts/
│   │   ├── arbitrator.py              # Communication conduit (backend-swappable)
│   │   ├── arbitrator/                # 13 resource scripts (markdown backend)
│   │   ├── project_storage.py         # Project management storage
│   │   ├── project-storage/markdown/  # 8 project resource scripts
│   │   ├── db/                        # SQLite database API
│   │   └── observers/                 # dispatch.py, stenographer.py, oslog.py
│   ├── services/dashboard/            # Web dashboard
│   ├── docs/                          # specialist-spec.md, specialist-guide.md, research/
│   └── tests/
├── docs/
│   ├── architecture.md                # CRITICAL — Single source of truth for system design
│   ├── planning/                      # 17 design/implementation docs
│   └── research/                      # Agent patterns, database research (8 docs)
├── tests/                             # 10 test areas, 122+ contract tests
│   ├── run_tests.py                   # Deterministic test runner
│   ├── arbitrator/                    # 58 contract tests
│   ├── project-storage/               # 64 contract tests
│   └── harness/                       # Test utilities & fixtures
├── planning/                          # todo.md, cookbook-requests.md
└── pyproject.toml
```

## Key Components

**Multi-agent Pipeline:** Team-lead orchestrates specialists → specialty-teams (worker-verifier loops, max 3 retries) → consulting-teams (cross-cutting review) → specialist-persona (voice translation)

**20 Specialists:** accessibility, claude-code, code-quality, data-persistence, development-process, devops-observability, localization-i18n, networking-api, platform-android, platform-database, platform-ios-apple, platform-web-backend, platform-web-frontend, platform-windows, project-manager, reliability, security, software-architecture, testing-qa, ui-ux-design

**Pluggable Backends:** Arbitrator and project-storage APIs with swappable backends (currently markdown, database in progress)

**Observer System:** SubagentStop hook auto-discovers observer modules for session logging

## Claude Configuration

- **Rules:** Always commit-and-push (non-negotiable), bump versions, DB schema design principles, optimize subagent dispatch, use project directories
- **Hook:** SubagentStop → `python3 observers/dispatch.py` (stenographer + oslog)
- **Skills:** create-specialist, lint-specialist

## Planning & Research Documents

- **architecture.md** — Single source of truth. Read first.
- **17 planning docs** covering: compare-code, lint migration, performance optimization, shared database, single router, specialty-team extraction, unified test strategy, Ralph Loop analysis
- **Database research:** 8 docs on schema design, sync strategies, performance, operations
- **Blocked:** DB schema finalization, specialist script design, database arbitrator backend

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Working tree:** Clean (3 untracked test directories)
- **Recent (2026-04-06):** Deterministic test runner, pytest migration, test coverage for all areas
- **Skill version:** 0.7.0, Plugin version: 0.4.0

## Build & Test Commands

```bash
python3 tests/run_tests.py           # Run all tests (deterministic order)
pytest tests/ -q                     # Run all pytest tests
pytest tests/arbitrator/ -q          # Specific test area
/dev-team interview                  # Launch interview workflow
```

No build step — plugin distributed as-is via marketplace.

## Notes

- Three-repo model: agentic-cookbook (principles), dev-team (plugin), workspace (user data)
- 232 specialty-teams across 20 categories + consulting-teams for cross-cutting concerns
- Commit discipline: must commit and push immediately after every change (rule-enforced)
- Active development, not yet ready for general use
