# Agentic Auth Service

## Project Summary

A shared RS256 JWT authentication microservice providing centralized user management and token issuance for the agentic ecosystem. Every site in the agentic ecosystem delegates authentication to this single service rather than implementing its own user management. Enables seamless cross-project authentication via asymmetric JWT validation — consumers only need the public key to verify tokens.

## Type & Tech Stack

**Type:** Backend Microservice (Authentication/Authorization)

**Tech Stack:**
- **Runtime:** Node.js 22 (LTS)
- **Framework:** Hono 4.7.0, TypeScript 5.7.0
- **Database:** PostgreSQL (Railway), Drizzle ORM 0.36.0
- **Auth:** JWT (jose 6.0.0, RS256), bcrypt 5.1.1
- **Deployment:** Railway (Docker)

## GitHub URL

https://github.com/agentic-cookbook/agenticauthservice

## Directory Structure

```
.
├── .claude/              # Claude Code configuration
│   └── CLAUDE.md
├── docs/
│   ├── research/
│   │   └── shared-auth-service.md
│   └── project/
│       └── description.md
├── src/
│   ├── app.ts                 # Hono app setup, middleware, route mounting
│   ├── index.ts               # Entry point — loads keys, starts server
│   ├── auth/
│   │   ├── jwt.ts             # Sign/verify RS256 tokens (4h access, 30d refresh)
│   │   ├── password.ts        # bcrypt hash/verify
│   │   └── session.ts         # Refresh token CRUD (SHA-256 hashed)
│   ├── config/
│   │   ├── env.ts             # Required/optional env vars
│   │   └── keys.ts            # RS256 key loading (PKCS8/SPKI), JWK export
│   ├── db/
│   │   ├── client.ts          # pg Pool + Drizzle instance
│   │   ├── migrate.ts         # Standalone migration runner
│   │   ├── schema.ts          # users + refresh_tokens tables
│   │   └── seed.ts            # Seed script (admin user)
│   ├── middleware/
│   │   ├── auth.ts            # Bearer token verification, adminOnly guard
│   │   ├── cors.ts            # CORS (configurable origins)
│   │   ├── error.ts           # Global error handler (RFC 7807 shape)
│   │   └── logger.ts          # JSON request logger with requestId
│   └── routes/
│       ├── auth.ts            # /api/auth/* — register, login, refresh, logout, me
│       ├── health.ts          # /api/health
│       ├── jwks.ts            # /.well-known/jwks.json (1h cache)
│       └── users.ts           # /api/admin/users — admin-only CRUD
├── Dockerfile             # Container image definition
├── drizzle.config.ts      # ORM configuration
├── package.json
├── tsconfig.json
├── .env.example
├── railway.toml           # Railway deployment config
└── .gitignore
```

## Key Files & Components

**Core Files:**
- `src/index.ts` — Server entry point, environment loading, key initialization
- `src/app.ts` — Hono middleware stack and route registration
- `src/db/schema.ts` — Database schema (users, refresh_tokens)
- `src/auth/jwt.ts` — RS256 token generation/verification
- `src/routes/auth.ts` — Public auth endpoints (register, login, refresh, logout)

**Configuration Files:**
- `package.json` — Project metadata and npm scripts
- `drizzle.config.ts` — Database ORM configuration
- `railway.toml` — Deployment target and environment variables
- `.env.example` — Environment variable template

**Documentation:**
- `docs/research/shared-auth-service.md` — Architecture research
- `docs/project/description.md` — Project purpose and status

## Claude Configuration

**Location:** `.claude/CLAUDE.md`

Contains quick reference including:
- Runtime and framework versions
- Database connection details (PostgreSQL, Railway)
- JWT configuration (RS256, kid: auth-service-1)
- Password requirements (bcrypt, 12 rounds, 12-char minimum)
- Deployment information (Railway, auto-migrations on start)
- Deployed URL: `https://backend-production-9b1f.up.railway.app`
- API route summary and authentication flows

## Planning & Research Documents

**Research:**
- `docs/research/shared-auth-service.md` — Architecture design and decisions

**Project Documentation:**
- `docs/project/description.md` — Project purpose, key features, status, and related projects

## Git History & Current State

**Current Branch:** main

**Remote:** git@github.com:agentic-cookbook/agenticauthservice.git

**Recent Commits:**
- `9023adb` — docs: add standardized project description
- `7aed6ff` — Add .claude/ project config
- `a48b32d` — docs: add architecture research document
- `bb9a47c` — chore: replace KeyLike with CryptoKey type in keys config
- `08a9668` — fix: standalone seed script, add deployed manifest and public key
- `5696997` — fix: standalone migration runner, increase healthcheck timeout
- `7c610b5` — feat: initial scaffold — RS256 JWT auth service

**Status:** Recently completed / stable — production-deployed.

## Build & Test Commands

```bash
# Development
npm run dev              # Watch mode with hot reload

# Production build
npm run build           # TypeScript compilation to dist/

# Server
npm start               # Run compiled server
npm run start:prod      # Run migrations then start (for production)

# Database
npm run db:generate     # Generate migration files
npm run db:migrate      # Run pending migrations
npm run db:seed         # Seed database (admin user)
```

## Notes

- This is the centralized authentication service for all agentic-cookbook projects
- Uses RS256 JWT with asymmetric keys for stateless verification across services
- Refresh tokens are stored in database with SHA-256 hashing for security
- Public key endpoint (/.well-known/jwks.json) is cached for 1 hour
- Deployed on Railway with automatic migrations on application start
- All passwords require minimum 12 characters and bcrypt hashing with 12 rounds
- CORS is configurable per environment for cross-origin requests
- Global error handling follows RFC 7807 problem details standard
- Related projects (MyAgenticProjects, Learn True Facts, Official Agent Registry) consume this auth service
