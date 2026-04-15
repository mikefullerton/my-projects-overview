# My Projects Overview

A comprehensive reference for all projects in `~/projects/`. Each project has a detailed `overview.md` with directory structure, tech stack, git history, Claude configuration, planning docs, and build commands.

Projects are organized on disk by lifecycle: `~/projects/active/` (in active development), `~/projects/paused/` (on hold), `~/projects/experimental/` (exploration / early R&D).

*Generated: 2026-04-15*

---

## macOS Native Apps

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [Whippet](projects/Whippet/overview.md) | Menu bar utility monitoring all active Claude Code sessions in real-time | Swift, AppKit, SwiftUI, SQLite, FSEvents | active |
| [Agentic Daemon](projects/agentic-daemon/overview.md) | User-space daemon watching a jobs directory for Swift scripts and running them on schedule | Swift 6, strict concurrency, launchd | active |
| [Stenographer](projects/stenographer/overview.md) | Headless macOS daemon capturing Claude Code session events into SQLite with HTTP/XPC APIs | Swift 6, Network.framework, SQLite, XPC, LaunchAgent | active |
| [Hairball](projects/Hairball/overview.md) | Menu bar app for window-level task context management across parallel development workstreams | Swift, SwiftUI, AppKit, Accessibility API | experimental |
| [Catnip Terminal](projects/catnip-terminal/overview.md) | Native terminal emulator with AI-powered session summarization | Swift, SwiftUI, AppKit, SwiftTerm | experimental |
| [Scratching Post](projects/scratching-post/overview.md) | Document-based multi-window IDE with terminal, notes, file browser, AI summarization | Swift, SwiftUI, AppKit, SQLite, SwiftTerm | experimental |
| [Search Helper](projects/search-helper/overview.md) | Search management app with global hotkeys and Finder Sync extension | Swift, XcodeGen, GRDB SQLite | paused |

## Cross-Platform Apps & Toolkits

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [Temporal](projects/temporal/overview.md) | Cross-platform calendar/time management with community forum, gamification, IoT integration | Kotlin Multiplatform, SwiftUI, Jetpack Compose, Ktor, PostgreSQL | active |
| [Agentic Toolkit](projects/agentic-toolkit/overview.md) | Cross-platform toolkit library for agentic development — Apple (Swift 6), Android, Windows | Swift 6, XcodeGen, AppKit/UIKit; Android/Windows TBD | active |
| [Agentic Plugins](projects/agentic-plugins/overview.md) | Framework for building and distributing LLM provider plugins across agentic tools | Swift, AppKit, SPM, plugin SDK | active |
| [Temporal Platform](projects/temporal-platform/overview.md) | Spec-driven application platform — shares behavioral specs (not code) across platforms | Markdown specs, Swift, Kotlin, TypeScript conformance tests | experimental |
| [QualityTime](projects/QualityTime/overview.md) | Cross-platform app targeting Apple, Android, Windows, and Web with full Claude CI pipeline | Kotlin Multiplatform, SwiftUI, Compose, React, Ktor, PostgreSQL | paused |

## Agentic Cookbook Ecosystem

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [Cookbook](projects/cookbook/overview.md) | Knowledge base of principles, guidelines, ingredients, recipes for AI-assisted development | Markdown, YAML, Vitest | active |
| [Cookbook Web](projects/cookbook-web/overview.md) | Public website for the Agentic Cookbook at agentic-cookbook.com | React 19, TypeScript, Tailwind 4, Vite, Cloudflare Workers | active |
| [Cookbook Backend](projects/cookbook-backend/overview.md) | npm workspaces monorepo: Hono/Drizzle/Postgres backend, auth service, admin/dashboard sites | Node, TypeScript, Hono, Drizzle, PostgreSQL, Cloudflare Workers, Railway | active |
| [Dev Tools](projects/dev-tools/overview.md) | Distributable Claude Code skills for scaffolding, deployment, and repo maintenance | Python 3.11+, TypeScript, Vitest | active |
| [Devtools Web Server](projects/devtools-web-server/overview.md) | Always-on local Caddy server with site lifecycle API and live dashboard | Caddy, Python, React, TypeScript | active |
| [Agenticdeveloperhub](projects/agenticdeveloperhub/overview.md) | Full-stack multi-site web app hub with admin, dashboard, and API docs | React 19, TypeScript, Hono, PostgreSQL, Cloudflare Workers, Railway | active |
| [Agenticdevteam](projects/agenticdevteam/overview.md) | Multi-agent Claude Code plugin for product discovery with specialists and team pipelines | Python 3.10+, pytest, multi-agent pipeline | active |
| [Agentic Auth Service](projects/agentic-auth-service/overview.md) | Shared RS256 JWT authentication microservice for the agentic ecosystem | Node.js, Hono, TypeScript, PostgreSQL, Drizzle, Railway | active |
| [MyAgenticProjects](projects/myagenticprojects/overview.md) | Full-stack SaaS platform with auth, feature flags, messaging, feedback | React 19, Hono, PostgreSQL, Cloudflare Workers, Railway | active |
| [MyAgenticWorkspace](projects/myagenticworkspace/overview.md) | Empty placeholder repository (freshly initialized) | — | active |
| [Official Agent Registry](projects/official-agent-registry/overview.md) | "DNS for AI agents" — identity platform for registering and discovering AI agents | TypeScript, React, Hono, PostgreSQL, Cloudflare Workers | active |
| [Persona Creator](projects/persona-creator/overview.md) | Python library + Claude Code skill generating AI personas with visual character generation | Python 3.12+, Pydantic, Click, httpx | active |
| [Shared Website Components](projects/shared-website-components/overview.md) | React 19 component library (Agentic theme system + chat widget) consumed via git submodule | React 19, TypeScript, Vite, Vitest | active |
| [Learn True Facts](projects/learntruefacts/overview.md) | AI improv comedian chat app — planning complete, pre-implementation | React 19, Hono, PostgreSQL, Cloudflare Workers, multi-LLM | active |
| [Agentic Cookbook Tools](projects/agentic-cookbook-tools/overview.md) | User-facing Claude Code skills and guidance rules for cookbook integration | Markdown, YAML | paused |
| [Roadmaps](projects/roadmaps/overview.md) | Feature planning and implementation system for Claude Code with live dashboards | Python, Flask, SQLite, pytest | paused |
| [Agentic Kitchen](projects/agentic-kitchen/overview.md) | Empty placeholder repository (freshly initialized) | — | experimental |

## Web Applications & SaaS

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [mikefullerton.com](projects/mikefullerton.com/overview.md) | Personal portfolio/resume website — recently migrated to React | React 19, Vite, TypeScript, Cloudflare Workers | active |
| [Scratchyfish.com](projects/scratchyfish.com/overview.md) | Static website for Scratchy Fish progressive jazz rock band | Jekyll, HTML, CSS | paused |
| [mikeisdrumming](projects/mikeisdrumming/overview.md) | GitHub Pages landing page for music/drumming brand with music API research | Vanilla HTML, CSS | paused |

## Claude Code Extensions & Tools

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [Cat Herding](projects/cat-herding/overview.md) | Personal Claude Code workflow extensions — yolo, custom-status-line, linting skills | Python, YAML | active |
| [Social Media Bot](projects/social-media-bot/overview.md) | AI content pipeline of 12 sequential bots drafting posts for X/LinkedIn/Bluesky/Substack | Python, claude-agent-sdk, click, SQLite | active |

## Fun & Creative

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [Catnip](projects/catnip/overview.md) | Web dashboard for monitoring autonomous Claude Code agents in real-time | TypeScript, React 19, Hono, PostgreSQL, WebSocket, Railway | experimental |
| [Name-Craft](projects/name-craft/overview.md) | Children's book character name generator using Claude AI with sound symbolism | Python, Flask, Anthropic API, SQLite | experimental |
| [Market Research](projects/market-research/overview.md) | AI market analysis CLI — 5 specialized agents per project, synthesized ranking | Python 3.9+, Anthropic SDK, Tavily, Pydantic | paused |

## Infrastructure & Meta

| Project | Summary | Tech | Location |
|---------|---------|------|----------|
| [MySetup](projects/mysetup/overview.md) | Development environment automation for macOS and Windows (WSL) | Bash, Python, Homebrew | ~/projects/mysetup |
| [My Projects](projects/my-projects/overview.md) | Project management dashboard tracking ~35 git repos | React 19, Vite, Node.js, Python scanners | active |
| [Site Demos](projects/site-demos/overview.md) | Static HTML/CSS/JS scratchpad with PersonaChat widget themes browser | Vanilla HTML, CSS, JS | ~/projects/data |
| [My Agentic Interviews](projects/my-agentic-interviews/overview.md) | Interview repository + knowledge management system with YAML-frontmatter markdown | Markdown, YAML | ~/projects/data |

---

## Quick Reference

### By Lifecycle Location

**`~/projects/active/`** (in active development): Whippet, Agentic Daemon, Stenographer, Temporal, Agentic Toolkit, Agentic Plugins, Cookbook, Cookbook Web, Cookbook Backend, Dev Tools, Devtools Web Server, Agenticdeveloperhub, Agenticdevteam, Agentic Auth Service, MyAgenticProjects, MyAgenticWorkspace, Official Agent Registry, Persona Creator, Shared Website Components, Learn True Facts, mikefullerton.com, Cat Herding, Social Media Bot, My Projects

**`~/projects/paused/`**: Search Helper, QualityTime, Agentic Cookbook Tools, Roadmaps, Scratchyfish.com, mikeisdrumming, Market Research

**`~/projects/experimental/`**: Hairball, Catnip Terminal, Scratching Post, Temporal Platform, Agentic Kitchen, Catnip, Name-Craft

**Other**: MySetup (`~/projects/mysetup`), Site Demos & My Agentic Interviews (`~/projects/data`)

### By Organization

**mikefullerton** (personal GitHub): Hairball, Whippet, Catnip Terminal, Scratching Post, Search Helper, Catnip, mikefullerton.com, Scratchyfish.com, mikeisdrumming, Cat Herding, Social Media Bot, Name-Craft, Market Research, My Projects, MySetup, My Agentic Interviews

**agentic-cookbook** (org): Cookbook, Cookbook Web, Cookbook Backend, Dev Tools, Devtools Web Server, Agentic Cookbook Tools, Agenticdeveloperhub, Agenticdevteam, Agentic Auth Service, Agentic Daemon, Agentic Kitchen, Agentic Plugins, Agentic Toolkit, Stenographer, MyAgenticProjects, MyAgenticWorkspace, Official Agent Registry, Roadmaps, Persona Creator, Shared Website Components, Site Demos, Learn True Facts

**temporal-company** (org): Temporal, Temporal Platform

**QualityTimeStudios** (org): QualityTime

### By Status

**Active development**: Whippet, Stenographer, Agentic Daemon, Temporal, Agentic Toolkit, Agentic Plugins, Cookbook, Cookbook Web, Cookbook Backend, Dev Tools, Devtools Web Server, Agenticdeveloperhub, Agenticdevteam, Agentic Auth Service, Official Agent Registry, Persona Creator, Shared Website Components, Social Media Bot, My Projects, Cat Herding, mikefullerton.com

**Planning / pre-implementation**: Learn True Facts, Name-Craft, Temporal Platform, mikeisdrumming, Site Demos, My Agentic Interviews

**Empty / placeholder**: Agentic Kitchen, MyAgenticWorkspace

**Paused / on hold**: Search Helper, QualityTime, Agentic Cookbook Tools, Roadmaps, Scratchyfish.com, Market Research
