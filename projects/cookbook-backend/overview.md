# cookbook-backend

## Project Summary

Backend API service (plus co-located auth service and admin/dashboard frontends) for managing and serving recipes for the Agentic Cookbook application. Organized as an npm workspaces monorepo containing a Hono/Drizzle/Postgres backend, a separate auth service, a shared types package, and two Cloudflare Workers React sites.

## Type & Tech Stack

- **Type**: Monorepo (npm workspaces) containing multiple deployable services
- **Languages**: TypeScript (ESM, Node 22)
- **Backend (`backend/`)**: Hono 4, @hono/node-server, Drizzle ORM 0.39, Postgres (`postgres` driver), Zod, `jose` (JWT), `bcrypt`, Vitest
- **Auth service (`auth/`)**: Hono 4, Drizzle ORM 0.38, `pg` driver, `jose`, `bcryptjs`, `uuid`, Zod
- **Shared (`shared/`)**: TypeScript types library built with `tsc`, Zod
- **Admin site (`sites/admin/`)**: React 19, Vite 6, TanStack Query + Router, Tailwind 4, deployed as a Cloudflare Worker (static assets via `ASSETS` binding)
- **Dashboard site (`sites/dashboard/`)**: React 19, Vite 6, TanStack Query + Router, Tailwind 4, Cloudflare Worker with a D1 database binding (`cookbook-backend-dashboard-db`)
- **Infrastructure**: Docker + Railway for `backend` and `auth`; Cloudflare Workers/D1 for the two sites; local Postgres 16 via `docker-compose.yml`

## GitHub URL

git@github.com:agentic-cookbook/cookbook-backend.git

## Directory Structure

```
cookbook-backend/
├── .claude/
│   ├── CLAUDE.md
│   └── settings.json
├── auth/                       # Auth service (Hono + Drizzle + pg)
│   ├── Dockerfile
│   ├── drizzle.config.ts
│   ├── package.json
│   ├── railway.toml
│   ├── tsconfig.json
│   └── src/
│       ├── app.ts
│       ├── index.ts
│       ├── auth/
│       ├── config/
│       ├── db/
│       ├── middleware/
│       └── routes/
├── backend/                    # Main API (Hono + Drizzle + postgres)
│   ├── drizzle.config.ts
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
│       ├── app.ts
│       ├── index.ts
│       ├── auth/
│       ├── config/
│       ├── db/
│       │   ├── client.ts
│       │   ├── migrate.ts
│       │   ├── schema.ts
│       │   ├── seed.ts
│       │   └── migrations/
│       ├── middleware/
│       ├── routes/
│       │   ├── admin/
│       │   ├── auth.ts
│       │   ├── health.ts
│       │   └── public.ts
│       └── services/
│           ├── feature-flags.ts
│           ├── messaging.ts
│           └── settings.ts
├── shared/                     # Shared TS types/zod schemas package
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
├── sites/
│   ├── admin/                  # React 19 admin UI on CF Workers
│   │   ├── package.json
│   │   ├── vite.config.ts
│   │   ├── wrangler.jsonc
│   │   ├── tailwind.config.ts
│   │   └── src/
│   └── dashboard/              # React 19 dashboard on CF Workers + D1
│       ├── migrations/
│       ├── package.json
│       ├── vite.config.ts
│       ├── wrangler.jsonc
│       ├── worker/
│       └── src/
├── docs/
│   ├── planning/planning.md
│   └── project/description.md
├── docker-compose.yml          # Local Postgres 16
├── Dockerfile                  # Builds backend for Railway
├── railway.toml                # Railway config for backend
├── package.json                # Workspace root
├── package-lock.json
└── README.md
```

## Key Files & Components

- **`package.json`** (root) — npm workspaces for `shared`, `backend`, `auth`, `sites/admin`, `sites/dashboard`. Defines `dev` (concurrently runs all four services), `build:*`, `deploy:*`, and `db:*` scripts.
- **`Dockerfile`** — Multi-stage Node 22 Alpine build for the main `backend` service. Entrypoint runs `backend/dist/db/migrate.js` then `backend/dist/index.js`, copying migration SQL into the image.
- **`railway.toml`** — Railway deploy config for the backend, healthcheck `/api/health`.
- **`auth/Dockerfile`** + **`auth/railway.toml`** — Separate Railway service for the auth API, port 3001, healthcheck `/health`.
- **`docker-compose.yml`** — Local Postgres 16 (`cookbook-backend_dev`, user/pass `postgres`, port 5432).
- **`backend/src/db/schema.ts`**, **`backend/src/db/migrate.ts`**, **`backend/src/db/migrations/`** — Drizzle schema, runtime migrator, and generated SQL migrations.
- **`backend/src/routes/`** — `health.ts`, `auth.ts`, `public.ts`, plus `admin/` subroutes.
- **`backend/src/services/`** — `feature-flags.ts`, `messaging.ts`, `settings.ts`.
- **`sites/admin/wrangler.jsonc`** — Cloudflare Worker serving built Vite assets; `API_BACKEND_URL` points at the deployed Railway backend (`https://backend-production-8dd93.up.railway.app`).
- **`sites/dashboard/wrangler.jsonc`** — Same pattern plus a D1 database binding (`cookbook-backend-dashboard-db`, id `d93842d4-8966-43da-bc4e-b454a4991a97`) and `MAIN_SITE_URL` / `ADMIN_SITE_URL` vars pointing at `agentic-cookbook.com` and `admin.agentic-cookbook.com`.

## Claude Configuration

- **`.claude/CLAUDE.md`** — Stub-level; names the project and leaves Tech Stack / Build / Architecture as "(to be determined)".
- **`.claude/settings.json`** — Enables the `superpowers@claude-plugins-official` plugin. No hooks or custom permissions.

## Planning & Research Documents

- **`docs/planning/planning.md`** — Placeholder ("(to be determined)").
- **`docs/project/description.md`** — One-line standardized description: "Backend API service for managing and serving recipes for the cookbook application".
- No `research/` directory.

## Git History & Current State

- **Remote**: `git@github.com:agentic-cookbook/cookbook-backend.git`
- **Current branch**: `main`
- **Working tree**: clean
- **Recent commits**:
  - `81f6aa4` Deploy: update wrangler configs, lower min password length, add lockfile
  - `2068972` Add generated backend database migration
  - `26ccece` Scaffold full project: backend API, admin site, dashboard, and auth service
  - `c98feb1` Initial project scaffolding

Project is early-stage — four commits total, freshly scaffolded monorepo with the backend already wired to a live Railway deployment.

## Build & Test Commands

From repo root (all via npm workspaces):

- `npm run dev` — runs `backend`, `auth`, `sites/admin`, and `sites/dashboard` concurrently
- `npm run build:shared` / `build:backend` / `build:auth` / `build:admin` / `build:dashboard` / `build:all`
- `npm run deploy:admin` / `deploy:dashboard` / `deploy:all` — Vite build + `wrangler deploy`
- `npm run db:generate` — Drizzle kit migration generation (backend)
- `npm run db:migrate` — apply migrations to Postgres (backend)
- `npm run db:seed` — seed backend database

Per-workspace:

- `backend`: `npm run dev` (tsx watch), `build` (tsc), `start:prod` (migrate + start), `test` (vitest)
- `auth`: `npm run dev`, `build`, `start`, `db:generate`, `db:migrate`, `db:seed`
- `sites/admin`, `sites/dashboard`: `npm run dev` (vite), `build`, `preview` (wrangler dev), `deploy` (vite build + wrangler deploy); dashboard also has `db:migrate` targeting D1

Local infra: `docker compose up` for the Postgres dev database.

## Notes

- Despite the repo name "cookbook-backend", this is effectively a full-stack monorepo for the Agentic Cookbook product — it also contains the admin site, user dashboard, and a standalone auth service. The name reflects its origin as the backend repo that later absorbed the other services.
- Two different Postgres drivers in use: `postgres` (postgres.js) in `backend/`, and `pg` (node-postgres) in `auth/`. Drizzle ORM versions also differ slightly (0.39 vs 0.38). A future harmonization target.
- Two different bcrypt libraries: `bcrypt` (native) in backend, `bcryptjs` (pure JS) in auth.
- `backend/` is deployed to Railway via the root `Dockerfile` + `railway.toml`; `auth/` is deployed to Railway via its own `auth/Dockerfile` + `auth/railway.toml`. Note `auth/Dockerfile` installs pnpm but then uses `npm install --frozen-lockfile`, which is inconsistent and likely a scaffolding bug.
- Both Cloudflare Workers sites hard-code the Railway backend URL (`backend-production-8dd93.up.railway.app`) as a `vars` entry in their `wrangler.jsonc` — no environment separation yet.
- The dashboard site uses Cloudflare D1 (SQLite) in addition to calling the Railway backend, suggesting it stores some per-user dashboard state at the edge.
- `.claude/CLAUDE.md` is a scaffolding stub — Tech Stack, Build, and Architecture sections all say "(to be determined)". Worth filling in now that the project has real structure.
- Superpowers plugin is enabled in `.claude/settings.json`.
- Tech stack leans heavily on recent versions: React 19, Vite 6, Tailwind 4, Hono 4, Drizzle 0.39, Wrangler 3.99, Node 22.
