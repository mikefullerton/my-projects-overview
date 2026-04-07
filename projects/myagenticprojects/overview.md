# MyAgenticProjects

## Project Summary

MyAgenticProjects is a full-stack SaaS platform bootstrapped from site-manager v1.3.0. Features a Hono backend API with PostgreSQL, three React+TypeScript frontends on Cloudflare Workers, shared type definitions, and integrated auth, feature flags, messaging, and feedback systems.

## Type & Tech Stack

- **Project Type:** Full-stack SaaS Application (multi-site architecture)
- **Backend:** Hono 4.7.0, Node.js 22, TypeScript 5.7, PostgreSQL 16, Drizzle ORM 0.39.0
- **Auth:** JWT (jose 6.0.0), bcrypt, GitHub/Google OAuth
- **Validation:** Zod 3.24.0
- **Frontend (3 SPAs):** React 19, TanStack Router 1.93.0, TanStack React Query 5.62.0, Tailwind CSS 4, Vite 6
- **Deployment:** Railway (backend/Docker), Cloudflare Workers (frontends)
- **Shared Library:** TypeScript + Zod schemas for all apps

## GitHub URL

`git@github.com:agentic-cookbook/myagenticprojects.git`

## Directory Structure

```
myagenticprojects/
├── .env.example, .env
├── docker-compose.yml                 # Local PostgreSQL
├── Dockerfile                         # Multi-stage production build
├── railway.toml
├── package.json                       # npm workspaces monorepo
├── site-manifest.json                 # Deployment URLs
├── .site/manifest.json                # site-manager v1.3.0 config
├── .github/workflows/                 # deploy-main.yml, deploy-admin.yml, deploy-dashboard.yml
├── shared/
│   └── src/                           # index.ts, types.ts, constants.ts, api-client.ts
├── backend/
│   └── src/
│       ├── index.ts, app.ts
│       ├── routes/                    # health, auth, public, admin/{users,flags,messaging,feedback}
│       ├── auth/                      # middleware, session, password, github OAuth
│       ├── db/
│       │   ├── schema.ts             # users, oauth_accounts, feature_flags, message_logs, feedback_submissions
│       │   ├── client.ts, migrate.ts, seed.ts, migrations/
│       └── middleware/
├── sites/
│   ├── main/                          # Public-facing website (React + Vite + Tailwind + Cloudflare Worker)
│   ├── admin/                         # Admin dashboard (users, flags, messaging, feedback routes)
│   └── dashboard/                     # Dashboard with D1 SQLite
└── node_modules/
```

## Key Components

**Database Schema:** users, oauth_accounts, feature_flags, message_logs, feedback_submissions

**API Routes:** health, auth (register/login/refresh), public endpoints, admin CRUD for users/flags/messaging/feedback

**Auth:** Email/password + GitHub/Google OAuth, JWT access+refresh tokens, bcrypt

**Deployment:** Railway backend at `myagenticprojects-backend-production.up.railway.app`, 3 Cloudflare Workers frontends with GitHub Actions auto-deploy

## Claude Configuration

No `.claude/` directory. Default Claude Code behavior.

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Working tree:** Clean
- **Recent (2026-04-06):** Seed script updates, manifest deployment URLs, site-manager v1.3.0 template updates
- **11 commits total** — scaffolded from site-manager, then deployed

## Build & Test Commands

```bash
npm run dev               # Run all services concurrently
npm run build:all         # Build shared + backend + all sites
npm run deploy:all        # Deploy all sites
npm run db:migrate        # Run migrations
npm run db:seed           # Seed admin user

# Individual workspaces
npm run dev -w backend    # Backend dev (:3000)
npm run dev -w sites/main # Frontend dev (:5173)
npm test -w backend       # Vitest
```

Local: `docker-compose up` (PostgreSQL) → `npm install` → `npm run db:migrate` → `npm run db:seed` → `npm run dev`

## Notes

- npm workspaces monorepo with shared types
- Scaffolded from agentic-cookbook's site-manager v1.3.0
- Feature flags, messaging (Postmark), SMS (Twilio) configured but not yet active
- No README.md or CLAUDE.md currently
