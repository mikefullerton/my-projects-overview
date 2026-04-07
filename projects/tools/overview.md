# tools (agentic-cookbook/tools)

## Project Summary

User-facing tools for interacting with the agentic cookbook system. Provides reusable Claude Code skills, guidance rules, and scripts for project authoring, linting, planning, and cookbook integration. This is a companion repository to the agentic-cookbook/cookbook (principles, guidelines, recipes, workflows) and agentic-cookbook/dev-team (multi-agent dev team for project discovery, generation, building, and review). The tools repo delivers the installable skills and rules that projects use to interact with the cookbook workflow.

## Type & Tech Stack

- **Type**: Claude Code tooling repository (skills, rules, scripts)
- **Format**: Markdown skill definitions (SKILL.md files), markdown rule files, shell scripts
- **No build system**: No package.json, pyproject.toml, or other build configuration
- **Runtime**: Claude Code (skills invoked via slash commands), bash (scripts)

## GitHub URL

`git@github.com:agentic-cookbook/tools.git`

## Directory Structure

```
tools/
├── .claude/
│   └── CLAUDE.md                      # Project-level Claude instructions
├── rules/                             # Guidance rule files (7 rules)
│   ├── authoring-ground-rules.md      # Authoring standards
│   ├── cookbook.md                     # Cookbook conventions (14K)
│   ├── extension-authoring.md         # Extension authoring guide
│   ├── generated-cookbook-template.md  # Template for generated cookbooks
│   ├── permissions.md                 # Permission model
│   ├── skill-authoring.md             # Skill creation guide
│   └── skill-versioning.md            # Skill version management
├── skills/                            # 21 Claude Code skills
│   ├── configure-cookbook/             # Configure cookbook settings
│   ├── contribute-to-cookbook/         # Contribute improvements back
│   ├── cookbook-bug/                   # Report cookbook bugs
│   ├── cookbook-help/                  # Get help with cookbook
│   ├── cookbook-next/                  # Next steps guidance
│   ├── cookbook-start/                 # Start a new cookbook project
│   ├── cookbook-suggestion/            # Suggest cookbook improvements
│   ├── install-cookbook/               # Install cookbook into a project
│   ├── install-recommended-tools/     # Install recommended tooling
│   ├── install-worktree-rule/         # Install git worktree rule
│   ├── lint-agent/                    # Lint agent definitions
│   ├── lint-compliance/               # Lint for compliance
│   ├── lint-project-with-cookbook/     # Lint project against cookbook
│   ├── lint-recipe/                   # Lint recipe files
│   ├── lint-skill/                    # Lint skill definitions
│   ├── optimize-rules/                # Optimize rule files
│   ├── plan-cookbook-recipe/           # Plan new recipes
│   ├── port-swiftui-to-appkit/        # Port SwiftUI to AppKit
│   ├── uninstall-cookbook/             # Remove cookbook from project
│   └── validate-cookbook/              # Validate cookbook configuration
├── scripts/
│   └── cookbook-statusline.sh          # Status line integration script
├── README.md                          # Repository overview
└── .gitignore
```

## Key Files & Components

- `rules/cookbook.md` -- Core cookbook conventions document (14K), the main rule file governing cookbook behavior
- `rules/skill-authoring.md` -- Guide for creating new Claude Code skills
- `rules/skill-versioning.md` -- Version management for skills
- `rules/authoring-ground-rules.md` -- Ground rules for all authoring
- `rules/permissions.md` -- Permission model documentation
- `rules/extension-authoring.md` -- Extension creation guide
- `skills/install-cookbook/` -- Primary entry point for adding cookbook to a project
- `skills/lint-*` -- 5 linting skills (agent, compliance, project, recipe, skill)
- `skills/cookbook-start/` -- Start a new cookbook project
- `scripts/cookbook-statusline.sh` -- Status line integration for cookbook operations
- `.claude/CLAUDE.md` -- References sibling repos: `../cookbook` (cookbook principles) and `../dev-team` (multi-agent dev team)

## Claude Configuration

- `.claude/CLAUDE.md` -- Project-level instructions referencing sibling repositories (cookbook, dev-team)
- No settings.json or settings.local.json
- Skills are designed to be globally installed via symlinks from `~/.claude/skills/`

## Planning & Research Documents

- No dedicated planning or research directories
- `rules/` directory serves as the authoritative reference for all cookbook conventions

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "feat: add lint skill directories (agent, compliance, project, recipe, skill)"
- **Working tree**: Clean
- **Recent activity**: Young repository (4 commits total, created 2026-04-03)
- **Commit history**:
  - 2026-04-06: Added lint skill directories
  - 2026-04-06: Standardize worktree directory
  - 2026-04-03: Add cookbook-statusline.sh script
  - 2026-04-03: Initial commit with rules, skills, and project setup

## Build & Test Commands

```bash
# No build system -- this is a tooling/skills repository
# Skills are invoked via Claude Code slash commands after installation

# Install cookbook into a project:
# /install-cookbook

# Lint a project:
# /lint-project-with-cookbook

# Start a new cookbook project:
# /cookbook-start
```

## Notes

- Part of the agentic-cookbook ecosystem (3 repos: cookbook, tools, dev-team)
- The tools repo is the user-facing entry point -- it provides the skills that projects invoke
- Sibling repos expected at `../cookbook` and `../dev-team`
- Very young repository (4 commits, created April 2026)
- Contains 21 skills organized by function: installation, linting, planning, configuration, contribution
- 5 lint skills added recently for checking agents, compliance, projects, recipes, and skills
- The `port-swiftui-to-appkit` skill is a notable specialized tool for macOS UI porting
- Rules serve as both documentation and runtime configuration for Claude Code behavior
