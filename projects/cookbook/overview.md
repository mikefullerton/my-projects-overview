# Agentic Cookbook - Project Overview

## Project Summary

The **Agentic Cookbook** is a comprehensive, open-source structured library of principles, guidelines, ingredients, recipes, and workflows designed for AI-assisted multi-platform software development. Written entirely in markdown with YAML frontmatter, it serves as the knowledge base consumed directly by AI agents (particularly Claude Code) to build complete, tested, accessible, secure applications across multiple platforms.

**Core Value Proposition**: Code built with the cookbook is "trusted" — complete, precise, consistent, verified, secure by default, accessible, tested, predictable, maintainable, native to each platform, incremental, documented, observable, and performant.

---

## Type & Tech Stack

**Project Type**: Knowledge base / Development framework / AI-agent resource library (no code generation; provides specifications for code generation tools)

**Tech Stack**:
- **Content Format**: Markdown with YAML frontmatter (no compiled languages)
- **Validation**: TypeScript + Vitest (test harness for skills in `.claude/tests/`)
- **Skills**: 7 custom Claude Code skills for managing, linting, approving, and syncing artifacts
- **Platform**: Git-based, GitHub-hosted, consumed by Claude Code via `.claude/` configuration
- **Dependencies**: Vitest 3.2.1 (for skill testing only)

**File Format Standards**:
- All content is `.md` files with YAML frontmatter (frontmatter required, no exceptions)
- Each artifact has: `id` (UUID), `title`, `domain` (agentic-cookbook://...`), `type`, `version`, `status`, `created`, `modified`, `author`, `summary`, `platforms`, `tags`, `depends-on`, `related`, `references`
- Change history table required for all artifacts
- Named requirements using RFC 2119 keywords (MUST, SHOULD, MAY) with kebab-case names

---

## GitHub URL

**Repository**: https://github.com/agentic-cookbook/cookbook

**Organization**: agentic-cookbook (collaborative, open-source)

**Remote**: `git@github.com:agentic-cookbook/cookbook.git`

---

## Directory Structure

```
cookbook/
├── .claude/                          # Claude Code integration
│   ├── CLAUDE.md                     # Agent context file (copy of README with config notes)
│   ├── settings.json                 # Permissions for skills/tools
│   ├── settings.local.json           # Local overrides
│   ├── rules/                        # 3 git & artifact workflow rules
│   │   ├── always-use-worktrees-and-prs.md
│   │   ├── after-adding-an-artifact.md
│   │   └── artifact-formatting.md
│   ├── skills/                       # 7 custom skills
│   │   ├── add-artifact/
│   │   ├── approve-artifact/
│   │   ├── create-artifact/
│   │   ├── lint-artifact/
│   │   ├── repair-cookbook/
│   │   ├── update-website/
│   │   └── install-cookbook-global/
│   ├── tests/                        # Vitest harness
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── vitest.config.ts
│   │   ├── specs/                    # Test suites for each skill
│   │   ├── lib/                      # Test helpers
│   │   └── fixtures/                 # Sample artifacts for testing
│   └── worktrees/                    # Temporary git worktrees for PR workflows
│
├── introduction/                     # Getting started (3 files)
│   ├── getting-started.md
│   ├── conventions.md                # File format, naming, cross-referencing rules
│   ├── glossary.md                   # Term definitions
│   └── INDEX.md
│
├── principles/                       # 18 engineering principles
│   ├── simplicity.md
│   ├── yagni.md
│   ├── fail-fast.md
│   ├── dependency-injection.md
│   ├── immutability-by-default.md
│   ├── composition-over-inheritance.md
│   ├── separation-of-concerns.md
│   ├── design-for-deletion.md
│   ├── explicit-over-implicit.md
│   ├── small-reversible-decisions.md
│   ├── tight-feedback-loops.md
│   ├── manage-complexity-through-boundaries.md
│   ├── principle-of-least-astonishment.md
│   ├── idempotency.md
│   ├── native-controls.md
│   ├── open-source-preference.md
│   ├── support-automation.md
│   ├── make-it-work-make-it-right-make-it-fast.md
│   ├── meta-principle-optimize-for-change.md
│   └── INDEX.md
│
├── guidelines/                       # 88 topic-organized guidelines
│   ├── testing/                      # Test pyramid, patterns, doubles, mutation testing
│   ├── security/                     # Auth, tokens, CORS, privacy, secure storage
│   ├── ui/                           # Typography, spacing, color, layout, accessibility
│   ├── networking/                   # API design, caching, retries, timeouts
│   ├── accessibility/                # Screen readers, keyboard nav, Dynamic Type
│   ├── internationalization/         # Localization, RTL support
│   ├── concurrency/                  # Background work, main thread safety
│   ├── logging/                      # Structured logging, analytics
│   ├── feature-management/           # Feature flags, A/B testing, debug mode
│   ├── code-quality/                 # Linting, atomic commits
│   ├── language/                     # Language-specific guidance (Swift, Kotlin, C#, Python)
│   ├── platform/                     # Deep linking, search, widgets, notifications
│   ├── database-design/              # SQLite best practices (22 artifacts added Apr 6)
│   ├── skills-and-agents/            # Authoring skills, rules, agents
│   └── INDEX.md (master index)
│
├── ingredients/                      # 18 atomic component specs (building blocks)
│   ├── ui/
│   │   ├── components/               # Leaf UI controls
│   │   │   ├── ai-chat-control.md
│   │   │   ├── color-profile.md
│   │   │   ├── empty-state.md
│   │   │   ├── git-status-indicator.md
│   │   │   ├── metadata-line.md
│   │   │   ├── status-bar.md
│   │   │   ├── collapsible-pane-header.md
│   │   │   └── INDEX.md
│   │   └── panels/                   # Content panes
│   │       ├── ai-settings-panel.md
│   │       ├── code-editor-pane.md
│   │       ├── debug-panel.md
│   │       ├── file-tree-browser.md
│   │       ├── inspector-panel.md
│   │       ├── terminal-pane.md
│   │       └── INDEX.md
│   ├── infrastructure/               # Non-visual patterns
│   │   ├── logging.md
│   │   ├── settings-keys.md
│   │   ├── window-frame-persistence.md
│   │   └── INDEX.md
│   ├── developer-tools/
│   │   ├── yolo-mode.md
│   │   └── INDEX.md
│   ├── web/
│   │   ├── appearance-mode-toggle.md
│   │   └── INDEX.md
│   └── INDEX.md (master)
│
├── recipes/                          # 11 compositions of ingredients into features
│   ├── ui/
│   │   ├── components/               # Composed controls
│   │   │   └── INDEX.md
│   │   ├── panels/                   # Composed panes
│   │   │   └── INDEX.md
│   │   ├── windows/                  # Full windows
│   │   │   ├── settings-window.md
│   │   │   ├── standalone-terminal-window.md
│   │   │   └── INDEX.md
│   │   └── INDEX.md
│   ├── app/                          # App-level recipes
│   │   └── INDEX.md
│   ├── developer-tools/
│   │   └── INDEX.md
│   ├── autonomous-dev-bots/
│   │   └── INDEX.md
│   ├── infrastructure/
│   │   └── INDEX.md
│   ├── web/
│   │   └── INDEX.md
│   └── INDEX.md (master)
│
├── compliance/                       # 10 categories, 81 checks (verification checklists)
│   ├── security.md                   # ~10 checks
│   ├── user-safety.md                # ~7 checks
│   ├── performance.md                # ~7 checks
│   ├── best-practices.md             # ~9 checks
│   ├── access-patterns.md            # ~8 checks
│   ├── accessibility.md              # ~9 checks
│   ├── privacy-and-data.md           # ~9 checks
│   ├── platform-compliance.md        # ~7 checks
│   ├── reliability.md                # ~10 checks
│   ├── internationalization.md       # ~8 checks
│   ├── artifact-formatting/          # Formatting specs for each artifact type
│   │   ├── principle-formatting.md   # 7 structural checks
│   │   ├── guideline-formatting.md   # 8 structural checks
│   │   ├── ingredient-formatting.md  # 16 structural checks
│   │   ├── recipe-formatting.md      # 14 structural checks
│   │   ├── cookbook-formatting.md    # 10 structural checks (formerly concoction)
│   │   └── INDEX.md
│   └── INDEX.md (master)
│
├── workflows/                        # 6 workflow specifications
│   ├── branching-strategy.md         # Git branch patterns, worktree flow
│   ├── code-planning.md              # Design, spec, review cycles
│   ├── code-implementation.md        # Commit, test, lint patterns
│   ├── code-verification.md          # Testing, linting, accessibility, logging
│   ├── code-review.md                # Review checklist, approval process
│   ├── guideline-checklist.md        # Checklist of all 88 guidelines for verification
│   ├── _template.md                  # Template for new workflows
│   └── INDEX.md
│
├── reference/                        # External resources, schemas, examples
│   ├── cookbook.schema.json          # JSON Schema for cookbook.json manifests
│   ├── best-practices/               # Links to external best-practice resources
│   ├── examples/                     # Example project cookbooks
│   │   ├── my-document-editor-cookbook/
│   │   │   ├── cookbook.json         # Complete manifest example
│   │   │   ├── app/
│   │   │   ├── resources/
│   │   │   └── context/
│   │   └── INDEX.md
│   └── INDEX.md
│
├── appendix/                         # Research and supporting materials
│   ├── contributing/                 # Contribution guidelines
│   ├── decisions/                    # Architectural decision records
│   │   ├── ingredient-recipe-cookbook-hierarchy.md
│   │   └── other decisions...
│   ├── research/                     # Design research, evaluations
│   └── INDEX.md
│
├── docs/                             # Working documents and plans (not published)
│   └── superpowers/
│       ├── plans/                    # Implementation plans
│       │   └── 2026-04-04-skill-test-harness.md
│       └── specs/                    # Design specifications
│           ├── 2026-04-06-rename-concoction-to-cookbook-design.md
│           └── 2026-04-04-skill-test-harness-design.md
│
├── .superpowers/                     # Claude Code superpowers integration
│   └── brainstorm/
│
├── index.md                          # Master table of contents (3.2.0)
├── README.md                         # Human-facing documentation
├── LICENSE                           # MIT license
└── .gitignore
```

---

## Key Files & Components

### Content Artifacts (196 markdown files)
- **Principles** (18 files): Foundational engineering concepts that guide decisions
- **Guidelines** (88 files): Topic-organized rules for planning and implementation
- **Ingredients** (18 files): Atomic, reusable component specifications (UI controls, panels, infrastructure)
- **Recipes** (11 files): Composed features combining multiple ingredients

Each artifact follows a strict format:
- YAML frontmatter with metadata
- Semantic sections (Overview, Behavioral Requirements, Appearance, States, Accessibility, Conformance Test Vectors, Edge Cases, Change History)
- Named requirements using RFC 2119 keywords
- Kebab-case requirement identifiers
- Cross-references using `agentic-cookbook://` domain URLs

### Compliance (81 verification checks in 10 categories)
- Security, User Safety, Performance, Best Practices, Access Patterns, Accessibility, Privacy & Data, Platform Compliance, Reliability, Internationalization
- Plus artifact-formatting specs for each artifact type (principle, guideline, ingredient, recipe, cookbook)

### Workflows (6 process specifications)
- Branching strategy (worktree-based PR flow)
- Planning, implementation, verification, review, guideline checklists

### Claude Code Integration (.claude/)

#### Rules (3 files)
1. **always-use-worktrees-and-prs.md**: Enforces worktree-based git workflow; all changes through branches + PRs, no direct main commits
2. **after-adding-an-artifact.md**: Post-change checklist: lint, update indexes, sync to cookbook-web
3. **artifact-formatting.md**: Structural requirements for each artifact type

#### Skills (7 custom tools)
1. **lint-artifact**: Validates artifact against type-specific formatting spec
2. **approve-artifact**: Runs lint + stamps frontmatter with approval metadata
3. **add-artifact**: Interactive tool to create new artifacts
4. **create-artifact**: Create artifact with scaffolding
5. **repair-cookbook**: Fix referential integrity, broken cross-references, orphaned files
6. **update-website**: Rsync cookbook content to cookbook-web repo
7. **install-cookbook-global**: Onboarding skill (in this repo; also available via dev-team plugin)

#### Tests (Vitest harness in .claude/tests/)
- `package.json`: npm scripts for test:lint, test:approve, test:add, test:create, test:website, test:repair, test:install, test:smoke
- `vitest.config.ts` + `vitest.e2e.config.ts`: Test configuration
- `specs/`: 7 test files, one per skill
- `fixtures/`: Sample artifacts (valid principle, guideline, recipe, cookbook; bad frontmatter, structure)
- `lib/`: Helper functions for test setup, sandbox directory management, CLI invocation

#### Permissions (settings.json)
Allows: Read, Glob, Grep, Edit, Write, Bash (git, gh, ls, find, wc, diff, mkdir, cp, rm, mv, cat, head, tail, grep, python3, claude)

---

## Claude Configuration

**Integration Points**:
- `.claude/CLAUDE.md`: Context document listing all 196 artifacts, sibling projects, conventions, git workflow
- `.claude/rules/`: 3 mandatory rules controlling git workflow, artifact lifecycle, formatting compliance
- `.claude/skills/`: 7 reusable skills for cookbook management (lint, approve, add, create, repair, update-website, install)
- `.claude/settings.json`: Permissions allowing powerful file manipulation for workflow automation

**Git Workflow** (via rules):
1. All changes through git worktrees (`git worktree add .claude/worktrees/<branch-name>`)
2. Branch patterns: `feature/<description>`, `revise/<description>`, `fix/<description>`
3. Draft PR created immediately before any code is written
4. Small atomic commits with clear messages, push after each commit
5. PR marked ready when all work is done
6. CI checks must pass before merge
7. Squash merge via `gh pr merge --squash`
8. Worktree cleaned up immediately after merge

**Artifact Lifecycle** (via rules):
1. Create artifact from type-specific template
2. Run `/approve-artifact` (must pass all lint checks)
3. Update `index.md` and relevant section indexes
4. Update cross-references in other artifacts
5. Update artifact counts in README.md and CLAUDE.md
6. Run `/update-website` to sync to cookbook-web

---

## Planning & Research Documents

**Recent Work** (in `docs/superpowers/`):

### 1. Rename Concoction to Project Cookbook (Apr 6, 2026)
**Status**: Completed, merged as commit `319cba9`
**Summary**: Renamed the "concoction" concept to "project cookbook" to better fit the cooking metaphor (ingredients → recipes → cookbook). Introduced clear distinction:
- **Top-level cookbook**: This repo (source of principles, guidelines, ingredients, recipes)
- **Project cookbook**: An assembly of recipes + ingredients into a complete app (defined by `cookbook.json` manifest)

**Changes**:
- 4 file/dir renames (concoction → cookbook)
- 13 content updates across README, CLAUDE.md, conventions, glossary, schema, etc.
- Domain identifiers updated in cross-references

### 2. Skill Test Harness Implementation (Apr 4, 2026)
**Status**: Completed, merged as commit `c8b1f6b`
**Summary**: Built a Vitest-based test harness in `.claude/tests/` to test all 7 cookbook skills by invoking them via `claude -p` against sandboxed temp directories in `/tmp/`.

**Architecture**: 
- Runner reads SKILL.md, substitutes variables, invokes Claude CLI
- Fixtures create minimal cookbook copies in temp directories
- Assertions check filesystem outcomes and CLI output
- All execution sandboxed — real repo never modified

**Tech Stack**: Vitest 3.x, TypeScript, Node.js child_process, Claude CLI

**Test scripts**:
- `npm test` — all tests
- `npm run test:lint` — lint-artifact skill
- `npm run test:approve` — approve-artifact skill
- `npm run test:smoke` — quick smoke test (lint + approve)

---

## Git History & Current State

**Branch**: `main`

**Remote Status**: Ahead of `origin/main` by 1 commit (local work not yet pushed)

**Working Tree**: Clean (no uncommitted changes)

**Recent Commits** (30 most recent):
1. `319cba9` (2026-04-06 18:40:53) — docs: add rename concoction-to-cookbook design spec
2. `fe12a56` (2026-04-06 17:41:34) — Add 22 database-design cookbook artifacts for platform-database specialist
3. `db65074` (2026-04-06 16:33:39) — Rename concoction to project cookbook (#44)
4. `f83631e` (2026-04-06 16:05:13) — Document worktree directory path in CLAUDE.md git workflow section
5. `0face55` (2026-04-05 13:14:37) — Reclassify recipes into ingredients and update sibling projects (#43)
6. `90e5f7a` — Add ingredient/recipe/concoction artifact hierarchy (#42)
7. `c8b1f6b` — Add skill test harness with Vitest + Claude CLI (#41)
8. `af90c86` — Lint and approve all 149 cookbook artifacts (#40)
9. `f52c333` — Add artifact skills, rules, and compliance formatting (#39)
10. `2f3678a` — Add .claude/worktrees/ to .gitignore

**Key Milestones** (last 30 commits):
- Massive artifact approval run (149 artifacts linted & approved in one commit)
- Reorganized repo as a "book" with clear structure (commit `10bb1d1`)
- Moved skills, rules, scripts to dev-team plugin
- Fixed referential integrity and broken links across codebase
- Added orphan detection and repair tools
- Updated GitHub org to agentic-cookbook/cookbook

---

## Build & Test Commands

**No build step** (markdown-based knowledge base, no compilation)

**Test Commands** (in `.claude/tests/`):
```bash
# All tests
npm test

# End-to-end tests (slower, tests artifact creation)
npm run test:e2e

# Individual skill tests
npm run test:lint        # lint-artifact skill
npm run test:approve     # approve-artifact skill
npm run test:add         # add-artifact skill
npm run test:create      # create-artifact skill (e2e)
npm run test:website     # update-website skill
npm run test:repair      # repair-cookbook skill
npm run test:install     # install-cookbook-global skill

# Quick smoke test
npm run test:smoke       # lint + approve tests
```

**Setup** (if running tests locally):
```bash
cd .claude/tests
npm install
npm test
```

**Linting & Validation** (via skills, not CI):
- `/lint-artifact <path>` — Check formatting against type spec
- `/approve-artifact <path>` — Lint + stamp frontmatter
- `/repair-cookbook` — Fix broken references, orphaned files
- `/validate-cookbook` — (via dev-team plugin) Full integrity check

---

## Notes

### Project Purpose & Philosophy
The Agentic Cookbook is a **knowledge base for AI agents**, not a code library. It defines what "trusted" code means: complete, tested, accessible, secure, maintainable, and native to each platform. It's consumed by AI assistants (Claude Code) to generate high-quality code that follows these principles.

### Artifact Format Innovation
Every artifact is a markdown file with strict structure:
- YAML frontmatter (metadata, versioning, approval tracking)
- Named requirements with RFC 2119 keywords
- Test vectors and edge cases
- Change history table
- Cross-referencing via domain URLs (`agentic-cookbook://principles/simplicity`)

This format is designed to be both human-readable (for manual review) and machine-parseable (for automated validation).

### Sibling Projects
1. **dev-team** (GitHub: agentic-cookbook/dev-team): Multi-agent orchestration system. Provides user-facing cookbook skills (install, configure, plan-recipe, contribute, validate, lint, help). Also contains the same skills as local copies (.claude/skills/).

2. **cookbook-web** (GitHub: agentic-cookbook/cookbook-web): Cloudflare Workers web app for browsing the cookbook. React 19, TypeScript, Tailwind 4. Serves as public-facing website. Synced via `/update-website` skill.

### Recent Major Changes
- **Database Design Guidelines** (Apr 6): Added 22 new artifacts covering SQLite best practices, schema design, performance, device-to-server sync, production operations.
- **Rename Concoction → Project Cookbook** (Apr 6): Introduced clearer terminology to distinguish source cookbook (this repo) from project cookbooks (app-specific assemblies).
- **Artifact Approval at Scale** (Apr 4): Linted and approved all 149 cookbook artifacts in a single coordinated run.
- **Test Harness** (Apr 4): Added Vitest-based testing for all 7 skills with sandboxed execution.

### Current State Highlights
- **196 markdown artifact files**: 18 principles, 88 guidelines, 18 ingredients, 11 recipes, plus 61 other reference/compliance/workflow files
- **7 custom skills** for management (lint, approve, add, create, repair, update-website, install)
- **Vitest harness** with 7 test suites covering all skills
- **3 mandatory rules** controlling git workflow, artifact lifecycle, formatting
- **10 compliance categories** with 81 verification checks
- **6 workflow specifications** for planning, implementation, verification, review
- **1 commit ahead of origin** (awaiting push)

### Contribution Workflow
External contributors use fork-based PRs. The `/contribute-to-cookbook` skill (in dev-team) detects this automatically and adjusts the workflow (fork as origin, PR to upstream). Owners use local worktrees + direct PRs to the main repo.

### Knowledge Consumption Model
AI agents consume this knowledge in multiple ways:
1. **Direct read**: `.claude/CLAUDE.md` provides full context at session start
2. **Skill invocation**: `/lint-artifact`, `/approve-artifact`, `/repair-cookbook` perform specific tasks
3. **Index navigation**: `index.md` and section indexes (INDEX.md in each directory) guide agents through the catalog
4. **Cross-references**: Domain URLs (`agentic-cookbook://...`) link artifacts together, allowing agents to traverse relationships
5. **Rule enforcement**: `.claude/rules/` defines mandatory workflows that Claude Code agents follow

---

**Last Updated**: 2026-04-07 (This overview created after commits through 2026-04-06 18:40:53)

**Status**: Active development. Most recent work on database design guidelines and concoction → project cookbook rename.

