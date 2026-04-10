# Catnip

## Project Summary

A hosted web service that monitors autonomous Claude Code agent progress in real-time with a React dashboard and WebSocket push. When running multiple Claude Code agents autonomously, it's difficult to track their progress. Catnip provides a production-grade full-stack web service with a real-time dashboard showing what each agent is doing, replacing an earlier local-only Python progress tool. Features GitHub OAuth authentication, REST + WebSocket APIs, and a CLI for reporting agent status.

## Type & Tech Stack

**Type:** Full-Stack Web Service (Agent Monitoring/Dashboard)

**Tech Stack:**
- **Backend:** TypeScript, Node.js, Hono, Drizzle ORM, PostgreSQL, WebSocket (@hono/node-ws)
- **Frontend:** TypeScript, React 19, Vite 6, Tailwind CSS 4, React Router 7, TanStack Query
- **CLI:** TypeScript (tsx)
- **Testing:** Vitest (backend + frontend), Testing Library + jsdom
- **Hosting:** Railway (backend + PostgreSQL), Cloudflare Pages (frontend)
- **Authentication:** GitHub OAuth with JWT bearer tokens

## GitHub URL

https://github.com/mikefullerton/catnip

## Directory Structure

```
.
├── .claude/              # Claude Code configuration
│   ├── settings.local.json
│   └── worktrees/
├── docs/
│   └── project/
│       └── description.md
├── backend/              # Node.js + Hono API server
│   ├── src/
│   │   ├── index.ts      # Server entry point
│   │   ├── db/           # Database schema, migrations, client
│   │   ├── routes/       # API endpoints (REST + WebSocket)
│   │   ├── auth/         # GitHub OAuth, JWT handling
│   │   ├── models/       # TypeScript types and interfaces
│   │   └── (other modules)
│   ├── scripts/
│   │   └── demo-roadmap.ts   # Demo script
│   ├── package.json
│   ├── tsconfig.json
│   ├── drizzle.config.ts
│   └── vitest.config.ts
├── frontend/             # React + Vite dashboard
│   ├── src/
│   │   ├── main.tsx      # React entry point
│   │   ├── App.tsx       # Root component
│   │   ├── pages/        # Page components
│   │   ├── components/   # Reusable components
│   │   ├── hooks/        # Custom React hooks
│   │   ├── styles/       # Tailwind CSS configuration
│   │   └── (other modules)
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   └── vitest.config.ts
├── cli/                  # Node.js CLI for agent reporting
│   ├── src/
│   │   └── (CLI implementation)
│   ├── package.json
│   └── tsconfig.json
├── Roadmaps/             # Feature planning (File Record structure)
│   └── (roadmap files)
├── package.json          # Root workspace configuration (if any)
├── .gitignore
└── README.md
```

## Key Files & Components

**Backend (src/):**
- `index.ts` — Server entry point with middleware and route setup
- `db/` — Drizzle ORM schema, migrations, client initialization
- `routes/` — API endpoints and WebSocket handlers
- `auth/` — GitHub OAuth flow and JWT token generation/validation
- `models/` — TypeScript interfaces for agents, runs, events

**Frontend (src/):**
- `main.tsx` — React application bootstrap
- `App.tsx` — Root component with routing
- `pages/` — Page components (dashboard, run details, etc.)
- `components/` — Reusable UI components
- `hooks/` — Custom hooks (WebSocket integration, API queries)
- TanStack Query for data fetching and caching
- React Router 7 for client-side routing

**CLI (src/):**
- Agent CLI tool for reporting progress to Catnip server
- Used by Claude Code agents to push updates

**Configuration Files:**
- `backend/drizzle.config.ts` — Database ORM configuration
- `frontend/vite.config.ts` — Frontend build configuration
- `frontend/tailwind.config.ts` — Tailwind CSS customization

**Deployment:**
- Railway deployment (backend + PostgreSQL)
- Cloudflare Pages deployment (frontend SPA)

## Claude Configuration

**Location:** `.claude/settings.local.json`

**Permissions:**
- Allows git operations (add, commit, push)
- Allows gh issue commands for GitHub integration
- Supports worktree-based development

## Planning & Research Documents

**Feature Planning:**
- `Roadmaps/` — Feature roadmaps in File Record structure format
- Historical roadmaps show completion of major features:
  - CatnipWebService feature (archived)
  - Steps tracking (11-12 completed)

**Project Documentation:**
- `docs/project/description.md` — Project purpose, features, tech stack, and status

## Git History & Current State

**Current Branch:** main

**Remote:** git@github.com:mikefullerton/catnip.git

**Recent Commits:**
- `b473105` — docs: add standardized project description
- `0c6264a` — chore: standardize worktree directory to .claude/worktrees/
- `3894133` — chore: rename cat-herding → agentic-roadmaps in roadmap and demo script
- `ccea5a3` — refactor: rename runs to roadmaps across frontend, backend, and CLI
- `d6daec6` — refactor: migrate 1 roadmaps to flat file format
- `5cb0120` — refactor: migrate roadmaps to per-directory File Record structure
- `0ebecbf` — docs: add author and GUID metadata to all roadmap files
- `4db6e8a` — refactor: move roadmap files from .claude/Features/ to Roadmaps/
- `01fb5a6` — docs: complete feature CatnipWebService — archive roadmap
- `ed9ffd9` — docs: mark Step 12 as Complete in CatnipWebService Roadmap (#12)
- `3b390ec` — feat: add deployment configuration for Railway and Cloudflare Pages (#22)
- (15+ more commits with features, deployment, and refactoring)

**Status:** Recently completed / stable. Major features complete with ongoing maintenance.

## Build & Test Commands

```bash
# Install dependencies
npm install

# Development - run backend
cd backend
npm run dev              # Watch mode with hot reload

# Development - run frontend
cd frontend
npm run dev              # Vite development server

# Production build
cd backend
npm run build            # TypeScript compilation

cd frontend
npm run build            # Vite build for production
npm run preview          # Preview production build locally

# Database operations
cd backend
npm run db:generate      # Generate migration files
npm run db:migrate       # Run pending migrations
npm run db:migrate:prod  # Run migrations with node (for production)
npm run db:seed          # Seed database with test data

# Testing
cd backend
npm run test             # Run Vitest suite

cd frontend
npm run test             # Run Vitest suite

# Demo
cd backend
npm run demo             # Run demo-roadmap.ts script

# Production deployment
cd backend
npm run start:prod       # Run migrations then start server
```

## Notes

- Full-stack monorepo with backend, frontend, and CLI in separate directories
- Backend uses Hono framework for lightweight HTTP server with WebSocket support
- WebSocket integration via @hono/node-ws for real-time push updates to clients
- GitHub OAuth provides secure multi-user authentication
- JWT bearer tokens for stateless API authentication
- PostgreSQL database with Drizzle ORM for type-safe queries
- React 19 with modern hooks and functional components
- TanStack Query for sophisticated data fetching and caching
- React Router 7 for client-side navigation
- Tailwind CSS 4 for responsive styling
- Vitest for both backend and frontend testing with jsdom for browser simulation
- Dashboard shows real-time agent progress with WebSocket updates
- CLI tool enables agents to push status updates autonomously
- Feature planning uses File Record structure for roadmap organization
- Recent refactoring renamed "runs" to "roadmaps" for better semantics
- Deployment to Railway (backend) and Cloudflare Pages (frontend)
- Production backend runs migrations automatically on startup
- Replaced earlier local-only Python progress tracking tool
- Related to Whippet (native macOS menu bar app approach) and Catnip Terminal (terminal emulator)
