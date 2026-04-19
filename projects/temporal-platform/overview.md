# Temporal Platform

## Project Summary

A spec-driven application platform for building offline-first, cross-platform applications. Instead of sharing code across platforms, this repository contains behavioral specifications (markdown documents) precise enough for LLMs to generate correct, testable implementations on any platform (Swift, Kotlin, TypeScript). Includes client-server architecture blueprints, optional feature modules, conformance test vectors, and operational runbooks.

## Type & Tech Stack

**Project Type:** Specification/blueprint repository (no application code)

**Core Technologies:**
- **Markdown** — Specification format with YAML frontmatter
- **JSON** — Conformance test vectors
- **YAML** — Spec metadata, configuration
- **Swift/Kotlin/TypeScript** — Test runners (implementation language examples)
- **Git** — Spec version control and history
- **Claude Code** — Skills and agents for spec initialization and implementation

**Architecture:**
Specs → (shared via generated copies) → Swift/Kotlin/TypeScript implementations → Conformance test vectors ensure all platforms behave identically.

## GitHub URL

`git@github.com:temporal-company/temporal-platform.git`

https://github.com/temporal-company/temporal-platform

## Directory Structure

```
temporal-platform/
├── client-server/                       # Main architecture specs
│   ├── blueprints/                      # Behavioral specifications
│   │   ├── shared/                      # Cross-platform foundation
│   │   │   ├── models/                  # Data structures (syncable, content, project, user)
│   │   │   ├── sync/                    # Offline-first sync engine
│   │   │   ├── persistence/             # SQLite schema and repositories
│   │   │   ├── content-types/           # Plugin architecture
│   │   │   └── auth/                    # Authentication and authorization
│   │   ├── server/                      # Server-side specs
│   │   │   └── backend/                 # API contracts, database, services
│   │   ├── clients/                     # Per-platform client specs
│   │   │   ├── apple/                   # iOS, macOS, tvOS, watchOS specs
│   │   │   ├── android/                 # Android specs
│   │   │   ├── windows/                 # Windows specs
│   │   │   └── web/                     # Web specs
│   │   └── modules/                     # Optional feature modules
│   │       ├── discussions/             # Forums, threads, replies
│   │       ├── messaging/               # Direct messages
│   │       ├── gamification/            # Points, badges, levels
│   │       ├── notifications/           # Push/email/SMS
│   │       ├── calendar-integration/    # Google Calendar sync
│   │       ├── feature-flags/           # Server-controlled toggles
│   │       ├── feedback/                # In-app feedback
│   │       ├── admin/                   # Admin dashboard
│   │       └── oauth-providers/         # OAuth integrations
│   ├── recipes/                         # Operational runbooks
│   │   ├── railway-setup.md             # Railway CLI setup
│   │   └── cloudflare-setup.md          # Cloudflare CLI setup
│   └── verification/                    # Conformance testing
│       ├── vectors/                     # Test vectors (JSON)
│       ├── runners/                     # Platform test runners
│       │   ├── swift/                   # XCTest implementation
│       │   ├── kotlin/                  # JUnit implementation
│       │   └── typescript/              # Vitest/Jest implementation
│       └── ci-configs/                  # CI pipeline configs
├── apps/                                # Per-platform runnable scaffolds
│   ├── apple/                           # Xcode project template
│   ├── android/                         # Android Studio template
│   ├── windows/                         # Windows template
│   └── web/                             # Vite/React template
├── playbooks/                           # High-level orchestration
│   ├── full-stack-playbook.md           # Complete app setup
│   └── [other playbooks]
├── tools/                               # Developer tools
│   ├── skills/                          # Claude Code skills
│   │   ├── init-platform/               # Onboarding wizard
│   │   └── temporal-plan-spec/          # Spec planning
│   └── agents/                          # Claude Code agents
├── docs/                                # Explanatory documentation
│   ├── client-server/                   # Architecture docs
│   │   ├── shared/                      # Foundation docs
│   │   ├── clients/                     # Platform-specific docs
│   │   └── modules/                     # Feature module docs
│   ├── spec-authoring-guide.md          # How to write specs
│   └── [other docs]
├── CLAUDE.md                            # Project rules
├── README.md                            # Getting started
└── .gitignore
```

## Key Files & Components

**Spec Format:**
Every spec follows the template in `client-server/blueprints/modules/_module-template/TEMPLATE.md` with sections:
- Frontmatter (YAML with version, status, platforms, dependencies)
- Overview (purpose, scope)
- Terminology (domain terms table)
- Behavioral Requirements (RFC 2119 keywords: MUST, SHOULD, MAY)
- Data Structures (JSON Schema with examples)
- States (state table with transitions)
- API Contract (endpoints, request/response, errors)
- Conformance Test Vectors (behavioral table + data JSON)
- Edge Cases, Logging, Deep Linking, Privacy, Accessibility, Feature Flags, Analytics, Platform Notes, Design Decisions, Changelog

**Shared Specs:**
- `client-server/blueprints/shared/models/` — syncable.md, content.md, project.md, user.md, calendar-event.md, edit-operation.md
- `client-server/blueprints/shared/sync/` — sync-engine.md, snapshot-builder.md, conflict-resolution.md
- `client-server/blueprints/shared/persistence/` — local-database.md, repositories.md
- `client-server/blueprints/shared/content-types/` — content-type-system.md (plugin architecture)
- `client-server/blueprints/shared/auth/` — authentication.md, authorization.md

**Backend Specs:**
- `client-server/blueprints/server/backend/api/` — REST API conventions, content endpoints, project endpoints, sync protocol

**Optional Modules:**
- `client-server/blueprints/modules/discussions/` — Forums, threads, replies, reactions, polls
- `client-server/blueprints/modules/messaging/` — Direct messages with WebSocket
- `client-server/blueprints/modules/gamification/` — Points, badges, levels, leaderboards
- `client-server/blueprints/modules/notifications/` — Push/email/SMS
- `client-server/blueprints/modules/calendar-integration/` — Google Calendar sync
- `client-server/blueprints/modules/feature-flags/` — Feature toggles
- `client-server/blueprints/modules/feedback/` — In-app feedback collection
- `client-server/blueprints/modules/admin/` — Admin dashboard
- `client-server/blueprints/modules/oauth-providers/` — OAuth integrations

**Tools & Skills:**
- `tools/skills/init-platform/` — Onboarding wizard (walks through app identity, API config, module selection, platform targets)
- `tools/skills/temporal-plan-spec/` — Spec planning and review skill

**Test Vectors:**
- `client-server/verification/vectors/` — JSON test vectors for every MUST requirement
- `client-server/verification/runners/` — Platform-specific test runners (Swift XCTest, Kotlin JUnit, TypeScript Vitest)

**Playbooks:**
- `playbooks/` — High-level orchestration combining recipes and blueprints

**Operational Recipes:**
- `client-server/recipes/railway-setup.md` — Railway CLI infrastructure setup
- `client-server/recipes/cloudflare-setup.md` — Cloudflare CLI setup

## Claude Configuration

**Configuration Files:**
- `.claude/` — Claude Code project settings
- `CLAUDE.md` — Project rules, agentic-roadmaps integration

**Shared Project Integration:**
- Uses agentic-roadmaps for planning and implementation
- Path: `../agentic-roadmaps/`
- Skills symlinked from `~/.claude/skills/`

## Planning & Research Documents

Specs ARE the planning/research. Each spec includes:
- Frontmatter with version and status (draft → review → accepted → deprecated)
- Design Decisions section
- Changelog for evolution tracking

No separate planning directory — specs are versioned specifications.

## Git History & Current State

**Recent Activity:**
- `afe9c15` docs: add standardized project description
- `f600b40` chore: standardize worktree directory to .claude/worktrees/
- `cf2749c` chore: rename catherding → agentic-roadmaps
- `83c4a21` Update CLAUDE.md: litterbox → agentic-cookbook
- `a3e849b` fix: remove Swift .build artifacts and fix .gitignore
- `6cf7187` feat: add full-stack verification playbook
- `02456c0` feat: add playbook template format
- `76e33c0` fix: update all path references for new structure
- `6ea0d3e` chore: replace .gitkeep with tbd.md
- `f02ca9c` refactor: reorganize into multi-architecture platform
- `6066390` refactor: move verification vectors/runners
- `8de380f` refactor: move all specs under blueprints/
- `9846534` docs: add agentic-roadmaps shared project
- `0b0fdee` feat: add Railway CLI setup recipe
- `ac061e5` feat: add Cloudflare CLI setup recipe

**Pattern:** Ongoing spec organization, documentation, and infrastructure setup recipes.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Onboarding:**
```bash
/init-platform              # Interactive setup wizard
```

**Spec Viewing & Editing:**
```bash
# Specs are markdown files in client-server/blueprints/
# Edit with any text editor
# Follow spec authoring guide in docs/spec-authoring-guide.md
```

**Run Test Vectors:**
```bash
# Navigate to client-server/verification/runners/{platform}/
cd client-server/verification/runners/swift
# Load and run test vectors with platform's test runner
xcodebuild test  # Swift/XCTest

cd ../kotlin
./gradlew test   # Kotlin/JUnit

cd ../typescript
npm run test     # TypeScript/Vitest
```

## Notes

**Architecture Highlights:**

1. **Spec-Driven Design** — Reusable artifact is specification, not code
2. **Concrete Precision** — Data structures with exact JSON, algorithmic pseudocode, exact SQL
3. **Conformance Testing** — Test vectors ensure all implementations behave identically
4. **Template Variables** — Specs use placeholders ({{app_name}}, {{api_base_url}}) for customization
5. **Modular Specs** — Pick features you need via optional module selection
6. **Version Control** — Specs have explicit versions, status, dependencies, changelog

**Spec Format Standards:**

- **Frontmatter:** version, status, created, last-updated, author, copyright, platforms, tags, dependencies, supersedes
- **Sections:** Overview, Terminology, Behavioral Requirements (RFC 2119), Data Structures (JSON Schema), States, API Contract, Conformance Test Vectors, Edge Cases, Logging, Deep Linking, Privacy, Accessibility, Feature Flags, Analytics, Platform Notes, Design Decisions, Changelog
- **Requirements:** RFC 2119 keywords (MUST, SHOULD, MAY), numbered sequentially (REQ-001, REQ-002), every MUST has at least one test vector
- **Test Vectors:** Behavioral (tables) or Data (JSON blocks)

**Onboarding Wizard (/init-platform):**

1. **App Identity** — Name, organization, package prefix
2. **API Configuration** — Production and dev URLs
3. **Module Selection** — Pick features (discussions, messaging, gamification, etc.)
4. **Platform Targets** — Choose platforms (Apple, Android, Web, Windows)
5. **Generation** — Produces customized, resolved specs into your project

**Key Engineering Principles:**

1. **Prefer native controls** — Use platform frameworks before custom implementations
2. **Surface design decisions** — All LLM choices need explicit approval
3. **Post-generation verification** — Build, test, lint, verify logs, accessibility audit
4. **Small atomic commits** — One logical change per commit
5. **Comprehensive testing** — Unit tests before integration tests
6. **No main-thread blocking** — Use platform async primitives
7. **Always show progress** — Determinate or indeterminate UI feedback
8. **Deep linking** — All significant views must be deep linkable
9. **Accessibility from day one** — Semantic labels, keyboard nav, contrast, Dynamic Type
10. **Localizability** — All user-facing strings must be localizable
11. **RTL layout support** — Use leading/trailing not left/right
12. **Privacy by default** — Data minimization, consent, secure storage
13. **Feature flags from init** — Gate all features behind toggles
14. **Analytics from init** — Instrument significant user actions
15. **A/B testing support** — ExperimentProvider interface
16. **Debug mode** — Dev-only configuration panel
17. **Linting from day one** — SwiftLint, ktlint, ESLint configured
18. **Scriptable & automatable** — AppIntents, AppActions, API endpoints

**Best Practices References:**

Specs link to authoritative documentation:
- **Apple:** Human Interface Guidelines, Swift API Design Guidelines, Accessibility docs
- **Android:** Material Design 3, Architecture Recommendations, Kotlin Conventions
- **Web:** WCAG 2.1, WAI-ARIA Practices, OWASP Top 10
- **Cross-platform:** Nielsen Heuristics, OWASP Mobile Security (MASVS)

**Use Cases:**

1. **Platform Teams** — Share specs across implementations, ensure consistency
2. **Distributed Teams** — Clear contracts for parallel platform development
3. **AI-Assisted Development** — LLMs generate implementations from specs
4. **Documentation** — Specs serve as authoritative behavior documentation
5. **Testing** — Test vectors ensure all implementations behave identically
6. **Onboarding** — New developers get complete spec instead of scattered docs

**Philosophy:**

Traditional cross-platform frameworks (React Native, Flutter, KMP) share code. Temporal Platform shares behavioral specifications instead. Each platform implements natively using its own language, frameworks, and conventions. Conformance test vectors ensure all implementations behave identically.

```
            Specs (this repo)
           /        |        \
          /         |         \
    Swift       Kotlin     TypeScript
  (native)    (native)     (native)
      \         |          /
       \        |         /
     Conformance Tests
```
