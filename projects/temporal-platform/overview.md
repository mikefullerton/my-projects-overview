# Temporal Platform - Project Overview

**Last Updated**: 2026-04-07  
**Repository**: https://github.com/temporal-company/temporal-platform

---

## Project Summary

Temporal Platform is a spec-driven application platform for building offline-first, cross-platform applications. Instead of sharing code across platforms (like Kotlin Multiplatform, React Native, or Flutter), it shares **behavioral specifications** — precise markdown documents that an LLM can use to generate correct, testable implementations on any platform. Each platform implements specs natively using its own language and frameworks, with conformance test vectors ensuring all implementations behave identically.

---

## Type & Tech Stack

### Project Type
- **Specification Framework** (not application code)
- **LLM-Driven Code Generation Platform**
- **Conformance Testing Framework**
- **Infrastructure for offline-first, cross-platform applications**

### Architecture
Client-server architecture with:

| Component | Language | Framework | Platforms |
|-----------|----------|-----------|-----------|
| **Shared Data Layer** | Markdown specs | N/A | Cross-platform |
| **Backend/Server** | Kotlin | Ktor + PostgreSQL | JVM (Railway deployment) |
| **Apple Clients** | Swift | SwiftUI | iOS, macOS, watchOS, tvOS, visionOS |
| **Android Clients** | Kotlin | Jetpack Compose + Material 3 | Android phone/tablet/foldable |
| **Windows Client** | C# | WinUI 3 | Windows Desktop (x64) |
| **Web Client** | TypeScript | React 19 + Tailwind CSS | All modern browsers |
| **Admin Dashboard** | TypeScript | React | Web |
| **Monitoring Dashboard** | TypeScript/JavaScript | Cloudflare Workers + D1 | Web (status.*.today) |
| **Conformance Tests (TypeScript)** | TypeScript | Vitest | Node.js |
| **Conformance Tests (Swift)** | Swift | XCTest | iOS/macOS |

### Technology Highlights
- **Sync Engine**: Last-Writer-Wins (LWW) conflict resolution with edit operations
- **Persistence**: SQLite with dual-table architecture (base + snapshot)
- **Authentication**: JWT-based with OAuth providers
- **Feature Modules**: Plugin architecture (discussions, messaging, gamification, notifications, calendar integration, feature flags, feedback, OAuth providers)
- **Testing**: JSON-based conformance test vectors with per-platform runners
- **Deployment**: Railway (backend), platform-native for clients
- **Skill Framework**: Claude Code skills for onboarding (init-platform) and spec planning (temporal-plan-spec)

---

## GitHub URL

```
git@github.com:temporal-company/temporal-platform.git
https://github.com/temporal-company/temporal-platform
```

**Owned by**: Temporal Company  
**Current Branch**: main (up to date with origin/main)  
**Uncommitted Changes**: None (working tree clean)

---

## Directory Structure

```
temporal-platform/                           Root
├── README.md                                 Overview and getting started guide
├── CLAUDE.md                                 Development guidelines, rules, standards
├── .gitignore                                (.build/, .DS_Store, .temporal/, .claude/worktrees/)
├── .git/                                     Git repository metadata
├── .claude/                                  Claude Code configuration (currently empty)
│
├── client-server/                            Client-server architecture specs
│   ├── blueprints/                           Behavioral specifications (78 markdown files)
│   │   ├── shared/                           Cross-platform data layer (14 specs)
│   │   │   ├── auth/                         Authentication & authorization
│   │   │   │   ├── authentication.md         JWT, OAuth, password auth specs
│   │   │   │   └── authorization.md         Capabilities-based authorization
│   │   │   ├── models/                       Core entity specs (6 models)
│   │   │   │   ├── syncable.md               Base interface for syncable entities
│   │   │   │   ├── content.md                Generic content entity
│   │   │   │   ├── project.md                Project entity
│   │   │   │   ├── user.md                   User entity
│   │   │   │   ├── calendar-event.md         Calendar event entity
│   │   │   │   └── edit-operation.md         Field-level edit change log
│   │   │   ├── persistence/                  Local database specs
│   │   │   │   ├── local-database.md         SQLite schema with dual-table architecture
│   │   │   │   └── repositories.md           CRUD repository patterns
│   │   │   ├── sync/                         Sync engine specs (3 specs)
│   │   │   │   ├── sync-engine.md            LWW sync orchestration
│   │   │   │   ├── snapshot-builder.md       Replay edits on base records
│   │   │   │   └── conflict-resolution.md    Last-Writer-Wins algorithm
│   │   │   └── content-types/                Plugin architecture
│   │   │       └── content-type-system.md    ContentType interface for extensibility
│   │   │
│   │   ├── server/                           Backend specifications
│   │   │   ├── backend/                      API, database, services
│   │   │   │   ├── overview.md               Backend architecture overview
│   │   │   │   ├── api/                      REST API specs (4 specs)
│   │   │   │   │   ├── conventions.md        API design conventions
│   │   │   │   │   ├── content-endpoints.md  CRUD endpoints for content
│   │   │   │   │   ├── project-endpoints.md  CRUD endpoints for projects
│   │   │   │   │   └── sync-protocol.md      Sync request/response protocol
│   │   │   │   ├── database/                 Schema specs
│   │   │   │   │   └── schema.md             PostgreSQL schema, migrations
│   │   │   │   ├── services/                 Server-side logic specs
│   │   │   │   │   ├── sync-server.md        Server-side sync orchestration
│   │   │   │   │   └── auth-server.md        JWT issuance and validation
│   │   │   │   ├── deployment/               Infrastructure specs
│   │   │   │   │   ├── railway.md            Railway deployment configuration
│   │   │   │   │   ├── docker.md             Dockerfile and container specs
│   │   │   │   │   └── environment.md        Environment variables, secrets
│   │   │   │   └── module-integration.md     How modules extend the backend
│   │   │   │
│   │   │   ├── admin-dashboard/              Admin panel specs (3 specs)
│   │   │   │   ├── overview.md               Admin dashboard purpose and structure
│   │   │   │   ├── api.md                    Admin API endpoints
│   │   │   │   └── deployment.md             Admin dashboard deployment
│   │   │   │
│   │   │   └── monitoring-dashboard/         Status page specs (5 specs)
│   │   │       ├── overview.md               Monitoring dashboard overview
│   │   │       ├── metrics.md                Health metrics and dashboards
│   │   │       ├── incidents.md              Incident tracking and history
│   │   │       ├── deployments.md            Deployment status and history
│   │   │       └── database.md               Monitoring database schema
│   │   │
│   │   ├── clients/                          Per-platform client specs
│   │   │   ├── apple/                        Apple platforms (5 specs)
│   │   │   │   ├── architecture.md           SwiftUI app structure
│   │   │   │   ├── auth.md                   Apple-specific auth integration
│   │   │   │   ├── data.md                   SwiftData/SQLite integration
│   │   │   │   ├── daemon.md                 macOS daemon with Mach services IPC
│   │   │   │   └── deployment.md             App Store Connect, TestFlight specs
│   │   │   │
│   │   │   ├── android/                      Android platform (4 specs)
│   │   │   │   ├── architecture.md           Jetpack Compose app structure
│   │   │   │   ├── auth.md                   Android-specific auth integration
│   │   │   │   ├── data.md                   Room/SQLite integration
│   │   │   │   └── deployment.md             Google Play distribution specs
│   │   │   │
│   │   │   ├── windows/                      Windows platform (4 specs)
│   │   │   │   ├── architecture.md           WinUI 3 app structure
│   │   │   │   ├── auth.md                   Windows-specific auth integration
│   │   │   │   ├── daemon.md                 Named-pipe IPC to Kotlin/Native daemon
│   │   │   │   └── deployment.md             MSIX packaging and distribution
│   │   │   │
│   │   │   └── web/                          Web platform (3 specs)
│   │   │       ├── architecture.md           React 19 app structure
│   │   │       ├── auth.md                   Web-specific auth (cookies, tokens)
│   │   │       └── deployment.md             Vercel/CloudFlare deployment
│   │   │
│   │   ├── modules/                          Optional feature modules (8 modules)
│   │   │   ├── _module-template/             Template for creating new modules
│   │   │   │   ├── TEMPLATE.md               17-section spec template
│   │   │   │   └── module.json               Module manifest schema
│   │   │   │
│   │   │   ├── discussions/                  Community forums
│   │   │   │   └── module.json               Models, API, database specs
│   │   │   │
│   │   │   ├── messaging/                    Direct messaging
│   │   │   │   └── module.json               WebSocket real-time delivery
│   │   │   │
│   │   │   ├── gamification/                 Points, badges, leaderboards
│   │   │   │   └── module.json
│   │   │   │
│   │   │   ├── notifications/                Push/email/SMS notifications
│   │   │   │   └── module.json
│   │   │   │
│   │   │   ├── calendar-integration/         Google Calendar, Apple EventKit
│   │   │   │   └── module.json
│   │   │   │
│   │   │   ├── feature-flags/                Server-controlled feature toggles
│   │   │   │   └── module.json
│   │   │   │
│   │   │   ├── feedback/                     In-app feedback collection
│   │   │   │   └── module.json
│   │   │   │
│   │   │   └── oauth-providers/              Google/Apple Sign-In
│   │   │       └── module.json
│   │   │
│   │   └── docs/                             Blueprint documentation
│   │       └── tbd.md                        Placeholder
│   │
│   ├── recipes/                              Operational runbooks (3 recipes)
│   │   ├── RECIPE-TEMPLATE.md                 4-phase recipe template (detection, install, auth, smoke tests)
│   │   ├── railway-cli-setup.md              Railway CLI setup and authentication
│   │   └── cloudflare-cli-setup.md           Cloudflare CLI setup and authentication
│   │
│   └── verification/                         Conformance testing
│       ├── vectors/                          Test vectors (JSON)
│       │   ├── _schema/                      Vector file JSON schema
│       │   │   └── vector-file.schema.json   Schema definition
│       │   ├── core/                         Core conformance test vectors
│       │   │   ├── api/                      API wire format tests
│       │   │   ├── models/                   Model serialization tests
│       │   │   └── sync/                     Sync algorithm tests
│       │   └── modules/                      Module-specific test vectors
│       │
│       └── runners/                          Per-platform test runners
│           ├── swift/                        Apple (XCTest)
│           │   ├── Package.swift              Swift Package definition
│           │   ├── Sources/                  Test support code
│           │   └── Tests/                    Conformance test suite
│           │
│           ├── kotlin/                        Android (JUnit) — runner implementation pending
│           │
│           ├── typescript/                    Web (Vitest)
│           │   ├── package.json               npm dependencies (TypeScript, Vitest)
│           │   ├── tsconfig.json
│           │   └── tests/                     Conformance test suite
│           │
│           └── csharp/                        Windows (NUnit) — runner implementation pending
│
├── apps/                                      Per-platform runnable app scaffolds
│   ├── apple/                                 iOS/macOS/watchOS/tvOS/visionOS scaffolds
│   │   └── tbd.md
│   ├── android/                               Android scaffold
│   │   └── tbd.md
│   ├── windows/                               Windows scaffold
│   │   └── tbd.md
│   └── web/                                   React web scaffold
│       └── tbd.md
│
├── playbooks/                                 High-level orchestration (2 playbooks + template)
│   ├── PLAYBOOK-TEMPLATE.md                   Multi-phase playbook template
│   ├── full-stack-verification.md            End-to-end verification workflow
│   └── tbd.md                                 Placeholder for future playbooks
│
├── tools/                                     Skills, agents, and platform tooling
│   ├── skills/                                Claude Code skills
│   │   ├── init-platform/                     Onboarding wizard skill
│   │   │   ├── SKILL.md                       Interactive wizard (6 phases)
│   │   │   ├── platform.json                  Platform metadata (modules, specs, versions)
│   │   │   └── templates/                     Consumer project templates
│   │   │       ├── consumer-claude-md.md      CLAUDE.md template for consumer projects
│   │   │       ├── consumer-readme.md         README template for consumer projects
│   │   │       └── platform-config.json       Config template with source version tracking
│   │   │
│   │   └── temporal-plan-spec/                Spec planning skill
│   │       └── SKILL.md                       Interactive conversation for spec planning
│   │
│   └── agents/                                Claude Code agents
│       └── tbd.md                             Placeholder for custom agents
│
└── docs/                                      Explanatory documentation
    └── client-server/                         Mirrors architecture hierarchy
        ├── architecture.md                    Vision, product components, data layer
        ├── rationale.md                       Why spec-driven (4.6k words)
        └── conformance-testing.md             Test vector format and strategy
```

---

## Key Files & Components

### Core Documentation

1. **`README.md`** (9.6 KB)
   - Getting started guide
   - What's in the box (models, sync, persistence, auth, content types, modules)
   - Spec authoring standards (5 pillars: concrete data structures, algorithmic precision, exact SQL, wire format examples, test vectors)
   - Templating system with placeholder variables
   - Repository structure overview
   - Origin story (extracted from Temporal cross-platform app)

2. **`CLAUDE.md`** (14 KB)
   - Development guidelines and implementation rules (18 rules)
   - Spec format with frontmatter and 17 standard sections
   - Template variable definitions
   - Test vector formats (behavioral table vs. JSON data)
   - Logging requirements with per-platform frameworks
   - Implementation rules (native controls, design decisions, post-generation verification, commits, testing, async, progress, deep linking, accessibility, localization, RTL, privacy, feature flags, analytics, A/B testing, debug mode, linting)
   - Best practices references (HIG, Material Design, WCAG, Kotlin conventions, Swift guidelines)
   - Engineering principles (simplicity, composition, DI, immutability, fail fast, idempotency, design for deletion)

3. **`docs/client-server/rationale.md`** (6.1 KB)
   - Deep analysis of why spec-driven > shared code for this use case
   - The original KMP experience: 151-line Gradle file, 5 plugins, XCFramework generation, C interop
   - Numbers: 4,633 lines of shared code: 40% types, 39% logic, 21% plumbing
   - The web client proof: never used KMP, already spec-driven against REST API
   - General principle: specs win when logic is simple, sharing overhead is high, platforms diverge, team is small
   - Virtuous cycle: write specs → LLM generation → conformance tests → spec refinement → repeat
   - Trade-offs: N x implementation, coordination overhead, bug duplication risk, spec maintenance
   - Gains: build simplicity, debugging, idiomatic code, independent deployment, LLM-assisted generation, onboarding, IDE support

4. **`docs/client-server/architecture.md`** (8.6 KB)
   - Vision statement (spec = single source of truth, not code)
   - Product components (backend: Ktor+PostgreSQL on Railway; clients: 4 platforms)
   - Shared data layer (models, LWW sync, SQLite dual-table, ContentType plugins, JWT auth)
   - Module system (composable features)
   - Consumer workflow (fork platform repo, run /init-platform, customize specs, implement)

### Specifications (78 markdown files)

**Shared Layer** (14 specs):
- Models: `syncable.md`, `content.md`, `project.md`, `user.md`, `calendar-event.md`, `edit-operation.md`
- Sync: `sync-engine.md`, `snapshot-builder.md`, `conflict-resolution.md`
- Persistence: `local-database.md`, `repositories.md`
- Auth: `authentication.md`, `authorization.md`
- Plugins: `content-type-system.md`

**Backend** (12 specs):
- API: `conventions.md`, `content-endpoints.md`, `project-endpoints.md`, `sync-protocol.md`
- Database: `schema.md`
- Services: `sync-server.md`, `auth-server.md`
- Deployment: `railway.md`, `docker.md`, `environment.md`
- Integration: `module-integration.md`, `overview.md`

**Clients** (16 specs):
- Apple: 5 specs (architecture, auth, data, daemon, deployment)
- Android: 4 specs (architecture, auth, data, deployment)
- Windows: 4 specs (architecture, auth, daemon, deployment)
- Web: 3 specs (architecture, auth, deployment)

**Admin/Monitoring** (8 specs):
- Admin: overview, api, deployment
- Monitoring: overview, metrics, incidents, deployments, database

**Modules** (8 modules with manifests):
- discussions, messaging, gamification, notifications, calendar-integration, feature-flags, feedback, oauth-providers

### Test Infrastructure

1. **`client-server/verification/vectors/`** (JSON test vectors)
   - `_schema/vector-file.schema.json` — JSON Schema for test vectors
   - `core/api/` — API wire format tests
   - `core/models/` — Model serialization tests
   - `core/sync/` — Sync algorithm tests
   - `modules/` — Module-specific vectors

2. **`client-server/verification/runners/`** (Per-platform test runners)
   - **Swift** (XCTest): Package.swift, Sources/, Tests/
   - **TypeScript** (Vitest): package.json, tsconfig.json, tests/
   - **Kotlin** (JUnit) — pending
   - **C#** (NUnit) — pending

3. **`tools/skills/init-platform/platform.json`** (Platform metadata)
   - Platform version: 0.2.0
   - All specs indexed by category
   - Module list with categories
   - Template variables definition
   - Supported platforms with runner paths

### Tooling

1. **`/init-platform` Skill** (Onboarding wizard)
   - 6 phases: app identity, API config, module selection, platform targets, customization, generation
   - Interactive prompts with defaults
   - Generates customized specs with resolved placeholders
   - Templates: CLAUDE.md, README.md, platform-config.json
   - Stores platform source version for upstream contribution

2. **`/temporal-plan-spec` Skill** (Spec planning)
   - Interactive conversation for spec planning
   - Discovery phase: feature identity, location, platforms, dependencies
   - Requirements phase: REQ-NNN enumeration with RFC 2119 keywords
   - Data structures: JSON Schema, field tables, examples
   - API contract: endpoints, request/response, errors
   - Test vectors: behavioral table + data JSON
   - Edge cases, logging, deep linking, privacy, accessibility, feature flags, analytics, platform notes, design decisions

### Recipes (3 operational runbooks)

1. **`RECIPE-TEMPLATE.md`** (4 phases)
   - Detection: check if tool is installed/authenticated
   - Installation: platform-specific install commands
   - Authentication: interactive login (user hands off to browser)
   - Smoke tests: verify access and permissions

2. **`railway-cli-setup.md`** — Railway CLI authentication and verification
3. **`cloudflare-cli-setup.md`** — Cloudflare CLI authentication and verification

### Playbooks (2 orchestration workflows)

1. **`PLAYBOOK-TEMPLATE.md`** (Multi-phase orchestration)
   - State management via `.temporal/playbook-state.json`
   - Phases with checkpoint gates
   - Teardown section for resource cleanup
   - Design decisions and changelog

2. **`full-stack-verification.md`** (End-to-end verification)
   - Combines recipes and blueprints
   - Verifies conformance across all platforms
   - Produces JUnit XML, JSON summary, determinism reports

---

## Claude Configuration

The `.claude/` directory is currently empty. No local Claude Code settings, commands, rules, plugins, or scripts are configured yet.

**Potential future use cases**:
- Custom Claude Code hooks for spec validation
- Linting rules for spec authoring
- Commands for generating from specs
- Settings for workspace-wide configuration

---

## Planning & Research Documents

### Architecture Documentation
- **`docs/client-server/architecture.md`** — Complete vision, product components, shared data layer, module system, consumer workflow
- **`docs/client-server/rationale.md`** — Detailed analysis of spec-driven vs. shared code, with historical context from the original Temporal app

### Specification Authoring Guides
- **`CLAUDE.md`** — Comprehensive spec format, 18 implementation rules, logging requirements, best practices references
- **`client-server/blueprints/modules/_module-template/TEMPLATE.md`** — 17-section template for new modules
- **`client-server/recipes/RECIPE-TEMPLATE.md`** — 4-phase template for operational runbooks
- **`playbooks/PLAYBOOK-TEMPLATE.md`** — Multi-phase template for orchestration workflows

### Metadata & Configuration
- **`tools/skills/init-platform/platform.json`** — Platform inventory: 78 specs across 8 categories, 8 modules, supported platforms

---

## Git History & Current State

### Recent Commits (5 most recent)
```
2026-04-06 16:18:01 -0700  chore: standardize worktree directory to .claude/worktrees/
2026-03-31 06:36:57 -0700  chore: rename cat-herding → agentic-roadmaps in shared project reference
2026-03-27 11:12:24 -0700  Update CLAUDE.md: litterbox → agentic-cookbook
2026-03-25 21:54:07 -0700  fix: remove Swift .build artifacts and fix .gitignore
2026-03-25 19:10:48 -0700  feat: add full-stack verification playbook
```

### Full History (Last 30 commits)
```
f600b40 chore: standardize worktree directory to .claude/worktrees/
cf2749c chore: rename cat-herding → agentic-roadmaps in shared project reference
83c4a21 Update CLAUDE.md: litterbox → agentic-cookbook
a3e849b fix: remove Swift .build artifacts and fix .gitignore
6cf7187 feat: add full-stack verification playbook
02456c0 feat: add playbook template format
76e33c0 fix: update all path references for new directory structure
6ea0d3e chore: replace .gitkeep with tbd.md in placeholder directories
f02ca9c refactor: reorganize into multi-architecture platform structure
6066390 refactor: move vectors/ and runners/ under verification/
8de380f refactor: move all specs under blueprints/ directory
9846534 docs: add cat-herding shared project and recipes dir to CLAUDE.md
0b0fdee feat: add Railway CLI setup recipe
ac061e5 feat: add Cloudflare CLI setup recipe
02231c5 feat: add recipe template for infrastructure CLI setup runbooks
2db3815 feat: add /temporal-plan-spec skill
aeeec51 refactor: reorganize as full product platform
19d5e33 feat: complete spec-driven application platform
006d94e docs: initial spec-driven architecture design
```

### Current State
- **Branch**: main
- **Remote**: origin/main (up to date, no divergence)
- **Working Tree**: clean (no uncommitted changes)
- **Repository Size**: 4.1 MB
- **Git Ignored**: `.build/`, `.DS_Store`, `.temporal/`, `.claude/worktrees/`

---

## Build & Test Commands

### Conformance Testing

**TypeScript/Web conformance tests**:
```bash
cd client-server/verification/runners/typescript/
npm install
npm run test          # Run once
npm run test:watch    # Run in watch mode
```

**Swift/Apple conformance tests**:
```bash
cd client-server/verification/runners/swift/
swift build
swift test
```

**Kotlin/Android conformance tests** (runner pending implementation):
- Planned to use JUnit with gradle
- Will load same JSON vectors as other runners

**C#/Windows conformance tests** (runner pending implementation):
- Planned to use NUnit
- Will load same JSON vectors as other runners

### Spec Authoring & Generation

**Interactive platform initialization** (from any consumer project):
```
/init-platform
```
This launches the 6-phase onboarding wizard that:
1. Collects app identity (name, org, package)
2. Configures API URLs and database name
3. Selects optional modules
4. Chooses target platforms
5. Customizes any specs
6. Generates fully resolved specs with no placeholder tokens

**Spec planning** (from temporal-platform repo):
```
/temporal-plan-spec
```
Interactive skill for planning new specifications — produces structured outline without writing files.

### No Traditional Build Commands
This repository contains **specifications only** — no application code to build. The `/init-platform` and `/temporal-plan-spec` skills are the primary interfaces for consuming and extending the platform.

---

## Notes & Interesting Aspects

### Origin Story
Temporal Platform was extracted from [Temporal](https://github.com/temporal-company/temporal), a real cross-platform productivity app that originally used Kotlin Multiplatform (KMP) to share ~1,000 lines of sync logic across 7 platforms. The KMP build infrastructure (XCFramework generation, SKIE plugin, C interop, 5 Gradle plugins, 151-line Gradle config) was complex relative to the ~983 lines of actual shared logic (mostly simple: LWW conflict resolution, CRUD repositories, JWT auth). The web client never used KMP and instead implemented specs natively — proving the concept worked. This experience led to the full spec-driven platform architecture.

### Shared Project Dependency
The project references a shared project for roadmap planning:
- **Project**: `agentic-roadmaps`
- **Repo**: `git@github.com:mikefullerton/agentic-roadmaps.git`
- **Expected Path**: `../agentic-roadmaps/`
- **Usage**: Roadmap planning, implementation, and review skills are globally installed as symlinks from `~/.claude/skills/` back to `../agentic-roadmaps/skills/`

### Philosophy: The Spec is the Platform

Key insight from README and CLAUDE.md:
- Traditional frameworks share code (React Native, Flutter, KMP)
- This platform shares **specifications** — the reusable artifact is precision documentation, not code
- Each platform implements natively using best-in-class tools
- Conformance test vectors (JSON) guarantee identical behavior across implementations
- Specs must be precise enough for LLM code generation: concrete data structures, algorithmic pseudocode, exact SQL, wire format examples, test vectors
- "Litmus test": Can an engineer implement this spec having read only this file and its declared dependencies?

### Modular Architecture

The platform supports 8 optional feature modules that compose cleanly:
1. **Discussions** (community forums with threads, replies, reactions, polls, bookmarks, tags)
2. **Messaging** (direct messages with WebSocket real-time delivery)
3. **Gamification** (points, badges, levels, leaderboards)
4. **Notifications** (push/email/SMS)
5. **Calendar Integration** (Google Calendar, Apple EventKit)
6. **Feature Flags** (server-controlled feature toggles)
7. **Feedback** (in-app feedback collection)
8. **OAuth Providers** (Google Sign-In, Apple Sign-In)

Each module declares dependencies (core + optional other modules) and contributions (models, API endpoints, database tables, content types, sync entity types) via `module.json` manifest.

### Offline-First Sync Architecture

Three-layer data model on each platform:
```
UI reads from ──> [Snapshot Table]  (pre-computed, fast)
                        ^
                        |
                  [SnapshotBuilder]  (replays edits on base)
                        ^
                  /           \
          [Base Table]  [EditOperation Table]
              ^              ^
              |              |
        sync engine      UI writes
```

- **Base records**: Last-synced server state, updated by sync
- **Edit operations**: Field-level change log, synced independently
- **Snapshots**: Materialized view, rebuilt after sync
- **Conflict resolution**: Last-Writer-Wins (LWW) via timestamp comparison

### Consumer Workflow

1. Fork the platform repo (or initialize from /init-platform)
2. Run `/init-platform` to customize specs for your app
3. Modify specs as your app evolves
4. Generate code per-platform using Claude Code (specs → LLM → platform-native code)
5. Run conformance test vectors to verify all implementations behave identically
6. Optionally contribute improvements back via `/contribute-upstream`

### Implementation Standards

18 rules for implementing from specs:
1. Prefer native controls and libraries
2. Surface all design decisions for user approval
3. Post-generation verification (build, test, lint, log verification, accessibility audit, code review)
4. Small, atomic commits (one logical change per commit)
5. Comprehensive testing (unit over integration)
6. No blocking the main thread (async everywhere)
7. Always show progress (determinate or indeterminate)
8. Deep linking (Universal Links/custom schemes on Apple, App Links on Android, URLs on Web)
9. Accessibility from day one (roles, labels, keyboard nav, Dynamic Type, contrast, focus order)
10. Localizability (no hardcoded strings)
11. RTL layout support (leading/trailing, not left/right)
12. Privacy and security by default (data minimization, consent, secure storage, no PII logging, TLS only, input sanitization)
13. Feature flags (gate all features from initial implementation via FeatureFlagProvider interface)
14. Analytics (instrument via AnalyticsProvider interface, no direct coupling to backend)
15. A/B testing (ExperimentProvider interface for variant assignment)
16. Debug mode (feature flag overrides, analytics log, experiment picker, environment info)
17. Linting from day one (SwiftLint, ktlint, ESLint per platform)
18. Scriptable and automatable (AppIntents/Shortcuts on Apple, AppActions on Android, API on Web)

### Logging Requirements

Every behavioral spec MUST include logging section with exact log messages. Enables verification via grepping output rather than visual inspection.

Format: `Subsystem: {{org_package}} | Category: ComponentName`

Per-platform logging:
- **Apple**: `os.log` (Logger from os module) — subsystem matching bundle ID, category per component
- **Android/Kotlin**: `Timber` or `android.util.Log`
- **Web/JS/TS**: `console` with structured prefixes, or `pino`/`winston` in Node

### Conformance Testing Strategy

Shared JSON test vectors with per-platform runners:
- **Swift runner** (XCTest): Loads vectors from `../../vectors`, asserts outcomes
- **TypeScript runner** (Vitest): Same vectors, TypeScript assertions
- **Kotlin runner** (JUnit): Pending, will load same vectors
- **C# runner** (NUnit): Pending, will load same vectors

Two vector formats:
1. **Behavioral table** (state/action/outcome tests)
2. **Data JSON blocks** (serialization, algorithms, wire formats)

---

## Project Maturity

- **Status**: Active development
- **Version**: 0.2.0 (platform), 1.0.0 (shared specs and runners)
- **Copyright**: 2026 Mike Fullerton / Temporal. All rights reserved. (Proprietary)
- **Last Major Update**: 2026-04-06 (worktree standardization)
- **Completeness**: 
  - Core architecture: Complete (14 shared specs, 12 backend specs, 16 client specs, 8 modules)
  - Verification: Partial (Swift and TypeScript runners implemented; Kotlin and C# pending)
  - Skills: 2 implemented (/init-platform, /temporal-plan-spec)
  - Playbooks: 1 implemented (full-stack-verification)
  - Recipes: 2 implemented (railway-cli-setup, cloudflare-cli-setup)

---

## Quick Start for New Team Members

1. **Understand the philosophy**: Read `README.md` and `docs/client-server/rationale.md`
2. **Learn the spec format**: Read `CLAUDE.md` sections on "Spec format" and "Standard sections"
3. **Review an example spec**: Start with `client-server/blueprints/shared/models/syncable.md`
4. **See how specs become code**: Review a platform spec like `client-server/blueprints/clients/apple/architecture.md`
5. **Understand conformance testing**: Read `docs/client-server/conformance-testing.md` and explore `client-server/verification/vectors/`
6. **Try the onboarding**: Run `/init-platform` to generate customized specs for a test project
7. **Plan a new spec**: Use `/temporal-plan-spec` to practice spec planning

---

**Generated**: 2026-04-07  
**Project Location**: `/Users/mfullerton/projects/active/temporal-platform/`
