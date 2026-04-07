# My Projects

## Project Summary

My Projects is a personal project management dashboard that tracks ~35 git repositories across multiple development categories. It provides a unified web UI for monitoring git status, branches, commits, modified files, tech stacks, and cross-project metadata (todos, issues, concerns, decisions, dependencies). Recently converted from vanilla JavaScript to React + Vite.

## Type & Tech Stack

- **Project Type:** Web Dashboard / Project Management System
- **Frontend:** React 19.2.4, Vite 8.0.5, Vanilla CSS (21KB)
- **Backend:** Node.js HTTP server (port 3456)
- **Scanner:** Bash/Python scripts for git repo scanning
- **Storage:** localStorage adapter pattern (SQLite support stubbed for future)
- **Data:** ProjectDB class with pluggable adapter interface

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
│   ├── local-file-writing-projects.md # Current data architecture
│   ├── requirements/
│   │   └── myagenticprojects-storage-requirements.md
│   └── superpowers/specs/
│       └── 2026-04-06-react-conversion-design.md
├── projects/                          # Per-project markdown notes
├── scanner/
│   ├── scan-projects.sh               # Main scanner (461 lines)
│   ├── scan-branches.py
│   └── scan-modified.py
├── server/
│   ├── server.js                      # HTTP server with /api/refresh
│   └── start.sh
└── site/                              # React + Vite frontend
    ├── vite.config.js                 # React plugin + API proxy to :3456
    ├── package.json
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── index.css                  # All styles (21KB)
        ├── context/DataContext.jsx     # ProjectDB provider
        ├── hooks/useData.js
        ├── components/                # Sidebar, StatsBar, ProjectGrid, ProjectDetail, AttentionView, TodosView, IssuesView, DecisionsView, GitIndicators, ItemList
        └── lib/
            ├── db.js                  # ProjectDB + adapter pattern
            ├── config.js
            └── seed.js                # SEED_DATA with project metadata
```

## Key Components

**Scanner:** Walks git repos, gathers status/branches/commits, outputs JSON. Auto-generates todos for uncommitted files and open branches.

**/refresh skill:** Scans all projects, runs git commands, detects tech stack, preserves manual data, bumps SEED_VERSION.

**Components:** Sidebar (nav/project tree), StatsBar (5 stat cards), ProjectGrid (grouped cards), ProjectDetail (full view), AttentionView (uncommitted/high-priority), TodosView, IssuesView, DecisionsView

**Data Model:** projects, todos, issues, concerns, decisions, dependencies — 6 tables with auto-generated and manual entries.

## Claude Configuration

- `/refresh` skill for scanning and updating project data
- No other Claude-specific configuration

## Planning & Research Documents

- **unified-data-abstraction.md** — Unify Roadmaps, Dev-Team, Social Media Bot under 10 core entity types
- **react-conversion-design.md** — Vanilla JS → React + Vite port (zero visual changes)
- **myagenticprojects-storage-requirements.md** — Server-side persistent storage specs
- **local-file-writing-projects.md** — Current data architecture across 3 projects

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Uncommitted changes:** DataContext.jsx, seed.js modified
- **Recent (2026-04-06):** Inline git status, scanner async/spinner, React conversion, repo reorganization

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
- Future: Replace localStorage adapter with ApiAdapter for persistent backend
- Vision: unify data across Roadmaps, Dev-Team, and Social Media Bot systems
