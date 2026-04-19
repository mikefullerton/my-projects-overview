# Agentic Cookbook - Project Overview

## Project Summary

The **Agentic Cookbook** is a comprehensive, open-source structured library of principles, guidelines, ingredients, recipes, and workflows designed for AI-assisted multi-platform software development. Written entirely in markdown with YAML frontmatter, it serves as the knowledge base consumed directly by AI agents (particularly Claude Code) to build complete, tested, accessible, secure applications across multiple platforms.

**Core Value Proposition**: Code built with the cookbook is "trusted" -- complete, precise, consistent, verified, secure by default, accessible, tested, predictable, maintainable, native to each platform, incremental, documented, observable, and performant.

## Type & Tech Stack

**Project Type**: Knowledge base / Development framework / AI-agent resource library (no compiled code; provides specifications for code generation tools)

**Tech Stack**:
- **Content Format**: Markdown with YAML frontmatter (no compiled languages)
- **Validation**: TypeScript + Vitest (test harness for skills in `.claude/tests/`)
- **Skills**: 7 custom Claude Code skills for managing, linting, approving, and syncing artifacts
- **Platform**: Git-based, GitHub-hosted, consumed by Claude Code via `.claude/` configuration

**File Format Standards**:
- All content is `.md` files with YAML frontmatter
- Each artifact has: `id` (UUID), `title`, `domain` (`agentic-cookbook://...`), `type`, `version`, `status`, `created`, `modified`, `author`, `summary`, `platforms`, `tags`, `depends-on`, `related`, `references`
- Named requirements using RFC 2119 keywords (MUST, SHOULD, MAY) with kebab-case names
- Change history table required for all artifacts

## GitHub URL

**Repository**: https://github.com/agentic-cookbook/cookbook
**Remote**: `git@github.com:agentic-cookbook/cookbook.git`

## Directory Structure

```
cookbook/
├── .claude/
│   ├── CLAUDE.md                     # Agent context (repo structure, conventions, workflow)
│   ├── settings.json                 # Permissions for skills/tools
│   ├── settings.local.json           # Local overrides
│   ├── rules/                        # 3 rules
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
│   ├── tests/                        # Vitest harness for skill testing
│   └── worktrees/                    # Temporary git worktrees for PR workflows
├── introduction/                     # Getting started, conventions, glossary
├── principles/                       # 18 engineering principles
├── guidelines/                       # 88 topic-organized guidelines
│   ├── testing/                      # Test pyramid, patterns, doubles, mutation testing
│   ├── security/                     # Auth, tokens, CORS, privacy, secure storage
│   ├── ui/                           # Typography, spacing, color, layout
│   ├── accessibility/                # Screen readers, keyboard nav, Dynamic Type
│   ├── internationalization/         # Localization, RTL
│   ├── concurrency/                  # Background work, main thread safety
│   ├── logging/                      # Structured logging, analytics
│   ├── feature-management/           # Feature flags, A/B testing
│   ├── code-quality/                 # Linting, atomic commits
│   ├── database-design/              # 22 SQLite best practices (added Apr 6)
│   └── skills-and-agents/            # Authoring skills, rules, agents
├── ingredients/                      # 18 atomic component specs
│   ├── ui/components/                # Leaf UI controls (7)
│   ├── ui/panels/                    # Content panes (6)
│   ├── infrastructure/               # Non-visual patterns (3)
│   ├── developer-tools/              # Dev tool specs (1)
│   └── web/                          # Web components (1)
├── recipes/                          # 11 compositions of ingredients
│   ├── ui/windows/                   # Full windows (settings, terminal)
│   └── (other categories)
├── compliance/                       # 10 categories, 81 checks
│   ├── artifact-formatting/          # Formatting specs per artifact type (5)
│   └── (security, performance, accessibility, etc.)
├── workflows/                        # 6 workflow specs
├── reference/                        # Schemas, examples, best-practices links
│   ├── cookbook.schema.json           # JSON Schema for cookbook.json manifests
│   └── examples/my-document-editor-cookbook/
├── appendix/                         # Research, decisions, contributing
├── docs/superpowers/                 # Design specs and implementation plans
├── index.md                          # Master table of contents
├── README.md                         # Human-facing documentation
└── LICENSE                           # MIT
```

## Key Files & Components

### Content Artifacts (135+ markdown files)
- **Principles** (18): Simplicity, YAGNI, Fail Fast, DI, Immutability, Composition, Separation of Concerns, Design for Deletion, Explicit > Implicit, Small Reversible Decisions, Tight Feedback Loops, Manage Complexity, Least Astonishment, Idempotency, Native Controls, Open Source Preference, Make It Work/Right/Fast, Optimize for Change
- **Guidelines** (88): Testing, Security, UI, Accessibility, i18n, Concurrency, Logging, Feature Management, Code Quality, Database Design, Skills & Agents, Language, Platform
- **Ingredients** (18): Atomic component specs (UI controls, panels, infrastructure patterns)
- **Recipes** (11): Composed features combining configured ingredients

### Compliance (81 checks in 10 categories)
Security, User Safety, Performance, Best Practices, Access Patterns, Accessibility, Privacy & Data, Platform Compliance, Reliability, Internationalization. Plus artifact-formatting specs for each type.

### Workflows (6)
Branching strategy, code planning, implementation, verification, review, guideline checklist.

### Cookbook Manifest (cookbook.json)
A self-contained, platform-agnostic project definition assembling recipes and ingredients into a complete application. See `reference/cookbook.schema.json` for schema.

## Claude Configuration

### Rules (3)
1. **always-use-worktrees-and-prs.md**: All changes through worktrees + PRs. Draft PR before code. Small commits pushed after each. Squash merge via `gh pr merge --squash`. Clean up worktree after merge.
2. **after-adding-an-artifact.md**: Run `/approve-artifact`, update `index.md`, fix cross-references, update README/CLAUDE.md counts, sync to agenticcookbookweb via `/update-website`.
3. **artifact-formatting.md**: Read type-specific compliance file before writing. Follow required section orders. Use RFC 2119 keywords and kebab-case requirement names.

### Skills (7)
1. **lint-artifact**: Validate against type-specific formatting spec
2. **approve-artifact**: Lint + stamp frontmatter with approval metadata
3. **add-artifact**: Interactive artifact creation
4. **create-artifact**: Scaffolded artifact creation
5. **repair-cookbook**: Fix referential integrity, broken cross-references
6. **update-website**: Rsync content to agenticcookbookweb repo
7. **install-cookbook-global**: Onboarding -- set up CLAUDE.md and install rules

### Permissions (settings.json)
Allows: Read, Glob, Grep, Edit, Write, Bash (git, gh, ls, find, wc, diff, mkdir, cp, rm, mv, cat, head, tail, grep, python3, claude)

### Tests (Vitest harness in .claude/tests/)
7 test suites covering all skills. Sandboxed execution in `/tmp/`. Run with `npm test` from `.claude/tests/`.

## Planning & Research Documents

### docs/superpowers/
- **2026-04-06 Rename Concoction to Cookbook** -- Completed. Renamed "concoction" to "project cookbook" for better metaphor alignment. 4 file renames, 13 content updates.
- **2026-04-04 Skill Test Harness** -- Completed. Vitest-based harness testing all 7 skills via `claude -p` against sandboxed temp directories.

### appendix/
- **decisions/**: Architectural decision records (ingredient-recipe-cookbook hierarchy, etc.)
- **research/**: Design research and evaluations
- **contributing/**: Contribution guidelines

## Git History & Current State

**Branch:** `main`
**Working Tree:** Clean (no uncommitted changes)

**Recent Commits:**
```
319cba9 (2026-04-06) docs: add rename concoction-to-cookbook design spec
fe12a56 (2026-04-06) Add 22 database-design cookbook artifacts for platform-database specialist
db65074 (2026-04-06) Rename concoction to project cookbook (#44)
f83631e (2026-04-06) Document worktree directory path in CLAUDE.md git workflow section
0face55 (2026-04-05) Reclassify recipes into ingredients and update sibling projects (#43)
```

**Key Recent Milestones:**
- 22 database-design guidelines added (Apr 6)
- "Concoction" renamed to "project cookbook" (Apr 6)
- Recipes reclassified into ingredients (Apr 5)
- Skill test harness added (Apr 4)
- All 149 artifacts linted and approved (Apr 4)
- Repo reorganized as a "book" structure (Apr 2)

## Build & Test Commands

**No build step** (markdown-based knowledge base)

```bash
# Skill tests (from .claude/tests/)
cd .claude/tests && npm install && npm test

# Individual skill tests
npm run test:lint        # lint-artifact
npm run test:approve     # approve-artifact
npm run test:smoke       # quick lint + approve
npm run test:e2e         # end-to-end (slower)

# Via skills (in Claude Code)
/lint-artifact <path>
/approve-artifact <path>
/repair-cookbook
/validate-cookbook         # (via dev-team plugin)
```

## Notes

1. **Knowledge base for AI agents**, not a code library. Defines what "trusted" code means and provides specifications AI assistants use to generate high-quality code.

2. **Artifact format**: YAML frontmatter + named requirements (kebab-case, RFC 2119) + test vectors + change history + cross-references via domain URLs (`agentic-cookbook://principles/simplicity`).

3. **Sibling projects**: dev-team (multi-agent plugin, provides user-facing skills), agenticcookbookweb (React 19 + Cloudflare Workers web app at agentic-cookbook.com).

4. **Git workflow**: Owner edits direct to main. Claude Code sessions through worktree + branch + PR. Worktree directory: `.claude/worktrees/`.

5. **Contribution workflow**: External contributors use fork-based PRs via `/contribute-to-cookbook` skill (in dev-team). Owners use local worktrees + direct PRs.

6. **Active development**: Most recent work on database design guidelines and concoction-to-cookbook rename.
