# Catnip

## Project Summary

Catnip is a hosted, multi-user web service that monitors autonomous Claude Code agent progress in real-time. It replaces a local-only Python progress dashboard with a production-grade full-stack application featuring GitHub OAuth authentication, REST + WebSocket APIs, and a React-based dashboard.

## Type & Tech Stack

- **Project Type:** Full-stack web service (API + Frontend Dashboard + CLI)
- **Backend:** TypeScript, Hono, Drizzle ORM, PostgreSQL, WebSocket (`@hono/node-ws`)
- **Frontend:** TypeScript, React 19, Vite 6, TailwindCSS 4, React Router 7, TanStack Query
- **CLI:** TypeScript (tsx)
- **Auth:** GitHub OAuth, JWT bearer tokens
- **Real-time:** WebSocket push from server to dashboard
- **Hosting:** Railway (backend + PostgreSQL), Cloudflare Pages (frontend)
- **Testing:** Vitest (backend + frontend), Testing Library + jsdom (frontend)

## GitHub URL

`git@github.com:mikefullerton/catnip.git`

## Directory Structure

```
catnip/
├── .claude/
│   ├── settings.local.json          # Permissions: git add/commit/push, gh issue
│   └── worktrees/                   # Git worktrees for feature development
├── Roadmaps/
│   └── CatnipWebService-Roadmap.md  # Feature roadmap (Status: Complete)
├── backend/
│   ├── src/
│   │   ├── index.ts                 # Server entry, route mounting
│   │   ├── types.ts                 # Shared types
│   │   ├── db/
│   │   │   ├── schema.ts            # users, api_tokens, roadmaps, roadmap_steps, roadmap_events
│   │   │   ├── index.ts             # DB client
│   │   │   ├── migrate.ts           # Migration runner
│   │   │   └── migrations/          # SQL migrations
│   │   ├── routes/
│   │   │   ├── auth.ts              # GitHub OAuth auth
│   │   │   ├── health.ts            # Health check
│   │   │   ├── roadmaps.ts          # Roadmap CRUD
│   │   │   ├── roadmaps.test.ts
│   │   │   ├── tokens.ts            # API token management
│   │   │   └── tokens.test.ts
│   │   ├── middleware/
│   │   │   ├── auth.ts              # Bearer token auth
│   │   │   ├── auth.test.ts
│   │   │   ├── cors.ts
│   │   │   └── cors.test.ts
│   │   └── ws/
│   │       ├── handler.ts           # WebSocket connection handler
│   │       ├── handler.test.ts
│   │       ├── broadcast.ts         # WebSocket event broadcasting
│   │       └── broadcast.test.ts
│   ├── scripts/demo-roadmap.ts      # Demo script for testing
│   ├── drizzle.config.ts
│   ├── package.json
│   └── tsconfig.json
├── frontend/
│   ├── src/
│   │   ├── App.tsx                  # Router & layout
│   │   ├── main.tsx
│   │   ├── index.css
│   │   ├── components/              # NavBar, StepList, StepIcon, StepItem,
│   │   │                            # ProgressBar, StatusBadge, EventLog,
│   │   │                            # ControlButtons, ConnectionStatus,
│   │   │                            # IssuePanel, PRPanel, ProtectedRoute
│   │   ├── hooks/
│   │   │   └── useRoadmaps.ts       # API data fetching hook
│   │   └── utils/
│   │       ├── time.ts              # Time formatting
│   │       └── time.test.ts
│   ├── vite.config.ts
│   └── package.json
├── cli/
│   ├── src/
│   │   ├── index.ts                 # CLI entry point
│   │   ├── client.ts                # API client
│   │   ├── config.ts                # CLI config
│   │   └── commands/
│   │       ├── login.ts             # Auth command
│   │       ├── list.ts              # List roadmaps
│   │       ├── show.ts              # Show roadmap detail
│   │       └── control.ts           # Control commands (pause/resume/stop)
│   └── package.json
└── .gitignore
```

## Key Files & Components

**Database Schema:** users (GitHub auth), api_tokens (personal access), roadmaps (agent runs with state/status/repo/branch), roadmap_steps (progress), roadmap_events (audit log)

**Auth Flow:** GitHub OAuth --> JWT token --> Bearer auth for API. Agents use separate API tokens.

**Real-time:** WebSocket push from server to dashboard subscribers on step/event updates.

**CLI Commands:** `catnip-cli login`, `list`, `show <id>`, `pause/resume/stop <id>`

**Frontend Components:** NavBar, StepList with StepIcon/StepItem, ProgressBar, StatusBadge, EventLog, ControlButtons, ConnectionStatus, IssuePanel, PRPanel, ProtectedRoute

## Claude Configuration

- **`.claude/settings.local.json`** -- Permissions: git add/commit/push, gh issue operations
- No CLAUDE.md, rules, or skills
- Worktrees directory at `.claude/worktrees/` (active worktree: `roadmaps-api`)

## Planning & Research Documents

**`Roadmaps/CatnipWebService-Roadmap.md`** -- Complete. Full feature roadmap covering: Railway setup, Cloudflare setup, OAuth, backend scaffolding, auth endpoints, token management, API endpoints, WebSocket real-time, frontend dashboard, deployment config.

**Deferred items:** Agent back-channel (how UI control signals reach remote agents), control signal implementation.

## Git History & Current State

- **Branch:** main
- **Working tree:** Clean
- **Recent activity (2026-04-06):** Standardize worktree directory, rename cat-herding references, refactor runs to roadmaps

Recent commits:
```
0c6264a chore: standardize worktree directory to .claude/worktrees/
3894133 chore: rename cat-herding -> agentic-roadmaps in roadmap and demo script
ccea5a3 refactor: rename runs to roadmaps across frontend, backend, and CLI
d6daec6 refactor: migrate 1 roadmaps to flat file format
5cb0120 refactor: migrate roadmaps to per-directory File Record structure
0ebecbf docs: add author and GUID metadata to all roadmap files
4db6e8a refactor: move roadmap files from .claude/Features/ to Roadmaps/
01fb5a6 docs: complete feature CatnipWebService -- archive roadmap
ed9ffd9 docs: mark Step 12 as Complete in CatnipWebService Roadmap (#12)
3b390ec feat: add deployment configuration for Railway and Cloudflare Pages (#22)
```

## Build & Test Commands

```bash
# Backend
cd backend
npm run dev              # Dev server (tsx watch)
npm run build            # tsc -> dist/
npm start                # node dist/index.js
npm run start:prod       # Run migrations then start
npm run db:generate      # Drizzle generate
npm run db:migrate       # Run pending migrations
npm test                 # vitest run
npm run demo             # Simulate agent workflow

# Frontend
cd frontend
npm run dev              # Vite dev server (:5173)
npm run build            # tsc + vite build
npm run preview          # Vite preview
npm test                 # vitest run

# CLI
cd cli
npm start                # tsx src/index.ts
```

## Notes

- Monorepo with 3 independent npm projects (backend, frontend, cli) -- no workspace manager
- TypeScript throughout for full type safety
- Recent refactoring renamed "runs" to "roadmaps" across the entire codebase
- Backend uses Hono with WebSocket support via `@hono/node-ws`
- Frontend uses React 19, Vite 6, Tailwind CSS 4, and TanStack Query
- Backend tests cover routes, middleware, and WebSocket handlers
- Frontend tests use Testing Library with jsdom
- Demo script (`scripts/demo-roadmap.ts`) validates API contracts during development
