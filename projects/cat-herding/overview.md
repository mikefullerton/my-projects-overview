# Cat Herding

## Project Summary

Cat Herding is a personal collection of Claude Code extensions, plugins, skills, and CLI tools designed to augment development workflows. It contains 6 installable plugins, 11 local skills, 2 Python CLIs (site-manager and webinator), research documents, and configuration rules. Functions as a local plugin marketplace for Claude Code.

## Type & Tech Stack

- **Project Type:** Development tool ecosystem for Claude Code
- **Python 3.11+** -- site-manager and webinator CLIs (zero external dependencies, stdlib only)
- **JavaScript/Node.js** -- Test harness (Vitest)
- **Bash** -- Shell scripts for plugins and status line integration
- **YAML** -- Skill/plugin manifests
- **Key tools:** `uv` (Python tool installer), `pytest`, `vitest`

## GitHub URL

`git@github.com:mikefullerton/cat-herding.git`

## Directory Structure

```
cat-herding/
├── .claude/
│   ├── skills/                        # 11 local skills
│   │   ├── lint-skill/                # Lint skills against best practices
│   │   ├── lint-rule/                 # Lint rules against best practices
│   │   ├── lint-agent/                # Lint agents against best practices
│   │   ├── optimize-rules/            # Consolidate rule files
│   │   ├── install-worktree-rule/     # Install worktree/PR git workflow
│   │   ├── port-swiftui-to-appkit/    # Plan SwiftUI-to-AppKit conversions
│   │   ├── install-recommended-tools/ # Install developer tools
│   │   ├── install-status-enhancements/  # Install status line pipeline
│   │   ├── uninstall-status-enhancements/
│   │   └── show-project-setup/        # Show project dashboard
│   ├── rules/
│   │   ├── cli-versioning.md          # Auto-bump CLI versions on source changes
│   │   └── plugin-development.md      # Plugin dev workflow guide
│   └── settings.local.json
├── .claude-plugin/
│   └── marketplace.json               # Plugin registry (6 plugins)
├── .superpowers/                      # Superpowers integration
├── cli/
│   ├── site-manager/                  # v0.3.0 - Multi-site web deployment manager (8 commands)
│   │   ├── pyproject.toml
│   │   ├── src/site_manager/
│   │   └── tests/
│   └── webinator/                     # v0.1.0 - Web infrastructure manager (11+ commands)
│       ├── pyproject.toml
│       ├── src/webinator/
│       └── tests/
├── plugins/                           # 6 Claude Code plugins
│   ├── yolo/                          # Per-session auto-approve mode
│   ├── custom-status-line/            # Composable status line pipeline
│   ├── repo-tools/                    # Repository cleanup & diagnostics
│   ├── show-project-setup/            # Project dashboard (HTML)
│   ├── site-manager/                  # Plugin for site deployment skill
│   └── webinitor/                     # Plugin for infrastructure skill
├── tests/                             # Test infrastructure
├── docs/
│   ├── research/                      # cli-packaging.md
│   └── superpowers/
│       ├── plans/                     # Implementation plans
│       └── specs/                     # Design specifications
├── research/
│   ├── claude-code-plugins.md         # Plugin architecture research
│   └── claude-code-usage-limits.md
├── skills/
│   └── quick-ref/                     # Quick reference skill
├── CLAUDE.md
└── README.md
```

## Key Files & Components

### CLIs

**site-manager (v0.3.0)** -- Scaffold and manage multi-site web projects. Architecture per project: Backend (Hono + Drizzle + PostgreSQL on Railway), Main/Admin/Dashboard (React 19 + Vite + Tailwind 4 on Cloudflare Workers). Install: `uv tool install -e ./cli/site-manager`

**webinator (v0.1.0)** -- Web infrastructure management (domains, DNS, deployments) for Cloudflare, Railway, GoDaddy. Install: `uv tool install -e ./cli/webinator`

Both CLIs: Zero external dependencies (stdlib only), shell out to `gh`, `railway`, `wrangler`, `curl`, `docker`.

### Plugins (6 total)

1. **yolo** -- Per-session auto-approve for tool calls
2. **custom-status-line** -- Composable status line with project info, git stats
3. **repo-tools** -- Recursive repo cleanup, interactive conflict resolution
4. **show-project-setup** -- HTML dashboard of rules, skills, plugins, tools
5. **site-manager** -- Skill plugin for /site-manager command
6. **webinitor** -- Skill plugin for /webinitor command

### Local Skills (11 total)

lint-skill, lint-rule, lint-agent, optimize-rules, install-worktree-rule, port-swiftui-to-appkit, install-recommended-tools, install-status-enhancements, uninstall-status-enhancements, show-project-setup

### Distributable Rules

| Rule | Purpose |
|------|---------|
| `always-use-worktrees-and-prs.md` | Enforce worktree + PR git workflow |
| `authoring-ground-rules.md` | Foundation rule for all authoring |
| `skill-authoring.md` | Best practices for writing skills |
| `skill-versioning.md` | Semver versioning protocol for skills/rules |
| `extension-authoring.md` | Best practices for writing extensions |
| `permissions.md` | Permission management guidelines |

## Claude Configuration

- **CLAUDE.md** -- Skills table (11 skills), distributable rules list (6 rules), git workflow instructions
- **Rules:** `cli-versioning.md` (bump versions on CLI edits), `plugin-development.md` (structure, marketplace, workflow)
- **settings.local.json** -- Extensive permission allowlist for git, file ops, tool installation, status line scripts

## Planning & Research Documents

- **`research/claude-code-plugins.md`** -- Plugin architecture, SKILL.md frontmatter, marketplace registration
- **`research/claude-code-usage-limits.md`** -- Claude Code usage limits research
- **`docs/research/cli-packaging.md`** -- Evaluation of CLI packaging approaches; decision: `uv tool install -e` (editable installs)
- **`docs/superpowers/plans/`** -- Implementation plans (site-manager v1, webinitor v2, smoke tests, site-manager deploy fixes)
- **`docs/superpowers/specs/`** -- Design specifications (webinitor v2, site-manager planning, smoke tests, deploy fix)

## Git History & Current State

- **Branch:** main
- **Recent activity (2026-04-06):** CLAUDE.md updates, status-line alignment, egg-info cleanup, plan/spec docs, site-manager features
- **Modified files (uncommitted):** 3 modified in plugins/custom-status-line and plugins/repo-tools
- **Untracked files:** 2 new plan/spec docs, repo-tools references directory

Recent commits:
```
bb830ca docs: update CLAUDE.md skills table, repo-tools v2.0.0
a1a0461 feat(status-line): align columns, dynamic widths, YOLO in model col
ef97e5c chore: remove tracked egg-info directories (now gitignored)
72203bd docs: update plans, specs, and plugin development rule
cb9e8be feat(site-manager): project types, auth service, go-live, migrate
f15c9f2 feat(site-manager): add verify/repair system with .site directory
4b28567 feat: CLI packaging, versioning, and test suites
48a80e8 chore: update .gitignore for Python artifacts and tool directories
63b2d67 refactor: update plugins to delegate deterministic commands to CLIs
68dc0b3 feat: add site-manager CLI for macOS
```

## Build & Test Commands

```bash
# Install CLIs
uv tool install -e ./cli/site-manager
uv tool install -e ./cli/webinator

# Test CLIs
cd cli/site-manager && python3 -m pytest tests/
cd cli/webinator && python3 -m pytest tests/

# JS test harness
cd tests/harness && npm test

# Load plugins locally (instant feedback, no install)
claude --plugin-dir ./plugins/yolo --plugin-dir ./plugins/custom-status-line

# Install via marketplace
claude plugin marketplace add ~/projects/active/cat-herding
claude plugin install yolo@cat-herding

# Update installed plugins after edits
claude plugin update yolo@cat-herding
```

## Notes

- Owner edits go direct to main; Claude Code sessions use worktree + PR workflow (`.claude/worktrees/`)
- Marketplace enables `claude plugin install <name>@cat-herding`
- Python + `uv` chosen over Swift/Go/Rust for CLI simplicity
- Editable installs mean source edits are live (no rebuild)
- Active development on site-manager and webinitor plugins/CLIs for infrastructure management
