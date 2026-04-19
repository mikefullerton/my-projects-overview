# Cat Herding

## Project Summary

Personal collection of Claude Code skills, plugins, hooks, and workflow extensions. Cat Herding provides personal workflow extensions for Claude Code: YOLO mode for auto-approving tool calls, a composable status line pipeline for terminal progress tracking, internal linting and authoring skills, and configuration rules for development workflows.

## Type & Tech Stack

**Type:** Claude Code Skills & Extensions / Workflow Tools

**Tech Stack:**
- **Language:** Python 3.11+, Bash/Shell
- **Runtime:** Claude Code (skills invoked via slash commands)
- **Testing:** pytest
- **Plugins:** Claude Code plugins for custom functionality

## GitHub URL

https://github.com/mikefullerton/catherding

## Directory Structure

```
.
├── .claude/              # Claude Code configuration
│   ├── CLAUDE.md
│   ├── settings.local.json
│   ├── rules/            # Configuration rules
│   │   ├── (rule files)
│   │   └── (workflow specifications)
│   ├── skills/           # Internal skills
│   │   ├── lint-skill/
│   │   ├── lint-rule/
│   │   ├── lint-agent/
│   │   ├── optimize-rules/
│   │   ├── install-worktree-rule/
│   │   └── (more skills)
│   └── worktrees/        # Git worktree management
├── .claude-plugin/       # Claude Code plugin definition
│   └── marketplace.json
├── .pytest_cache/        # pytest cache
├── .wrangler/            # Wrangler configuration (Cloudflare Workers)
├── .superpowers/         # Superpowers plugin configuration
├── docs/
│   ├── research/
│   │   └── claude-code-usage-limits.md
│   ├── project/
│   │   └── description.md
│   └── superpowers/
│       ├── plans/        # Implementation plans
│       │   └── 2026-04-07-status-line-python-conversion.md
│       └── specs/        # Design specifications
│           └── 2026-04-07-status-line-python-conversion-design.md
├── skills/               # 2 distributable skills
│   ├── yolo/             # Toggle YOLO mode (auto-approve tool calls)
│   │   └── SKILL.md
│   └── custom-status-line/  # Composable status line pipeline
│       ├── SKILL.md
│       └── (supporting files)
├── install.sh            # Installation script
├── uninstall.sh          # Uninstallation script
├── README.md
└── .gitignore
```

## Key Files & Components

**Distributable Skills:**
- `skills/yolo/SKILL.md` — Toggle YOLO mode for auto-approving tool calls
- `skills/custom-status-line/SKILL.md` — Composable status line pipeline for terminal progress

**Internal Skills (in .claude/skills/):**
- `lint-skill/` — Linting for skill definitions
- `lint-rule/` — Linting for rule definitions
- `lint-agent/` — Agent linting utilities
- `optimize-rules/` — Rule optimization helpers
- `install-worktree-rule/` — Worktree management

**Rules (in .claude/rules/):**
- CLI versioning rules
- Plugin development rules
- Worktree branch cleanup rules
- Workflow standards

**Configuration:**
- `.claude/CLAUDE.md` — Project overview and git workflow documentation
- `.claude/settings.local.json` — Local Claude Code settings with permissions
- `.claude-plugin/marketplace.json` — Plugin marketplace definition

**Documentation:**
- `docs/research/claude-code-usage-limits.md` — Research on Claude Code constraints
- `docs/superpowers/plans/` — Implementation plans for features
- `docs/superpowers/specs/` — Design specifications

## Claude Configuration

**Location:** `.claude/CLAUDE.md` and `.claude/settings.local.json`

**CLAUDE.md:**
- Project overview as personal Claude Code extensions collection
- Repository structure breakdown (skills, .claude/skills/, rules)
- Skill definitions and purposes
- Git workflow documentation (must use worktrees for all branches)

**settings.local.json:**
- Extensive permissions configuration
- Allows: git operations (add, commit, push), cp, mkdir, status line updates
- Permissions for integrating with ~/.claude-status-line/ progress tracking

## Planning & Research Documents

**Research:**
- `docs/research/claude-code-usage-limits.md` — Research on Claude Code usage constraints and optimization

**Planning & Design (Superpowers):**
- `docs/superpowers/plans/2026-04-07-status-line-python-conversion.md` — Plan for status line conversion to Python
- `docs/superpowers/specs/2026-04-07-status-line-python-conversion-design.md` — Design spec for conversion

**Project Documentation:**
- `docs/project/description.md` — Project purpose and features

## Git History & Current State

**Current Branch:** main

**Remote:** git@github.com:mikefullerton/catherding.git

**Recent Commits:**
- `bd20fa8` — fix(status-line): add col0 prefix to session line for column alignment (#31)
- `03c0ace` — Merge pull request #30 from mikefullerton/worktree-more-status-line
- `18ab356` — fix(status-line): always show session name column on model line
- `e4aa071` — refactor(status-line): centralize column reformatting for all line types
- `4b2ba4c` — fix(status-line): version upgrade line uses plain separators and aligned columns
- `5c516e2` — Move claude-skills-tester-cli and plugins research to devtools
- `3473770` — Move 6 skills and related docs to devtools repo
- `9b571ef` — rename: tests/ to claude-skills-tester-cli/
- `c76b813` — chore: move CLAUDE.md into .claude/
- `00e06f5` — chore: move research/ contents into docs/research/
- (20+ more commits showing active development)

**Status:** Active development. Recent work on status line improvements and repo organization.

## Build & Test Commands

```bash
# Installation
./install.sh             # Install skills and extensions

# Uninstallation
./uninstall.sh           # Remove skills and extensions

# Testing
pytest                   # Run pytest suite for internal components
pytest -v                # Verbose test output

# Skills invocation (in Claude Code)
/yolo                           # Toggle YOLO mode
/custom-status-line install    # Install status line pipeline
/custom-status-line uninstall  # Remove status line pipeline
```

## Notes

- Personal project for Claude Code workflow optimization and skill development
- All work done in worktree branches, merged via PR to main (see Git Workflow in CLAUDE.md)
- Uses pytest for testing internal Python components
- Status line is a composable pipeline for terminal progress tracking
- YOLO mode auto-approves tool calls when enabled (toggle per session)
- Includes research on Claude Code usage limits and optimization strategies
- Recent focus on status line improvements (column alignment, formatting)
- Skills are designed to be personal extensions but some are marked as distributable
- Rules enforce workflow standards (CLI versioning, plugin development, worktree cleanup)
- Wrangler configuration suggests potential Cloudflare Workers integration
- Superpowers plugin provides additional development workflows
- Several skills and tools previously developed here were moved to devtools repo
- This repo centralizes personal Claude Code customizations and extensions
