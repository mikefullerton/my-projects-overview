# Cookbook Web Project Overview

## Project Summary

A Cloudflare Workers web application that serves as the public-facing browsable interface for the Agentic Cookbook — a structured collection of principles, guidelines, recipes, and workflows for AI-assisted multi-platform development. Built with React 19, TypeScript, and Tailwind CSS 4, deployed to `agentic-cookbook.com`.

## Type & Tech Stack

**Project Type:** Web Application / Public Documentation Site

**Core Technologies:**
- **Runtime:** Cloudflare Workers (serverless edge computing)
- **Frontend:** React 19, TypeScript 5.7
- **Styling:** Tailwind CSS 4, PostCSS 8
- **Routing:** React Router 7
- **Build Tools:** Vite 6, Wrangler 4.78
- **Markdown Processing:** Remark + Rehype unified ecosystem (remark-parse, remark-gfm, rehype-slug, rehype-autolink-headings)
- **Syntax Highlighting:** Shiki 1.0
- **Search:** Fuse.js 7.0
- **Testing:** Playwright 1.58 (visual regression tests)
- **Node.js Target:** ES2022

**Key Dependencies:**
- `react@^19.0.0`, `react-dom@^19.0.0`
- `react-router@^7.0.0`
- `@cloudflare/vite-plugin@^1.30.2`
- `unified@^11.0.0`, `remark-*` packages
- `rehype-*` packages for HTML transformations
- `gray-matter@^4.0.3` for YAML frontmatter parsing
- `@tailwindcss/postcss@^4.2.2`, `@tailwindcss/typography@^0.5.19`
- `@playwright/test@^1.58.2` for visual testing
- `.mcp.json` configured for Playwright MCP (vision capabilities)

## GitHub URL

[https://github.com/agentic-cookbook/cookbook-web](https://github.com/agentic-cookbook/cookbook-web)

## Directory Structure

```
cookbook-web/
├── .claude/                          # Claude Code configuration
│   └── rules/
│       ├── cookbook.md              # Cookbook rules (6 core principles)
│       └── site-design.md           # Comprehensive design system spec (12KB)
├── .cookbook/                        # Cookbook configuration directory
├── .playwright-mcp/                  # Playwright MCP integration
├── .wrangler/                        # Wrangler build artifacts
├── cookbook/                         # The Agentic Cookbook content
│   ├── appendix/
│   │   └── research/                # Research materials and evaluations
│   ├── compliance/                  # 10+ compliance categories with checks
│   ├── docs/                        # Documentation
│   ├── guidelines/                  # ~105 markdown files on UI, testing, security, etc.
│   ├── ingredients/                 # ~23 atomic component specs
│   ├── introduction/                # Getting started materials
│   ├── principles/                  # ~20 engineering principles
│   ├── recipes/                     # ~24 feature composition files
│   ├── reference/                   # External best-practices links, schemas
│   ├── workflows/                   # 6 workflow specifications
│   ├── index.md                     # Cookbook table of contents
│   ├── README.md                    # Cookbook overview (159 lines)
│   ├── LICENSE                      # MIT license
│   └── .superpowers/                # Untracked superpowers data
├── dist/                             # Production build output
│   └── assets/
├── node_modules/                     # Dependencies (198 packages)
├── public/                           # Static assets
├── src/                              # Source code (~2,647 lines TypeScript)
│   ├── App.tsx                       # Root component with routing
│   ├── main.tsx                      # React entry point
│   ├── index.css                     # Global styles
│   ├── components/
│   │   ├── content/                 # Content rendering components
│   │   │   ├── DocPage.tsx          # Main documentation page renderer
│   │   │   ├── PlatformFilter.tsx   # Platform filtering UI
│   │   │   ├── SearchDialog.tsx     # Command+K search interface
│   │   │   └── StatusBadge.tsx      # Status indicators
│   │   ├── layout/                  # Layout components
│   │   │   ├── Header.tsx           # Sticky top navigation bar
│   │   │   ├── Sidebar.tsx          # Desktop + mobile sidebar navigation
│   │   │   ├── Breadcrumbs.tsx      # Breadcrumb navigation
│   │   │   └── TableOfContents.tsx  # In-page TOC for doc pages
│   │   └── sections/                # Page-specific section components
│   │       ├── HomePage.tsx         # Main overview page
│   │       ├── SectionIndex.tsx     # Index pages (Principles, Guidelines, etc.)
│   │       ├── DocPage.tsx          # Individual document pages
│   │       ├── GettingStartedPage.tsx
│   │       ├── ProjectsPage.tsx     # Projects showcase
│   │       └── ToolingPage.tsx      # Tooling information
│   ├── contexts/
│   │   ├── ContentContext.tsx       # Loads cookbook data from virtual module
│   │   └── ThemeContext.tsx         # Dark/light theme management
│   ├── lib/                         # Utilities
│   ├── plugins/
│   │   ├── vite-plugin-cookbook.ts  # Custom Vite plugin that:
│   │   │   - Scans cookbook directories for .md files
│   │   │   - Parses YAML frontmatter with gray-matter
│   │   │   - Converts Markdown to HTML via remark/rehype pipeline
│   │   │   - Extracts headings and generates table of contents
│   │   │   - Creates virtual module for build-time injection
│   │   └── rehype-cross-references.ts # Cross-reference link processing
│   └── types/
│       ├── cookbook.ts              # TypeScript types for cookbook entries
│       └── virtual-modules.d.ts     # Type definitions for virtual modules
├── tests/
│   ├── visual.spec.ts               # Playwright visual regression tests
│   └── visual.spec.ts-snapshots/    # Screenshot baselines
├── tools-site/                       # Separate Cloudflare Workers project (nested)
│   ├── src/
│   ├── dist/
│   ├── migrations/
│   └── scripts/
├── .gitignore                        # Ignores PNG screenshots in root
├── .mcp.json                        # MCP configuration (Playwright)
├── CLAUDE.md                         # Claude Code project configuration
├── index.html                        # Main HTML entry point
├── bookcover.html                    # Book cover landing page (animated)
├── package.json                      # Dependencies and scripts
├── package-lock.json                 # Locked dependency versions
├── tsconfig.json                     # TypeScript configuration
├── vite.config.ts                    # Vite build configuration
├── wrangler.jsonc                    # Cloudflare Wrangler config
├── playwright.config.ts              # Playwright test configuration
└── postcss.config.js                 # PostCSS configuration (Tailwind)
```

## Key Files & Components

### Configuration Files
- **`wrangler.jsonc`**: Cloudflare Workers config
  - Worker name: `agentic-cookbook`
  - Custom domains: `agentic-cookbook.com`, `www.agentic-cookbook.com`
  - SPA routing with single-page-application not-found handling
  - Node.js compatibility enabled
  - Observability enabled
  - Build command: `npm run build`

- **`vite.config.ts`**: Build configuration
  - Custom cookbook plugin that loads markdown from `/cookbook` directory
  - Additional directory support (e.g., `/decisions`)
  - Dual HTML entry points: `index.html` (main app), `bookcover.html` (landing)
  - Cloudflare integration via `@cloudflare/vite-plugin`

- **`tsconfig.json`**: 
  - Target: ES2022
  - Strict mode enabled
  - JSX: react-jsx
  - Module resolution: bundler
  - No unused locals/parameters warnings enabled

- **`playwright.config.ts`**:
  - Base URL: `http://localhost:5173` (dev server)
  - Color scheme: dark
  - Visual regression: max 1% pixel difference, 20% threshold
  - Dev server reuse enabled

### Core React Components

**Layout:**
- `Header.tsx`: Sticky navigation bar with logo, tabs, search button (Cmd+K), GitHub link, theme toggle
- `Sidebar.tsx`: Desktop (sticky) and mobile (overlay) navigation with collapsible sections
- `Breadcrumbs.tsx`: Hierarchical navigation display
- `TableOfContents.tsx`: Right-side sticky TOC for long doc pages (desktop only)

**Pages:**
- `HomePage.tsx`: Overview page with featured sections
- `SectionIndex.tsx`: Grid-based index pages (Principles, Guidelines, Ingredients, Recipes, etc.)
- `DocPage.tsx`: Individual markdown document renderer with metadata, prose styling, raw toggle

**Content Rendering:**
- `SearchDialog.tsx`: Full-text search interface using Fuse.js
- `PlatformFilter.tsx`: Filter components by target platform
- `StatusBadge.tsx`: Visual status indicators

**Contexts:**
- `ContentContext.tsx`: Provides cookbook data tree to all components
- `ThemeContext.tsx`: Dark/light mode with localStorage persistence

### Build Pipeline

**Custom Vite Plugin** (`vite-plugin-cookbook.ts`):
1. Recursively scans cookbook directories for `.md` files (excluding `_template.md`)
2. Parses YAML frontmatter using `gray-matter`
3. Converts Markdown to HTML via unified pipeline:
   - `remark-parse`: Parse markdown
   - `remark-gfm`: GitHub flavored markdown
   - `remark-rehype`: Convert to HTML AST
   - `rehype-slug`: Auto ID generation for headings
   - `rehype-autolink-headings`: Linkify headings
   - `rehype-cross-references`: Custom cross-reference processing
   - `rehype-stringify`: Convert AST to HTML string
4. Extracts h2/h3 headings for table of contents
5. Derives section/subsection from slug
6. Generates virtual module (`virtual:cookbook-data`) injected at build time
7. Supports additional directories (e.g., decisions) with section mapping

## Claude Configuration

### CLAUDE.md
- References the Agentic Cookbook as the project's knowledge base
- Cookbook path: `../agentic-cookbook/` (sibling directory)
- Rule: `cookbook.md` (~10 lines, guardrails only)
- Pipeline: `/cookbook-start` to begin, `/cookbook-next` to advance
- Available skills: /configure-cookbook, /install-cookbook, /cookbook-start, /cookbook-next, /lint-project-with-cookbook, /plan-cookbook-recipe, /contribute-to-cookbook

### .claude/rules/
1. **cookbook.md** (358 bytes):
   - 6 core principles for development
   - No Phase 2 skipping, no test skipping
   - Don't optimize without evidence
   - Investigate unfamiliar content before overwriting

2. **site-design.md** (12.6 KB):
   - Comprehensive design system specification
   - Defines 4 page types: Overview, Section Index, Doc Page, Static Page
   - Sidebar patterns: plain links vs. toggleable sections
   - Header and search dialog specifications
   - Complete theme token system (dark/light modes)
   - Specific Tailwind classes for every component
   - Prose styling overrides via Typography plugin
   - Screenshot verification requirement before/after changes

## Planning & Research Documents

### Cookbook Content Structure

The `/cookbook` directory contains structured AI-friendly documentation:

**Introduction** (~10 files)
- Getting started, conventions, glossary

**Principles** (~20 files)
- Engineering principles: Simplicity, YAGNI, Fail Fast, Dependency Injection, Immutability, Composition, Separation of Concerns, Design for Deletion, Explicit over Implicit, Small Reversible Decisions, Tight Feedback Loops, Manage Complexity, Least Astonishment, Idempotency, Native Controls, Open Source Preference, Make It Work/Right/Fast, Optimize for Change

**Guidelines** (~105 files)
- Organized by topic: Testing, Security, UI, Accessibility, Internationalization, Concurrency, Logging, Feature Management, Code Quality

**Ingredients** (~23 files)
- Atomic component specs: behavioral requirements, appearance, states, accessibility, configuration, test vectors, platform notes

**Recipes** (~24 files)
- Feature compositions: integration requirements, layout, shared state, test vectors

**Compliance** (10+ categories)
- 81+ curated checks: Security, User Safety, Performance, Best Practices, Access Patterns, Accessibility, Privacy & Data, Platform Compliance, Reliability, Internationalization

**Workflows** (6 files)
- Branching, planning, implementation, verification, review

**Reference**
- External best-practices links, schemas, examples

**Appendix**
- Research materials and evaluations

### Research Materials
Located in `/cookbook/appendix/research/` — design research and evaluations.

## Git History & Current State

### Branch & Status
- **Current Branch:** `main`
- **Ahead of Remote:** Yes, by 1 commit
- **Untracked Files:** `cookbook/.superpowers/` (build artifact)
- **Uncommitted Changes:** None (clean working tree)

### Recent Git Activity (Last 30 commits)

```
6da7c65 (HEAD) chore: gitignore PNG screenshots in project root
49002c9 Add cookbook project config and meta files
5b6b454 Update web app for cookbook restructuring
5c7bf0c Restructure cookbook: migrate recipes to ingredients, add formatting specs
d4cf696 Sync cookbook content: update guidelines, principles, and introduction
62c0e6c chore: standardize worktree directory to .claude/worktrees/
e189b33 Add Open Graph and Twitter meta tags with branded OG image
6f0455d Add Agentic Cookbook Family box with links to Dev Team and Agent Registry
7b69c2c Style hero blurb closer in italic serif for emphasis
848aee1 Style nav titles in gold accent, rename to The Agentic Cookbook, add selection bar
55c4d4d Fix broken fonts by switching from stale woff2 URLs to Google Fonts link tags
d97988e Add build command to wrangler config so CI deploys build automatically
...and 18 more commits
```

### Recent Changes (Last 5 commits)
- **2026-04-06 18:41:13 -0700:** gitignore PNG screenshots in project root
- **2026-04-06 17:33:46 -0700:** Add cookbook project config and meta files
- **2026-04-06 17:33:39 -0700:** Update web app for cookbook restructuring
- **2026-04-06 17:33:28 -0700:** Restructure cookbook: migrate recipes to ingredients, add formatting specs
- **2026-04-06 17:33:18 -0700:** Sync cookbook content: update guidelines, principles, and introduction

### Repository Metadata
- **Remote:** `git@github.com:agentic-cookbook/cookbook-web.git`
- **Fetch URL:** `git@github.com:agentic-cookbook/cookbook-web.git`
- **Push URL:** `git@github.com:agentic-cookbook/cookbook-web.git`

## Build & Test Commands

### Available npm Scripts
```bash
npm run dev                    # Start Vite dev server (port 5173)
npm run build                  # Compile TypeScript + build with Vite
npm run preview                # Build + run with wrangler dev (local preview)
npm run deploy                 # Build + deploy to Cloudflare Workers
npm run test:visual            # Run Playwright visual regression tests
npm run test:visual:update     # Update Playwright snapshot baselines
```

### Typical Development Workflow
```bash
npm run dev              # Start dev server
# In another terminal:
npm run test:visual      # Run visual tests
npm run test:visual:update  # Update baselines after intentional changes
```

### Deployment
```bash
npm run deploy           # Builds and deploys to agentic-cookbook.com
```

### Testing Strategy
- Visual regression tests via Playwright
- Screenshot baselines in `/tests/visual.spec.ts-snapshots/`
- Design rule enforcement (screenshot before/after)
- Max 1% pixel difference tolerance
- Dark theme by default for testing

## Notes

### Special Features

1. **Dual Entry Points**
   - `index.html` → React app at `/` with full routing
   - `bookcover.html` → Animated book cover landing page (particles, gradient background)

2. **Build-Time Content Processing**
   - Cookbook markdown is loaded and processed at build time via custom Vite plugin
   - No server-side rendering or runtime markdown parsing
   - Content is injected as JavaScript object in virtual module
   - Enables instant page loads and client-side navigation

3. **Search Integration**
   - Full-text search across all cookbook content
   - Powered by Fuse.js (fuzzy search)
   - Searchable fields: title, section, description, content
   - Triggered via Cmd+K or header search button

4. **Design System**
   - 12.6 KB site-design.md rule with exact Tailwind specifications
   - Theme tokens for dark/light modes (gold accent #c4a35a)
   - Custom fonts: Instrument Serif (display), DM Mono (monospace), Manrope (sans)
   - Responsive design: mobile (overlay sidebar), tablet, desktop (sticky sidebar)
   - Screenshot verification workflow to prevent design drift

5. **Related Projects**
   - **dev-team**: Multi-agent development orchestration plugin
   - **cookbook**: Main cookbook repository (content source)
   - **tools-site**: Nested Cloudflare Workers project (separate deployment)

6. **Accessibility & Polish**
   - Breadcrumb navigation with proper ARIA labels
   - Semantic HTML throughout
   - Tailwind Typography for prose styling
   - Dark mode respects system preferences with localStorage override
   - Sticky header with smooth scrolling behavior
   - TOC auto-generates with anchor links

7. **MCP Integration**
   - `.mcp.json` configures Playwright MCP with vision capabilities
   - Enables AI-assisted visual testing and screenshot comparison

### Deployment Platform
- **Host:** Cloudflare Workers (serverless edge computing)
- **Domains:** agentic-cookbook.com, www.agentic-cookbook.com
- **Observability:** Enabled via Wrangler
- **SPA Routing:** Fallback to index.html for all unknown routes

### Code Statistics
- **TypeScript/React:** ~2,647 lines of source code
- **Cookbook Content:** 172+ markdown files across 8+ categories
- **Package Size:** 198 npm dependencies
- **Build Output:** Production bundle in `/dist`

### Known Untracked Files
- `cookbook/.superpowers/` — superpowers framework data (build artifact, should be in .gitignore or generated)

### Design Philosophy
The site strictly adheres to a documented design system with 4 page types, mandatory screenshot verification, and exact Tailwind specifications for every component. Design drift is prevented through visual regression testing and the site-design.md rule.

