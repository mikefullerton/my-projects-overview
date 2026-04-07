# Agentic Auth Service - Project Overview

## Project Summary

A standalone **RS256 JWT authentication service** that provides centralized user management and token issuance for all projects in the agentic ecosystem. Every site delegates auth to this single service rather than implementing its own user management, enabling seamless cross-project authentication via asymmetric JWT validation.

---

## Type & Tech Stack

**Project Type:** Backend authentication microservice (production-deployed)

**Runtime & Framework:**
- Node.js 22 (LTS)
- Hono 4.7.0 (lightweight web framework)
- TypeScript 5.7.0

**Database & ORM:**
- PostgreSQL (hosted on Railway)
- Drizzle ORM 0.36.0

**Authentication & Security:**
- JWT (jose 6.0.0) - RS256 algorithm (asymmetric)
- bcrypt 5.1.1 - password hashing (minimum 12 chars)
- Refresh token rotation with SHA-256 hashing
- Token revocation on server side (opaque refresh tokens stored in DB)

**Build & Deployment:**
- TypeScript compiler (tsc)
- Docker containerization (Node 22 slim image)
- Railway platform deployment
- Healthcheck endpoint (`GET /api/health`)

**Development Tools:**
- tsx 4.19.0 - TypeScript execution and watch mode
- Drizzle Kit 0.30.0 - schema generation and migrations

---

## GitHub URL

**Repository:** `git@github.com:agentic-cookbook/agentic-auth-service.git`
**GitHub HTTPS:** `https://github.com/agentic-cookbook/agentic-auth-service`
**Deployed URL:** `https://backend-production-9b1f.up.railway.app`

---

## Directory Structure

```
agentic-auth-service/
├── src/
│   ├── index.ts                 # Entry point: loads keys, starts Hono server
│   ├── app.ts                   # Hono app setup, global middleware, route registration
│   ├── config/
│   │   ├── env.ts               # Environment variable validation and export
│   │   └── keys.ts              # JWT RS256 key loading (PKCS8 private, SPKI public)
│   ├── auth/
│   │   ├── jwt.ts               # SignJWT, verifyToken (RS256 with jose)
│   │   ├── password.ts          # bcrypt hash/verify utilities
│   │   └── session.ts           # Refresh token creation, validation, revocation
│   ├── db/
│   │   ├── client.ts            # Drizzle client initialization
│   │   ├── schema.ts            # Table definitions: users, refresh_tokens
│   │   ├── migrate.ts           # Standalone migration runner
│   │   ├── seed.ts              # Standalone seed script (creates admin user)
│   │   └── migrations/          # Generated Drizzle migration files
│   ├── middleware/
│   │   ├── auth.ts              # Bearer token extraction and JWT validation
│   │   ├── cors.ts              # CORS setup (configurable origin)
│   │   ├── error.ts             # RFC 7807 problem detail error formatting
│   │   └── logger.ts            # Request logging middleware
│   └── routes/
│       ├── auth.ts              # POST /register, /login, /refresh, /logout; GET /me
│       ├── users.ts             # Admin routes: GET /users, PATCH /users/:id, DELETE /users/:id
│       ├── jwks.ts              # GET /.well-known/jwks.json (public key discovery)
│       └── health.ts            # GET /api/health (healthcheck)
│
├── .site/
│   ├── jwt-public.pem           # Distributed public key (PEM format)
│   └── manifest.json            # Service metadata (site-manager v0.3.0 format)
│
├── docs/
│   └── research/
│       └── shared-auth-service.md  # Comprehensive architecture & design document
│
├── node_modules/                # npm dependencies
├── src/db/migrations/           # Generated Drizzle migration files
│
├── package.json                 # Dependencies: hono, drizzle-orm, jose, bcrypt, pg
├── package-lock.json            # Locked dependency versions
├── tsconfig.json                # TypeScript compiler config (ES2022, strict mode)
├── drizzle.config.ts            # Drizzle migration config
├── Dockerfile                   # Multi-stage Docker build for Railway
├── railway.toml                 # Railway deployment config (builder, healthcheck)
├── .env.example                 # Environment variable template
├── .gitignore                   # Git ignore rules
└── .git/                        # Git repository metadata

```

---

## Key Files & Components

### Entry Point & Server

**`src/index.ts`**
- Loads JWT keys via `loadKeys()`
- Starts Hono server on configured PORT (default 3000)
- Graceful error handling on startup failure

**`src/app.ts`**
- Hono app instance with custom `AppEnv` type for request context
- Global middleware: Hono logger, CORS, custom request logger, error handler
- Route registration:
  - `/api/health` - healthcheck
  - `/api/auth/*` - auth endpoints
  - `/.well-known/*` - JWKS endpoint
  - `/api/admin/users/*` - admin user management

### Configuration

**`src/config/env.ts`**
- Required variables: `DATABASE_URL`, `JWT_PRIVATE_KEY`, `JWT_PUBLIC_KEY`
- Optional variables: `PORT` (default 3000), `NODE_ENV`, `CORS_ORIGIN` (default `*`)
- Throws on missing required variables at startup

**`src/config/keys.ts`**
- Imports RSA keys from PEM format (PKCS8 private, SPKI public)
- Exports `CryptoKey` objects for JWT operations
- Generates JWK representation with `kid: "auth-service-1"` for JWKS endpoint

### Authentication & Authorization

**`src/auth/jwt.ts`**
- `signAccessToken()` - Issues RS256 access token (4-hour expiry)
  - Claims: `sub` (user ID), `email`, `role`
  - Header: `alg: "RS256"`, `kid: "auth-service-1"`
  - Issuer: `agentic-auth-service`
- `signRefreshToken()` - Issues RS256 refresh token (30-day expiry, minimal claims)
- `verifyToken()` - Validates token signature and issuer

**`src/auth/password.ts`**
- `hashPassword()` - bcrypt with cost factor (rounds)
- `verifyPassword()` - bcrypt comparison

**`src/auth/session.ts`**
- `createRefreshToken()` - Issues opaque token, stores SHA-256 hash + expiry in DB
- `validateRefreshToken()` - Verifies token against DB hash, returns user ID or null
- `revokeRefreshToken()` - Deletes token hash (revocation on refresh)

### Database

**`src/db/client.ts`**
- Drizzle ORM client using PostgreSQL driver

**`src/db/schema.ts`**
- **users** table:
  - `id` (UUID PK, auto-generated)
  - `email` (unique, not null)
  - `password_hash` (bcrypt, not null)
  - `role` (text, default "user"; values: "admin" | "user")
  - `created_at`, `updated_at` (timestamps)

- **refresh_tokens** table:
  - `id` (UUID PK, auto-generated)
  - `user_id` (FK to users, cascade delete)
  - `token_hash` (SHA-256 hash of opaque token)
  - `expires_at` (timestamp)
  - `created_at` (timestamp)

**`src/db/migrate.ts`**
- Standalone migration runner (requires only `DATABASE_URL`)
- Runs on container startup (see Dockerfile)

**`src/db/seed.ts`**
- Creates admin user: `admin@myagenticprojects.com`
- Generates default password
- Runs standalone: `npm run db:seed`

### API Endpoints

**`src/routes/auth.ts`** - Authentication routes

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| POST | `/register` | None | Create account, return access + refresh tokens |
| POST | `/login` | None | Authenticate with email/password, return tokens |
| POST | `/refresh` | None | Exchange refresh token for new pair (rotation) |
| POST | `/logout` | Bearer | Revoke refresh token |
| GET | `/me` | Bearer | Fetch current user profile |

**`src/routes/users.ts`** - Admin user management

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| GET | `/api/admin/users` | Bearer + admin | List all users |
| PATCH | `/api/admin/users/:id` | Bearer + admin | Update user role |
| DELETE | `/api/admin/users/:id` | Bearer + admin | Delete user (cascades refresh token revocation) |

**`src/routes/jwks.ts`** - Public key discovery

| Method | Path | Auth | Cache | Purpose |
|--------|------|------|-------|---------|
| GET | `/.well-known/jwks.json` | None | 1 hour | Serve public key in JWK format with `kid: "auth-service-1"` |

**`src/routes/health.ts`** - Health check

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| GET | `/api/health` | None | Return `{ status: "ok" }` (Railway healthcheck) |

### Middleware

**`src/middleware/auth.ts`**
- Extracts `Authorization: Bearer <token>` header
- Validates token with `verifyToken()`
- Populates context: `userId`, `userEmail`, `userRole`
- Returns 401 Unauthorized on failure

**`src/middleware/cors.ts`**
- Configurable origin via `CORS_ORIGIN` env var (default `*`)

**`src/middleware/error.ts`**
- Catches all thrown errors
- Returns RFC 7807 problem detail format:
  ```json
  { "type": "about:blank", "title": "...", "status": 400, "detail": "..." }
  ```

**`src/middleware/logger.ts`**
- Custom request logging with `requestId` (UUID)
- Stores in context for error tracking

### Deployment & Configuration

**`Dockerfile`**
- Multi-stage build: compile TypeScript, generate migrations, copy to slim image
- Runs migrations on startup: `node dist/db/migrate.js`
- Exposes port 3000
- Startup command: migrations then `node dist/index.js`

**`railway.toml`**
- Build method: `DOCKERFILE`
- Healthcheck: `GET /api/health` (120 second timeout)
- Restart policy: on failure, max 3 retries

**`.site/manifest.json`**
- Site manager v0.3.0 metadata
- Project type: `auth-service`
- Deployed URL: `https://backend-production-9b1f.up.railway.app`
- JWT config: RS256, 4h access, 30d refresh
- Last deployed: 2026-04-06 23:17:00Z

**`.site/jwt-public.pem`**
- Distributed RSA public key (PEM format)
- Used by consuming sites to validate tokens locally
- Also served via `/.well-known/jwks.json`

---

## Claude Configuration

**No `.claude/` directory found** — project does not use Claude-specific automation hooks or custom commands.

---

## Planning & Research Documents

### `docs/research/shared-auth-service.md`

Comprehensive architecture document covering:

**Problem & Solution:**
- Explains why per-site auth or shared DB are problematic
- Asymmetric JWT (RS256) as the solution

**Architecture Diagram:**
- Auth service (Railway + Postgres) → private key, issues tokens
- Multiple consuming sites ← public key, validate locally
- Stateless validation (no network calls to auth service at request time)

**Key Design Decisions:**
1. **RS256 (asymmetric) over HS256 (symmetric):** Only auth service holds private key; sites only need public key
2. **Refresh token rotation:** Old token revoked on each refresh; stolen token usable once
3. **Stateless validation:** No calls back to auth service; sites validate locally
4. **JWKS endpoint:** Auto-discovery by `kid` enables key rotation without redeploying sites

**Token Details:**
- Access token (RS256, 4h expiry): Contains `sub`, `email`, `role`; stored in-memory client-side
- Refresh token (opaque, 30d expiry): SHA-256 hash stored in Postgres; enablesstateful revocation

**API Surface & Error Format:**
- Public routes: register, login, refresh, logout, me, JWKS, health
- Admin routes: list/update/delete users
- Error format: RFC 7807 problem detail

**Integration Guide:**
- Consuming sites need to fetch public key (embed `.pem` or fetch JWKS)
- Verify token on each request with `jose` or any JWT library supporting RS256
- Extract `sub`, `role` from claims

**Operational Notes:**
- Seeding: `npm run db:seed` (standalone, only needs `DATABASE_URL`)
- Migrations: `npm run db:migrate` (standalone)
- Key rotation: Add new key with new `kid`, keep old until tokens expire (4h max)

**Open Questions / Future Work:**
- Rate limiting (no brute-force protection yet)
- Email verification (registration doesn't verify ownership)
- Password reset flow
- Multi-factor auth
- Session management UI
- CORS lockdown (currently `*`)
- Key rotation tooling automation

---

## Git History & Current State

### Recent Commits (last 5)

| Date | Commit | Message |
|------|--------|---------|
| 2026-04-07 06:01 | a48b32d | docs: add architecture research document |
| 2026-04-06 19:01 | bb9a47c | chore: replace KeyLike with CryptoKey type in keys config |
| 2026-04-06 16:19 | 08a9668 | fix: standalone seed script, add deployed manifest and public key |
| 2026-04-06 16:16 | 5696997 | fix: standalone migration runner, increase healthcheck timeout |
| 2026-04-06 15:15 | 7c610b5 | feat: initial scaffold — RS256 JWT auth service |

### Current Branch & Status

- **Branch:** `main`
- **Status:** Clean working tree (no uncommitted changes)
- **Ahead of Remote:** 2 commits ahead of `origin/main`
- **Remote:** `git@github.com:agentic-cookbook/agentic-auth-service.git`

### Full Commit Log (30 recent)

Only 5 commits in history (project very new):
1. Initial scaffold (RS256 JWT auth service)
2. Fix standalone migration runner
3. Fix standalone seed script + deployed manifest
4. Replace KeyLike type with CryptoKey
5. Add architecture research document

---

## Build & Test Commands

### Development

```bash
npm run dev
```
- Starts TypeScript watch mode with tsx
- Auto-reloads on file changes
- Listens on PORT (default 3000)

### Production Build

```bash
npm run build
```
- Compiles TypeScript to JavaScript in `dist/` directory

### Running Production Build

```bash
npm start
```
- Runs migrations: `node dist/db/migrate.js`
- Starts server: `node dist/index.js`

### Database

```bash
npm run db:generate
```
- Generates Drizzle ORM schema types and SQL

```bash
npm run db:migrate
```
- Runs pending Drizzle migrations
- Requires `DATABASE_URL` env var
- Standalone script (no app startup)

```bash
npm run db:seed
```
- Creates admin user in database
- Requires `DATABASE_URL` env var
- Standalone script (no app startup)

### Docker

```bash
docker build -t agentic-auth-service .
docker run -e DATABASE_URL=... -e JWT_PRIVATE_KEY=... -e JWT_PUBLIC_KEY=... -p 3000:3000 agentic-auth-service
```
- Multi-stage build
- Runs migrations on startup
- Exposes port 3000

---

## Environment Variables

**Required:**
- `DATABASE_URL` — PostgreSQL connection string (e.g., `postgresql://user:pass@host:5432/db`)
- `JWT_PRIVATE_KEY` — PEM-encoded RSA private key (RS256)
- `JWT_PUBLIC_KEY` — PEM-encoded RSA public key (RS256)

**Optional:**
- `PORT` — Server port (default: 3000)
- `NODE_ENV` — Environment name (development/production)
- `CORS_ORIGIN` — Allowed CORS origins, comma-separated (default: `*`)

**Generate RSA Keys:**
```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -in private.pem -pubout -out public.pem
```

---

## Notes & Interesting Details

### Project Maturity

- **Very fresh:** Only 5 commits, created 2026-04-06
- **Already deployed:** v1 live on Railway (backend-production-9b1f.up.railway.app)
- **Production-ready:** Includes healthcheck, migrations, seed script, Dockerfile

### Design Philosophy

**Stateless by Design:**
- Consuming sites validate JWTs locally — auth service can go down without breaking authenticated sessions
- Only revocation (logout) requires network calls to auth service
- Public key distributed via JWKS endpoint (1-hour cache) — auto-discovery for key rotation

**Security Features:**
- RS256 (asymmetric) prevents token forgery if one consuming site is compromised
- Bcrypt password hashing with 12-char minimum requirement
- Refresh token rotation: each refresh revokes old token
- Opaque refresh tokens stored as SHA-256 hashes (not plaintext)

### Deployment Pipeline

- Railway with Dockerfile builder
- Runs migrations automatically on container start
- Healthcheck via `GET /api/health` (120s timeout)
- Auto-restart on failure (max 3 retries)

### Integration Story

Consuming projects use this service by:
1. Getting public key from `/.well-known/jwks.json` (or embed `.site/jwt-public.pem`)
2. Users log in via `POST /api/auth/login` (returns access + refresh tokens)
3. On each request, sites verify JWT locally with public key
4. Zero network calls to auth service needed for request validation
5. Refresh tokens rotated to detect token theft

### Code Quality

- Full TypeScript with strict mode
- Type-safe Drizzle ORM queries
- RFC 7807 error formatting (standardized)
- Request logging with UUID tracking
- Separation of concerns: auth, DB, routes, middleware into modules

### Future Priorities

Based on research doc:
1. Rate limiting (brute-force protection)
2. Email verification
3. Password reset flow
4. Multi-factor auth
5. Session management UI
6. Restrict CORS to known origins
7. Automate key rotation

