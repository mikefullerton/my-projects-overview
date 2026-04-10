# My Projects Overview

A comprehensive reference for all active projects in `~/projects/`. Each project has a detailed `overview.md` with directory structure, tech stack, git history, Claude configuration, planning docs, and build commands.

*Generated: 2026-04-10*

---

## macOS Native Apps

| Project | Summary | Tech |
|---------|---------|------|
| [Hairball](projects/Hairball/overview.md) | Menu bar app for window-level task context management across parallel development workstreams | Swift, SwiftUI, AppKit, Accessibility API |
| [Whippet](projects/Whippet/overview.md) | Menu bar utility monitoring all active Claude Code sessions in real-time | Swift, AppKit, SwiftUI, SQLite, FSEvents |
| [Catnip Terminal](projects/catnip-terminal/overview.md) | Native terminal emulator with AI-powered session summarization | Swift, SwiftUI, AppKit, SwiftTerm |
| [Scratching Post](projects/scratching-post/overview.md) | Document-based multi-window IDE with terminal, notes, file browser, AI summarization | Swift, SwiftUI, AppKit, SQLite, SwiftTerm |
| [Search Helper](projects/search-helper/overview.md) | Search management app with global hotkeys and Finder Sync extension | Swift, XcodeGen, GRDB SQLite |
| [Agentic Daemon](projects/agentic-daemon/overview.md) | User-space daemon watching a jobs directory for Swift scripts and running them on schedule | Swift 6, strict concurrency, launchd |

## Cross-Platform Apps

| Project | Summary | Tech |
|---------|---------|------|
| [Temporal](projects/temporal/overview.md) | Cross-platform calendar/time management with community forum, gamification, IoT integration | Kotlin Multiplatform, SwiftUI, Jetpack Compose, Ktor, PostgreSQL |
| [Temporal Platform](projects/temporal-platform/overview.md) | Spec-driven application platform — shares behavioral specs (not code) across platforms | Markdown specs, Swift, Kotlin, TypeScript conformance tests |
| [QualityTime](projects/QualityTime/overview.md) | Cross-platform app targeting Apple, Android, Windows, and Web with full Claude CI pipeline | Kotlin Multiplatform, SwiftUI, Compose, React, Ktor, PostgreSQL |

## Agentic Cookbook Ecosystem

| Project | Summary | Tech |
|---------|---------|------|
| [Cookbook](projects/cookbook/overview.md) | Knowledge base of principles, guidelines, ingredients, recipes for AI-assisted development | Markdown, YAML, Vitest |
| [Cookbook Web](projects/cookbook-web/overview.md) | Public website for the Agentic Cookbook at agentic-cookbook.com | React 19, TypeScript, Tailwind 4, Vite, Cloudflare Workers |
| [Cookbook Backend](projects/cookbook-backend/overview.md) | npm workspaces monorepo: Hono/Drizzle/Postgres backend, auth service, admin/dashboard sites | Node, TypeScript, Hono, Drizzle, PostgreSQL, Cloudflare Workers, Railway |
| [Dev Team](projects/dev-team/overview.md) | Multi-agent product discovery plugin for Claude Code with specialists and team pipelines | Python, YAML, pytest |
| [Dev Tools](projects/dev-tools/overview.md) | Distributable Claude Code skills for scaffolding, deployment, and repo maintenance | Python 3.11+, TypeScript, Vitest |
| [Devtools Web Server](projects/devtools-web-server/overview.md) | Always-on local Caddy server with site lifecycle API and live dashboard | Caddy, Python, React, TypeScript |
| [Agentic Cookbook Tools](projects/agentic-cookbook-tools/overview.md) | User-facing Claude Code skills and guidance rules for cookbook integration | Markdown, YAML |
| [Agenticdeveloperhub](projects/agenticdeveloperhub/overview.md) | Full-stack multi-site web app hub with admin, dashboard, and API docs | React 19, TypeScript, Hono, PostgreSQL, Cloudflare Workers, Railway |
| [Agentic Auth Service](projects/agentic-auth-service/overview.md) | Shared RS256 JWT authentication microservice for the agentic ecosystem | Node.js, Hono, TypeScript, PostgreSQL, Drizzle, Railway |
| [Agentic Kitchen](projects/agentic-kitchen/overview.md) | Empty placeholder repository (freshly initialized) | — |
| [MyAgenticProjects](projects/myagenticprojects/overview.md) | Full-stack SaaS platform with auth, feature flags, messaging, feedback | React 19, Hono, PostgreSQL, Cloudflare Workers, Railway |
| [MyAgenticWorkspace](projects/myagenticworkspace/overview.md) | Empty placeholder repository (freshly initialized) | — |
| [Official Agent Registry](projects/official-agent-registry/overview.md) | "DNS for AI agents" — identity platform for registering and discovering AI agents | TypeScript, React, Hono, PostgreSQL, Cloudflare Workers |
| [Roadmaps](projects/roadmaps/overview.md) | Feature planning and implementation system for Claude Code with live dashboards | Python, Flask, SQLite, pytest |
| [Persona Creator](projects/persona-creator/overview.md) | Python library + Claude Code skill generating AI personas with visual character generation | Python 3.12+, Pydantic, Click, httpx |
| [Shared Website Components](projects/shared-website-components/overview.md) | React 19 component library (Agentic theme system + chat widget) consumed via git submodule | React 19, TypeScript, Vite, Vitest |
| [Site Demos](projects/site-demos/overview.md) | Static HTML/CSS/JS scratchpad with PersonaChat widget themes browser | Vanilla HTML, CSS, JS |
| [Learn True Facts](projects/learntruefacts/overview.md) | AI improv comedian chat app — planning complete, pre-implementation | React 19, Hono, PostgreSQL, Cloudflare Workers, multi-LLM |
| [My Agentic Interviews](projects/my-agentic-interviews/overview.md) | Interview repository + knowledge management system with YAML-frontmatter markdown | Markdown, YAML |

## Web Applications & SaaS

| Project | Summary | Tech |
|---------|---------|------|
| [mikefullerton.com](projects/mikefullerton.com/overview.md) | Personal portfolio/resume website — recently migrated to React | React 19, Vite, TypeScript, Cloudflare Workers |
| [Scratchyfish.com](projects/scratchyfish.com/overview.md) | Static website for Scratchy Fish progressive jazz rock band | Jekyll, HTML, CSS |
| [mikeisdrumming](projects/mikeisdrumming/overview.md) | GitHub Pages landing page for music/drumming brand with music API research | Vanilla HTML, CSS |

## Claude Code Extensions & Tools

| Project | Summary | Tech |
|---------|---------|------|
| [Cat Herding](projects/cat-herding/overview.md) | Personal Claude Code workflow extensions — yolo, custom-status-line, linting skills | Python, YAML |
| [Social Media Bot](projects/social-media-bot/overview.md) | AI content pipeline of 12 sequential bots drafting posts for X/LinkedIn/Bluesky/Substack | Python, claude-agent-sdk, click, SQLite |

## Fun & Creative

| Project | Summary | Tech |
|---------|---------|------|
| [Catnip](projects/catnip/overview.md) | Web dashboard for monitoring autonomous Claude Code agents in real-time | TypeScript, React 19, Hono, PostgreSQL, WebSocket, Railway |
| [Name-Craft](projects/name-craft/overview.md) | Children's book character name generator using Claude AI with sound symbolism | Python, Flask, Anthropic API, SQLite |
| [Market Research](projects/market-research/overview.md) | AI market analysis CLI — 5 specialized agents per project, synthesized ranking | Python 3.9+, Anthropic SDK, Tavily, Pydantic |

## Infrastructure & Meta

| Project | Summary | Tech |
|---------|---------|------|
| [MySetup](projects/mysetup/overview.md) | Development environment automation for macOS and Windows (WSL) | Bash, Python, Homebrew |
| [My Projects](projects/my-projects/overview.md) | Project management dashboard tracking ~35 git repos | React 19, Vite, Node.js, Python scanners |

---

## Quick Reference

### By Organization

**mikefullerton** (personal GitHub): Hairball, Whippet, Catnip Terminal, Scratching Post, Search Helper, Catnip, mikefullerton.com, Scratchyfish.com, mikeisdrumming, Cat Herding, Social Media Bot, Name-Craft, Market Research, My Projects, MySetup, My Agentic Interviews

**agentic-cookbook** (org): Cookbook, Cookbook Web, Cookbook Backend, Dev Team, Dev Tools, Devtools Web Server, Agentic Cookbook Tools, Agenticdeveloperhub, Agentic Auth Service, Agentic Daemon, Agentic Kitchen, MyAgenticProjects, MyAgenticWorkspace, Official Agent Registry, Roadmaps, Persona Creator, Shared Website Components, Site Demos, Learn True Facts

**temporal-company** (org): Temporal, Temporal Platform

**QualityTimeStudios** (org): QualityTime

### By Status

**Active development**: Hairball, Whippet, Catnip Terminal, Scratching Post, Catnip, Cookbook, Cookbook Web, Cookbook Backend, Dev Team, Dev Tools, Devtools Web Server, Agenticdeveloperhub, Agentic Auth Service, Agentic Daemon, Official Agent Registry, Roadmaps, Persona Creator, Shared Website Components, Temporal, QualityTime, Social Media Bot, Market Research, My Projects, MySetup, Cat Herding, mikefullerton.com

**Stable**: Agentic Cookbook Tools, Scratchyfish.com

**Planning / pre-implementation**: Learn True Facts, Name-Craft, Temporal Platform, mikeisdrumming, Site Demos, My Agentic Interviews

**Empty / placeholder**: Agentic Kitchen, MyAgenticWorkspace
