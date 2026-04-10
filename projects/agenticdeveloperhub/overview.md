# AgenticDeveloperHub

## Project Summary

A full-stack web application providing a unified hub for the agentic ecosystem. AgenticDeveloperHub features multiple sites (main, admin, dashboard, API docs) with a shared backend, database, and authentication system. Built from the Configurator v1.19.0 template with unified authentication and admin features.

## Type & Tech Stack

**Type:** Full-Stack Web Application (Multi-site Monorepo)

**Tech Stack:**
- **Frontend:** TypeScript, React, Vite, Tailwind CSS 4
- **Backend:** TypeScript, Node.js, Hono, Drizzle ORM, PostgreSQL
- **Runtime:** npm workspaces
- **Deployment:** Railway (backend + PostgreSQL), Cloudflare Pages (frontend)
- **Auth:** Unified auth system (inherited from Configurator)
- **Testing:** vitest

## GitHub URL

https://github.com/agentic-cookbook/agenticdeveloperhub

## Directory Structure

```
.
├── .claude/              # Claude Code configuration
│   ├── CLAUDE.md
│   └── settings.json
├── .github/              # GitHub workflows and CI/CD
├── .site/                # Deployment configuration
├── docs/
│   ├── planning/
│   │   └── planning.md
│   └── project/
│       └── description.md
├── backend/              # Shared backend API (Hono + Drizzle)
│   ├── src/
│   │   ├── index.ts      # Server entry point
│   │   ├── db/           # Database schema and migrations
│   │   ├── routes/       # API endpoints
│   │   └── (other modules)
│   ├── package.json
│   ├── tsconfig.json
│   └── drizzle.config.ts
├── shared/               # Shared TypeScript types and utilities
│   ├── src/
│   │   └── (shared code)
│   └── package.json
├── sites/                # Multiple frontend sites
│   ├── main/             # Main site
│   │   ├── src/
│   │   ├── package.json
│   │   └── vite.config.ts
│   ├── admin/            # Admin panel
│   │   ├── src/
│   │   └── package.json
│   ├── dashboard/        # Dashboard
│   │   ├── src/
│   │   └── package.json
│   └── api-docs/         # API documentation
│       ├── src/
│       └── package.json
├── Dockerfile            # Backend container image
├── docker-compose.yml    # Local development setup
├── package.json          # Root workspace configuration
├── railway.toml          # Railway deployment config
├── .env                  # Environment variables (local)
├── .env.example          # Environment template
└── .gitignore
```

## Key Files & Components

**Root Configuration:**
- `package.json` — npm workspaces configuration with dev/build scripts
- `docker-compose.yml` — PostgreSQL container for local development
- `Dockerfile` — Backend container image

**Backend (Hono + Drizzle):**
- `backend/src/index.ts` — Server entry point
- `backend/src/db/` — Database schema, migrations, seed
- `backend/src/routes/` — API endpoint handlers
- `backend/drizzle.config.ts` — ORM configuration

**Shared Code:**
- `shared/src/` — Shared TypeScript types and utilities used by all sites

**Frontend Sites:**
- `sites/main/` — Main public-facing site (React + Vite + Tailwind)
- `sites/admin/` — Admin panel for managing the ecosystem
- `sites/dashboard/` — Dashboard with monitoring/analytics
- `sites/api-docs/` — Interactive API documentation

**Environment Configuration:**
- `.env` — Local development environment variables
- `.env.example` — Template for required env vars
- `.site/` — Deployment configuration files

## Claude Configuration

**Location:** `.claude/CLAUDE.md` and `.claude/settings.json`

**settings.json:**
- Enables superpowers plugin (official Claude plugins)

## Planning & Research Documents

**Planning:**
- `docs/planning/planning.md` — Development roadmap and feature planning

**Project Documentation:**
- `docs/project/description.md` — Project purpose, features, tech stack, and status

## Git History & Current State

**Current Branch:** main

**Remote:** git@github.com:agentic-cookbook/agenticdeveloperhub.git

**Recent Commits:**
- `e63711c` — chore: update manifest with v1.19.0 deployment state and api-docs service
- `8bcecc0` — feat: upgrade to configurator v1.19.0 — unified auth, admin features, API docs
- `5ecf294` — chore: update manifest with deployment URLs
- `183abc6` — chore: add initial database migration
- `fe108e9` — feat: initial scaffold from configurator v1.18.0
- `ec00627` — Initial project scaffolding

**Status:** Active development. Recently upgraded to Configurator v1.19.0 with unified auth and admin features.

## Build & Test Commands

```bash
# Install dependencies
npm install

# Development - run all sites and backend concurrently
npm run dev

# Build individual workspaces
npm run build:shared     # Build shared utilities
npm run build:backend    # Build API backend
npm run build:main       # Build main site
npm run build:admin      # Build admin site
npm run build:dashboard  # Build dashboard
npm run build:all        # Build everything

# Deployment
npm run deploy:main      # Deploy main site
npm run deploy:admin     # Deploy admin site
npm run deploy:dashboard # Deploy dashboard

# Database
npm run db:generate      # Generate migration files
npm run db:migrate       # Run pending migrations
npm run db:seed          # Seed database with initial data

# Testing (backend)
npm run test -w backend  # Run backend tests with vitest
```

## Notes

- Multi-site monorepo using npm workspaces for code sharing
- All sites share the same backend API (Hono + Drizzle ORM)
- Shared code in `shared/` workspace used by backend and all frontend sites
- PostgreSQL database shared by all sites and backend
- Authentication is unified across all sites
- Recent upgrade to Configurator v1.19.0 adds admin panel and API docs
- Local development uses docker-compose for PostgreSQL
- Frontend sites use Vite for fast development and optimized builds
- Each site can be independently deployed to Cloudflare Pages
- Backend deploys to Railway with auto-migrations
- Uses TypeScript across entire stack for type safety
- Development workflow supports concurrent running of all sites/backend
- Configuration template inherited from Configurator project template
