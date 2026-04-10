# devtools-web-server

## Project Summary

An always-on local development web server built on Caddy, providing a site lifecycle management API and a live dashboard for serving, monitoring, and managing local development sites. Sites are deployed by dropping files into `~/.local-server/sites/` and accessed at `https://dev.local` or `http://localhost:2080`.

## Type & Tech Stack

- **Type:** Developer tooling / local infrastructure
- **Server:** Caddy (static file server + reverse proxy)
- **Backend daemon:** Python 3 (`site_manager.py` -- REST API + SSE on port 2081)
- **Frontend:** React 19 + TypeScript + Vite 6
- **OS integration:** macOS launchd (daemon auto-start), Homebrew (Caddy install)
- **Install/uninstall:** Shell scripts (`install.sh`, `uninstall.sh`)

## GitHub URL

`git@github.com:agentic-cookbook/devtools-web-server.git`

## Directory Structure

```
devtools-web-server/
  README.md
  install.sh                  # Full setup: Caddy, DNS, daemon, home page build
  uninstall.sh                # Tear down everything cleanly
  site-template/
    Caddyfile                 # Caddy config template (dev.local + :2080)
    site_manager.py           # REST API daemon (704 lines) -- site lifecycle
    site_watcher.py           # Legacy file watcher daemon (165 lines)
    browse.html               # Caddy browse template (541 lines)
    com.local-server.site-manager.plist
    com.local-server.site-watcher.plist
  home-page/                  # React app -- live dashboard at site root
    src/
      App.tsx
      ActivityLog.tsx
      SiteCard.tsx
      SiteList.tsx
      types.ts
      hooks/
    package.json              # "local-server-home"
    vite.config.ts
  react-template/             # Reusable React template for new sites
    src/
      App.tsx
      claude-bridge.ts        # SSE listener + event poster for Claude interaction
      config.ts
    package.json              # "local-site-template"
    vite.config.ts
  api-tester/                 # React app for testing site_manager.py endpoints
    src/
      App.tsx
      claude-bridge.ts
      config.ts
      styles.css
    package.json              # "api-tester"
    vite.config.ts
  docs/
    planning/
      planning.md             # Placeholder
    project/
      description.md          # Placeholder
  .claude/
    CLAUDE.md
    settings.json
    skills/
      test-site/              # Skill for testing claude-bridge interactions
    worktrees/
```

## Key Files & Components

### `site-template/site_manager.py`
The core backend daemon (704 lines). Provides a full REST API on port 2081 for site lifecycle management:
- `POST /sites` -- register a new site (name, path, config)
- `GET /sites` -- list all sites with metadata
- `GET /sites/:id` -- site details
- `PUT /sites/:id/state` -- set state (running/stopped/closed)
- `POST /sites/:id/update` -- signal browser refresh via SSE
- `DELETE /sites/:id` -- remove a site
- `POST /sites/:id/events` -- post event from site JS
- `GET /sites/:id/events` -- dequeue next event (Claude polls this)
- `GET /sites/:id/stream` -- SSE stream for browser push

Polls `~/.local-server/sites/` for filesystem changes and maintains a registry in `~/.local-server/registry.json`.

### `site-template/Caddyfile`
Caddy configuration using a shared snippet (`local-server`) for both `dev.local` (HTTPS with auto-TLS) and `:2080` (HTTP fallback). Routes `/_api/*` to the site manager on port 2081. Serves static files from `~/.local-server/sites/`.

### `home-page/`
React 19 + TypeScript dashboard deployed at the root of the sites directory. Components: `SiteList`, `SiteCard`, `ActivityLog`. Displays all registered sites with metadata, age timers, activity log, and management controls.

### `react-template/`
Starter template for creating new local sites. Includes `claude-bridge.ts` which connects to the site manager's SSE stream for live refresh, state changes (stop/close overlays), and custom event round-trips between Claude and the browser.

### `api-tester/`
React app for manually testing all `site_manager.py` API endpoints. Shares node_modules with `home-page/` via symlink.

### `install.sh`
Comprehensive installer: installs Caddy via Homebrew, sets up `dev.local` DNS in `/etc/hosts`, writes the Caddyfile, starts the site manager launchd daemon, builds and deploys the home page, installs the React template, and injects a Caddy section into the global `~/.claude/CLAUDE.md`.

### `uninstall.sh`
Clean removal: stops daemons, removes launchd plists, removes server files (preserves user sites), removes DNS entry, cleans up Caddyfile and global CLAUDE.md.

## Claude Configuration

### `.claude/CLAUDE.md`
- Enforces worktree-based workflow (never commit directly to main)
- Workflow: `EnterWorktree` -> work + draft PR -> `ExitWorktree` -> merge from main
- Tech stack, build, and architecture sections are placeholders

### `.claude/settings.json`
- Enabled plugin: `superpowers@claude-plugins-official`

### `.claude/skills/test-site/`
Skill for deploying a test page at `https://dev.local/test-site/` to verify claude-bridge interactions (SSE refresh, state changes, custom events).

## Planning & Research Documents

- `docs/planning/planning.md` -- placeholder (empty)
- `docs/project/description.md` -- placeholder (empty)

## Git History & Current State

- **Branch:** `main`
- **Status:** Clean working tree
- **Remote:** `git@github.com:agentic-cookbook/devtools-web-server.git`
- **Total commits:** 14

Recent history (newest first):
```
7b0111d docs: rewrite worktree workflow rule with clear step-by-step order
8cb857a docs: add worktree/PR workflow rule to project CLAUDE.md
d0a8cc3 refactor: move all logs to ~/.local-server/logs/ directory
5974690 feat: add test-site skill for testing claude-bridge interactions
8efc40f feat: add API Tester link to home page header
e90e29b fix: remove max-height cap on log entries so each shows full height
884c012 feat: add api-tester site for testing all site_manager.py endpoints
81a03c7 fix: remove display:flex from body to fix symmetric padding
11e5f57 fix: pin section frames to right viewport edge with consistent padding
62870c9 feat: site lifecycle management API + React template (#1)
004dfbf feat: switch dev.local to HTTPS with Caddy auto-TLS
8a164c3 feat: add dev.local DNS alias on port 80
90afc81 feat: add local web server install, uninstall, and site templates
01b1c9d Initial project scaffolding
```

## Build & Test Commands

```bash
# Install everything (Caddy, DNS, daemon, home page, template)
./install.sh

# Uninstall everything
./uninstall.sh

# Build home page separately
cd home-page && npm install && npx vite build

# Build api-tester separately
cd api-tester && npm install && npx vite build

# Build react-template separately
cd react-template && npm install && npx vite build

# Service management
brew services start/stop/restart caddy
launchctl load/unload ~/Library/LaunchAgents/com.local-server.site-manager.plist
```

## Notes

- The project installs infrastructure into `~/.local-server/` and writes a Caddy config section into the global `~/.claude/CLAUDE.md`, making it a system-wide development tool rather than a standalone app.
- `site_watcher.py` is the legacy daemon; `site_manager.py` is its replacement with the full REST API. The install script handles migration from watcher to manager.
- The `claude-bridge.ts` module is the key integration point between Claude Code and browser-based sites -- it enables Claude to push refresh signals, state changes, and custom events to running sites, and to poll for events posted by site JavaScript.
- The React template at `~/.local-server/react-template/` can optionally symlink to `~/projects/active/shared-website-components` if that project exists.
- All three React sub-projects (home-page, api-tester, react-template) use identical dependency stacks: React 19 + Vite 6 + TypeScript 5.8.
- Ports used: 443 (dev.local HTTPS), 2080 (HTTP fallback), 2081 (site manager API), 2019 (Caddy admin).
