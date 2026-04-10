# Learn True Facts

## Project Summary

Learn True Facts is a public-facing AI improv comedian chat application that blends real historical facts with absurdly plausible fictional details. Currently in the design and research phase, the project serves as a test bed for a modern tech stack (Cloudflare Workers + Railway + Hono + React) and persona-driven AI applications before scaling to production use with Temporal. Features include AI chat interface with improv comedian persona, multi-provider LLM abstraction, server-sent events for streaming, admin portal, analytics dashboard, and RS256 JWT authentication via a shared agentic-auth-service.

## Type & Tech Stack

**Type:** Full-Stack Web Application (SaaS - Chat Platform)

**Tech Stack:**
- **Frontend:** React 19, Vite, Tailwind CSS 4, TanStack Router/Query
- **Backend:** Hono (web framework), Drizzle ORM, PostgreSQL, Zod (schema validation)
- **Infrastructure:** Cloudflare Workers (frontend), Railway (backend/database)
- **Authentication:** RS256 JWT via shared agentic-auth-service
- **Real-time:** Server-Sent Events for streaming responses
- **Build:** npm workspaces (monorepo structure)
- **Node.js Version:** 20+ (for Hono + async runtime support)

## GitHub URL

https://github.com/agentic-cookbook/learntruefacts.git

## Directory Structure

```
learntruefacts/
├── package.json            # Monorepo root with workspaces
├── docker-compose.yml      # Local development database setup
├── Dockerfile              # Multi-stage Docker build for backend
├── railway.toml            # Railway.app deployment config
├── .env.example            # Environment variables template
├── .github/workflows/       # GitHub Actions CI/CD
├── shared/                 # Shared utilities & types (workspace)
│   ├── src/
│   └── package.json
├── backend/                # Hono backend API (workspace)
│   ├── src/
│   │   ├── app.ts          # Hono app setup
│   │   ├── index.ts        # Server entry point
│   │   ├── db/             # Drizzle ORM schemas & migrations
│   │   ├── routes/         # API route handlers
│   │   ├── services/       # Business logic services
│   │   ├── middleware/     # Auth, error handling, CORS
│   │   ├── auth/           # JWT validation
│   │   └── config/         # Environment & app config
│   ├── package.json
│   └── tsconfig.json
├── auth-service/           # Shared JWT auth service (workspace)
│   ├── src/
│   └── package.json
├── sites/                  # Frontend applications
│   ├── main/               # Main chat application (Vite + React)
│   │   ├── src/
│   │   ├── package.json
│   │   └── vite.config.ts
│   ├── admin/              # Admin dashboard (Vite + React)
│   │   ├── src/
│   │   └── package.json
│   └── dashboard/          # Analytics dashboard (Vite + React)
│       ├── src/
│       └── package.json
├── docs/
│   ├── project/description.md
│   ├── design/
│   ├── research/
│   └── ...
└── node_modules/           # Shared dependencies
```

## Key Files & Components

- **package.json** (root) - Monorepo configuration with npm workspaces; defines workspace structure (shared, backend, auth-service, sites/*) and root-level build/deploy scripts
- **docs/project/description.md** - Complete project description with purpose, key features, tech stack, status, and related projects
- **docs/design/initial-idea.md** - Initial design and concept documents
- **docs/research/llm-chat-widget-research.md** - Research on LLM chat widget implementations
- **backend/package.json** - Hono server configuration with Drizzle ORM, jose JWT, bcrypt, zod validation
- **backend/src/app.ts** - Hono application initialization
- **backend/src/db/** - Drizzle schema definitions and migrations
- **backend/src/routes/** - API endpoint handlers (chat, auth, admin, analytics)
- **backend/src/auth/** - RS256 JWT validation and authorization middleware
- **sites/main/package.json** - Main chat frontend (React 19 + Vite)
- **sites/admin/package.json** - Admin portal (React 19 + Vite)
- **.env.example** - Environment template for API keys, database URLs, JWT secrets

## Claude Configuration

No `.claude/` directory present; configuration managed at workspace or individual project level via package.json scripts.

## Planning & Research Documents

- **docs/project/description.md** - Project purpose, key features (planned), tech stack, status (planning/pre-implementation)
- **docs/design/initial-idea.md** - Initial design and concept research
- **docs/research/llm-chat-widget-research.md** - Research on LLM chat widget implementations and best practices

## Git History & Current State

- **Remote:** git@github.com:agentic-cookbook/learntruefacts.git
- **Current Branch:** main
- **Status:** Clean working tree (no uncommitted changes)
- **Recent Activity:**
  - Latest: chore: update manifest with deployment URLs (a388c6c)
  - fix: skip auth-service migration on startup temporarily (92ec62c)
  - fix: auth-service migration path and healthcheck timeout (6ae9f84)
  - fix: add AppEnv types to auth-service for Hono context (fa9f306)
  - fix: strip template conditionals, update wrangler configs (84458ae)
  - Deployed infrastructure fixes and config updates in recent commits

## Build & Test Commands

```bash
# Root monorepo commands
npm run dev                 # Start all workspaces in dev mode (backend, main, admin, dashboard)
npm run build:all          # Build all workspaces
npm run build:shared       # Build shared utilities
npm run build:backend      # Build backend API
npm run build:main         # Build main chat frontend
npm run build:admin        # Build admin dashboard
npm run build:dashboard    # Build analytics dashboard
npm run deploy:all         # Deploy all sites to Cloudflare
npm run deploy:main        # Deploy main site
npm run deploy:admin       # Deploy admin site
npm run deploy:dashboard   # Deploy dashboard site

# Backend commands (run in backend/ workspace)
npm run dev                # Start Hono dev server
npm run build              # TypeScript compilation
npm run start:prod         # Start with DB migrations
npm run db:generate        # Generate Drizzle ORM types
npm run db:migrate         # Run database migrations
npm run db:seed            # Seed database with initial data
npm run test               # Run Vitest unit tests

# Frontend commands (run in sites/main/, sites/admin/, sites/dashboard/)
npm run dev                # Start Vite dev server
npm run build              # Build for production
npm run preview            # Preview production build
```

## Notes

- **Status:** Design and research phase — no application code fully committed yet, infrastructure scaffolding in progress
- **Architecture:** Monorepo with shared workspace pattern; backend uses Hono + Drizzle ORM for type-safe database access; frontend uses React 19 + Vite for fast builds
- **Deployment:** Cloudflare Workers (frontend), Railway (backend + PostgreSQL database)
- **Authentication:** Centralized RS256 JWT via agentic-auth-service shared workspace
- **Domain:** learntruefacts.com
- **Related Projects:** MyAgenticProjects (similar Hono + React + Railway + Cloudflare stack), Agentic Auth Service (shared auth infrastructure)
- **Development:** Docker Compose for local PostgreSQL; environment variables from .env.example
