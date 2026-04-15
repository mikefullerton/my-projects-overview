# Agenticdevteam

## Project Summary

A Claude Code plugin for multi-agent product discovery, analysis, and project building. Distributed via the agentic-cookbook marketplace, it orchestrates specialized teams and expertise through a pipeline-based workflow system.

## Type & Tech Stack

- **Type**: Claude Code Plugin / Multi-Agent System
- **Language**: Python 3.10+
- **Key Components**: Multi-agent pipeline, specialist system, workflow orchestration
- **Test Framework**: pytest with unit, functional, and stress tests
- **Database**: Shared state management via scripts/db/
- **Deployment**: Distributed via agentic-cookbook marketplace

## GitHub URL

https://github.com/agentic-cookbook/agenticdevteam

## Directory Structure

```
agenticdevteam/
├── plugins/dev-team/              # Main plugin (self-enclosed)
│   ├── agents/                    # 20+ agent definitions
│   ├── specialists/               # 22 domain/platform specialists
│   ├── specialty-teams/           # 230+ worker-verifier team configs
│   ├── consulting-teams/          # Cross-cutting concern reviewers
│   ├── scripts/                   # Pipeline scripts, observers, DB init
│   ├── services/                  # Shared services
│   ├── skills/                    # Claude Code skills
│   └── .claude-plugin/            # Plugin metadata
├── teams/                         # Team definitions (devteam, projectteam, puppynamingteam)
├── docs/                          # Architecture, planning, research
│   ├── architecture.md            # Single source of truth for system design
│   ├── planning/                  # 10+ planning documents
│   ├── research/                  # Research notes (graphify, personas, patterns)
│   └── superpowers/               # Superpowers integration guides
├── testing/                       # Contract tests & test harness
│   ├── unit/                      # Unit tests
│   └── functional/                # Functional tests
├── tests/                         # pytest cache
├── .claude/                       # Local Claude Code config
│   ├── CLAUDE.md                  # Project overview & rules
│   ├── settings.json              # Hooks for observers & graphify
│   ├── rules/                     # 5 Claude Code rules
│   ├── skills/                    # Local project skills
│   └── worktrees/                 # Worktree management
├── graphify-out/                  # Knowledge graph (from graphify analysis)
├── deprecated/                    # Archived components
├── site/                          # Static assets (og.png)
├── index.html                     # Landing page (hosted at devteam.agentic-cookbook.com)
├── README.md                      # Quick start guide
├── pyproject.toml                 # Python config & test settings
└── CNAME                          # Custom domain (devteam.agentic-cookbook.com)
```

## Key Files & Components

- **plugins/dev-team/agents/**: 20+ agent definitions including specialist-analyst, code-generator, recipe-writer, artifact-reviewer, build-runner, smoke-tester
- **plugins/dev-team/specialists/**: 22 specialists organized by domain (accessibility, security, code-quality, testing-qa, etc.), platform (web, iOS, Android, Windows, database), and project-management
- **plugins/dev-team/specialty-teams/**: 230+ standalone worker-verifier team configs for cookbook artifact analysis
- **plugins/dev-team/scripts/**: Pipeline orchestration (run_specialty_teams.py, observers/dispatch.py, db_init.py)
- **docs/architecture.md**: 13KB comprehensive system design, terminology, component descriptions, data flow
- **docs/planning/**: 11 planning documents covering database design, system architecture v2, conductor architecture, comparison design, test strategy
- **docs/research/**: Research on agent patterns, conversational patterns, persona design, graphify integration, Claude cost optimization
- **.claude/CLAUDE.md**: Project overview with local testing instructions and graphify integration rules
- **pyproject.toml**: Python >=3.10, pytest config with unit/functional/stress test markers

## Claude Configuration

- **Local Testing**: `/dev-team interview` in repo root initializes ~/.agentic-cookbook/dev-team/config.json
- **Hooks (settings.json)**:
  - `SubagentStop`: Runs dispatch.py to observe and track subagent activity
  - `PreToolUse`: Injects graphify knowledge graph context for Glob/Grep searches
- **Rules** (5 files in .claude/rules/):
  - always-commit-and-push.md: Automated version control
  - bump-versions.md: Version management
  - db-schema-design.md: Database design patterns
  - optimize-subagent-dispatch.md: Subagent optimization
  - use-project-directories.md: Project directory conventions
- **Skills** (.claude/skills/): create-specialist, lint-specialist custom skills

## Planning & Research Documents

- **docs/planning/**: todo.md, design-spec.md, build-history.md, 9 dated planning docs (database, architecture, conductor, comparison, extraction, optimization, testing)
- **docs/research/**: agent-patterns.md, conversational-patterns.md, persona-design.md, graphify.md, claude-cost-optimization-research.md, database/ subdirectory

## Git History & Current State

- **Remote**: origin = git@github.com:agentic-cookbook/agenticdevteam.git
- **Current Branch**: main (up-to-date with origin/main)
- **Status**: Clean (no uncommitted changes)
- **Last 10 Commits**:
  1. ac9bb2a - docs(research): expand graphify research with landscape, meta-graph design, and devteam integration
  2. 80f5bd3 - docs(research): add graphify knowledge graph research notes
  3. 5f06d6c - chore: merge graphify section into .claude/CLAUDE.md, remove root CLAUDE.md
  4. c16adb1 - chore: install graphify claude hook and CLAUDE.md
  5. 15b384d - chore: gitignore graphify-out/ generated output
  6. 9650950 - fix: separate team.md (description) from index.md (table of contents)
  7. a74d528 - feat: add index.md to every directory in teams/
  8. 7e25c80 - fix: rename specialty-teams to specialities in all devteam specialist manifests
  9. 3d78ca5 - feat: create /teams with devteam, projectteam, puppynamingteam
  10. 0081ac7 - Move research-paper out to technical-writings repo

## Build & Test Commands

- **Local Testing**: `cd` into repo root, run `/dev-team interview`
- **Pytest Configuration** (pyproject.toml):
  - Test paths: testing/unit/tests, testing/unit/harness, testing/functional/tests
  - Default run: `pytest` (excludes stress tests)
  - Stress tests: `pytest -m stress` (opt-in)
  - Markers: unit, functional, stress

## Notes

- **Custom Domain**: CNAME points to devteam.agentic-cookbook.com; index.html is a SPA landing page with metadata
- **Knowledge Graph**: graphify-out/ contains knowledge graph for the codebase; read graphify-out/GRAPH_REPORT.md for god nodes before searching
- **Status**: Under active development (not ready for general use yet per README)
- **Related Plugins**: name-a-puppy, team-pipeline also in plugins/
- **Workspace Data**: Config stored in ~/.agentic-cookbook/dev-team/config.json; workspace_repo, cookbook_repo, authorized_repos managed per-user
