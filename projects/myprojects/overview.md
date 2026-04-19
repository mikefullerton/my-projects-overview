# My Projects

## Project Summary

My Projects is a personal project management dashboard providing a unified web UI for monitoring approximately 35 git repositories. Tracks git status, branches, recent commits, modified files, tech stacks, and cross-project metadata (todos, issues, concerns, decisions, dependencies). Recently converted from vanilla JavaScript to React 19 + Vite for improved performance and developer experience. Includes a Python scanner for repository analysis and a Node.js HTTP server backend. The dashboard displays clean/dirty repository status, project counts with visual indicators, recent commits, and tech stack detection.

## Type & Tech Stack

**Type:** Web Dashboard / Project Management System

**Tech Stack:**
- **Frontend:** React 19, Vite 8.0, TypeScript 6.0, CSS (custom styling)
- **Backend:** Node.js HTTP server (port 3456), Express-like routing
- **Scanner:** Python 3 (scan-branches.py, scan-modified.py)
- **Storage:** localStorage adapter pattern (pluggable for API backends)
- **Git Integration:** Direct git command execution (status, log, branch)
- **Build:** Vite for frontend bundling

## GitHub URL

https://github.com/mikefullerton/myprojects

## Directory Structure

```
myprojects/
├── config.json                    # Project registry (~35 projects)
│                                  # Maps project slugs to filesystem paths
├── site/                          # React frontend (Vite)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── ...
│   ├── dist/                      # Build output
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   ├── tsconfig.json
│   ├── index.html
│   └── node_modules/
├── server/                        # Node.js HTTP server
│   ├── server.js                  # HTTP server, API routes
│   └── start.sh                   # Startup script
├── scanner/                       # Python project scanner
│   ├── scan-branches.py           # Scan git branches across projects
│   ├── scan-modified.py           # Scan modified files/uncommitted changes
│   └── ...
├── projects/                      # Project-specific metadata (TODO, issues, decisions, dependencies)
│   └── <project-name>/
│       ├── metadata.json
│       └── ...
├── docs/
│   ├── project/description.md
│   ├── superpowers/
│   │   ├── plans/2026-04-07-typescript-python-conversion.md
│   │   └── specs/2026-04-07-typescript-python-conversion-design.md
│   ├── requirements/
│   └── ...
├── .claude/                       # Claude Code configuration
│   └── skills/
├── .git/
└── .gitignore
```

## Key Files & Components

- **config.json** - Project registry mapping ~35 project slugs to paths (relative to ../../). Examples:
  - catherding, socialmediabot, mysetup, dev-team, cookbook, roadmaps, whippet, hairball, catnip, etc.
  - Maps to ../../active/, ../../paused/, ../../deprecated/, ../../other/, ../../personal/, ../../tests/ directories
  - projectOrder array controls dashboard display order
- **site/package.json** - React 19, Vite 8.0, TypeScript, Playwright (testing)
- **site/src/** - React components for dashboard UI:
  - Project list view
  - Status indicators (clean/dirty repos)
  - Git commit history display
  - Tech stack badges
  - Metadata popover views (todos, issues, concerns, decisions, dependencies)
- **server/server.js** - Node.js HTTP server (port 3456) providing:
  - API endpoints for project data (/api/projects, /api/project/:name)
  - Git status polling
  - Metadata aggregation
- **scanner/scan-branches.py** - Python script for scanning git branches across all projects
- **scanner/scan-modified.py** - Python script for scanning modified files and uncommitted changes
- **docs/project/description.md** - Complete project description with purpose, features, tech stack, status, related projects
- **docs/superpowers/plans/2026-04-07-typescript-python-conversion.md** - Implementation plan for TypeScript/Python conversion
- **docs/superpowers/specs/2026-04-07-typescript-python-conversion-design.md** - Design specification for TypeScript/Python conversion

## Claude Configuration

Stored in **.claude/skills/** - Contains custom Claude Code skills for project management workflows.

## Planning & Research Documents

- **docs/project/description.md** - Project purpose, key features, tech stack, status (active development), related projects
- **docs/unified-data-abstraction.md** - Data abstraction patterns for unified project metadata
- **docs/local-file-writing-projects.md** - Documentation on projects that write local files
- **docs/requirements/myagenticprojects-storage-requirements.md** - Storage requirements specification
- **docs/superpowers/plans/2026-04-07-typescript-python-conversion.md** - Plan for TypeScript/Python conversion
- **docs/superpowers/specs/2026-04-07-typescript-python-conversion-design.md** - Design specification for conversion
- **docs/superpowers/specs/2026-04-06-react-conversion-design.md** - Design spec for React migration

## Git History & Current State

- **Remote:** git@github.com:mikefullerton/myprojects.git
- **Current Branch:** main
- **Status:** Clean working tree (no uncommitted changes)
- **Recent Activity:**
  - Latest: fix: update catherding description after reorg (3f29d19)
  - docs: add standardized project description (0ebd20f)
  - style: stats cards in joined pill shape with rounded ends (d952b59)
  - style: center stats cards side by side with flexbox (a0f0270)
  - style: separate status card next to project count (3dd5509)
  - style: green checkmark inline with project count (29377b5)
  - feat: dashboard shows dirty repos list or green checkmark (66a5556)
  - Recent work focused on UI/UX improvements, status display, dashboard refactoring

## Build & Test Commands

```bash
# Frontend (site/)
npm run dev                  # Start Vite dev server (port 5173)
npm run build               # Build React + Vite for production
npm run preview             # Preview production build locally
npm run typecheck           # Run TypeScript type checking

# Backend (server/)
./server/start.sh           # Start Node.js HTTP server (port 3456)
node server/server.js       # Direct Node.js execution

# Scanner (scanner/)
python3 scanner/scan-branches.py      # Scan git branches across all projects
python3 scanner/scan-modified.py      # Scan modified files and uncommitted changes

# Development workflow
npm run dev                 # (in site/) - starts frontend
./server/start.sh          # (in separate terminal) - starts backend
# Open http://localhost:5173 in browser
```

## Notes

- **Status:** Active development with recent React migration from vanilla JavaScript
- **Architecture:** Full-stack (React frontend, Node.js backend, Python scanner) with pluggable storage adapter (currently localStorage, extensible to API)
- **Dashboard Features:**
  - Unified view of ~35 git repositories
  - Git status monitoring (branches, commits, modified files)
  - Tech stack detection per project
  - Cross-project metadata tracking (todos, issues, concerns, decisions, dependencies)
  - Visual indicators (green checkmark for clean repos, stop sign for dirty repos)
  - Stats cards showing project count and repository status
  - Popovers showing metadata details on hover
- **Project Registry:** config.json maps project slugs to paths in ../../ directory structure (active/, paused/, deprecated/, other/, personal/, tests/)
- **Recent UI Improvements:** Styled stats cards as joined pills, responsive flexbox layout, status indicators, visual hierarchy improvements
- **Metadata System:** Storage adapter pattern allows easy migration from localStorage to API backend
- **Git Integration:** Direct git command execution for branch, status, and log queries
- **Tech Stack Detection:** Automatic detection of project technologies (JavaScript, Python, Swift, etc.)
- **Related Project:** My Projects Overview (complementary index focused on Claude Code reference with markdown + static HTML)
- **Conversion in Progress:** Plans for TypeScript/Python conversion to improve maintainability and add new features
