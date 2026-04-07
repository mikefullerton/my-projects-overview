# My Projects

## Project Summary

My Projects is a personal project management dashboard that tracks ~35 git repositories across multiple development categories. It provides a unified web UI for monitoring git status, branches, commits, modified files, tech stacks, and cross-project metadata (todos, issues, concerns, decisions, dependencies). Recently converted from vanilla JavaScript to React + Vite.

## Type & Tech Stack

- **Project Type:** Web Dashboard / Project Management System
- **Frontend:** React 19.2.4, Vite 8.0.5, Vanilla CSS (21KB)
- **Backend:** Node.js HTTP server (port 3456)
- **Scanner:** Bash (scan-projects.sh) + Python (scan-branches.py, scan-modified.py)
- **Storage:** localStorage adapter pattern (pluggable -- `ApiAdapter` stubbed for future)
- **Data:** ProjectDB class with adapter interface (getAll, get, put, remove, clear)

## GitHub URL

`git@github.com:mikefullerton/my-projects.git`

## Directory Structure

```
my-projects/
├── .claude/
│   └── skills/refresh/SKILL.md       # /refresh skill - scans projects, updates seed data
├── config.json                        # Project registry (~35 projects with paths)
├── docs/
│   ├── unified-data-abstraction.md    # Design: unify Roadmaps, Dev-Team, Bot under shared backend
│   ├── local-file-writing-projects.md # Current data architecture across 3 projects
│   ├── requirements/
│   │   └── myagenticprojects-storage-requirements.md
│   └── superpowers/specs/
├── projects/                          # Per-project markdown notes (8 files)
├── scanner/
│   ├── scan-projects.sh               # Main scanner script
│   ├── scan-branches.py
│   └── scan-modified.py
├── server/
│   ├── server.js                      # HTTP server with /api/refresh endpoint
│   └── start.sh
└── site/                              # React + Vite frontend
    ├── vite.config.js                 # React plugin + API proxy to :3456
    ├── package.json                   # project-hub v1.0.0
    └── src/
        ├── main.jsx
        ├── App.jsx                    # Main app with sidebar, stats, project views
        ├── index.css                  # All styles (21KB)
        ├── context/DataContext.jsx     # ProjectDB provider
        ├── hooks/useData.js
        ├── components/                # Sidebar, StatsBar, ProjectGrid, ProjectDetail, etc.
        └── lib/
            ├── db.js                  # ProjectDB + adapter pattern
            ├── config.js
            ├── seed.js                # SEED_DATA with project metadata
            └── theme.js               # Centralized color mappings
```

## Key Files & Components

**Scanner:** Walks git repos, gathers status/branches/commits/modified files, outputs JSON. Auto-generates todos for uncommitted files and open branches.

**/refresh skill:** Scans all projects, runs git commands, detects tech stack, preserves manual data, bumps SEED_VERSION.

**Components:** Sidebar (nav/project tree), StatsBar (5 stat cards), ProjectGrid (grouped cards), ProjectDetail (full view), AttentionView (uncommitted/high-priority), TodosView, IssuesView, DecisionsView, GitIndicators

**Data Model:** 6 tables -- projects, todos, issues, concerns, decisions, dependencies -- with auto-generated and manual entries.

**config.json:** Registry of ~35 projects across categories (active, paused, deprecated, tests, personal, other) with relative paths.

## Claude Configuration

- `/refresh` skill for scanning and updating project data
- No CLAUDE.md, settings.json, or rules configured

## Planning & Research Documents

| Document | Description |
|----------|-------------|
| `docs/unified-data-abstraction.md` | Design to unify Roadmaps, Dev-Team, Social Media Bot under 10 core entity types |
| `docs/local-file-writing-projects.md` | Documents 3 projects that write local files (Roadmaps, Dev-Team, Social Media Bot) |
| `docs/requirements/myagenticprojects-storage-requirements.md` | Server-side persistent storage specs replacing localStorage |
| `docs/superpowers/specs/` | React conversion design spec |
| `projects/` | Per-project markdown notes: cat-herding, my-agentic-interviews, my-projects, mysetup, name-craft, scratchyfish, social-media-bot-tests, social-media-bot |

## Git History & Current State

- **Branch:** main
- **Total Commits:** 12
- **Uncommitted changes:** `site/src/context/DataContext.jsx`, `site/src/lib/seed.js` modified

**Recent Commits (2026-04-06):**
1. `aa8dd4b` -- feat: inline git status after project name, remove colored subtitles
2. `a752d51` -- feat: replace colored subtitles with git status info for dirty repos
3. `d95ea0e` -- fix: make scanner run async, add scanning spinner to refresh button
4. `505ad58` -- fix: refresh button now works without page reload
5. `02bd89f` -- feat: update DataContext and seed data

**Major milestones:**
- React + Vite conversion from vanilla JS (`b6c3a7f`)
- Repo reorganization into site/, scanner/, server/ (`30c9d95`)
- Initial project management dashboard (`86bcff0`)

## Build & Test Commands

```bash
# Frontend
cd site && npm run dev     # Vite dev (:5173, proxies /api to :3456)
cd site && npm run build   # Production build

# Backend
cd server && ./start.sh    # Start on port 3456

# Scanner
./scanner/scan-projects.sh
```

## Notes

- Recently converted from monolithic vanilla JS (1700 lines) to modular React + Vite
- Two uncommitted files in working tree (DataContext.jsx, seed.js)
- Future: Replace localStorage adapter with ApiAdapter for persistent backend storage
- Vision: Unify data across Roadmaps, Dev-Team, and Social Media Bot systems into shared entity types
- Centralized color/theme system in `theme.js`
