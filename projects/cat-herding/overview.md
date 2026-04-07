# Cat Herding

## Project Summary

Cat Herding is a personal collection of Claude Code extensions, plugins, skills, and CLI tools designed to augment development workflows. It contains 6 installable plugins, 10 local skills, 2 Python CLIs (site-manager and webinator), research documents, and configuration rules.

## Type & Tech Stack

- **Project Type:** Development tool ecosystem for Claude Code
- **Python 3.11+** — site-manager and webinator CLIs (zero external dependencies, stdlib only)
- **JavaScript/Node.js** — Test harness (Vitest)
- **Bash** — Shell scripts for plugins and status line integration
- **YAML** — Skill/plugin manifests
- **Key tools:** `uv` (Python tool installer), `pytest`, `vitest`

## GitHub URL

`git@github.com:mikefullerton/cat-herding.git`

## Directory Structure

```
cat-herding/
├── .claude/
│   ├── skills/                        # 10 local skills (lint-skill, lint-rule, lint-agent, optimize-rules, etc.)
│   ├── rules/                         # cli-versioning.md, plugin-development.md
│   └── settings.local.json
├── cli/
│   ├── site-manager/                  # v0.3.0 - Multi-site web deployment manager (8 commands)
│   │   ├── pyproject.toml
│   │   ├── src/site_manager/          # cli.py, deploy.py, status.py, manifest.py, verify.py, test.py, claude.py
│   │   └── tests/
│   └── webinator/                     # v0.1.0 - Web infrastructure manager (11+ commands)
│       ├── pyproject.toml
│       ├── src/webinator/             # cli.py, api.py, config.py, domains.py, dns.py, deploy.py, status.py, claude.py
│       └── tests/
├── plugins/                           # 6 Claude Code plugins
│   ├── yolo/                          # v5.0.0 - Per-session auto-approve mode
│   ├── custom-status-line/            # v2.0.0+ - Composable status line pipeline
│   ├── repo-tools/                    # v3.0.0 - Repository cleanup & diagnostics
│   ├── show-project-setup/            # Project dashboard (HTML)
│   ├── site-manager/                  # v1.3.0 - Plugin for site deployment skill
│   └── webinitor/                     # v2.3.0+ - Plugin for infrastructure skill
├── tests/harness/                     # Vitest test infrastructure
├── docs/
│   ├── research/                      # claude-code-plugins.md, cli-packaging.md
│   └── superpowers/
│       ├── plans/                     # 6 implementation plans
│       └── specs/                     # 3 specification docs
├── .claude-plugin/marketplace.json    # Local plugin marketplace manifest
├── CLAUDE.md
└── README.md
```

## Key Files & Components

### CLIs

**site-manager (v0.3.0)** — Scaffold and manage multi-site web projects. Architecture per project: Backend (Hono + Drizzle + PostgreSQL on Railway), Main/Admin/Dashboard (React 19 + Vite + Tailwind 4 on Cloudflare Workers). Install: `uv tool install -e ./cli/site-manager`

**webinator (v0.1.0)** — Web infrastructure management (domains, DNS, deployments) for Cloudflare, Railway, GoDaddy. Install: `uv tool install -e ./cli/webinator`

Both CLIs: Zero external dependencies (stdlib only), shell out to `gh`, `railway`, `wrangler`, `curl`, `docker`.

### Plugins (6 total)

1. **yolo** (v5.0.0) — Per-session auto-approve for tool calls
2. **custom-status-line** (v2.0.0+) — Composable status line with project info, git stats
3. **repo-tools** (v3.0.0) — Recursive repo cleanup, interactive conflict resolution
4. **show-project-setup** — HTML dashboard of rules, skills, plugins, tools
5. **site-manager** (v1.3.0) — Skill plugin for /site-manager command
6. **webinitor** (v2.3.0+) — Skill plugin for /webinitor command

### Local Skills (10 total)

lint-skill, lint-rule, lint-agent, optimize-rules, install-worktree-rule, port-swiftui-to-appkit, install-recommended-tools, install-status-enhancements, uninstall-status-enhancements, show-project-setup

## Claude Configuration

- **Rules:** cli-versioning (bump versions on CLI edits), plugin-development (structure, marketplace, workflow)
- **settings.local.json:** Extensive permission allowlist for git, file ops, tool installation, status line scripts

## Planning & Research Documents

- **claude-code-plugins.md** — Plugin architecture, SKILL.md frontmatter, marketplace registration
- **cli-packaging.md** — Evaluation of CLI packaging approaches; decision: `uv tool install -e` (editable installs)
- **plans/** — 6 implementation plans (site-manager v1, webinitor v2, smoke tests)
- **specs/** — 3 design specifications

## Git History & Current State

- **Branch:** main (up to date with origin/main)
- **Recent activity (2026-04-06):** CLAUDE.md updates, status-line alignment, egg-info cleanup, plan/spec docs, site-manager features
- **Uncommitted changes:** 3 modified files in plugins/custom-status-line and plugins/repo-tools

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

# Load plugins locally
claude --plugin-dir ./plugins/yolo --plugin-dir ./plugins/custom-status-line
```

## Notes

- Owner edits go direct to main; Claude Code sessions use worktree + PR workflow
- Marketplace enables `claude plugin install <name>@cat-herding`
- Python + `uv` chosen over Swift/Go/Rust for CLI simplicity
- Editable installs mean source edits are live (no rebuild)
