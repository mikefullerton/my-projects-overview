# Roadmaps Project Overview

## Project Summary

A comprehensive feature planning and implementation system for Claude Code that transforms ideas into shipped code through structured planning artifacts, automated step-by-step implementation, and real-time progress monitoring. The system handles the full lifecycle from conversational planning through deterministic step execution with live dashboards.

## Type & Tech Stack

**Project Type:** Claude Code skill ecosystem with agent workers, service backend, and Python CLI tools

**Core Technologies:**
- **Python 3** — roadmap_lib, coordinator, dashboard service, CLI tools, comprehensive test suite
- **Bash** — skill scripts, server lifecycle, install/uninstall automation
- **Flask** — RESTful dashboard backend with SQLite database (WAL mode)
- **HTML/CSS/JavaScript** — interactive web UI for live progress tracking
- **GitHub CLI (`gh`)** — issue and PR automation
- **Claude Code CLI (`claude`)** — agent launching and skill execution
- **Git** — worktree management, branching, atomic commits
- **pytest** — 250+ unit tests plus extensive integration test suite

**Key Design:** No heavy external dependencies. Core libraries (roadmap_lib, dashboard_client) use only Python stdlib. Flask is the only significant external requirement.

## GitHub URL

`git@github.com:agentic-cookbook/roadmaps.git`

Hosted at: https://github.com/agentic-cookbook/roadmaps

## Directory Structure

```
roadmaps/
├── .claude/                              # Claude Code configuration
│   ├── rules/                            # Governance rules (versioning, committing, permissions, planning)
│   ├── projects/                         # Memory files from previous sessions
│   └── settings.json                     # Plugin enables, permissions, feature flags
├── .cookbook/                            # Agentic cookbook integration
├── .superpowers/                         # Superpowers plugin cache
├── .pytest_cache/                        # Pytest build artifacts
├── agents/                               # Claude Code worker agents (subprocess-based)
│   └── implement-step-agent.md           # Single-step implementation worker
├── docs/                                 # Planning & design documentation
│   ├── superpowers/
│   │   ├── plans/                        # Feature plans (2026-03-24 through 2026-03-29)
│   │   └── specs/                        # Design specifications
│   ├── index.html                        # Documentation homepage
│   └── claude-cat.png                    # Logo/branding
├── research/                             # Research documents
│   └── 2026-03-30-plugin-vs-install-script.md
├── services/                             # Backend services
│   └── dashboard/                        # Flask progress tracking service
│       ├── app.py                        # Flask application factory
│       ├── db.py                         # SQLite schema, migrations, WAL mode
│       ├── models.py                     # Data access layer (CRUD operations)
│       ├── server.sh                     # Service lifecycle (start/stop/status)
│       ├── api/                          # REST route handlers
│       └── static/                       # HTML/CSS/JavaScript UI
├── skills/                               # Claude Code slash commands
│   ├── plan-roadmap/                     # v17 — Two-phase feature planning
│   ├── plan-bugfix-roadmap/              # v3 — Batch bugfix planning from GitHub issues
│   ├── implement-roadmap/                # v19 — Automated deterministic implementation
│   ├── implement-roadmap-interactively/  # v10 — Interactive step-by-step with reviews
│   ├── list-roadmaps/                    # v5 — Progress bar overview of all roadmaps
│   ├── describe-roadmap/                 # v4 — Detailed roadmap inspection
│   ├── progress-dashboard/               # v17 — Reusable live progress display
│   ├── repair-roadmap/                   # v2 — Fix incomplete roadmaps
│   ├── generate-test-roadmap/            # v1 — Create test features automatically
│   └── import-shared-project/            # v1 — Add shared project references to CLAUDE.md
├── scripts/                              # Shared Python libraries and CLI tools
│   ├── roadmap_lib.py                    # Core library (parsing, discovery, state management)
│   ├── roadmaps.py                       # Cross-repo CLI scanner
│   ├── dashboard_client.py               # REST client for dashboard service
│   ├── migrate-roadmaps.py               # Data migration script
│   └── migrate-to-flat-roadmaps.py       # Archive conversion tool
├── Roadmaps/                             # Completed roadmap artifacts
│   └── [completed feature roadmaps as flat markdown files]
├── tests/                                # Comprehensive test suite
│   ├── unit/                             # 250+ unit tests covering all modules
│   │   ├── test_roadmap_lib.py
│   │   ├── test_dashboard_client.py
│   │   ├── test_coordinator.py
│   │   └── [more test files]
│   └── integration/                      # End-to-end workflow tests
│       ├── happy_path/
│       ├── planning/
│       ├── error_conditions/
│       ├── git_workflow/
│       ├── step_ordering/
│       └── cleanup/
├── CLAUDE.md                             # Project rules, dependencies, conventions
├── README.md                             # Skills documentation and usage guide
├── ROADMAPS-README.md                    # System architecture and design rationale
├── install.sh                            # Bootstrap script for new machines
├── uninstall.sh                          # Remove installed skills and agents
├── .gitignore                            # Standard git ignores
└── LICENSE                               # Open source license
```

## Key Files & Components

### Skill System (Planning & Implementation)

**Planning Workflow:**
- `skills/plan-roadmap/SKILL.md` — v17 main skill file with full discussion/planning phases
- `skills/plan-bugfix-roadmap/SKILL.md` — v3 lightweight variant for existing GitHub issues
- `skills/repair-roadmap/SKILL.md` — v2 for fixing incomplete roadmaps while preserving scope

**Implementation Workflow:**
- `skills/implement-roadmap/SKILL.md` — v19 autonomous coordinator with deterministic Python step selection
- `skills/implement-roadmap-interactively/SKILL.md` — v10 interactive variant with human review gates per step
- `agents/implement-step-agent.md` — v4 single-step worker agent (subprocess-based execution)

**Monitoring & Discovery:**
- `skills/list-roadmaps/SKILL.md` — v5 progress bars and counts for all active roadmaps
- `skills/describe-roadmap/SKILL.md` — v4 detailed inspection with dependency chains
- `skills/progress-dashboard/SKILL.md` — v17 reusable live progress display with pause/resume/stop

**Utilities:**
- `skills/generate-test-roadmap/SKILL.md` — v1 test data generator (20-step cat-herding feature)
- `skills/import-shared-project/SKILL.md` — v1 add external project references to CLAUDE.md

### Core Libraries

**Python:**
- `scripts/roadmap_lib.py` — 21KB library for roadmap discovery, YAML parsing, state management, step counting
- `scripts/dashboard_client.py` — 9KB REST client (urllib stdlib only) for dashboard integration
- `scripts/roadmaps.py` — 51KB cross-repo scanner and CLI tool for unified roadmap view
- `scripts/coordinator.py` — (referenced by implement-roadmap) deterministic step selection engine

**Dashboard Service:**
- `services/dashboard/app.py` — Flask application factory and request handling
- `services/dashboard/db.py` — SQLite schema, migrations, WAL mode for concurrent reads
- `services/dashboard/models.py` — Data access layer (CRUD operations)
- `services/dashboard/api/` — Route handlers for roadmaps, steps, state, history, controls, SSE sync
- `services/dashboard/static/overview.html` — Homepage with progress bars across all roadmaps
- `services/dashboard/static/dashboard.html` — Detail view with steps, issues, PRs, event log, control buttons

### Configuration & Rules

**Claude Code Settings:**
- `.claude/settings.json` — Plugin enables, permissions model, feature flags
- `.claude/rules/skill-versioning-rule.md` — Version numbering enforcement (semver style)
- `.claude/rules/committing-rule.md` — Git workflow (worktrees, draft PRs, atomic commits)
- `.claude/rules/roadmap-permissions-rule.md` — Single upfront permission prompt per session
- `.claude/rules/ROADMAP-PLANNING-RULE.md` — Auto-invocation triggers for /plan-roadmap
- `.claude/rules/cookbook.md` — Agentic cookbook integration rules

**Documentation:**
- `CLAUDE.md` — Project rules, dependencies, review configuration
- `README.md` — Skills guide with changelogs and usage examples
- `ROADMAPS-README.md` — Full system architecture, lifecycle overview, component reference

## Claude Configuration

### Plugin Dependencies (from CLAUDE.md)

**Required (core functionality):**
- `superpowers@claude-plugins-official` — Brainstorming, plan writing, TDD, debugging, worktrees, verification
- `pr-review-toolkit@claude-plugins-official` — Code review, silent failure hunting, test analysis
- `code-review@claude-plugins-official` — Guideline compliance checking
- `code-simplifier@claude-plugins-official` — Post-implementation simplification
- `feature-dev@claude-plugins-official` — Code exploration, architecture analysis, code review
- `security-guidance@claude-plugins-official` — Security vulnerability detection

**Recommended (enhanced workflows):**
- `frontend-design@claude-plugins-official` — Dashboard UI design
- `claude-md-management@claude-plugins-official` — CLAUDE.md file management
- `ralph-loop@claude-plugins-official` — Autonomous iteration loops
- `claude-code-setup@claude-plugins-official` — Project setup assistance
- `skill-creator@claude-plugins-official` — Skill benchmarking
- `document-skills@anthropic-agent-skills` — PDF/DOCX/PPTX/XLSX creation

**Language Support (LSP):**
- `swift-lsp`, `kotlin-lsp`, `typescript-lsp`, `pyright-lsp`, `csharp-lsp`

### Permissions Model

Project uses **allow-list permissions** in settings.json:
- `Read(~/.roadmaps/**)` — Read planning artifacts
- `Write(~/.roadmaps/**)` — Write planning artifacts
- `Edit(~/.roadmaps/**)` — Modify planning artifacts
- `Bash(git:*)` — Full git access (add, commit, push, mv, rev-parse, check-ignore)
- `Bash(gh:*)` — GitHub CLI access
- `Bash(mkdir -p:*)` — Directory creation for planning
- `Bash(head:*)` — File inspection
- `Bash(grep -q:*)` — Pattern matching

### Rules Enforcement

**Skill Versioning Rule:** Every skill/rule MUST have a `version` field in YAML frontmatter. Changes trigger semver bumps. All skills print version on invocation.

**Committing Rule:** All changes flow through: worktree → draft PR (created first) → commits → push after every commit → mark ready → merge → cleanup.

**Permissions Rule:** Single consolidated permission prompt at session start. No mid-session re-prompting.

**Roadmap Planning Rule:** Auto-invoke `/plan-roadmap` on user phrases like "make this into a roadmap" or "convert this plan to a roadmap".

**Cookbook Integration:** Uses agentic-cookbook for guidelines. Run `/configure-cookbook` to manage preferences.

## Planning & Research Documents

**Design Plans:**
- `docs/superpowers/plans/2026-03-24-integration-tests.md` — Integration test design
- `docs/superpowers/plans/2026-03-24-draft-roadmaps.md` — Draft roadmap system
- `docs/superpowers/plans/2026-03-24-plan-roadmap-permission-fixes.md` — Permission handling
- `docs/superpowers/plans/2026-03-23-atomic-batch-pr.md` — Single PR per implementation
- `docs/superpowers/plans/2026-03-29-roadmap-skill-ux-refinements.md` — UX improvements

**Design Specs:**
- `docs/superpowers/specs/2026-03-24-roadmap-description-design.md` — Roadmap detail view
- `docs/superpowers/specs/2026-03-24-atomic-batch-integration-tests-design.md` — Test architecture
- `docs/superpowers/specs/2026-03-24-plan-roadmap-testable-functions-design.md` — Testability
- `docs/superpowers/specs/2026-03-25-playwright-dashboard-tests-design.md` — Dashboard testing
- `docs/superpowers/specs/2026-03-23-test-suite-design.md` — Overall test strategy
- `docs/superpowers/specs/2026-03-29-roadmap-skill-ux-refinements-design.md` — UX refinements

**Research:**
- `research/2026-03-30-plugin-vs-install-script.md` — Technology choice analysis

## Git History & Current State

### Recent Activity (Last 30 Commits)

Latest commits show continuous feature development on roadmap planning and implementation systems:
- `a9f9c8f` (2026-04-06) docs: update CLAUDE.md, README, and docs index
- `2b98be2` (2026-04-06) chore: standardize worktree directory to .claude/worktrees/
- `4e19c1e` (2026-03-30) chore: install agentic cookbook (rule, manifest, preferences)
- `946ae74` (2026-03-30) Merge pull request #51 from mikefullerton/feature/progress-format
- `c712498` (2026-03-30) feat(implement-roadmap): standardize progress output format
- `dc658d7` (2026-03-30) chore: init progress format branch
- `0fb3e31` (2026-03-27) Merge pull request #49 from mikefullerton/feature/idempotent-resume
- `c5325d0` (2026-03-25) feat(coordinator): add resume command for interrupted implementations
- `4ccdf40` (2026-03-23) Merge pull request #48 from mikefullerton/feature/guideline-compliance-review
- `d86b428` (2026-03-23) feat(implement-step-agent): add guideline compliance check to final review
- `cd437c0` (2026-03-23) Merge pull request #47 from mikefullerton/feature/design-decisions
- `e0f9fd3` (2026-03-21) feat(implement-step-agent): add design decision audit trail
- `b5784c7` (2026-03-18) Merge pull request #46 from mikefullerton/feature/verification-summary
- `b29552e` (2026-03-18) feat(implement-step-agent): add verification summary PR comment
- `ffd11bc` (2026-03-17) Merge pull request #45 from mikefullerton/feature/plan-deviation
- `e606755` (2026-03-17) feat(implement-step-agent): add plan deviation handling

**Pattern:** Feature development follows consistent branching strategy (`feature/*` naming), with PRs merged to main on completion.

### Current State

**Branch:** main

**Status:** 1 commit ahead of origin/main (unpushed)

**Working Directory:** Clean staged state with uncommitted changes in test files and migration scripts:
- `scripts/migrate-roadmaps.py` — modified (data migration script)
- `tests/integration/conftest.py` — modified (test configuration)
- `tests/integration/cleanup/test_definition.py` — modified
- `tests/integration/error_conditions/test_definition.py` — modified
- `tests/integration/git_workflow/test_definition.py` — modified
- `tests/integration/happy_path/test_definition.py` — modified
- `tests/integration/planning/conftest.py` — modified
- `tests/integration/planning/test_definition.py` — modified
- `tests/integration/step_ordering/test_definition.py` — modified
- `tests/integration/helpers.py` — modified

**Untracked:** `misc test files?/` directory (likely test artifacts)

## Build & Test Commands

### Test Execution

```bash
# Run full test suite
pytest

# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/

# Run specific test file
pytest tests/unit/test_roadmap_lib.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=scripts --cov=services
```

**Test Organization:**
- **Unit tests** (`tests/unit/`) — 250+ tests covering roadmap_lib parsing, dashboard client, coordinator logic, API endpoints, database operations, data models
- **Integration tests** (`tests/integration/`) — End-to-end workflows including happy path, planning phase, step ordering, error conditions, git workflows, cleanup operations

### Installation & Deployment

```bash
# Install all skills and agents to ~/.claude/
bash install.sh

# Remove all installed skills and agents
bash uninstall.sh

# Start dashboard service
bash services/dashboard/server.sh start

# Check service status
bash services/dashboard/server.sh status

# Stop dashboard service
bash services/dashboard/server.sh stop
```

**Install Behavior:** Prompts for symlink vs copy method (important for WSL). Auto-detects Windows/WSL and uses apt for tool installation.

### Running Skills

All skills are invoked via Claude Code CLI:

```bash
# Plan a new feature
/plan-roadmap

# Plan bugfixes from existing GitHub issues
/plan-bugfix-roadmap 17 18 19 20
/plan-bugfix-roadmap all

# Implement a planned roadmap
/implement-roadmap
/implement-roadmap MyFeature

# Implement interactively with review gates
/implement-roadmap-interactively

# Inspect roadmaps
/list-roadmaps
/describe-roadmap
/describe-roadmap DashboardBugfixes

# Show live progress dashboard
/progress-dashboard MyFeature

# Generate test roadmap for demos
/generate-test-roadmap

# Repair an incomplete roadmap
/repair-roadmap
/repair-roadmap FeatureName

# Add shared project reference
/import-shared-project litterbox
/import-shared-project git@github.com:user/repo.git

# Configure cookbook integration
/configure-cookbook
/cookbook-start
/cookbook-next
```

## Notes

### Architecture Highlights

1. **Deterministic Step Selection:** The `/implement-roadmap` coordinator uses a Python regex parser (not LLM judgment) to select the next incomplete step. This prevents skipping, repeating, or wandering.

2. **File-Based Source of Truth:** All state lives in Markdown files with YAML frontmatter (in `~/.roadmaps/` during lifecycle, then copied to `Roadmaps/` on completion). Git history is the audit trail.

3. **Decoupled Dashboard Service:** The Flask dashboard knows nothing about git or roadmaps — it's a generic progress tracker. Skills push updates via REST API. This separation allows concurrent session isolation.

4. **One Step = One PR:** Each implementation step produces a separate worktree, PR, review, and merge. All PRs are created upfront as drafts, then marked ready when that step completes. A final atomic PR wraps all changes.

5. **Zero External Dependencies:** Core libraries (`roadmap_lib`, `dashboard_client`) use only Python stdlib. Flask is the only significant external requirement.

### Project Conventions

- **Versions** are single integers in skill YAML frontmatter, bumped as the first action for any change
- **Every change** must have tests
- **Every bugfix** must have a regression test
- **Dashboard HTML** pages have version numbers, incremented on every commit
- **Never** modify dashboard HTML while a real roadmap is running
- **Never** directly modify roadmap state — build tools for it
- **Commit and push immediately** after making changes

### Agentic Cookbook Integration

The project uses https://github.com/agentic-cookbook/cookbook for coding guidelines and best practices. Run `/configure-cookbook` to manage preferences. Recipe prompts and contribution prompts are enabled by default, with committing included.

### Performance & Scaling

- **SQLite with WAL mode** — Handles concurrent reads without locking
- **Lazy dashboard polling** — Updates every 3 seconds, slows down when complete
- **Regex-based parsing** — Deterministic step selection (no LLM latency)
- **Worktree isolation** — Each step runs in its own git worktree (true parallelization potential)
- **Stateless agents** — Single-step workers can be reused or parallelized

### Known Limitations & Future Directions

Based on research document `2026-03-30-plugin-vs-install-script.md`, the project chose install scripts over Claude Code plugin marketplace to retain full control over skill versioning and distribution. This maintains the tight feedback loop with cookbook integration.

Current implementation focuses on sequential step execution within a single shared worktree. Future work could explore per-step worktrees with true parallelization, though this would require architectural changes to the coordinator and PR merge strategy.

### Development Workflow Example

The project itself uses the `/plan-roadmap` + `/implement-roadmap` workflow for its own feature development, as evidenced by the feature branches in git history. Each feature goes through:
1. Planning phase with discussion and artifacts
2. Implementation phase with step-by-step PRs
3. Integration with agentic cookbook guidelines
4. Documentation updates post-completion

This dogfooding ensures the system is battle-tested and responsive to real-world needs.

---

## Quick Start References

**For new users:**
- Read `README.md` for skill documentation and changelogs
- Read `ROADMAPS-README.md` for system architecture overview
- Run `bash install.sh` to bootstrap skills and agents
- Run `/plan-roadmap` to begin your first feature

**For maintainers:**
- Check `.claude/rules/` for governance rules (versioning, committing, permissions)
- Run `pytest` to validate changes before committing
- Follow the committing rule: worktree → draft PR → commits → mark ready → merge
- Update skill versions in YAML frontmatter for every change
- Sync with agentic-cookbook via `/configure-cookbook` and `/cookbook-start`

**For architects:**
- Review `ROADMAPS-README.md` for component reference and design rationale
- Study `services/dashboard/` for REST API and web UI patterns
- Review `scripts/roadmap_lib.py` for core state management and parsing logic
- Check `tests/integration/` for end-to-end workflow examples
