# Stenographer

## Project Summary
A headless macOS launchd daemon that installs Claude Code hooks, captures all session events into SQLite, and exposes HTTP and XPC APIs for real-time insight into Claude activity. Monitors Claude Code sessions and agent activity, reporting on execution with strict concurrency and no external dependencies.

## Type & Tech Stack
- **Type**: macOS daemon + CLI tool
- **Language**: Swift 6 (strict concurrency)
- **Platform**: macOS 14+
- **Build System**: Xcode (project generated from `project.yml` via XcodeGen)
- **HTTP**: Network.framework (NWListener) — no external dependencies
- **XPC**: NSXPCConnection with MachServices
- **Database**: SQLite via C API (WAL mode, FULLMUTEX)
- **Distribution**: LaunchAgent (~/Library/LaunchAgents/)

## GitHub URL
`git@github.com:agentic-cookbook/stenographer.git`

## Directory Structure
```
stenographer/
├── Apple/
│   ├── Stenographer.xcworkspace/        # root workspace
│   └── Stenographer/
│       ├── project.yml                  # XcodeGen spec
│       ├── Stenographer.xcodeproj/      # generated Xcode project
│       ├── StenographerXPCProtocol/     # @objc protocol + Codable DTOs
│       ├── StenographerCLILib/          # CLI helpers + StenographerCLITests
│       ├── StenographerLib/             # daemon logic (HTTP, XPC, SQLite)
│       ├── stenographer/                # CLI executable
│       ├── stenographerd/               # daemon executable
│       └── com.agentic-cookbook.stenographer.plist
├── agentic-daemon/                      # submodule
├── agentic-plugins/                     # submodule
├── agentic-toolkit/                     # submodule
├── skills/
│   └── custom-status-line/              # Claude Code skill
├── docs/
│   ├── designs/
│   ├── planning/
│   ├── project/
│   └── superpowers/
├── tests/
│   └── test_dev_reload.py
├── .claude/
│   ├── CLAUDE.md
│   ├── settings.json
│   └── worktrees/
├── .gitmodules                          # submodule configuration
├── install.sh                           # installation script
├── uninstall.sh                         # uninstallation script
├── dev-reload.py                        # development reload helper
└── README.md
```

## Key Files & Components

**Submodules** (git submodules):
- `agentic-plugins` — plugin infrastructure
- `agentic-daemon` — daemon utilities
- `agentic-toolkit` — shared toolkit

**Core Binaries**:
- `stenographerd` — daemon executable (launchd service)
- `stenographer` — CLI tool (symlinked to /usr/local/bin)

**XPC & HTTP**:
- `StenographerXPCProtocol` — @objc protocol and Codable DTOs
- HTTP endpoints (NWListener on port 22847):
  - `GET /health`
  - `GET /sessions[?status=active&project=...]`
  - `GET /sessions/:id`
  - `GET /sessions/:id/events[?limit=&offset=&type=...]`
  - `GET /events[?type=&since=&limit=...]`
  - `GET /events/stream` (Server-Sent Events)

**Hooks & Storage**:
- Hook marker: `# stenographer-hook` (coexists with Whippet's `# whippet-hook`)
- Drop directory: `~/.claude/stenographer-events/` (event JSON files)
- Database: `~/Library/Application Support/com.agentic-cookbook.stenographer/stenographer.db`
- Logs: `~/Library/Logs/com.agentic-cookbook.stenographer/`

## Claude Configuration
Located at `.claude/CLAUDE.md`:
- Strict concurrency architecture overview
- Build commands (XcodeGen + xcodebuild)
- HTTP/XPC endpoint documentation
- CLI command reference
- Database and hook conventions
- Graphify knowledge graph integration

## Planning & Research Documents
- `docs/project/description.md` — project overview
- `docs/planning/planning.md` — planning and analysis
- `docs/designs/status-line-design.md` — UI/CLI design docs
- `docs/superpowers/specs/` — feature specifications
- `docs/superpowers/plans/` — implementation plans (e.g., Python conversion for dev-reload)

## Git History & Current State
- **Remote**: origin → `git@github.com:agentic-cookbook/stenographer.git`
- **Branch**: main (770ac37)
- **Status**: clean
- **Recent commits**:
  1. 770ac37 — Organize Apple/Stenographer by target (#5)
  2. 72fd708 — Import custom-status-line skill from cat-herding (#4)
  3. 1c130c8 — Convert to XcodeGen Xcode project (#3)
  4. 0a17b5f — docs: point worktree location at ~/projects/worktrees/stenographer/
  5. 4d9c23a — Add agentic-daemon submodule
  6. 7c45f2a — Add agentic-plugins submodule
  7. 2225cf9 — chore: merge graphify section into .claude/CLAUDE.md, remove root CLAUDE.md
  8. 4660f47 — chore: install graphify claude hook and CLAUDE.md
  9. 4bcdaf9 — chore: gitignore graphify-out/ generated output
  10. fa13985 — Add .swiftpm/ to .gitignore

## Build & Test Commands
```bash
# Regenerate Xcode project from XcodeGen spec
cd Apple/Stenographer && cc-xcgen

# Build (debug)
swift build --package-path .

# Build (Release)
xcodebuild -workspace Apple/Stenographer.xcworkspace -scheme Stenographer -configuration Release build

# Run tests
xcodebuild -workspace Apple/Stenographer.xcworkspace -scheme Stenographer test

# Development reload (build + hot-swap daemon)
python3 dev-reload.py          # build + full reload
python3 dev-reload.py --quick  # skip build, just kickstart

# Install to system
./install.sh

# Uninstall from system
./uninstall.sh

# Verify running daemon
stenographer health
launchctl list | grep stenographer
```

## Notes
- **install.sh**: Builds Release binary, copies to `~/Library/Application Support/com.agentic-cookbook.stenographer/`, symlinks CLI to `/usr/local/bin/stenographer`, registers LaunchAgent plist, bootstraps launchd service
- **uninstall.sh**: Uninstalls hooks, stops launchd service, removes plist and binaries, optionally removes logs and event drop directory
- **dev-reload.py**: Python script for rapid development iteration — builds debug binary, writes dev LaunchAgent plist, hot-swaps running daemon via launchctl kickstart/bootstrap, optionally skips build with `--quick` flag
- Submodules are working copies of `agentic-daemon`, `agentic-plugins`, and `agentic-toolkit`; included in `Stenographer.xcworkspace` for unified build
- Graphify knowledge graph available at `graphify-out/` (auto-rebuilt via watch system)
- Worktree location: `~/projects/worktrees/stenographer/<branch>/`
