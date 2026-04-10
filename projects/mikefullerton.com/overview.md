# mikefullerton.com

## Project Summary

mikefullerton.com is a personal portfolio and resume website showcasing professional software engineering background and creative pursuits. Built as a static site deployed via GitHub Pages with a custom domain. Features a mobile-responsive grid-based layout with dark theme, comprehensive SEO optimization (Open Graph, Twitter Cards, JSON-LD Person schema), and automated GitHub Actions deployment. Recently migrated to React + Vite with shared website component library as a submodule to support reusable persona-driven chat components across projects.

## Type & Tech Stack

**Type:** Personal Portfolio Website (Static Site with React Frontend)

**Tech Stack:**
- **Frontend:** React 19, Vite 6.0, TypeScript 5.7, Playwright (testing)
- **Styling:** CSS (custom styles with CSS variables), Tailwind CSS (via shared components)
- **Deployment:** GitHub Pages (via GitHub Actions)
- **Infrastructure:** Cloudflare Workers (wrangler deploy)
- **Shared Components:** Custom submodule (shared-website-components) for reusable React components
- **Build:** TypeScript compilation + Vite bundling
- **Browser Support:** Modern browsers (HTML5, CSS3)

## GitHub URL

https://github.com/mikefullerton/mikefullerton.com

## Directory Structure

```
mikefullerton.com/
├── site/                                # Main website (React + Vite)
│   ├── src/
│   │   └── ...                         # React components, pages
│   ├── public/                         # Static assets
│   ├── dist/                           # Build output
│   ├── .wrangler/                      # Wrangler (Cloudflare) config
│   ├── index.html
│   ├── vite.config.js
│   ├── tsconfig.json
│   ├── package.json
│   └── wrangler.toml                   # Cloudflare Workers config
├── shared-website-components/          # Shared React components (submodule)
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat.tsx               # Persona-driven chat component
│   │   │   ├── PersonaChat.tsx
│   │   │   └── ...
│   │   ├── types/
│   │   └── ...
│   ├── chat/                          # Chat-specific components
│   ├── examples/
│   ├── docs/
│   ├── package.json
│   └── .claude/
├── .claude/                           # Claude Code configuration
│   ├── settings.local.json
│   └── worktrees/                     # Git worktree management
├── .superpowers/                      # Superpowers session logs
│   └── brainstorm/
├── docs/
│   ├── project/description.md
│   ├── research/activity-feed-architecture.md
│   └── superpowers/
│       ├── plans/2026-04-06-react-migration.md
│       └── specs/2026-04-06-react-migration-design.md
├── .gitignore
├── .gitmodules                        # Git submodule configuration
└── .git/
```

## Key Files & Components

- **site/package.json** - Frontend React + Vite configuration with TypeScript, Playwright
- **site/vite.config.js** - Vite build configuration
- **site/tsconfig.json** - TypeScript configuration
- **site/wrangler.toml** - Cloudflare Workers deployment configuration
- **site/index.html** - Entry HTML with React root
- **site/src/** - React components and application logic
- **site/public/** - Static assets (images, fonts, etc.)
- **shared-website-components/** - Git submodule with reusable React components:
  - **Chat.tsx / PersonaChat.tsx** - Persona-driven chat UI components (inline mode support)
  - **theme tokens** - Shared styling and dark mode support
  - **examples/** - Example implementations
- **docs/project/description.md** - Project purpose, key features, tech stack, deployment, status (completed/stable)
- **docs/research/activity-feed-architecture.md** - Research on activity feed architecture patterns
- **docs/superpowers/plans/2026-04-06-react-migration.md** - Plan for React migration
- **docs/superpowers/specs/2026-04-06-react-migration-design.md** - Design specification for React migration

## Claude Configuration

Stored in **.claude/settings.local.json** - Local Claude Code settings for development.

Worktree management in **.claude/worktrees/** for isolated feature development.

## Planning & Research Documents

- **docs/project/description.md** - Complete project description with purpose, key features, tech stack, status
- **docs/research/activity-feed-architecture.md** - Research on activity feed architecture patterns for potential features
- **docs/superpowers/plans/2026-04-06-react-migration.md** - Implementation plan for React migration
- **docs/superpowers/specs/2026-04-06-react-migration-design.md** - Technical specification for React migration design

## Git History & Current State

- **Remote:** git@github.com:mikefullerton/mikefullerton.com.git
- **Current Branch:** main
- **Status:** Clean working tree (no uncommitted changes)
- **Recent Activity:**
  - Latest: chore: update shared-website-components submodule (b4ff294)
  - chore: update shared-website-components submodule (d996a21)
  - refactor: replace site chat code with shared React components (2d3ba70)
  - feat: add inline mode to Chat component (5e3c072)
  - fix: remove dark class hack, update submodule (682f026)
  - fix: add dark class to html element for shared theme tokens (019a70a)
  - feat: integrate shared-website-components submodule (9b2a3cd)
  - Recent commits focus on shared component integration and theme/styling fixes
  - Mobile website worktree work completed and merged

## Build & Test Commands

```bash
# Development
npm run dev                  # Start Vite dev server (site workspace)
npm run build               # TypeScript compilation + Vite build
npm run preview             # Preview production build locally
npm run typecheck           # Run TypeScript type checking

# Deployment
npm run deploy              # Build and deploy to Cloudflare Workers
npm run deploy:preview      # Build and deploy to Cloudflare preview environment

# Testing (if configured)
# Playwright setup for E2E testing
```

## Notes

- **Status:** Recently completed / stable, with ongoing React migration and shared component integration
- **Architecture:** Single-page application (SPA) using React 19 and Vite for fast builds; shared component library (submodule) for reusable UI components across projects
- **Deployment:** GitHub Pages for static hosting; Cloudflare Workers for serverless functions if needed via wrangler
- **Key Recent Work:** Migration from vanilla HTML/CSS to React + Vite; integration of shared persona-driven chat component library; dark mode and theme improvements
- **SEO:** Open Graph tags, Twitter Cards, JSON-LD Person schema for search engine optimization
- **Styling:** CSS variables for theming, custom dark theme, mobile-responsive design
- **Shared Components:** Reusable React components in submodule (Chat, PersonaChat) for consistent UI across projects (mikefullerton.com, other persona-driven apps)
- **Build Optimization:** TypeScript compilation via tsc + Vite bundling for fast, optimized production builds
- **Related Projects:** My Projects (project tracking dashboard), Hairball (macOS menu bar app using shared patterns)
