# temporal

## Project Summary

Cross-platform desktop, mobile, and web application with IoT integration, built on Kotlin Multiplatform (KMP) for shared business logic with native UIs per platform. The app targets iOS, macOS, watchOS, tvOS, visionOS (SwiftUI), Android (Jetpack Compose), Windows (Compose Multiplatform), and Web (React + TypeScript). Backend is Ktor Server + PostgreSQL + Exposed ORM. Features include offline-first sync with LWW conflict resolution, Google authentication with per-user data isolation, and a full-featured community/discussion forum (8 phases implemented: core forum, rich content, identity/social, notifications/discovery, structure/quality, gamification, real-time WebSocket messaging, and native Apple + Android clients). Also includes a status dashboard (Cloudflare Pages + Workers + D1), admin dashboard, and landing page.

## Type & Tech Stack

- **Type**: Cross-platform application (desktop, mobile, web, IoT)
- **Languages**: Kotlin (shared/backend/Android/Windows), Swift (Apple clients), TypeScript (Web), C# (Windows native UI)
- **Shared core**: Kotlin Multiplatform -- business logic, persistence (SQLDelight), networking (Ktor Client)
- **Backend**: Ktor Server + PostgreSQL + Exposed ORM, JWT auth, WebSocket support
- **Apple clients**: SwiftUI (iOS, macOS, watchOS, tvOS, visionOS) via XCFramework + SKIE
- **Android client**: Jetpack Compose + Koin DI
- **Windows client**: Compose Multiplatform (desktop)
- **Web client**: React 19 + TypeScript + Tailwind CSS 4 + Vite 7
- **Status dashboard**: Cloudflare Pages + Workers + D1 (SQLite)
- **Build system**: Gradle (Kotlin DSL) with version catalog
- **Gradle plugins**: KMP, Android Library/Application, Compose Compiler, SQLDelight, SKIE, Ktor Server, Kotlin Serialization, Compose Multiplatform
- **CI/CD**: GitHub Actions (11 workflow files including CI, security review, Claude review, deploy verification)
- **Deployment**: Railway (backend), Cloudflare Pages/Workers (web, status, admin, landing)

## GitHub URL

`git@github.com:temporal-company/temporal.git`

Secondary remote: `mfullerton@192.168.4.35:~/projects/temporal` (macmini)

## Directory Structure

```
temporal/
├── .claude/
│   ├── settings.json                  # Build/test permission allowlists + enabled plugins
│   ├── settings.local.json            # Git and CI permissions
│   └── worktrees/                     # Git worktree for repo-reorg branch
├── .github/
│   └── workflows/                     # 11 CI/CD workflows
│       ├── ci.yml
│       ├── claude-review.yml
│       ├── security-review.yml
│       ├── deploy-verify.yml
│       └── ... (7 more)
├── shared/                            # KMP shared module
│   └── src/
│       ├── commonMain/kotlin/         # Shared business logic, models, validation
│       ├── commonTest/kotlin/         # Shared tests
│       ├── androidMain/kotlin/        # Android expect/actual
│       ├── appleMain/kotlin/          # Apple expect/actual
│       ├── iosMain/kotlin/            # iOS-specific
│       ├── jvmMain/kotlin/            # JVM (desktop, backend)
│       └── jsMain/kotlin/             # JS/WASM (web)
├── backend/
│   ├── src/                           # Ktor server application
│   ├── build.gradle.kts
│   ├── docker-compose.yml             # PostgreSQL for local dev
│   └── Dockerfile
├── client-apps/
│   ├── apple/                         # SwiftUI apps (Xcode project)
│   ├── android/                       # Jetpack Compose app
│   ├── windows/                       # Compose Multiplatform desktop
│   ├── web/                           # React + TypeScript frontend
│   ├── iot/                           # IoT modules
│   ├── windows-cli/                   # Windows CLI
│   └── windows-ui/                    # Windows native UI (.NET/WPF)
├── client-daemons/
│   ├── macos/                         # macOS background daemon
│   └── windows/                       # Windows daemon + SQLite mingwX64
├── admin-apps/
│   ├── admin-website/                 # Admin dashboard (Cloudflare)
│   └── status-website/                # Status dashboard (Cloudflare Workers + D1)
├── public-apps/
│   └── landing-website/               # Landing page (Cloudflare)
├── Roadmaps/                          # 9 roadmap documents + 1 subdirectory
├── docs/
│   ├── decisions/                     # 16 ADRs (tech stack, sync, auth, etc.)
│   ├── designs/                       # 3 design docs
│   ├── research/                      # 3 research docs
│   ├── personas/                      # AI persona definitions
│   ├── ideas/                         # Product ideas
│   └── ci/                            # CI setup docs
├── scripts/                           # Setup and utility scripts
├── build.gradle.kts                   # Root Gradle build
├── settings.gradle.kts                # Module includes
├── CLAUDE.md                          # Comprehensive project guide (22K)
├── AGENTS.md                          # Agent instructions (18K)
├── install.sh / uninstall.sh          # System install/uninstall scripts
└── .mcp.json                          # MCP server configuration
```

## Key Files & Components

- `CLAUDE.md` -- Comprehensive project documentation (22K) covering all platforms, architecture, commands, community feature (8 phases), status dashboard, database tables, API endpoints
- `AGENTS.md` -- Agent-specific instructions (mirrors CLAUDE.md structure)
- `shared/` -- KMP shared module with business logic, models, persistence (SQLDelight), networking (Ktor Client)
- `backend/` -- Ktor server with PostgreSQL, Exposed ORM, JWT auth, WebSocket support, community API (20+ endpoint groups)
- `client-apps/web/` -- React 19 + TypeScript + Tailwind CSS 4 + Vite 7
- `admin-apps/status-website/` -- Cloudflare Workers + D1 status monitoring (5 services: backend, backend-db, web, Cloudflare Pages, Railway)
- `Roadmaps/` -- 9 roadmap files: WindowsDesktopParity, AdminAuth, CIVerification, CommunityBugfixBatch, CommunityCleanup, ConfigurableLayouts, StatusDashboard, TransactionalMessaging, UserSchemaV2
- `docs/decisions/` -- 16 ADRs covering tech stack, DI, sync strategy, authentication, logging/metrics/flags, daemon/CLI architecture, integration architecture, and more

## Claude Configuration

- **Settings (project)**: Permissions for gradlew, xcodebuild, xcodegen, swift, npm, git, gh, tree, ls, open, xcrun, WebSearch, WebFetch (github.com, ktor.io, docs.anthropic.com)
- **Enabled plugins**: superpowers, frontend-design, code-review, pr-review-toolkit, document-skills
- **Settings (local)**: Additional permissions for gh issue, git fetch, git operations, worktree access, YAML validation
- **MCP**: `.mcp.json` configured
- **Worktrees**: `repo-reorg` worktree in `.claude/worktrees/`

## Planning & Research Documents

- `Roadmaps/` -- 9 active roadmaps (WindowsDesktopParity with step tracking, AdminAuth, CIVerification, CommunityBugfixBatch, CommunityCleanup, ConfigurableLayouts, StatusDashboard, TransactionalMessaging, UserSchemaV2)
- `docs/decisions/` -- 16 Architecture Decision Records
- `docs/designs/` -- openclaw.md, transactional-messaging.md, user-database-schema.md
- `docs/research/` -- community-platforms.md, financial-integration-providers.md, railway-api.md
- `docs/personas/` -- charlie.md, temporal-ai-persona-research.md
- `docs/ideas/` -- auth-hardening.md, product-naming.md, product-vision.md

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-05 -- "docs: consolidate persona files and enrich naming research"
- **Working tree**: Clean
- **Recent activity**: Active development (multiple commits per day through early April 2026)
- **Key recent changes**: Persona consolidation, web smoke test fix, seed discussion categories fix, repo structure reorganization, merge queue support, Windows Desktop Parity roadmap (11/12 steps complete), Event Log viewer, refresh token support

## Build & Test Commands

```bash
# Prerequisites: JDK 17+, Docker, xcodegen

# Shared module
./gradlew :shared:build
./gradlew :shared:assembleSharedReleaseXCFramework
./gradlew :shared:allTests

# Backend
cd backend && docker compose up -d         # Start PostgreSQL
./gradlew :backend:build
./gradlew :backend:run
./gradlew :backend:run -Pdevelopment        # Dev mode
./gradlew :backend:buildFatJar

# Apple client
cd client-apps/apple && xcodegen generate
open client-apps/apple/Temporal.xcodeproj

# Web client
cd client-apps/web && npm install && npm run dev
cd client-apps/web && npm run build
cd client-apps/web && npm run lint

# Android client
./gradlew :client-apps:android:assembleDebug
./gradlew :client-apps:android:installDebug

# Windows desktop
./gradlew :client-apps:windows:run
./gradlew :client-apps:windows:packageMsi

# Status dashboard
cd admin-apps/status-website && npm install && npm run dev
cd admin-apps/status-website && npm run deploy
```

## Notes

- This is a large, multi-platform project with 7+ target platforms sharing a Kotlin Multiplatform core
- The community feature is the most developed area (8 phases, 20+ database tables, full WebSocket real-time support, native clients for Apple and Android)
- Status dashboard at `status.temporal.today` monitors 5 services with 1-minute health checks
- 11 GitHub Actions workflows for CI, code review (Claude-powered), security review, and deployment verification
- The `settings.gradle.kts` conditionally includes Android/Windows modules (skippable via `skipAndroid` Gradle property)
- Backend deployed on Railway, web/admin/status/landing on Cloudflare
- Community feature includes gamification (points, badges, levels, leaderboard), polls, nested replies, full-text search, direct messages, and real-time WebSocket events
