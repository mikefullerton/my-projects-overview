# Temporal

## Project Summary

A cross-platform desktop, mobile, and web application with IoT integration for time/calendar management. Built on Kotlin Multiplatform (KMP) for shared business logic across iOS, macOS, tvOS, watchOS, Android, Windows, Web, and IoT platforms. Features a Ktor backend with PostgreSQL, full-featured community discussion system with gamification, real-time messaging, and comprehensive admin dashboards.

## Type & Tech Stack

**Project Type:** Cross-platform mobile, desktop, web, and IoT application

**Core Technologies:**
- **Kotlin Multiplatform (KMP)** — Shared core (commonMain, platform-specific expect/actual)
- **Ktor** — Backend server + client HTTP
- **PostgreSQL** — Primary database with Exposed ORM
- **SQLDelight** — Local sync database (cross-platform)
- **SwiftUI** — Apple platforms UI (iOS, macOS, tvOS, watchOS, visionOS)
- **Jetpack Compose** — Android UI
- **Compose Multiplatform** — Windows desktop UI
- **React 19 + TypeScript** — Web client (Cloudflare Pages)
- **Kotlin/Native & Kotlin/JVM** — IoT and backend implementations
- **Docker** — PostgreSQL containerization for local dev
- **GitHub Actions** — CI/CD pipeline with merge queue
- **Railway** — Cloud deployment
- **Cloudflare** — Admin dashboards and status site

**Architecture Principle:**
Shared-first approach: all business logic in KMP commonMain, platform-specific code via expect/actual declarations, native UI per platform.

## GitHub URL

`git@github.com:temporal-company/temporal.git`

https://github.com/temporal-company/temporal

## Directory Structure

```
temporal/
├── .claude/                             # Claude Code configuration
├── .mcp.json                            # MCP configuration
├── shared/                              # KMP shared module
│   └── src/
│       ├── commonMain/kotlin/          # Shared logic: models, validation, sync
│       ├── commonTest/kotlin/          # Shared tests
│       ├── androidMain/kotlin/         # Android-specific implementations
│       ├── appleMain/kotlin/           # Shared Apple (expect/actual)
│       ├── iosMain/kotlin/             # iOS-specific code
│       ├── jvmMain/kotlin/             # JVM backend, desktop implementations
│       └── jsMain/kotlin/              # JS/WASM web implementations
├── backend/                             # Ktor server + PostgreSQL
│   ├── docker-compose.yml              # PostgreSQL for local dev
│   └── src/                            # Backend Kotlin code
├── client-apps/                         # User-facing applications
│   ├── apple/                          # Xcode project (SwiftUI: iOS, macOS, tvOS, watchOS)
│   ├── android/                        # Android Studio (Jetpack Compose)
│   ├── windows/                        # Compose Multiplatform desktop
│   ├── web/                            # React + TypeScript (Cloudflare)
│   ├── iot/                            # IoT modules (Kotlin/Native, Kotlin/JVM)
│   ├── macos-cli/                      # macOS CLI (placeholder)
│   ├── windows-cli/                    # Windows CLI
│   └── windows-ui/                     # Windows .NET/WPF UI
├── client-daemons/                     # Background services
│   ├── macos/                          # macOS daemon
│   └── windows/
│       ├── daemon/                     # Windows daemon
│       └── sqlite3/                    # SQLite for mingwX64
├── admin-apps/                         # Internal tools
│   ├── admin-website/                  # Admin dashboard (Cloudflare)
│   └── status-website/                 # Status monitor (Cloudflare Workers + D1)
├── public-apps/                        # Public sites
│   └── landing-website/                # Landing page (Cloudflare)
├── Roadmaps/                           # Feature roadmaps (Phase 1-8 complete)
├── docs/                               # Documentation
│   ├── decisions/                      # Architecture Decision Records (ADRs)
│   ├── research/                       # Research documents
│   ├── designs/                        # Design documents
│   ├── ci/                             # CI/CD documentation
│   └── [other docs]
├── scripts/                            # Build and utility scripts
├── build/                              # Build configuration
├── gradle/                             # Gradle wrapper
├── settings.gradle.kts                 # Gradle root settings
├── build.gradle.kts                    # Root build configuration
├── gradlew / gradlew.bat               # Gradle wrapper scripts
├── CLAUDE.md                           # Project rules and dependencies
├── README.md                           # Project documentation
├── AGENTS.md                           # Agent documentation
├── LICENSE
└── .gitignore
```

## Key Files & Components

**Shared Kotlin Module:**
- `shared/src/commonMain/kotlin/` — Core models, sync logic, validation, persistence
- `shared/src/*/kotlin/` — Platform-specific implementations via expect/actual

**Backend:**
- `backend/src/` — Ktor server implementation
- `backend/docker-compose.yml` — PostgreSQL for local development
- Database: PostgreSQL with Exposed ORM
- API routes following Ktor conventions
- JWT authentication and capabilities-based authorization
- Discussion/community feature (Phase 1-8 complete)

**Community Feature (Phases 1-8):**
- **Phase 1:** Core forum with threads, replies, categories, pagination
- **Phase 2:** Rich content (markdown, edit history, tags, attachments)
- **Phase 3:** Identity & social (profiles, reactions, bookmarks, user roles)
- **Phase 4:** Notifications & discovery (mentions, watching, full-text search, sorting)
- **Phase 5:** Structure & quality (nested replies, answered marks, polls)
- **Phase 6:** Gamification (points, levels, badges, leaderboards)
- **Phase 7:** Real-time & messaging (WebSocket, direct messages, typing indicators, online presence)
- **Phase 8a:** Apple native UI (SwiftUI community experience)
- **Phase 8b:** Android native UI (Jetpack Compose)

**Admin Dashboards:**
- `admin-apps/admin-website/` — Admin dashboard for user/content management
- `admin-apps/status-website/` — Public status monitor (all-Cloudflare: Pages + Worker + D1)

**Client Applications:**
- `client-apps/apple/` — Xcode project with SwiftUI for iOS, macOS, tvOS, watchOS, visionOS
- `client-apps/android/` — Android Studio with Jetpack Compose
- `client-apps/windows/` — Compose Multiplatform desktop app
- `client-apps/web/` — React 19 + TypeScript frontend

## Claude Configuration

**Configuration Files:**
- `.claude/` — Claude Code project settings
- `.mcp.json` — MCP (Model Context Protocol) configuration

**Dependencies:**
- `CLAUDE.md` lists all required Claude Code plugins
- Cookbook integration for coding guidelines

## Planning & Research Documents

**Design Decisions:**
- `docs/decisions/001-tech-stack.md` — KMP + native UI rationale
- `docs/decisions/002-dependency-injection.md` — DI pattern
- `docs/decisions/003-sync-strategy.md` — Offline-first sync with LWW
- `docs/decisions/004-authentication.md` — JWT-based auth
- `docs/decisions/006-daemon-cli-architecture.md` — Background services
- `docs/decisions/007-integration-architecture.md` — Third-party integrations
- Other ADRs and decision docs

**Research:**
- `docs/research/railway-api.md` — Railway deployment
- `docs/research/community-platforms.md` — Community system research
- `docs/research/financial-integration-providers.md` — Payment integrations
- Other research documents

**Design Documents:**
- `docs/designs/user-database-schema.md` — Database design
- `docs/designs/transactional-messaging.md` — Messaging architecture
- `docs/designs/openclaw.md` — Feature design
- Other design specs

## Git History & Current State

**Recent Activity:**
- `2d00db5` docs: add standardized project description
- `392ea17` docs: consolidate persona files and enrich naming
- `a6a05ab` fix: web smoke test CORS error and Apple CI
- `d093e24` fix: make seed discussion categories public
- `225d641` refactor: reorganize repo structure by purpose
- `2e806eb` refine documents layout
- `8eb5ea0` docs: add planning directory with decisions, designs, research
- `89b7412` docs: add AI persona spec template and Charlie persona
- `4d2e5d9` ci: enable merge queue support
- `b77e7fa` Update CLAUDE.md: litterbox → agentic-cookbook
- `7f6762c` feat: add Event Log viewer with singleton logger
- Other community feature implementation commits

**Pattern:** Active development on community features, documentation organization, and infrastructure.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree, up to date

## Build & Test Commands

**Prerequisites:**
```bash
brew install openjdk@17 docker xcodegen
```

**Shared Module:**
```bash
./gradlew :shared:build              # Build shared
./gradlew :shared:assembleSharedReleaseXCFramework  # iOS framework
./gradlew :shared:allTests           # Run tests
```

**Apple Client:**
```bash
cd client-apps/apple && xcodegen generate
open client-apps/apple/Temporal.xcodeproj
```

**Backend:**
```bash
cd backend && docker compose up -d    # Start PostgreSQL
./gradlew :backend:build              # Build backend
./gradlew :backend:run                # Run development
./gradlew :backend:run -Pdevelopment  # Dev mode
./gradlew :backend:buildFatJar        # Production JAR
```

**Web Client:**
```bash
cd client-apps/web && npm install
npm run dev                            # Development server
npm run build                          # Production build
npm run lint
```

**Android Client:**
```bash
./gradlew :client-apps:android:assembleDebug
./gradlew :client-apps:android:installDebug
```

**Windows Desktop:**
```bash
./gradlew :client-apps:windows:run
./gradlew :client-apps:windows:packageMsi
```

**Status Dashboard:**
```bash
cd admin-apps/status-website && npm install
npm run dev                            # Development
npm run build                          # Build
npm run deploy                         # Deploy to Cloudflare
npm run lint
```

**Run Tests:**
```bash
./gradlew :shared:allTests             # KMP tests
./gradlew :backend:test                # Backend tests
cd client-apps/web && npm run test     # Web tests
```

## Notes

**Architecture Highlights:**

1. **Shared-First KMP** — Business logic in commonMain, platform-specific via expect/actual
2. **Native UI Per Platform** — SwiftUI (Apple), Compose (Android/Windows), React (Web)
3. **Offline-First Sync** — LWW conflict resolution, sync engine, SQLDelight persistence
4. **Full-Featured Community** — Forums, messaging, gamification, real-time (phases 1-8)
5. **Multi-Platform Admin** — Admin dashboard + separate Cloudflare-based status site
6. **Comprehensive Database** — PostgreSQL backend with 30+ tables for community features

**Community System Completeness:**

- **Core forum** with categories, threads, replies, pagination
- **Rich content** with markdown, edit history, tags, image attachments
- **Social features** with reactions, bookmarks, user roles, profiles
- **Discovery** with full-text search, sorting, notifications, @mentions
- **Structure** with nested replies, accepted answers, polls
- **Engagement** with gamification (points, levels, badges, leaderboards)
- **Real-time** with WebSocket messaging, typing indicators, online presence
- **Native clients** for Apple (iOS/macOS/tvOS/watchOS) and Android
- **Admin tooling** for user management, moderation, feature flags

**Technology Stack Rationale:**

- **KMP** for maximum code sharing while maintaining platform integrity
- **PostgreSQL** for relational community data with full-text search
- **SwiftUI/Compose** for native-first user experience per platform
- **Ktor** for lightweight, coroutine-based backend
- **Cloudflare** for status monitoring and public dashboards

**Development Workflow:**

- Worktree-based feature development
- Merge queue for safe integration
- Comprehensive documentation via ADRs
- CI/CD via GitHub Actions
- Dogfooding via internal testing

**Status & Roadmap:**

- Phases 1-8 of community features complete
- Windows Desktop Client Community UI (Phase 8c) in progress
- Admin Dashboard authentication completed
- Ready for public launch

**Notable Features:**

- **WebSocket infrastructure** for live updates and real-time messaging
- **Gamification system** with points ledger, badges, levels, leaderboards
- **Full-text search** using PostgreSQL tsvector with GIN indexes
- **Nested replies** with depth limiting and tree view
- **Edit history** with all previous versions preserved
- **Polls** with voting and optional expiration
- **Direct messaging** with conversation history
- **Online presence** tracking across platforms
