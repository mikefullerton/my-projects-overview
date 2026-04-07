# Catnip

## Project Summary

Catnip is a hosted, multi-user web service that monitors autonomous Claude Code agent progress in real-time. It replaces a local-only Python progress dashboard with a production-grade full-stack application featuring GitHub OAuth authentication, REST + WebSocket APIs, and a React-based dashboard.

## Type & Tech Stack

- **Project Type:** Full-stack web service (API + Frontend Dashboard + CLI)
- **Backend:** TypeScript, Hono, Drizzle ORM, PostgreSQL
- **Frontend:** TypeScript, React 19, Vite, TailwindCSS 4, React Router, TanStack Query
- **CLI:** TypeScript (Node.js)
- **Auth:** GitHub OAuth, JWT bearer tokens
- **Real-time:** WebSocket
- **Hosting:** Railway (backend + PostgreSQL), Cloudflare Pages (frontend)
- **Container:** Docker (Node.js 20-alpine)

## GitHub URL

`git@github.com:mikefullerton/catnip.git`

## Directory Structure

```
catnip/
├── .claude/
│   ├── settings.local.json          # Permissions: git add/commit/push, gh issue
│   └── worktrees/
├── Roadmaps/
│   └── CatnipWebService-Roadmap.md  # Feature roadmap (Status: Complete)
├── backend/
│   ├── src/
│   │   ├── index.ts                 # Server entry, route mounting
│   │   ├── db/
│   │   │   ├── schema.ts            # users, api_tokens, roadmaps, roadmap_steps, roadmap_events
│   │   │   └── migrate.ts
│   │   ├── routes/
│   │   │   ├── health.ts, auth.ts, tokens.ts, roadmaps.ts
│   │   ├── middleware/
│   │   │   ├── auth.ts, cors.ts
│   │   └── ws/
│   │       ├── handler.ts, broadcast.ts
│   ├── scripts/demo-roadmap.ts
│   ├── Dockerfile, railway.toml, start.sh
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── App.tsx                  # Router & layout
│   │   ├── pages/                   # LoginPage, AuthCallbackPage, RoadmapListPage, RoadmapDetailPage
│   │   ├── components/              # NavBar, StepList, ProgressBar, EventLog, ControlButtons, etc.
│   │   ├── hooks/                   # useAuth, useWebSocket, useRoadmap
│   │   └── api/
│   └── package.json
├── cli/
│   ├── src/
│   │   ├── index.ts, client.ts, config.ts
│   │   └── commands/                # login, list, show, control
│   └── package.json
└── .gitignore
```

## Key Files & Components

**Database Schema:** users (GitHub auth), api_tokens (personal access), roadmaps (agent runs with state/status/repo/branch), roadmap_steps (progress), roadmap_events (audit log)

**Auth Flow:** GitHub OAuth → JWT token → Bearer auth for API. Agents use separate API tokens.

**Real-time:** WebSocket push from server to dashboard subscribers on step/event updates.

**CLI Commands:** `catnip-cli login`, `list`, `show <id>`, `pause/resume/stop <id>`

## Claude Configuration

- Permissions: git add/commit/push, gh issue operations only
- Worktrees for feature development

## Planning & Research Documents

**CatnipWebService-Roadmap.md** — Complete. 9 of 12 steps done. Covers: Railway setup, Cloudflare setup, OAuth, backend scaffolding, auth endpoints, token management, API endpoints, WebSocket, frontend.

**Deferred:** Agent back-channel (how UI control signals reach remote agents), control signal implementation.

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Working tree:** Clean
- **Recent commits (2026-04-06):** Standardize worktree directory, rename cat-herding references, refactor runs→roadmaps

## Build & Test Commands

```bash
# Backend
npm run dev              # Dev server (tsx watch)
npm run build && npm start
npm run db:migrate       # Run migrations
npm run demo             # Simulate agent workflow

# Frontend
npm run dev              # Vite dev server (:5173)
npm run build            # Production build

# CLI
npm start                # Run CLI
```

## Notes

- Monorepo with 3 independent npm projects (backend, frontend, cli)
- TypeScript throughout for full type safety
- Recent refactoring renamed "runs" → "roadmaps"
- Demo script validates API contracts during development
