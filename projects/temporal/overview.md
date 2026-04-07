# Temporal

## Project Summary

Temporal is a cross-platform desktop, mobile, and web application featuring a full discussion forum ("community") with gamification, real-time messaging, and IoT integration. Built with Kotlin Multiplatform for shared business logic and native UIs (SwiftUI, Jetpack Compose, Compose Multiplatform, React) across iOS, macOS, watchOS, tvOS, visionOS, Android, Windows, and web.

## Type & Tech Stack

- **Project Type:** Cross-platform collaborative AI assistant application with community features
- **Shared Module:** Kotlin Multiplatform (KMP) — business logic, models, persistence (SQLDelight), networking (Ktor Client)
- **Apple (iOS/macOS/watchOS/tvOS/visionOS):** SwiftUI with Swift Concurrency
- **Android:** Jetpack Compose with MVVM + StateFlow
- **Windows Desktop:** Compose Multiplatform (Kotlin/JVM)
- **Web:** React 19 + TypeScript + Tailwind CSS 4 + Vite 7
- **Backend:** Ktor Server + PostgreSQL + Exposed ORM
- **IoT:** Kotlin/Native (ARM) and Kotlin/JVM
- **Admin/Monitoring:** React + Cloudflare Workers + D1 SQLite
- **Build:** Gradle 8 with version catalog and convention plugins

## GitHub URL

`https://github.com/temporal-company/temporal`

## Directory Structure

```
temporal/
├── CLAUDE.md (22KB)                   # Full feature breakdown, schema, API docs
├── AGENTS.md                          # Agent-focused documentation
├── README.md
├── Roadmaps/                          # 10 feature roadmaps
│   ├── WindowsDesktopParity-Roadmap.md (14 steps)
│   ├── AdminAuth-Roadmap.md
│   ├── CommunityCleanup-Roadmap.md
│   └── ... (7 more)
├── shared/                            # Kotlin Multiplatform shared module
│   └── src/{commonMain,androidMain,appleMain,iosMain,jvmMain,jsMain}/
├── backend/                           # Ktor Server + PostgreSQL
│   ├── docker-compose.yml
│   ├── migrations/
│   └── src/.../backend/
│       ├── database/tables/           # 17 tables (8 user + 9 community)
│       ├── routes/{auth,discussions,notifications,websocket,admin}/
│       ├── services/                  # PointsService, WebSocketManager, MentionParser
│       └── security/
├── client-apps/
│   ├── apple/                         # SwiftUI (iOS/macOS/watchOS/tvOS/visionOS)
│   │   ├── project.yml               # xcodegen config
│   │   └── Sources/{iOS,macOS,Shared/Community/}/
│   ├── android/                       # Jetpack Compose
│   │   └── src/.../community/{api,screens}/
│   ├── windows/                       # Compose Multiplatform desktop
│   ├── web/                           # React 19 + TypeScript + Tailwind + Vite
│   │   ├── wrangler.jsonc             # Cloudflare deployment
│   │   └── src/{components/community,hooks,pages}/
│   └── iot/
├── admin-apps/
│   ├── admin-website/                 # Admin dashboard (WIP)
│   └── status-website/               # Status monitoring (Cloudflare Worker + D1)
├── public-apps/landing-website/
├── docs/
│   ├── decisions/                     # 7 ADRs (tech stack, DI, sync, auth, logging, daemon, integration)
│   ├── designs/                       # user-database-schema.md, transactional-messaging.md
│   ├── research/                      # community-platforms, financial-integration, railway-api
│   ├── personas/                      # Charlie ("The Body Man" AI persona)
│   └── ideas/                         # product-vision.md, product-naming.md, auth-hardening.md
├── .claude/
│   ├── settings.local.json
│   ├── commands/                      # /issue, /buildall
│   └── worktrees/
├── .github/workflows/                 # 10 workflows (CI, deploy, review, security, auto-merge)
├── build.gradle.kts, settings.gradle.kts
└── .mcp.json                          # GitHub API MCP server
```

## Key Components

**Database Schema (17 tables):**
- User tables (8): Users, UserProfiles, UserRoles, UserCapabilities, UserPoints, UserBadges, RefreshTokens, IntegrationConnections
- Community tables (9): DiscussionThreads, Replies, Reactions, Bookmarks, Notifications, Watches, PollVotes, Messages, Conversations

**Community Feature (8 phases implemented):**
1. Core Forum (categories, threads, replies)
2. Rich Content (markdown, edit history, tags, images)
3. Identity & Social (profiles, reactions, bookmarks, roles)
4. Notifications & Discovery (@mentions, search, trending)
5. Structure & Quality (nested replies, polls, answered marking)
6. Gamification (points ledger, levels, badges, leaderboard)
7. Real-time & Messaging (WebSocket, typing indicators, DMs, presence)
8a/8b. Apple & Android native community UI (8c Windows in progress)

**Product Vision:** "Cognitive Relief" — AI assistant that absorbs open loops. AI persona: Charlie ("The Body Man").

**Status Dashboard:** Cloudflare Worker + D1 monitoring 5 services with cron health checks.

## Claude Configuration

- Permissions: git operations, bash YAML validation
- Commands: `/buildall` (all Apple targets), `/issue` (worktree-linked GitHub issues)
- Worktrees for feature branches

## Planning & Research Documents

- **7 ADRs** covering tech stack, DI, sync (Last-Write-Wins), auth (Google OAuth/PKCE/JWT), logging, daemon, integration
- **10 roadmaps** (Windows Desktop Parity: 14 steps, AdminAuth, CommunityCleanup, etc.)
- **Product vision:** Cognitive relief, "What should I focus on right now?"
- **Naming:** "Temporal" is placeholder (trademark risk — Temporal Technologies $2.5B)
- **AI Persona:** Charlie — anticipatory, loyal, honest, reliable

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Working tree:** Clean
- **Recent:** Persona consolidation, web smoke test fix, seed categories fix, repo reorganization
- **Active:** Windows Desktop Parity (~50%), Community Phase 8c, Admin Dashboard auth

## Build & Test Commands

```bash
# Shared
./gradlew :shared:build                    # All targets
./gradlew :shared:allTests                 # All tests

# Backend
cd backend && docker compose up -d         # PostgreSQL
./gradlew :backend:run                     # Dev server
./gradlew :backend:buildFatJar             # Deploy JAR

# Apple
cd client-apps/apple && xcodegen generate  # Generate Xcode project
xcodebuild -scheme Temporal build          # iOS/macOS/etc.

# Android
./gradlew :client-apps:android:assembleDebug

# Windows
./gradlew :client-apps:windows:run
./gradlew :client-apps:windows:packageMsi

# Web
cd client-apps/web && npm run dev          # Vite dev
npm run deploy                             # Cloudflare Pages
npm run test:smoke                         # Playwright

# Status Dashboard
cd admin-apps/status-website && npm run dev
```

## Notes

- Shared-first architecture: Kotlin Multiplatform business logic, native UIs per platform
- WebSocket multiplexing for real-time (replies, reactions, notifications, typing, presence, DMs)
- Gamification: points ledger with reason/source tracking, levels, badges, leaderboard
- Auth: Google OAuth (PKCE for native), JWT with refresh tokens, DPAPI on Windows
- 10 GitHub Actions workflows including CI, deploy verification, security review, merge queue
