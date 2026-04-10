# Agentic Cookbook Tools

## Project Summary

User-facing Claude Code skills, guidance rules, and scripts for interacting with the Agentic Cookbook ecosystem. This is a companion repository to the Agentic Cookbook, providing installable skills and rules that projects use to interact with the cookbook workflow. Delivers reusable Claude Code skills for project authoring, linting, planning, and cookbook integration.

## Type & Tech Stack

**Type:** Claude Code Skills & Tools Library

**Tech Stack:**
- **Format:** Markdown skill definitions (SKILL.md files), markdown rules
- **Runtime:** Claude Code (skills invoked via slash commands)
- **No build system** — no package.json, pyproject.toml, or other build configuration

## GitHub URL

https://github.com/agentic-cookbook/tools

## Directory Structure

```
.
├── .claude/              # Claude Code configuration
│   ├── CLAUDE.md
│   └── (worktrees)
├── docs/
│   └── project/
│       └── description.md
├── rules/                # 8 guidance rules for authoring and workflow
│   ├── (markdown rule files)
│   └── (guidance specifications)
├── skills/               # 20 distributable Claude Code skills
│   ├── (skill-name/
│   │   ├── SKILL.md
│   │   └── (supporting files)
│   └── (more skills...)
├── scripts/              # Cookbook integration and maintenance scripts
│   ├── cookbook-statusline.sh
│   └── (other scripts)
├── README.md
└── .gitignore
```

## Key Files & Components

**Documentation:**
- `.claude/CLAUDE.md` — Project overview and sibling repository references
- `docs/project/description.md` — Purpose, key features, and status
- `README.md` — Skill list and related repositories

**Skills Directory:**
- 20 distributable Claude Code skills for various tasks
- Each skill packaged as a markdown definition with supporting materials

**Rules Directory:**
- 8 guidance rules for authoring standards and workflow practices

**Scripts Directory:**
- `cookbook-statusline.sh` — Status line integration script
- Integration utilities for cookbook interaction

## Claude Configuration

**Location:** `.claude/CLAUDE.md`

Contains:
- Repository purpose and structure
- Sibling repository references (cookbook, dev-team)
- Information about distributable skills
- Guidance on accessing and extending rules

## Planning & Research Documents

**Project Documentation:**
- `docs/project/description.md` — Detailed project purpose, features, tech stack, and status

**Related Projects:**
- [Cookbook](../../cookbook/docs/project/description.md) — the knowledge base these tools operate on
- [Dev Team](../../dev-team/docs/project/description.md) — multi-agent platform
- [Roadmaps](../../roadmaps/docs/project/description.md) — feature planning system

## Git History & Current State

**Current Branch:** main

**Remote:** git@github.com:agentic-cookbook/tools.git

**Recent Commits:**
- `9fd9dda` — docs: add standardized project description
- `80b2526` — feat: add lint skill directories (agent, compliance, project, recipe, skill)
- `60b97e1` — chore: standardize worktree directory to .claude/worktrees/
- `102490f` — Add cookbook-statusline.sh script from dev-team repo
- `6288621` — Initial commit: tools repo with rules, skills, and project setup

**Status:** Recently completed / stable.

## Build & Test Commands

No build system required. Skills and rules are pure markdown and shell scripts.

**To use the skills:**
1. Clone the repository or reference it from your projects
2. Install skills via Claude Code's skill installation mechanism
3. Invoke skills using slash commands (e.g., `/skill-name`)

**To test integration:**
- Run scripts manually or as part of Claude Code automation
- Verify skills load correctly in Claude Code

## Notes

- This is a pure tools/skills repository with no runtime compilation or build dependencies
- Skills are designed to be reusable across agentic-cookbook projects
- Rules provide standardized guidance for project authoring and cookbook compliance
- Scripts facilitate integration between projects and the cookbook system
- Close dependency on sibling repositories: ../cookbook and ../dev-team (must be at same directory level)
- Skills can be individually distributed or installed as a collection
- Includes markdown-based skill definitions that follow Claude Code conventions
- Rules are meant to be integrated into project workflows via Claude Code rules system
