# My Agentic Interviews

## Project Summary

My Agentic Interviews is a personal interview repository and knowledge management system for the Agentic Interview Team system. It stores structured interview data across multiple projects using an AI-driven specialist interview system, tracking user profiles, per-project interviews (transcripts and analysis), and accumulated learnings. The system reads and writes markdown files with standardized YAML frontmatter for metadata, enabling systematic knowledge capture from development work across all projects. Designed to integrate with Claude Code interview commands and feed learnings back into project development workflows.

## Type & Tech Stack

**Type:** Knowledge Management System / Interview Repository

**Tech Stack:**
- **Language:** Markdown (structured with YAML frontmatter)
- **Storage:** Git repository (version-controlled)
- **Integration:** Claude Code (via /interview command)
- **Configuration:** JSON (system config at ~/.agentic-interviewer/config.json)
- **Metadata:** YAML frontmatter in markdown files
- **No Code Runtime:** Pure data/documentation project

## GitHub URL

Not specified in current files; appears to be a personal/internal repository

## Directory Structure

```
my-agentic-interviews/
├── profiles/               # User profiles
│   └── mike/
│       ├── profile.md      # Auto-maintained developer profile (YAML frontmatter + markdown)
│       └── resume/         # Resume files for interview context
├── projects/               # Per-project interview data
│   ├── <project-name>/
│   │   ├── transcript/     # Raw Q&A files (timestamped)
│   │   ├── analysis/       # Specialist analysis files
│   │   └── checklist.md    # Living coverage checklist
│   └── ...
├── knowledge/              # Accumulated learnings across all interviews
│   └── insights/           # Cross-project patterns and learnings
├── README.md               # Project overview and usage
├── .claude/
│   ├── CLAUDE.md          # Claude Code configuration
│   └── rules/             # Interview system rules and prompts
└── .git/
```

## Key Files & Components

- **README.md** - Project description, usage instructions, file structure, config location
- **.claude/CLAUDE.md** - Claude Code configuration for interview system, file naming conventions, frontmatter schema, usage instructions
- **.claude/rules/** - Interview system rules and specialist prompts
- **profiles/mike/profile.md** - Developer profile with YAML frontmatter including:
  - id, title, type (profile)
  - created/modified timestamps (ISO 8601)
  - summary, tags, platforms (ios, macos, windows, android, web)
  - author, related projects metadata
- **projects/<name>/transcript/** - Timestamped interview Q&A files (format: YYYY-MM-DD-HH-MM-SS-descriptive-slug.md)
- **projects/<name>/analysis/** - Specialist analysis files (extraction, insights, recommendations)
- **projects/<name>/checklist.md** - Living coverage checklist tracking interview topics covered
- **knowledge/** - Accumulated cross-project insights and patterns discovered through interviews

## Claude Configuration

Stored in **.claude/CLAUDE.md** - Comprehensive documentation of:
- **File Conventions:** YAML frontmatter schema for all markdown files with fields: id (UUID), title, type (transcript/analysis/checklist/profile/summary), created/modified (ISO 8601), author, summary, tags, platforms, related, project, session, specialist
- **File Naming:** Timestamp-based convention for transcripts and analysis (YYYY-MM-DD-HH-MM-SS-descriptive-slug.md)
- **Usage:** Invoke `/interview` from any project directory; system automatically reads/writes to this repository
- **Structure:** Organized by profiles, projects, and knowledge domains for systematic learning capture

## Planning & Research Documents

- **README.md** - Project overview, structure, usage instructions, configuration location
- **.claude/CLAUDE.md** - Detailed file conventions, YAML frontmatter schema, file naming patterns, usage instructions for interview system
- **projects/<name>/checklist.md** - Per-project coverage checklists tracking interview progress
- **knowledge/** - Accumulated learnings and cross-project insights

## Git History & Current State

- **Remote:** Not specified in output; appears to be personal/internal
- **Current Branch:** main
- **Status:** Clean working tree (no uncommitted changes)
- **Recent Activity:**
  - Latest: Ignore .DS_Store files (34ab4bf)
  - chore: remove whippet-cookbook docs (moved elsewhere) (5078664)
  - Multiple recipe additions (SQLite persistence, AIRequestBuilder, floating session panel, etc.) (f86b7cc onwards)
  - Last 15 commits show addition of Whippet cookbook recipes for infrastructure patterns (session panels, menu bar, notifications, window activation, etc.)

## Build & Test Commands

```bash
# No build process; pure markdown repository
# Usage is via Claude Code /interview command:
/interview                            # Run interview for current project
# (System automatically reads/writes to this repository)

# Manual operations:
git status                            # View uncommitted changes
git add <files>                       # Stage interview outputs
git commit -m "..."                   # Commit new interview data
```

## Notes

- **Status:** Active development for interview data capture and knowledge management
- **Purpose:** Systematic interview-driven knowledge capture across all development projects; feed learnings back into development workflows
- **System Integration:** Designed to integrate with Claude Code via `/interview` command that reads project context and writes structured interview outputs
- **Data Format:** YAML frontmatter + markdown for flexible, version-controllable knowledge storage
- **Configuration:** System configuration at ~/.agentic-interviewer/config.json (external, not in repo)
- **Coverage Tracking:** Per-project checklists track which topics have been interviewed, enabling progressive knowledge building
- **Knowledge Accumulation:** Cross-project insights extracted and stored in knowledge/ directory for pattern recognition across projects
- **Metadata:** Comprehensive frontmatter (id, created, modified, author, specialist, session, platform tags) enables rich querying and knowledge extraction
- **File Naming:** Timestamp-based naming (YYYY-MM-DD-HH-MM-SS-slug) ensures chronological ordering and prevents conflicts
- **Specialist System:** Different specialists can contribute analysis (marked by specialist field in frontmatter)
- **Related Projects:** Feeds into multiple projects (Hairball, Whippet, etc.) through extracted patterns and insights
- **Recipes:** Repository includes cookbook recipes for common patterns (SQLite persistence, launch-at-login, floating panels, menu bar items, notifications, window activation, click actions, session summarization, event ingestion, hooks, liveness monitoring, etc.)
