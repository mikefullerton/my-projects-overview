# Whippet

A macOS menu bar app that monitors Claude Code sessions in real time.

## Project Summary

Whippet is a lightweight macOS menu bar application that provides real-time visibility into all active Claude Code sessions running on a machine. It consumes session events produced by Claude Code global hooks via a file-based event queue (`~/.claude/session-events/`), stores them in a local SQLite database, and displays active sessions in a floating NSPanel grouped by project. The app supports configurable click actions (open terminal, open transcript, copy session ID, custom shell commands, notifications), AI-powered session summarization (with multi-provider support: Anthropic, OpenAI, Google, custom), accessibility-based window activation, and staleness detection for idle sessions.

## Type & Tech Stack

- **Type**: macOS menu bar application (LSUIElement)
- **Language**: Swift
- **UI Frameworks**: AppKit (NSPanel, NSStatusItem, NSHostingController) + SwiftUI (hosted via NSHostingController)
- **Storage**: SQLite3 (C API with Swift wrapper, WAL mode)
- **File System Monitoring**: DispatchSource (FSEvents for watching event queue directory)
- **Notifications**: UNUserNotificationCenter (macOS notifications)
- **Launch Integration**: SMAppService (launch-at-login support)
- **Build System**: Xcode (Whippet.xcodeproj)
- **Testing**: XCTest (44 Swift files, 14+ test files)

## GitHub URL

`git@github.com:mikefullerton/Whippet.git`

## Directory Structure

```
Whippet/
├── .claude/
│   └── settings.local.json       # Claude Code local settings
├── .git/                         # Git repository
├── docs/
│   └── project/
│       └── description.md        # Project documentation
├── Roadmaps/
│   └── CreateApp-Roadmap.md     # Feature roadmap and implementation plan
├── Scripts/                      # Utility scripts
├── CLAUDE.md                     # Claude Code project guide
├── .gitignore
└── Whippet/                      # Xcode project root
    ├── Whippet/                  # Main source code (44 Swift files)
    │   ├── AppDelegate.swift     # App entry point and lifecycle
    │   ├── main.swift
    │   ├── Log.swift
    │   ├── Info.plist
    │   ├── Whippet.entitlements
    │   ├── Assets.xcassets
    │   ├── Actions/              # Session action handling
    │   │   ├── SessionActionHandler.swift
    │   │   ├── SessionClickAction.swift
    │   │   └── ActivationTestLog.swift
    │   ├── Database/             # SQLite data layer
    │   │   ├── DatabaseManager.swift
    │   │   └── Models.swift
    │   ├── Hooks/                # Claude Code hook installation
    │   │   └── HookInstaller.swift
    │   ├── Ingestion/            # Event consumption and processing
    │   │   ├── EventIngestionManager.swift
    │   │   ├── EventFile.swift
    │   │   ├── GitMetadataResolver.swift
    │   │   ├── SessionLivenessMonitor.swift
    │   │   └── SessionSummarizer.swift
    │   ├── Notifications/        # macOS notification system
    │   │   └── NotificationManager.swift
    │   ├── Settings/             # Settings UI and AI integration
    │   │   ├── SettingsView.swift
    │   │   ├── SettingsViewModel.swift
    │   │   ├── SettingsWindowController.swift
    │   │   ├── AIRequestBuilder.swift
    │   │   ├── MiniChatView.swift
    │   │   ├── MiniChatViewModel.swift
    │   │   ├── LaunchAtLoginManager.swift
    │   │   └── KeychainHelper.swift
    │   └── Window/               # UI for floating session panel
    │       ├── SessionPanel.swift
    │       ├── SessionPanelController.swift
    │       ├── SessionListViewModel.swift
    │       ├── SessionContentView.swift
    │       ├── WindowDiscoveryView.swift
    │       ├── WindowDiscoveryViewModel.swift
    │       └── SummarizerDebugWindowController.swift
    ├── Whippet.xcodeproj/        # Xcode project configuration
    └── WhippetTests/             # Test suite (14+ test files)
```

## Key Files & Components

### Core Architecture Files
- **AppDelegate.swift** — Main app entry point, lifecycle management, menu bar setup
- **DatabaseManager.swift** — SQLite database connection, schema creation, session CRUD operations
- **EventIngestionManager.swift** — Watches event queue directory, consumes JSON files, inserts into database

### Session Management
- **SessionActionHandler.swift** — Processes click actions on sessions (terminal, transcript, copy ID, custom commands)
- **SessionLivenessMonitor.swift** — Detects and marks idle/stale sessions
- **SessionSummarizer.swift** — Generates AI-powered session summaries via configurable providers

### UI Components
- **SessionPanel.swift** / **SessionPanelController.swift** — Floating NSPanel window configuration
- **SessionListViewModel.swift** / **SessionContentView.swift** — SwiftUI-based session list display
- **SettingsView.swift** / **SettingsViewModel.swift** — Settings UI and state management
- **WindowDiscoveryView.swift** — Panel for discovering and activating windows via Accessibility API

### Integration & Configuration
- **HookInstaller.swift** — Installs Claude Code hooks on first launch
- **AIRequestBuilder.swift** — Builds API requests for session summarization (Anthropic, OpenAI, Google, custom)
- **KeychainHelper.swift** — Stores API keys securely in macOS Keychain
- **GitMetadataResolver.swift** — Extracts git metadata (remote URL, branch) from session events
- **NotificationManager.swift** — Manages macOS notifications
- **LaunchAtLoginManager.swift** — Handles launch-at-login functionality via SMAppService

### Configuration
- **CLAUDE.md** — Claude Code project guide with conventions and build commands
- **CreateApp-Roadmap.md** — Comprehensive feature roadmap with implementation details
- **Info.plist** — macOS app configuration
- **Whippet.entitlements** — App entitlements for Accessibility and other APIs

## Claude Configuration

- **Claude Code Settings**: `.claude/settings.local.json` (with copy permissions for cookbook rules)
- **Worktree Directory**: `.claude/worktrees/` (as specified in CLAUDE.md)
- **Conventions**:
  - Use native SwiftUI/AppKit controls before building custom equivalents
  - All lengthy tasks must be done asynchronously; never block the main thread
  - Always use PRs and git worktrees; never commit directly to main
  - Commit and push immediately after each batch of changes

## Planning & Research Documents

- **docs/project/description.md** — Comprehensive project overview with purpose, features, tech stack, and architecture
- **Roadmaps/CreateApp-Roadmap.md** — Detailed roadmap with 12 implementation steps, task breakdown, and progress tracking

## Git History & Current State

- **Current Branch**: `main`
- **Remote**: `git@github.com:mikefullerton/Whippet.git`
- **Recent Commits** (last 15):
  - `0517e2a` — docs: add standardized project description
  - `4173947` — cleanup
  - `f0cdd3a` — chore: standardize worktree directory to .claude/worktrees/
  - `eb5f062` — Update CLAUDE.md: litterbox → agentic-cookbook
  - `caa388c` — feat: AI session summarization, frontmost window tracking, minimal UI
  - `15a6a1b` — fix: snapshot app metadata on main thread, enumerate windows on background
  - `1624c2d` — docs: update CLAUDE.md with litterbox component spec instructions
  - `e3926b8` — refactor: migrate 1 roadmaps to flat file format
  - `65e5b3e` — fix: lock window width when settings inspector is collapsed
  - `cac9324` — fix: enable horizontal resize and restore window position on inspector close
  - `0ce5b58` — refactor: use NavigationSplitView for settings inspector layout
  - `8fcfc09` — refactor: use native NSSplitViewController inspector for settings drawer
  - `72b4d0f` — feat: replace settings window with slide-out drawer on session panel
  - `205fd2e` — fix: accessibility re-prompting, window titles, and add window discovery panel
  - `7b6c9c5` — feat: complete CreateApp feature — actions, settings, logging, git metadata, and security fixes
- **Status**: Active development; 11 of 12 roadmap steps complete (manual integration testing remains)

## Build & Test Commands

```bash
# Build debug configuration
xcodebuild -scheme Whippet -configuration Debug build

# Run tests
xcodebuild -scheme Whippet -configuration Debug test

# Build release configuration
xcodebuild -scheme Whippet -configuration Release build
```

## Notes

- **Session Event Format**: JSON files in `~/.claude/session-events/` produced by Claude Code hooks
- **Database**: SQLite with WAL mode for efficient concurrent access
- **Accessibility API**: Used for window discovery and activation (requires accessibility permissions)
- **Multi-provider AI Summarization**: Supports Anthropic, OpenAI, Google, and custom API providers
- **Related Project**: [Hairball](https://github.com/mikefullerton/Hairball) — another menu bar app for managing window task contexts
- **macOS Requirements**: macOS 14+
- **App Type**: LSUIElement (no Dock presence, menu bar only)
- **Status**: Actively maintained with regular commits and feature refinements
