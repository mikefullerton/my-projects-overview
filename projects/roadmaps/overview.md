# Roadmaps

## Project Summary

A comprehensive feature planning and implementation system for Claude Code that transforms ideas into shipped code through structured planning artifacts, automated step-by-step implementation, and real-time progress monitoring. Part of the agentic-cookbook ecosystem, providing reusable skills for feature planning, bugfix batching, implementation automation, and live dashboards.

## Type & Tech Stack

**Project Type:** Claude Code skill ecosystem with agent workers, dashboard backend, and Python CLI tools

**Core Technologies:**
- **Python 3** — planning libraries, coordinator, dashboard service, CLI tools, 250+ test suite
- **Bash** — skill scripts, server lifecycle, install/uninstall automation
- **Flask** — RESTful dashboard backend with SQLite (WAL mode)
- **HTML/CSS/JavaScript** — interactive live progress tracking UI
- **GitHub CLI (`gh`)** — issue and PR automation
- **Claude Code CLI (`claude`)** — agent launching and skill execution
- **Git** — worktree management, branching, atomic commits
- **pytest** — comprehensive unit and integration test suite

**Design Principle:** Zero heavy external dependencies. Core libraries use only Python stdlib.

## GitHub URL

`git@github.com:agentic-cookbook/roadmaps.git`

https://github.com/agentic-cookbook/roadmaps

## Directory Structure

```
roadmaps/
├── .claude/                           # Claude Code configuration
│   ├── rules/                         # Governance (versioning, committing, planning)
│   ├── projects/                      # Session memory files
│   └── settings.json                  # Plugin config & permissions
├── .cookbook/                         # Agentic cookbook integration
├── agents/                            # Worker agents
│   └── implement-step-agent.md        # Single-step implementation
├── docs/                              # Planning & design documents
│   ├── superpowers/plans/             # Feature plans
│   └── superpowers/specs/             # Design specifications
├── research/                          # Research documents
├── services/dashboard/                # Flask progress tracking service
│   ├── app.py, db.py, models.py
│   ├── api/                           # REST routes
│   └── static/                        # HTML/CSS/JavaScript UI
├── skills/                            # Claude Code slash commands
│   ├── plan-roadmap/                  # v17 — Two-phase feature planning
│   ├── plan-bugfix-roadmap/           # v3 — Batch bugfix planning
│   ├── implement-roadmap/             # v19 — Autonomous implementation
│   ├── implement-roadmap-interactively/ # v10 — Interactive with reviews
│   ├── list-roadmaps/                 # v5 — Progress overview
│   ├── describe-roadmap/              # v4 — Detailed inspection
│   ├── progress-dashboard/            # v17 — Live display
│   └── [other utility skills]
├── scripts/                           # Python libraries and CLI tools
│   ├── roadmap_lib.py                 # Core (parsing, discovery, state)
│   ├── dashboard_client.py            # REST client
│   ├── roadmaps.py                    # Cross-repo CLI scanner
│   └── coordinator.py                 # Step selection engine
├── Roadmaps/                          # Completed roadmap artifacts
├── tests/                             # Unit & integration tests (250+)
├── CLAUDE.md                          # Project rules and dependencies
├── README.md                          # Skills documentation
├── ROADMAPS-README.md                 # System architecture
├── install.sh                         # Bootstrap installation
└── uninstall.sh                       # Cleanup removal
```

## Key Files & Components

**Planning Skills:**
- `skills/plan-roadmap/SKILL.md` — Main two-phase planning (discussion → artifacts)
- `skills/plan-bugfix-roadmap/SKILL.md` — Lightweight variant for GitHub issues

**Implementation Skills:**
- `skills/implement-roadmap/SKILL.md` — Deterministic autonomous implementation
- `skills/implement-roadmap-interactively/SKILL.md` — Interactive with review gates
- `agents/implement-step-agent.md` — Single-step worker agent

**Monitoring Skills:**
- `skills/list-roadmaps/SKILL.md` — Progress overview with bars
- `skills/describe-roadmap/SKILL.md` — Detailed inspection
- `skills/progress-dashboard/SKILL.md` — Reusable live progress display

**Core Libraries:**
- `scripts/roadmap_lib.py` — YAML parsing, state management, discovery
- `scripts/dashboard_client.py` — REST client for progress service
- `scripts/coordinator.py` — Deterministic step selection (regex-based)

**Dashboard Service:**
- `services/dashboard/app.py` — Flask application
- `services/dashboard/db.py` — SQLite schema with WAL mode
- `services/dashboard/api/` — REST endpoints
- `services/dashboard/static/` — HTML/CSS/JavaScript UI

**Configuration:**
- `.claude/rules/` — Governance (versioning, committing, planning)
- `.claude/settings.json` — Plugin enables and permissions model

## Claude Configuration

**Required Plugins:**
- `superpowers`, `pr-review-toolkit`, `code-review`, `code-simplifier`, `feature-dev`, `security-guidance`

**Recommended Plugins:**
- `frontend-design`, `claude-md-management`, `ralph-loop`, `skill-creator`, `document-skills`

**Language Support:**
- `swift-lsp`, `kotlin-lsp`, `typescript-lsp`, `pyright-lsp`, `csharp-lsp`

**Permissions Model:**
- Allow-list model in settings.json (Read/Write ~/.roadmaps/**, Bash git/gh/mkdir)

**Governance:**
- Skill Versioning Rule — single integer bumped per change
- Committing Rule — worktree → draft PR → commits → mark ready → merge
- Permissions Rule — single consolidated prompt at session start
- Cookbook Integration — via `/configure-cookbook`

## Planning & Research Documents

**Plans:**
- `docs/superpowers/plans/2026-03-24-integration-tests.md`
- `docs/superpowers/plans/2026-03-24-draft-roadmaps.md`
- `docs/superpowers/plans/2026-03-29-roadmap-skill-ux-refinements.md`

**Specs:**
- `docs/superpowers/specs/2026-03-24-roadmap-description-design.md`
- `docs/superpowers/specs/2026-03-25-playwright-dashboard-tests-design.md`

**Research:**
- `research/2026-03-30-plugin-vs-install-script.md` — Technology choice analysis

## Git History & Current State

**Recent Activity:**
- `a19690c` fix: replace stale references with Roadmaps
- `b0c139c` docs: add standardized project description
- `bf7eac0` fix: confine test harness to ~/projects/tests/
- `a9f9c8f` docs: update CLAUDE.md, README, docs index
- `2b98be2` chore: standardize worktree directory
- `4e19c1e` chore: install agentic cookbook
- `946ae74` Merge pull request #51 (progress format)

**Pattern:** Feature development with `feature/*` branches, PRs to main, consistent versioning.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree, up to date with origin/main

## Build & Test Commands

**Run Tests:**
```bash
pytest                               # Full suite
pytest tests/unit/                   # Unit tests only
pytest tests/integration/            # Integration tests only
pytest -v                            # Verbose
pytest --cov=scripts --cov=services  # With coverage
```

**Installation:**
```bash
bash install.sh      # Install skills and agents
bash uninstall.sh    # Remove all
```

**Dashboard Service:**
```bash
bash services/dashboard/server.sh start   # Start service
bash services/dashboard/server.sh status  # Check status
bash services/dashboard/server.sh stop    # Stop service
```

**Run Skills:**
```bash
/plan-roadmap                    # Plan new feature
/plan-bugfix-roadmap 17 18 19   # Plan bugfixes
/implement-roadmap               # Autonomous implementation
/implement-roadmap-interactively # Interactive with reviews
/list-roadmaps                   # Progress overview
/describe-roadmap                # Detailed inspection
/progress-dashboard MyFeature    # Live progress
/repair-roadmap                  # Fix incomplete roadmaps
```

## Notes

**Architecture Highlights:**

1. **Deterministic Step Selection** — Regex-based next-step selection, no LLM wandering
2. **File-Based Source of Truth** — YAML markdown files in ~/.roadmaps/, git history is audit trail
3. **Decoupled Dashboard** — Flask knows nothing about git/roadmaps, generic progress tracker
4. **One Step = One PR** — Each step gets own worktree, PR, review, merge
5. **Zero Heavy Dependencies** — Core libs use Python stdlib only

**Project Conventions:**

- Versions are single integers in skill YAML, bumped on every change
- Every change must have tests; every bugfix must have regression test
- Dashboard HTML pages have version numbers, incremented on commits
- Never modify dashboard while roadmap running
- Never directly modify roadmap state — build tools
- Commit and push immediately after changes

**Key Integration:**

- Uses agentic-cookbook for coding guidelines (run `/configure-cookbook`)
- Install scripts chosen over plugin marketplace for version control
- Sequential step execution in shared worktree (future: per-step parallelization)

**Test Coverage:**

- 250+ unit tests covering roadmap_lib, dashboard client, coordinator, API, database
- Integration tests for happy path, planning, step ordering, error conditions, git workflows

**Development Workflow:**

The project dogfoods its own system — features planned with `/plan-roadmap` and implemented with `/implement-roadmap`, providing continuous real-world validation.
