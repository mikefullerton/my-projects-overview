# Cookbook Web - Project Overview

## Project Summary

A Cloudflare Workers web application that serves as the public-facing browsable interface for the Agentic Cookbook -- a structured collection of principles, guidelines, ingredients, recipes, and workflows for AI-assisted multi-platform development. Built with React 19, TypeScript, and Tailwind CSS 4, deployed to `agentic-cookbook.com`.

## Type & Tech Stack

**Project Type:** Web Application / Public Documentation Site

**Core Technologies:**
- **Runtime:** Cloudflare Workers (serverless edge computing)
- **Frontend:** React 19, TypeScript 5.7
- **Styling:** Tailwind CSS 4, PostCSS 8, @tailwindcss/typography
- **Routing:** React Router 7
- **Build Tools:** Vite 6, Wrangler 4.78
- **Markdown Processing:** Remark + Rehype unified ecosystem (remark-parse, remark-gfm, rehype-slug, rehype-autolink-headings, rehype-stringify)
- **Syntax Highlighting:** Shiki 1.0
- **Search:** Fuse.js 7.0 (fuzzy full-text search)
- **Testing:** Playwright 1.58 (visual regression tests)
- **Animations:** tw-animate-css

**Key Dependencies:**
- `react@^19.0.0`, `react-dom@^19.0.0`, `react-router@^7.0.0`
- `@cloudflare/vite-plugin@^1.30.2`
- `unified@^11.0.0`, `gray-matter@^4.0.3`
- `shiki@^1.0.0` for code syntax highlighting

## GitHub URL

https://github.com/agentic-cookbook/agenticcookbookweb

## Directory Structure

```
agenticcookbookweb/
├── .claude/
│   └── rules/
│       ├── cookbook.md                # 6 core development principles
│       └── site-design.md            # Comprehensive design system spec (12KB)
├── .cookbook/                         # Cookbook configuration
├── .mcp.json                         # MCP config (Playwright with vision)
├── .playwright-mcp/                  # Playwright MCP integration
├── .wrangler/                        # Wrangler build artifacts
├── cookbook/                          # Agentic Cookbook content (synced from ../cookbook/)
│   ├── principles/                   # 18 engineering principles
│   ├── guidelines/                   # 88+ guidelines
│   ├── ingredients/                  # 18 atomic component specs
│   ├── recipes/                      # 11 feature compositions
│   ├── compliance/                   # Verification checklists
│   ├── workflows/                    # 6 workflow specs
│   ├── introduction/                 # Getting started materials
│   ├── reference/                    # Schemas, examples
│   ├── appendix/                     # Research materials
│   └── index.md                      # Table of contents
├── dist/                             # Production build output
├── src/
│   ├── App.tsx                       # Root component with routing
│   ├── main.tsx                      # React entry point
│   ├── index.css                     # Global styles + theme tokens
│   ├── components/
│   │   ├── content/                  # DocPage, SearchDialog, PlatformFilter, StatusBadge
│   │   ├── layout/                   # Header, Sidebar, Breadcrumbs, TableOfContents
│   │   └── sections/                 # HomePage, SectionIndex, DocPage, GettingStartedPage, ProjectsPage, ToolingPage
│   ├── contexts/
│   │   ├── ContentContext.tsx        # Loads cookbook data from virtual module
│   │   └── ThemeContext.tsx          # Dark/light theme management
│   ├── lib/                          # Utilities (domain-utils, manifest, navigation, search)
│   ├── plugins/
│   │   ├── vite-plugin-cookbook.ts   # Custom Vite plugin: scans markdown, parses frontmatter, converts to HTML
│   │   └── rehype-cross-references.ts
│   └── types/                        # TypeScript types + virtual module declarations
├── tests/
│   ├── visual.spec.ts                # Playwright visual regression tests
│   └── visual.spec.ts-snapshots/     # Screenshot baselines
├── tools-site/                       # Nested Cloudflare Workers project
│   ├── src/                          # API + worker source
│   ├── migrations/                   # D1 database migrations
│   ├── scripts/                      # Utility scripts
│   └── wrangler.jsonc
├── public/                           # Static assets
├── bookcover.html                    # Animated book cover landing page
├── index.html                        # Main HTML entry point
├── package.json                      # Dependencies and scripts
├── vite.config.ts                    # Vite build config
├── wrangler.jsonc                    # Cloudflare Workers config
├── tsconfig.json                     # TypeScript configuration
├── playwright.config.ts              # Playwright test config
└── postcss.config.js                 # PostCSS (Tailwind)
```

## Key Files & Components

### Build Pipeline (Custom Vite Plugin)
`src/plugins/vite-plugin-cookbook.ts`:
1. Recursively scans `cookbook/` for `.md` files (excluding `_template.md`)
2. Parses YAML frontmatter via `gray-matter`
3. Converts Markdown to HTML via unified pipeline (remark-parse, remark-gfm, remark-rehype, rehype-slug, rehype-autolink-headings, rehype-cross-references, rehype-stringify)
4. Extracts h2/h3 headings for table of contents
5. Generates virtual module (`virtual:cookbook-data`) injected at build time

### React Components
**Layout:** Header (sticky nav, tabs, Cmd+K search, GitHub link, theme toggle), Sidebar (desktop sticky + mobile overlay with collapsible sections), Breadcrumbs, TableOfContents (right-side sticky)

**Pages (4 types):**
1. **Overview (HomePage):** Landing page with narrative intro and section card grid
2. **Section Index:** Grid of artifact cards with subsection headings
3. **Doc Page:** Individual markdown document with metadata, prose, raw toggle, TOC sidebar
4. **Static Page:** Free-form prose (Getting Started)

**Content:** SearchDialog (Fuse.js), PlatformFilter, StatusBadge
**Contexts:** ContentContext (cookbook data tree), ThemeContext (dark/light with localStorage)

### Design System (site-design.md)
12.6 KB specification defining exact Tailwind classes for every component, theme tokens for dark/light modes (gold accent #c4a35a), custom fonts (Instrument Serif, DM Mono, Manrope), responsive breakpoints, prose overrides, and screenshot verification workflow.

### tools-site/ (Nested Project)
Separate Cloudflare Workers project with its own `wrangler.jsonc`, D1 database migrations, API source, and build config.

## Claude Configuration

### CLAUDE.md
References agentic-cookbook as the project's knowledge base. Cookbook path: `../agentic-cookbook/`. Available skills: /configure-cookbook, /install-cookbook, /cookbook-start, /cookbook-next, /lint-project-with-cookbook, /plan-cookbook-recipe, /contribute-to-cookbook.

### Rules (2)
1. **cookbook.md**: 6 core principles -- confirm correct project, investigate before overwriting, fix only what was asked, don't skip Phase 2, don't skip tests, don't optimize without evidence.
2. **site-design.md**: Comprehensive design system -- 4 page types, sidebar patterns, header/search specs, theme tokens (dark/light), exact Tailwind classes, prose overrides, screenshot verification requirement.

### MCP Integration
`.mcp.json` configures Playwright MCP with vision capabilities for AI-assisted visual testing.

No settings.json, no skills, no `.claude/CLAUDE.md`.

## Planning & Research Documents

Cookbook content in `/cookbook/appendix/research/` -- design research and evaluations.

No dedicated planning directory for the web app itself. Design decisions are encoded in the site-design.md rule.

## Git History & Current State

**Branch:** `main`
**Working Tree:** Clean (1 untracked file: `cookbook/.superpowers/`)

**Recent Commits:**
```
6da7c65 (2026-04-06) chore: gitignore PNG screenshots in project root
49002c9 (2026-04-06) Add cookbook project config and meta files
5b6b454 (2026-04-06) Update web app for cookbook restructuring
5c7bf0c (2026-04-06) Restructure cookbook: migrate recipes to ingredients, add formatting specs
d4cf696 (2026-04-06) Sync cookbook content: update guidelines, principles, and introduction
```

**Key Recent Changes:**
- Cookbook content restructuring synced (recipes to ingredients migration)
- Open Graph and Twitter meta tags added
- Agentic Cookbook Family box with sibling project links
- Font fixes (Google Fonts), gold accent styling
- Build command added to wrangler config for CI deploys

## Build & Test Commands

```bash
npm run dev                    # Start Vite dev server (port 5173)
npm run build                  # Compile TypeScript + build with Vite
npm run preview                # Build + run with wrangler dev (local preview)
npm run deploy                 # Build + deploy to Cloudflare Workers
npm run test:visual            # Run Playwright visual regression tests
npm run test:visual:update     # Update Playwright snapshot baselines
```

## Notes

1. **Dual Entry Points:** `index.html` (React app with full routing) and `bookcover.html` (animated book cover landing page with particles).

2. **Build-Time Content Processing:** Cookbook markdown is loaded and processed at build time via custom Vite plugin. No server-side rendering or runtime markdown parsing. Content injected as JavaScript object via virtual module.

3. **Deployment:** Cloudflare Workers at `agentic-cookbook.com` and `www.agentic-cookbook.com`. SPA routing fallback. Observability enabled. Node.js compatibility flags.

4. **Content Sync:** Cookbook content in `/cookbook` is synced from the main cookbook repo via the `/update-website` skill. Not a git submodule -- files are copied.

5. **Visual Testing:** Playwright with max 1% pixel difference tolerance. Dark theme by default. Screenshot verification required before/after design changes per site-design.md rule.

6. **Sibling Projects:** cookbook (content source), dev-team (multi-agent plugin), tools-site (nested Cloudflare Workers project for API/tools).
