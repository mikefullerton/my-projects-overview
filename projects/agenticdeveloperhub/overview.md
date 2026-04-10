# agenticdeveloperhub

## Project Summary

A full-stack multi-site web application scaffolded from the configurator (v1.19.0). It provides a shared Hono/PostgreSQL backend with unified auth (email + GitHub OAuth), admin features, feature flags, messaging, and feedback -- plus four Cloudflare-hosted frontends (main, admin, dashboard, api-docs).

## Type & Tech Stack

**Type:** Full-stack multi-site monorepo (npm workspaces)

| Layer | Technology |
|-------|-----------|
| Backend framework | Hono (TypeScript, Node 22) |
| Database | PostgreSQL 16 + Drizzle ORM / drizzle-kit |
| Auth | JWT (jose), bcrypt, GitHub OAuth, unified auth-methods table |
| Frontend (main/admin/dashboard) | React 19, Vite 6, TanStack Router + Query, Tailwind CSS 4 |
| api-docs site | Cloudflare Worker only (no React) |
| Backend hosting | Railway (Docker multi-stage build) |
| Frontend hosting | Cloudflare Workers + Assets |
| Dashboard DB | Cloudflare D1 (SQLite) |
| Testing | vitest |
| CI/CD | GitHub Actions (per-site deploy workflows) |

## GitHub URL

`git@github.com:agentic-cookbook/agenticdeveloperhub.git`

## Directory Structure

```
agenticdeveloperhub/
├── .claude/
│   ├── CLAUDE.md               # Placeholder (to be determined)
│   └── settings.json           # Enables superpowers plugin
├── .github/workflows/          # deploy-main, deploy-admin, deploy-dashboard, deploy-api-docs
├── .site/manifest.json         # Configurator deployment state (v1.19.0)
├── backend/
│   ├── src/
│   │   ├── index.ts            # Server entry (port 3000)
│   │   ├── app.ts              # Hono app wiring: middleware + routes
│   │   ├── auth/               # github.ts, middleware.ts, password.ts, session.ts
│   │   ├── config/env.ts
│   │   ├── db/
│   │   │   ├── schema.ts       # Drizzle schema (12 tables)
│   │   │   ├── client.ts
│   │   │   ├── migrate.ts
│   │   │   ├── seed.ts
│   │   │   └── migrations/     # 0000_ordinary_typhoid_mary.sql, 0001_unified_auth_v1_19.sql
│   │   ├── middleware/         # cors, error, logger, rate-limit
│   │   ├── routes/
│   │   │   ├── auth.ts
│   │   │   ├── health.ts
│   │   │   ├── openapi.ts      # Auto-generated OpenAPI spec
│   │   │   ├── public.ts
│   │   │   └── admin/          # users, flags, messaging, feedback, settings, api-tokens
│   │   └── services/           # feature-flags, messaging, settings
│   ├── drizzle.config.ts
│   └── package.json
├── shared/
│   └── src/
│       ├── index.ts
│       ├── types.ts            # User, Auth, FeatureFlag, Feedback, etc.
│       ├── constants.ts
│       └── api-client.ts       # Typed API client for frontends
├── sites/
│   ├── main/                   # Public site (React + Vite + Cloudflare Worker)
│   ├── admin/                  # Admin panel (React + Vite + Cloudflare Worker)
│   ├── dashboard/              # User dashboard (React + Vite + Cloudflare + D1)
│   └── api-docs/               # API docs (Cloudflare Worker, no React)
├── docs/
│   ├── planning/planning.md    # Placeholder
│   └── project/description.md  # Placeholder
├── Dockerfile                  # Multi-stage backend build (node:22-alpine)
├── docker-compose.yml          # Local PostgreSQL 16
├── railway.toml                # Railway deploy config (healthcheck /api/health)
├── package.json                # Root workspace
├── .env / .env.example
└── .gitignore
```

## Key Files & Components

### Database Schema (`backend/src/db/schema.ts`, 12 tables)

- **users** -- core user (id, email, role, displayName, avatarUrl, emailVerified)
- **userAuthMethods** -- unified provider table (password, github, google, apple)
- **userCapabilities** -- fine-grained permissions (e.g. `admin:users`, `api:write`)
- **refreshTokens** -- JWT refresh rotation with revocation + replacement chain
- **apiTokens** -- API keys with per-token capabilities
- **settings** -- JSONB key/value app settings
- **featureFlags** -- with JSON rule payload
- **messageLog** -- email/SMS delivery tracking
- **feedbackSubmissions** -- feedback with admin workflow
- **notificationPreferences** -- per-user, per-category email/SMS opt-in
- **integrationConnections** -- third-party OAuth (Google Calendar, etc.) with sync state
- **schemaVersions** -- migration tracking

### API Routes (`backend/src/app.ts`)

Public: `/api/health`, `/api/auth`, `/api/auth/github`, `/api/openapi.json`, `/api/public`

Admin (auth + admin role): `/api/admin/{users,flags,messaging,feedback,settings,api-tokens}`

### Shared Package

`shared/src/` exports TypeScript types and a typed API client consumed by all frontend sites.

### Deployment State (from `.site/manifest.json`)

All 5 services show as deployed (as of 2026-04-09):

| Service | Platform | URL |
|---------|----------|-----|
| backend | Railway | backend-production-5770.up.railway.app |
| main | Cloudflare | agenticdeveloperhub-main.mwfullerton.workers.dev |
| admin | Cloudflare | agenticdeveloperhub-admin.mwfullerton.workers.dev |
| dashboard | Cloudflare + D1 | agenticdeveloperhub-dashboard.mwfullerton.workers.dev |
| api-docs | Cloudflare | agenticdeveloperhub-api-docs.mwfullerton.workers.dev |

Custom domains: `agenticdeveloperhub.com`, `admin.`, `dashboard.`, `api.`, `backend.`

Features enabled: auth (email + github, admin seeded), featureFlags, observability (built-in), structured logging. Disabled: email, sms, abTesting, 2FA, emailVerification.

## Claude Configuration

- **`.claude/CLAUDE.md`** -- 12 lines, all placeholders (tech stack, build, architecture marked "to be determined").
- **`.claude/settings.json`** -- Enables `superpowers@claude-plugins-official` plugin.

## Planning & Research Documents

- `docs/planning/planning.md` -- "(to be determined)"
- `docs/project/description.md` -- Placeholder (title only, no content)

Both files are scaffolded stubs yet to be filled in.

## Git History & Current State

**Branch:** `main` -- clean working tree (zero staged/unstaged/untracked)

```
e63711c chore: update manifest with v1.19.0 deployment state and api-docs service
8bcecc0 feat: upgrade to configurator v1.19.0 -- unified auth, admin features, API docs
5ecf294 chore: update manifest with deployment URLs
183abc6 chore: add initial database migration
fe108e9 feat: initial scaffold from configurator v1.18.0
ec00627 Initial project scaffolding
```

Only 6 commits; project was initialized 2026-04-09 and immediately upgraded from configurator v1.18.0 -> v1.19.0.

## Build & Test Commands

```bash
# Install
npm install

# Start local PostgreSQL
docker compose up -d

# Development (runs backend + main + admin + dashboard concurrently)
npm run dev

# Build individual workspaces
npm run build:shared
npm run build:backend
npm run build:main
npm run build:admin
npm run build:dashboard
npm run build:all

# Database
npm run db:generate         # drizzle-kit generate
npm run db:migrate          # tsx src/db/migrate.ts
npm run db:seed             # seed admin user

# Deploy Cloudflare sites
npm run deploy:main
npm run deploy:admin
npm run deploy:dashboard
npm run deploy:all
# Backend deploys to Railway via git push (Dockerfile)

# Test
npm run test -w backend     # vitest
```

## Notes

- Very early-stage: 6 commits, all project docs (CLAUDE.md, planning.md, description.md) are placeholders.
- Generated entirely by the configurator scaffolding tool -- structure closely mirrors the standard configurator v1.19.0 template.
- Dashboard site uniquely binds a Cloudflare D1 (SQLite) database (id `7a324733-3cbd-4b81-8a6a-daf72f8b2760`) in addition to the shared PostgreSQL backend.
- OAuth providers: GitHub (implemented); Google/Apple scaffolded in the schema but not wired up.
- Optional integrations: Postmark (email) and Twilio (SMS) -- env vars commented out, currently disabled.
- The `.env` file is tracked in the repo despite `.gitignore` listing `.env` -- but it's byte-identical to `.env.example` (1656 bytes), so no real secrets are committed.
- Backend healthcheck path `/api/health` is wired into `railway.toml`.
- The api-docs site is a pure Cloudflare Worker (no React bundle) and likely serves the OpenAPI spec generated by `backend/src/routes/openapi.ts`.
