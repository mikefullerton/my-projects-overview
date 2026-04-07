# my-agentic-interviews

## Project Summary

A personal interview repository for the Agentic Interview Team system. Stores user profiles, per-project interview transcripts, specialist analyses, coverage checklists, and accumulated knowledge across interviews. Designed to be invoked via `/interview` from any project directory. Also previously contained Whippet cookbook docs (now moved elsewhere). Includes structured file conventions with YAML frontmatter and timestamp-based naming.

## Type & Tech Stack

- **Type**: Knowledge base / data repository (no compiled code)
- **Format**: Markdown files with YAML frontmatter
- **Naming**: Timestamp-based (`YYYY-MM-DD-HH-MM-SS-descriptive-slug.md`)
- **Config**: External config at `~/.agentic-interviewer/config.json`

## GitHub URL

`git@github.com:mikefullerton/my-agentic-interviews.git`

## Directory Structure

```
my-agentic-interviews/
├── .claude/
│   ├── CLAUDE.md                    # Agent context (structure, conventions)
│   └── rules/
│       └── always-commit-and-push.md  # Auto-commit rule
├── knowledge/                        # Accumulated learnings across interviews
├── profiles/
│   └── mike/                        # User profile and resume
│       └── resume/                  # Resume files
│       └── profile.md              # Auto-maintained profile
├── projects/                        # Per-project interview data
│   └── <project-name>/
│       ├── transcript/             # Raw Q&A transcript files
│       ├── analysis/               # Specialist analysis files
│       └── checklist.md            # Living coverage checklist
└── README.md                        # Usage docs
```

## Key Files & Components

- `.claude/CLAUDE.md` -- Agent context: directory structure, file conventions (YAML frontmatter with id, title, type, created, modified, author, summary, tags, platforms, related, project, session, specialist fields), file naming scheme
- `.claude/rules/always-commit-and-push.md` -- Rule requiring immediate commit and push after every file change
- `profiles/mike/` -- User profile directory with resume and auto-maintained profile
- `projects/` -- Per-project interview data (transcripts, analyses, checklists)
- `knowledge/` -- Cross-interview accumulated learnings
- `README.md` -- Usage documentation and structure overview

## Claude Configuration

- `.claude/CLAUDE.md` -- Defines file conventions: all markdown files use YAML frontmatter (id UUID, title, type, created/modified ISO 8601, author, summary, tags, platforms, related, project, session, specialist)
- `.claude/rules/always-commit-and-push.md` -- Non-negotiable rule: commit and push after every file change
- No settings.json or settings.local.json

## Planning & Research Documents

- Previously contained Whippet cookbook docs (removed in commit "chore: remove whippet-cookbook docs (moved elsewhere)")
- Various interview transcripts and analyses stored in `projects/` subdirectories

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-07 -- "Ignore .DS_Store files"
- **Working tree**: Clean
- **Total commits**: 15+ (viewed)
- **Recent activity**: Active through April 2026 -- Whippet cookbook recipe additions (Apr 2026), cookbook docs removal, gitignore updates
- **Key recent changes**: SQLite persistence recipe, AIRequestBuilder recipe, launch-at-login recipe, floating session panel recipe, menu-bar-status-item recipe, NotificationManager recipe (all for Whippet cookbook, later moved)

## Build & Test Commands

```bash
# No build step -- pure markdown knowledge base
# Usage: Invoke /interview from any project directory
# Config: ~/.agentic-interviewer/config.json
```

## Notes

- This is a data-only repository -- no executable code
- Designed to work with the Agentic Interview Team system (invoked via `/interview` command)
- YAML frontmatter fields are extensive (id, title, type, created, modified, author, summary, tags, platforms, related, project, session, specialist)
- The always-commit-and-push rule ensures the remote is always in sync
- Previously hosted Whippet cookbook recipes before they were moved to a separate location
