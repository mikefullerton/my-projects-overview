# Official Agent Registry - Project Overview

## Project Summary

The Official Agent Registry is a centralized hub and identity layer for AI agents. It provides unique namespaces, public profiles, verifiable identities, and rich personas for agents—positioning itself as "DNS for AI agents." The platform enables agents to become characters in digital life with discoverable addresses, customizable personas, and reputation tracking.

**Primary domain:** agenticregistry.com  
**Current version:** 0.5.3

---

## Type & Tech Stack

**Project Type:** Full-stack web application (SPA + API) with social/identity features

### Frontend
- **Framework:** Vanilla TypeScript + HTML/CSS
- **Build Tool:** Vite 6.0.0
- **Deployment:** Cloudflare Workers (edge computing)
- **Dependencies:** @cloudflare/vite-plugin, wrangler

### Backend
- **Runtime:** Node.js
- **Framework:** Hono 4.7.0 (lightweight HTTP framework)
- **Database:** PostgreSQL (via Drizzle ORM)
- **Authentication:** GitHub OAuth + JWT (via jose)
- **Validation:** Zod
- **Deployment:** Railway (auto-deploys on push to main)
- **Dev Runtime:** tsx (TypeScript executor)

### Shared Library
- **Purpose:** Shared type definitions across client and server
- **Content:** TypeScript interfaces, constants, types
- **Build:** TypeScript compiler

### Infrastructure
- **Client Hosting:** Cloudflare Workers (agenticregistry)
- **Server Hosting:** Railway (PostgreSQL database)
- **Domain Management:** Cloudflare (DNS, 301 redirects)
- **CI/CD:** GitHub Actions (auto-deploy on client changes)

---

## GitHub URL

```
git@github.com:agentic-cookbook/agenticregistry.git
https://github.com/agentic-cookbook/agenticregistry
```

**Branch:** main (up to date with origin)

---

## Directory Structure

```
agenticregistry/
├── client/                      # Vite SPA + Cloudflare Worker
│   ├── src/
│   │   ├── index.html          # SPA entry point
│   │   ├── main.ts             # Core application logic
│   │   ├── worker.ts           # Cloudflare Worker (reverse proxy)
│   │   ├── env.d.ts            # Environment type definitions
│   │   └── public/             # Static assets (favicon, og image)
│   ├── dist/                   # Built output
│   ├── package.json            # Dependencies (vite, wrangler, CF plugin)
│   ├── vite.config.ts          # Vite configuration
│   ├── wrangler.jsonc          # Cloudflare Worker config
│   └── tsconfig.json
│
├── server/                     # Hono API + PostgreSQL
│   ├── src/
│   │   ├── index.ts           # Entry point (Node.js server)
│   │   ├── app.ts             # Hono app setup
│   │   ├── auth/              # GitHub OAuth + JWT session logic
│   │   │   ├── github.ts
│   │   │   ├── middleware.ts
│   │   │   └── session.ts
│   │   ├── config/
│   │   │   └── env.ts         # Environment variables
│   │   ├── db/
│   │   │   ├── schema.ts      # Drizzle ORM schema (see below)
│   │   │   ├── client.ts      # Database connection
│   │   │   ├── migrate.ts     # Migration runner
│   │   │   └── seed.ts        # Database seeding
│   │   ├── middleware/
│   │   │   ├── logger.ts
│   │   │   └── error.ts
│   │   ├── lib/
│   │   │   ├── pagination.ts
│   │   │   └── crypto.ts
│   │   └── routes/            # API endpoints
│   │       ├── auth.ts        # POST /auth/github/login, /callback, logout
│   │       ├── bots.ts        # CRUD for bot profiles
│   │       ├── keys.ts        # API key management
│   │       ├── runs.ts        # Bot execution runs
│   │       ├── records.ts     # Bot activity records
│   │       ├── events.ts      # Bot events
│   │       ├── query.ts       # Query builder (runs/records/events)
│   │       ├── public.ts      # Public bot profiles
│   │       └── health.ts      # Health check
│   ├── tests/
│   │   └── smoke.ts           # Basic connectivity tests
│   ├── drizzle/               # Migration files
│   ├── .env                   # Environment variables (local dev)
│   ├── .env.example           # Template
│   ├── drizzle.config.ts      # Drizzle CLI config
│   ├── package.json
│   └── tsconfig.json
│
├── shared/                    # Shared TypeScript types
│   ├── src/
│   │   ├── index.ts          # Re-exports types
│   │   ├── types.ts          # Main type definitions (see below)
│   │   └── constants.ts      # Shared constants
│   ├── dist/                 # Compiled output
│   ├── package.json
│   └── tsconfig.json
│
├── docs/
│   ├── research/
│   │   ├── agenticregistry-overview.md     # Vision & business model
│   │   ├── agenticregistry-overview.pdf    # PDF version
│   │   ├── deployment-guide.md                     # Infrastructure setup
│   │   ├── seo-domain-redirect-strategy.md         # Multi-domain SEO strategy
│   │   ├── ai-persona-research.md                  # Research on persona design
│   │   └── ai-persona-template.md                  # Reusable persona template
│   └── .DS_Store
│
├── .claude/                   # Claude Code configuration
│   └── rules/
│       ├── versioning.md      # Strict versioning rule (deploy = version bump)
│       └── commit-and-push.md # Strict git rule (always push after commit)
│
├── .github/
│   └── workflows/
│       └── deploy-client.yml  # Auto-deploy client on push to main
│
├── .superpowers/              # Claude Code integration files (git ignored)
├── VERSION                    # Semver version file (0.5.3)
├── package.json               # Root build script
├── docker-compose.yml         # Local development (PostgreSQL)
├── Dockerfile                 # Server container image
├── railway.toml               # Railway deployment config
└── .gitignore
```

---

## Key Files & Components

### Data Model (Server Database Schema)

**Users Table**
- `id` (UUID, PK)
- `githubId`, `githubLogin` (unique)
- `displayName`, `avatarUrl`
- Timestamps

**Bots Table** (Agent Profiles)
- `id` (UUID, PK)
- `ownerId` (FK → users)
- `slug` (unique per user, the agent's URL path)
- `displayName`, `description`, `botType`
- `config` (JSONB for customizable persona/metadata)
- `isPublic` (discoverable in directory)
- Timestamps
- Index: `(ownerId, slug)` for fast lookups

**API Keys Table** (for external integrations)
- `id`, `userId` (FK), `botId` (optional FK)
- `keyHash`, `keyPrefix` (for masked display)
- `name`, `scopes`, `expiresAt`, `revokedAt`
- `lastUsedAt` (audit trail)

**Runs Table** (Agent Execution Records)
- `id`, `botId` (FK), `parentRunId` (for nesting)
- `runType`, `status` (running/completed/failed/interrupted)
- `data` (JSONB execution context)
- `startedAt`, `completedAt`

**Records Table** (Activity Records)
- `id`, `botId` (FK), `runId` (optional FK)
- `recordType`, `status`, `data` (JSONB)

**Events Table** (Granular Event Log)
- `id`, `botId` (FK), `runId`, `recordId`
- `eventType`, `data` (JSONB)

### API Routes (Hono Server)

| Route | Purpose |
|-------|---------|
| `POST /auth/github/login` | Initiate GitHub OAuth flow |
| `GET /auth/github/callback` | OAuth callback handler |
| `POST /auth/logout` | Clear session |
| `GET /api/user` | Current authenticated user |
| `GET /api/bots` | List user's bots |
| `POST /api/bots` | Create new bot |
| `GET /api/bots/:botId` | Get bot details |
| `PUT /api/bots/:botId` | Update bot |
| `DELETE /api/bots/:botId` | Delete bot |
| `GET /api/bots/:botId/keys` | List API keys for bot |
| `POST /api/bots/:botId/keys` | Create API key |
| `GET /api/bots/:botId/runs` | Query bot runs |
| `POST /api/bots/:botId/runs` | Create run |
| `GET /api/bots/:botId/records` | Query records |
| `POST /api/bots/:botId/records` | Create record |
| `GET /api/bots/:botId/events` | Query events |
| `POST /api/bots/:botId/events` | Create event |
| `POST /api/query` | Advanced query builder |
| `GET /:botSlug` | Public bot profile page |
| `GET /health` | Server health check |

### Client Features (Vite SPA)

- GitHub OAuth login flow
- Bot management (CRUD)
- API key generation & management
- Dashboard with bot profiles
- Data table views for runs, records, events
- Public bot profile pages (profile at `/:botSlug`)
- Bot persona customization UI (stub)

### Cloudflare Worker (Reverse Proxy)

- Serves static SPA assets from `/dist`
- Proxies `/api/*`, `/auth/*`, `/health` to Railway backend
- Serves custom domain: `agenticregistry.com` + `www.agenticregistry.com`

---

## Claude Configuration (.claude/)

### Rules

1. **versioning.md** — STRICT RULE
   - Every deploy MUST bump version in `/VERSION`
   - Update matching versions in `shared/`, `server/`, `client/` package.json files
   - Client reads VERSION at build time via Vite's define global
   - Non-negotiable: version in UI confirms new code is served

2. **commit-and-push.md** — STRICT RULE
   - Always commit AND push together (no local-only commits)
   - Remote must always have latest work

---

## Planning & Research Documents

Located in `docs/research/`:

### agenticregistry-overview.md
- **Purpose:** Vision, business model, and competitive positioning
- **Key sections:**
  - The Problem: Faceless agents need identity
  - The Vision: "DNS for AI agents"
  - Core Features: Unique identity, homepages, discovery, gamification, skills marketplace
  - Business Model: Free tier (1 bot), $10/year paid tier (multiple bots, API, advanced personas)
  - Flywheel: Naming lock-in → engagement → viral personas → discovery → reputation → marketplace
  - Domain Portfolio: 12+ domain variants secured, all redirect to primary

### deployment-guide.md
- Client → Cloudflare Worker (automated via GitHub Actions)
- Server → Railway (auto-deploy on push)
- Environment variables: CLIENT_URL, CORS_ORIGIN, GitHub OAuth credentials, SESSION_SECRET, DATABASE_URL
- GitHub OAuth App credentials & setup
- Version bumping procedure
- DNS/Cloudflare management (Zone ID, custom domains)
- Troubleshooting: SSL 525, OAuth redirect_uri mismatches

### ai-persona-research.md
- Research on designing AI personas for LLM products
- Key structural ingredients: who they are, values, communication style, constraints, sample interactions
- Full vs. lightweight personas (Charlie persona example, Biff iOS reviewer example)
- Principles: persona serves function, constrained output, explicit non-behaviors, emotional tone

### ai-persona-template.md
- Reusable markdown template for defining AI personas
- Sections: Identity, Purpose & Desire, Backstory, Values, Personality Traits, Contradictions, Emotional Range, Voice & Communication, Relationship Model, Growth Arc, Anti-Patterns, Sample Interactions

### seo-domain-redirect-strategy.md
- 301 redirects (permanent, pass link equity)
- Canonical domain setup (www vs. non-www, https mandatory)
- Cloudflare Bulk Redirects implementation
- Google Search Console multi-domain management
- GoDaddy domain management (transfer DNS to Cloudflare)

---

## Git History & Current State

**Current branch:** main  
**Status:** Clean working tree (no uncommitted changes)  
**Remote:** origin (github.com:agentic-cookbook/agenticregistry.git)

### Recent Commits (Last 5)

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| b123d23 | 2026-04-06 16:18 | Claude | chore: standardize worktree directory to .claude/worktrees/ |
| 675811e | 2026-04-05 10:35 | Claude | docs: add generalized AI persona research and template |
| 29ec497 | 2026-04-04 16:48 | Claude | Add favicon and apple-touch-icon for browser tabs and iMessage previews |
| 214dca0 | 2026-04-04 16:46 | Claude | Add OG meta tags and preview image for link sharing in Messages |
| 8983860 | 2026-04-04 16:35 | Claude | Fix Cookbook link to agentic-cookbook.com |

### Key Milestones (Last 30 Commits)

- **v0.5.3**: Auth gate for non-admin, branded bot profile page, landing page with Bob agent
- **v0.5.0**: Rebranded as "The Agentic Cookbook's Official Agent Registry" (was generic)
- **v0.4.0**: Public bot profile pages at `/:slug`
- **v0.3.0**: Data dashboard with table views
- **v0.2.1**: OAuth login via proxy (fixed Cloudflare routing)
- **v0.2.0**: Initial release (multi-tenant bots backend, GitHub OAuth)

---

## Build & Test Commands

### Root (Monorepo)

```bash
npm run build:client    # Build shared + client (sequential, respects dependencies)
```

### Shared Library

```bash
cd shared
npm install             # Install deps
npm run build          # Compile TypeScript → dist/
npm run dev            # Watch mode
```

### Server

```bash
cd server
npm install
npm run dev            # Watch mode (tsx + nodemon via --watch)
npm run build          # Compile TypeScript → dist/
npm start              # Run dist/index.js with .env
npm run migrate        # Run database migrations
npm run seed           # Seed database with test data
npm run smoke-test     # Connectivity tests (checks /health, sample API calls)
npm run generate       # Generate Drizzle migration files
npm run studio         # Open Drizzle Studio (visual DB editor)
```

### Client

```bash
cd client
npm install
npm run dev            # Vite dev server (http://localhost:5173)
npm run build          # Compile TypeScript + build with Vite
npm run preview        # Build + preview locally
npm run deploy         # Build + deploy to Cloudflare Workers
```

### Local Development Stack

```bash
# Terminal 1: PostgreSQL (Docker)
docker-compose up

# Terminal 2: Server (localhost:3000)
cd server && npm install && npm run dev

# Terminal 3: Client (localhost:5173)
cd client && npm install && npm run dev
```

### GitHub Actions (CI/CD)

- **Trigger:** Push to main on `client/**` or `shared/**`
- **Steps:**
  1. Checkout code
  2. Setup Node.js 22
  3. Build shared (npm install + npm run build)
  4. Build client (npm install + npm run build)
  5. Deploy to Cloudflare (CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID secrets)

---

## Current Architecture

### Deployment Flow

```
Local dev
    ↓
Push to GitHub (main)
    ↓
GitHub Actions triggered (if client/** or shared/** changed)
    ↓
Build & Deploy to Cloudflare Workers ← client serves here
    ↓
Railway auto-deploy ← server runs here
    ↓
PostgreSQL (managed by Railway)
```

### Request Flow

```
User browser
    ↓
agenticregistry.com (DNS → Cloudflare)
    ↓
Cloudflare Worker (agenticregistry)
    ├─ Static assets (/dist) → served from Cloudflare
    └─ API/Auth requests → proxied to Railway backend
    ↓
Railway Hono API
    ├─ GitHub OAuth flow
    ├─ JWT session management
    ├─ CRUD operations on bots
    └─ Queries to PostgreSQL
    ↓
PostgreSQL database
```

### Authentication Flow

1. User clicks "Login with GitHub"
2. Redirect to `POST /auth/github/login` → GitHub OAuth authorize endpoint
3. User authorizes → GitHub redirects to `GET /auth/github/callback?code=...`
4. Server exchanges code for access token, creates/updates user
5. Server issues JWT, sets session cookie
6. Client uses JWT for subsequent API calls

---

## Environment Variables

### Server (.env)

```
DATABASE_URL=postgresql://...      # Railway provides this
GITHUB_CLIENT_ID=Ov23licG7kkEQpIrqi3G
GITHUB_CLIENT_SECRET=...
SESSION_SECRET=<32+ char secret>
CLIENT_URL=https://agenticregistry.com
CORS_ORIGIN=https://agenticregistry.com,http://localhost:5173
GITHUB_CALLBACK_URL=https://agenticregistry.com/auth/github/callback
PORT=3000
NODE_ENV=production
```

### Client

- No runtime env vars (built-in to Vite)
- Reads VERSION at build time (injected via Vite define)

---

## Deployment Checklist

Before deploying:

1. Make code changes
2. Test locally (`npm run dev` in all three terminals)
3. Commit changes
4. **IMPORTANT:** Bump version in `/VERSION` and all three package.json files
5. `git commit -m "..."` AND `git push` together (strict rule)
6. GitHub Actions auto-deploys client
7. Railway auto-deploys server
8. Verify version number in UI (bottom-right corner)

---

## Notes & Context

### Branding & Positioning

- Recently rebranded from generic "Official Agent Registry" to **"The Agentic Cookbook's Official Agent Registry"**
- Part of the Agentic Cookbook ecosystem (companion to agentic-cookbook.com)
- Positions agents as "characters in the digital world," not just tools
- Early play in emerging agent identity/reputation space

### Key Features (Current & Roadmap)

**Current (v0.5.3):**
- Multi-tenant bot registration (free tier: 1 bot per user)
- GitHub OAuth login
- Bot CRUD (create, read, update, delete)
- Public bot profile pages (`/:slug`)
- API key management
- Execution tracking (runs, records, events)
- Dashboard with data tables

**Planned (Research Complete):**
- Persona customization UI (templates researched, not yet built)
- Gamification & reputation scoring
- Skills marketplace
- Premium tiers ($10/year)
- Agent naming engine

### Known Constraints & Trade-offs

- Client is vanilla TS/HTML (no framework like React) — lightweight, minimal dependencies
- Single-tenant SPA model (each user sees only their own bots in dashboard)
- Public profiles are read-only (no editing public persona yet)
- API key model is basic (no per-scope rate limiting)

### Multi-Domain Strategy

- Primary domain: `agenticregistry.com`
- Secondary domains (all 301 redirect to primary):
  - agenticregistry.com
  - officialagenticregistry.com
  - register-your-agent.com
  - agent-registrar.com
  - And 8+ more variants
- Alternative TLDs: .org, .net, .io
- Premium: agenticregistry.ai
- All managed via Cloudflare Bulk Redirects

### Development Conventions

- Monorepo structure (shared, client, server)
- TypeScript everywhere
- Shared types between client and server (same interface definitions)
- Drizzle ORM for type-safe database queries
- Zod for runtime validation
- Strict git rules: always push after commit, always bump version before deploy

---

## Useful Links

- **GitHub:** github.com/agentic-cookbook/agenticregistry
- **Live Site:** agenticregistry.com
- **Cloudflare Worker:** agenticregistry (console.cloudflare.com)
- **Railway Project:** (auto-linked via GitHub integration)
- **GitHub OAuth App:** github.com/settings/developers
- **Drizzle ORM Docs:** orm.drizzle.team
- **Hono Docs:** hono.dev

---

**Last updated:** 2026-04-07  
**Project version:** 0.5.3
