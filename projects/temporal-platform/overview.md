# temporal-platform

## Project Summary

A spec-driven application platform for building offline-first, cross-platform apps. Instead of sharing code across platforms (like KMP, React Native, Flutter), Temporal Platform shares behavioral specifications -- markdown documents precise enough for an LLM to generate correct, testable implementations on any platform. Each platform implements specs natively using its own language and frameworks, while conformance test vectors ensure identical behavior. The repo contains specifications only -- no application code. Extracted from the Temporal app project as a reusable platform layer.

## Type & Tech Stack

- **Type**: Specification repository / platform framework (no application code)
- **Format**: Markdown specifications with YAML frontmatter, JSON test vectors
- **Spec features**: Concrete data structures, algorithmic pseudocode, exact SQL DDL, wire format examples, conformance test vectors
- **Target platforms**: Apple (Swift/SwiftUI), Android (Kotlin/Compose), Windows (Kotlin/Compose Multiplatform), Web (TypeScript/React)
- **Verification**: JSON test vectors with per-platform runners (Swift/XCTest, Kotlin/JUnit, TypeScript/Vitest)
- **Templating**: `{{placeholder}}` tokens for app-specific values (app_name, org_package, api_base_url, etc.)
- **Copyright**: Proprietary (2026 Mike Fullerton / Temporal)

## GitHub URL

`git@github.com:temporal-company/temporal-platform.git`

## Directory Structure

```
temporal-platform/
├── .claude/
│   └── (settings)
├── client-server/                     # Client-server architecture
│   ├── blueprints/                    # Behavioral specifications
│   │   ├── shared/                    # Cross-platform data layer
│   │   │   (models, sync, persistence, auth, content-types)
│   │   ├── server/                    # Server-side specs
│   │   │   ├── backend/              # API contracts, database, services, deployment
│   │   │   ├── admin-dashboard/      # Admin dashboard specs
│   │   │   └── monitoring-dashboard/ # Status/monitoring dashboard specs
│   │   ├── clients/                   # Per-platform client specs
│   │   │   ├── apple/
│   │   │   ├── android/
│   │   │   ├── web/
│   │   │   └── windows/
│   │   └── modules/                   # Optional feature modules
│   │       (discussions, messaging, gamification, notifications, calendar,
│   │        feature-flags, feedback, admin, oauth-providers)
│   ├── recipes/                       # Operational runbooks
│   │   ├── cloudflare-cli-setup.md
│   │   ├── railway-cli-setup.md
│   │   └── RECIPE-TEMPLATE.md
│   └── verification/                  # Conformance testing
│       ├── vectors/                   # Test vectors (JSON)
│       ├── runners/                   # Per-platform test runners
│       └── ci-configs/                # CI pipeline configs
├── apps/                              # Per-platform runnable app scaffolds
│   ├── apple/
│   ├── android/
│   ├── web/
│   └── windows/
├── playbooks/                         # High-level orchestration
│   ├── full-stack-verification.md
│   └── PLAYBOOK-TEMPLATE.md
├── tools/                             # Skills, agents, and tooling
│   ├── skills/                        # Claude Code skills (init-platform, temporal-plan-spec)
│   └── agents/                        # Claude Code agents
├── docs/                              # Documentation
│   └── client-server/                 # Docs mirroring architecture hierarchy
├── CLAUDE.md                          # Comprehensive spec authoring guide (14K)
└── README.md                          # Platform overview and getting started
```

## Key Files & Components

- `CLAUDE.md` -- Comprehensive guide (14K): spec format, template variables, test vector formats, implementation rules (18 rules), best practices references, engineering principles
- `README.md` -- Platform overview explaining the spec-driven approach, module system, sync architecture, content type plugin system, onboarding
- `client-server/blueprints/shared/` -- Core specs: syncable, content, project, user, calendar-event, edit-operation, sync-engine, snapshot-builder, conflict-resolution, local-database, repositories, content-type-system, authentication, authorization
- `client-server/blueprints/modules/` -- 9 optional modules: Discussions, Messaging, Gamification, Notifications, Calendar Integration, Feature Flags, Feedback, Admin, OAuth Providers
- `client-server/blueprints/modules/_module-template/TEMPLATE.md` -- Canonical spec template
- `playbooks/full-stack-verification.md` -- Full-stack verification playbook
- `tools/skills/` -- Claude Code skills including `init-platform` onboarding wizard

## Claude Configuration

- `CLAUDE.md` acts as the primary Claude configuration document with detailed spec authoring standards and implementation rules
- References shared project: `agentic-roadmaps` (expected at `../agentic-roadmaps/`)
- Skills globally installed as symlinks from `~/.claude/skills/` to `../agentic-roadmaps/skills/`

## Planning & Research Documents

- `playbooks/` -- Orchestration playbooks (full-stack-verification.md, PLAYBOOK-TEMPLATE.md)
- `docs/client-server/` -- Documentation mirroring the architecture hierarchy
- `client-server/recipes/` -- Infrastructure CLI setup runbooks (Cloudflare, Railway)

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: standardize worktree directory to .claude/worktrees/"
- **Working tree**: Clean
- **Recent activity**: Moderate (several commits per week through early April 2026)
- **Key recent changes**: Worktree standardization, agentic-roadmaps rename, Swift .build artifact cleanup, full-stack verification playbook, multi-architecture platform restructuring

## Build & Test Commands

```bash
# This is a specification-only repository -- no build commands
# Consumer projects use the /init-platform skill to generate customized specs

# For contributors editing specs:
# Follow the authoring standards in CLAUDE.md
# Use the template at client-server/blueprints/modules/_module-template/TEMPLATE.md
```

## Notes

- This is a specs-only repository -- no application code lives here
- Extracted from the Temporal app project; the original app used KMP to share ~1,000 lines of sync logic across 7 platforms, but build complexity outweighed the benefit
- The spec-driven approach trades shared code for shared specifications -- each platform gets native tooling while conformance tests guarantee consistent behavior
- Core sync engine uses Last-Writer-Wins (LWW) conflict resolution with a three-layer data architecture: base records, edit operations, and materialized snapshots
- Content Type Plugin System allows adding new feature areas (Notes, Projects, Reminders, etc.) without switch statements or hardcoded feature lists
- Each module has a `module.json` manifest declaring models, API endpoints, database tables, dependencies, and integration points
- 18 implementation rules in CLAUDE.md covering native controls, design decisions, accessibility, localization, RTL, privacy, feature flags, analytics, A/B testing, debug mode, linting, and scriptability
- The `/init-platform` skill walks consumers through app identity, API config, module selection, platform targets, and generates fully resolved specs
