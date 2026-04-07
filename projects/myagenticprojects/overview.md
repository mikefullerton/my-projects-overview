# MyAgenticProjects

## Project Summary

MyAgenticProjects is a full-stack SaaS platform bootstrapped from site-manager v1.3.0. Features a Hono backend API with PostgreSQL on Railway, three React+TypeScript frontends on Cloudflare Workers, shared type definitions, and integrated auth, feature flags, messaging, and feedback systems. All services are deployed and live.

## Type & Tech Stack

- **Project Type:** Full-stack SaaS Application (multi-site monorepo)
- **Backend:** Hono 4.7.0, Node.js 22, TypeScript 5.7, PostgreSQL 16, Drizzle ORM 0.39.0
- **Auth:** JWT (jose 6.0.0), bcrypt, GitHub/Google OAuth, email/password
- **Validation:** Zod 3.24.0
- **Frontend (3 SPAs):** React 19, TanStack Router, TanStack React Query, Tailwind CSS 4, Vite
- **Deployment:** Railway (backend via Docker), Cloudflare Workers (3 frontends via GitHub Actions)
- **Database:** PostgreSQL 16 (Railway) + D1 SQLite (dashboard)
- **Shared Library:** TypeScript + Zod schemas for cross-app types
- **Package Manager:** npm workspaces monorepo
- **Domain:** myagenticprojects.com (DNS not yet pointed to Cloudflare)

## GitHub URL

`git@github.com:agentic-cookbook/myagenticprojects.git`

## Directory Structure

```
myagenticprojects/
├── .env, .env.example                 # Environment variables
├── docker-compose.yml                 # Local PostgreSQL 16-alpine
├── Dockerfile                         # Multi-stage Node 22 production build
├── railway.toml                       # Railway deployment config
├── package.json                       # npm workspaces monorepo root
├── site-manifest.json                 # Public deployment URLs
├── .site/
│   ├── manifest.json                  # site-manager v1.3.0 config
│   └── issues.json                    # Known deployment issues (2 blocking, 3 warnings)
├── .github/workflows/
│   ├── deploy-main.yml                # Auto-deploy main site on push
│   ├── deploy-admin.yml               # Auto-deploy admin site on push
│   └── deploy-dashboard.yml           # Auto-deploy dashboard on push
├── shared/
│   └── src/                           # index.ts, types.ts, constants.ts, api-client.ts
├── backend/
│   └── src/
│       ├── index.ts, app.ts           # Hono server entry
│       ├── routes/                    # health, auth, public, admin/{users,flags,messaging,feedback}
│       ├── auth/                      # middleware, session, password, github OAuth
│       ├── db/
│       │   ├── schema.ts             # users, oauth_accounts, feature_flags, message_logs, feedback_submissions
│       │   ├── client.ts, migrate.ts, seed.ts, migrations/
│       └── middleware/, services/, config/
├── sites/
│   ├── main/                          # Public-facing website (wrangler.jsonc)
│   ├── admin/                         # Admin dashboard
│   └── dashboard/                     # Dashboard with D1 SQLite
└── node_modules/
```

## Key Files & Components

**Database Schema:** users, oauth_accounts, feature_flags, message_logs, feedback_submissions (Drizzle ORM + PostgreSQL)

**API Routes:** health check, auth (register/login/refresh), public endpoints, admin CRUD for users/flags/messaging/feedback

**Auth System:** Email/password + GitHub/Google OAuth, JWT access+refresh tokens, bcrypt password hashing

**Deployment Pipeline:**
- Backend: Railway (Docker multi-stage build, healthcheck at `/api/health`)
- Main site: `myagenticprojects-main.mwfullerton.workers.dev`
- Admin site: `myagenticprojects-admin.mwfullerton.workers.dev`
- Dashboard: `myagenticprojects-dashboard.mwfullerton.workers.dev`

**Known Issues (.site/issues.json):**
- BLOCKING: Auth routes return 404 (router not registered in app.ts)
- BLOCKING: DNS not yet pointing to Cloudflare (nameservers still at GoDaddy)
- 3 warnings: missing manifest fields

## Claude Configuration

No `.claude/` directory or `CLAUDE.md`. Default Claude Code behavior.

## Planning & Research Documents

None. Project was scaffolded from site-manager v1.3.0 templates.

## Git History & Current State

- **Branch:** main
- **Working tree:** Clean
- **Total Commits:** 11

**Recent Commits (2026-04-06):**
1. `b9981d8` -- fix: update seed script to support password resets and lower minimum to 10 chars
2. `553f8fe` -- chore: update manifest with deployment URLs
3. `11441c7` -- chore: update templates to site-manager v1.3.0
4. `446f449` -- chore: update manifest with deployment URLs
5. `5b1fcea` -- chore: remove custom domain routes pending DNS setup

**Origin:** Scaffolded from site-manager v1.2.0, then upgraded to v1.3.0

## Build & Test Commands

```bash
npm run dev               # Run all services concurrently (backend + 3 frontends)
npm run build:all         # Build shared + backend + all sites
npm run deploy:all        # Deploy all Cloudflare Worker sites
npm run db:generate       # Generate Drizzle migrations
npm run db:migrate        # Run database migrations
npm run db:seed           # Seed admin user

# Individual workspaces
npm run dev -w backend           # Backend dev (:3000)
npm run dev -w sites/main        # Frontend dev
npm run dev -w sites/admin       # Admin dev
npm run dev -w sites/dashboard   # Dashboard dev
npm test -w backend              # Vitest
```

**Local setup:** `docker-compose up` (PostgreSQL) -> `npm install` -> `npm run db:migrate` -> `npm run db:seed` -> `npm run dev`

## Notes

- npm workspaces monorepo with shared types library
- Scaffolded from agentic-cookbook's site-manager v1.3.0
- All 4 services are deployed (backend on Railway, 3 frontends on Cloudflare Workers)
- Feature flags, messaging (Postmark), SMS (Twilio) configured but not yet active
- Auth routes have a known blocking issue (404s, router not registered)
- Custom domain DNS migration from GoDaddy to Cloudflare still pending
- No README.md or CLAUDE.md currently
