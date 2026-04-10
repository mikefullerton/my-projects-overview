# Cat Herding

## Project Summary

Cat Herding is a personal collection of Claude Code skills, plugins, hooks, and workflow extensions. It provides 2 distributable skills (yolo, custom-status-line), internal linting/authoring skills, and configuration rules.

## Type & Tech Stack

- **Project Type:** Personal Claude Code workflow extensions
- **Python 3.11+** — scripts and hooks
- **YAML** — Skill manifests
- **Key tools:** Claude Code CLI

## GitHub URL

`git@github.com:mikefullerton/cat-herding.git`

## Directory Structure

```
cat-herding/
├── .claude/
│   ├── CLAUDE.md
│   ├── skills/                        # Internal skills
│   │   ├── lint-skill/                # Lint skills against best practices
│   │   ├── lint-rule/                 # Lint rules against best practices
│   │   ├── lint-agent/                # Lint agents against best practices
│   │   ├── optimize-rules/            # Consolidate rule files
│   │   ├── install-worktree-rule/     # Install worktree/PR git workflow
│   │   └── ...
│   └── rules/
│       ├── cli-versioning.md
│       ├── plugin-development.md
│       └── worktree-branch-cleanup.md
├── skills/
│   ├── yolo/                          # Per-session auto-approve mode
│   └── custom-status-line/            # Composable status line pipeline
├── docs/
│   └── research/                      # Claude Code research docs
├── install.sh
├── uninstall.sh
└── README.md
```

## Key Components

### Distributable Skills (2)

1. **yolo** — Per-session auto-approve for tool calls
2. **custom-status-line** — Composable shell status line (git stats, YOLO, progress)

### Internal Skills

lint-skill, lint-rule, lint-agent, optimize-rules, install-worktree-rule, and others.

### Rules

- `cli-versioning.md` — Auto-bump CLI versions on source changes
- `plugin-development.md` — Plugin dev workflow guide
- `worktree-branch-cleanup.md` — Worktree cleanup after merge

## Claude Configuration

- **CLAUDE.md** — Skills table, git workflow instructions
- **Rules:** cli-versioning, plugin-development, worktree-branch-cleanup

## Related Projects

- [dev-tools](../../tools/dev-tools/) — configurator, webinitor, new-project, quick-ref, show-project-setup, repo-cleaner (moved from this repo 2026-04-10)
- [devtools-web-server](../../tools/devtools-web-server/) — local Caddy web server (moved from this repo 2026-04-10)

## Notes

- Owner edits go direct to main; Claude Code sessions use worktree + PR workflow
- Significantly slimmed down on 2026-04-10: dev-tools skills, CLIs, and web server moved to their own repos
