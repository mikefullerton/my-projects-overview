# Whippet Project Overview

## Project Summary

Whippet is a macOS menu bar application that monitors Claude Code sessions in real time. It consumes session events produced by Claude Code global hooks via a file-based event queue, displays active sessions in a floating window with grouping by project, and supports configurable click actions, AI-powered session summarization, window activation, and notifications.

## Type & Tech Stack

**Project Type**: macOS native desktop application (menu bar utility)

**Primary Language**: Swift 5.0

**UI Framework**: 
- AppKit (NSStatusItem, NSPanel, NSHostingController)
- SwiftUI (via NSHostingController for hosted content)

**Data Persistence**: SQLite3 (built-in macOS C API)

**Key Technologies**:
- FSEvents / DispatchSource (file system monitoring)
- UNUserNotificationCenter (macOS notifications)
- SMAppService (launch at login)
- Claude Code global hooks (event producers)
- Accessibility API (window activation)
- os.Logger (structured logging with 10+ named categories)

**Architecture Pattern**: Menu bar app (LSUIElement) with floating session monitor window

**Deployment Target**: macOS 14.0+

**Current Version**: 0.1.0

## GitHub URL

`git@github.com:mikefullerton/Whippet.git`

Repository branch: `main` (up to date with origin/main)

## Directory Structure

```
Whippet/
├── .claude/
│   ├── settings.local.json          # Claude Code local configuration
│   └── worktrees/                   # Claude Code worktree directory
├── .git/                            # Git repository
├── .gitignore                       # Git ignore patterns
├── CLAUDE.md                        # Project conventions and context
├── Roadmaps/
│   ├── CreateApp-Roadmap.md         # 12-step feature implementation plan
│   └── repair.log
├── Scripts/                         # Test scripts (untracked)
│   ├── test_click_activation.swift
│   └── test_window_activation.swift
├── Whippet/                         # Xcode project root
│   ├── Whippet/                     # Source code
│   │   ├── Actions/
│   │   │   ├── SessionActionHandler.swift
│   │   │   ├── SessionClickAction.swift
│   │   │   └── ActivationTestLog.swift
│   │   ├── Assets.xcassets/         # App icon and assets
│   │   ├── Database/
│   │   │   ├── DatabaseManager.swift
│   │   │   └── Models.swift
│   │   ├── Hooks/
│   │   │   └── HookInstaller.swift
│   │   ├── Ingestion/
│   │   │   ├── EventIngestionManager.swift
│   │   │   ├── EventFile.swift
│   │   │   ├── SessionSummarizer.swift
│   │   │   ├── GitMetadataResolver.swift
│   │   │   └── SessionLivenessMonitor.swift
│   │   ├── Notifications/
│   │   │   └── NotificationManager.swift
│   │   ├── Settings/
│   │   │   ├── SettingsViewModel.swift
│   │   │   ├── SettingsView.swift
│   │   │   ├── SettingsWindowController.swift
│   │   │   ├── MiniChatView.swift
│   │   │   ├── MiniChatViewModel.swift
│   │   │   ├── AIRequestBuilder.swift
│   │   │   ├── KeychainHelper.swift
│   │   │   └── LaunchAtLoginManager.swift
│   │   ├── Window/
│   │   │   ├── SessionPanelController.swift
│   │   │   ├── SessionPanel.swift
│   │   │   ├── SessionListViewModel.swift
│   │   │   ├── SessionContentView.swift
│   │   │   ├── WindowDiscoveryView.swift
│   │   │   ├── WindowDiscoveryViewModel.swift
│   │   │   └── SummarizerDebugWindowController.swift
│   │   ├── AppDelegate.swift
│   │   ├── Log.swift
│   │   ├── main.swift
│   │   ├── Info.plist
│   │   └── Whippet.entitlements
│   ├── WhippetTests/                # 14 test files, 100+ test cases
│   │   ├── DatabaseManagerTests.swift
│   │   ├── EventIngestionManagerTests.swift
│   │   ├── HookInstallerTests.swift
│   │   ├── IngestionIntegrationTests.swift
│   │   ├── LaunchAtLoginManagerTests.swift
│   │   ├── NotificationManagerTests.swift
│   │   ├── SessionActionHandlerTests.swift
│   │   ├── SessionListViewModelTests.swift
│   │   ├── SessionLivenessMonitorTests.swift
│   │   ├── SessionPanelControllerTests.swift
│   │   ├── SessionSummarizerTests.swift
│   │   ├── SettingsViewModelTests.swift
│   │   ├── AIRequestBuilderTests.swift
│   │   └── WhippetTests.swift
│   └── Whippet.xcodeproj/
└── Whippet-cookbook/                # Cookbook component documentation
    ├── app/
    ├── context/
    ├── resources/
    └── cookbook-project.json        # Recipe index and metadata
```

**Total Swift Files**: 77

## Key Files & Components

### Core Application

**AppDelegate.swift** (350 lines)
- Entry point and lifecycle manager
- Initializes all subsystems: database, ingestion, notifications, settings, panel
- Sets up menu bar presence with NSStatusItem
- Requests accessibility permissions on launch
- Manages shutdown sequence

### Data Layer

**DatabaseManager.swift** (950+ lines)
- SQLite3 C API wrapper with Swift interface
- WAL mode enabled for concurrent read performance
- Schema: `sessions`, `events`, `settings` tables
- CRUD operations for sessions and events
- Upsert semantics for event deduplication
- Migration system for schema versioning
- 23 unit tests

**Models.swift**
- Session data model (id, session_id, cwd, model, status, timestamps)
- Event data model (type, session_id, timestamp, raw JSON)

### Event Ingestion Pipeline

**EventIngestionManager.swift** (500+ lines)
- Watches `~/.claude/session-events/` via DispatchSource
- Reads JSON event files, parses, inserts into SQLite
- Handles concurrent file writes with minimum age delay (50ms)
- Deletes processed files
- Routes malformed JSON to error directory
- 30+ test cases

**HookInstaller.swift** (450+ lines)
- Auto-installs Claude Code hooks into `~/.claude/settings.json`
- Supports 9 hook event types: SessionStart, SessionEnd, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStart, SubagentStop, Notification
- Detects existing hooks (idempotent)
- Merges with existing settings (no overwrites)
- Uses `jq` for JSON generation from stdin
- Supports uninstallation
- 29 unit tests

**SessionLivenessMonitor.swift** (250+ lines)
- PID-based liveness detection
- Timeout-based stale detection (configurable, default 1 minute)
- Marks sessions as stale/dead when unresponsive
- 10+ unit tests

**SessionSummarizer.swift** (400+ lines)
- AI-powered session naming (3-8 words)
- Debounced to avoid excessive API calls
- Multi-provider support (Anthropic, OpenAI, Google, Custom)
- 10+ unit tests

**GitMetadataResolver.swift**
- Extracts repository name and git metadata from working directory
- Used for session grouping and labeling

### UI Components

**SessionPanelController.swift** (270+ lines)
- Manages NSPanel window lifecycle
- Configurable floating/normal window level
- Transparency adjustment (0.3-1.0)
- Position persistence across toggles
- SwiftUI content via NSHostingController
- 28 unit tests

**SessionContentView.swift**
- SwiftUI session list display
- Groups sessions by repository
- Shows: working directory, model, time started, last activity, last tool, status indicator
- Real-time updates from SQLite

**SessionListViewModel.swift** (550+ lines)
- Manages session display logic
- Grouping and sorting
- Status calculation (active/stale/ended)
- Real-time UI updates
- 15+ unit tests

**SettingsWindowController.swift**
- Preferences window with sidebar categories:
  - General (staleness timeout, always-on-top, transparency)
  - Notifications (per-event-type preferences)
  - Click Actions (select from 7 available actions)
  - AI Settings (multi-provider API key management)
  - Launch at Login
  - Window Discovery (debug)
  - AI Chat (embedded multi-turn conversation)

**SettingsView.swift** (600+ lines)
- SwiftUI settings panel
- Settings form with persistence
- Real-time configuration
- 15+ unit tests

**MiniChatView.swift** & **MiniChatViewModel.swift**
- Embedded AI chat UI in settings
- Multi-turn conversation support
- Used for session summarization configuration

### Actions & Interactions

**SessionActionHandler.swift** (750+ lines)
- Executes 7 configurable click actions:
  1. Open Terminal (cd to session directory, launch Terminal.app)
  2. Open Transcript (reveal session transcript file)
  3. Copy Session ID (clipboard)
  4. Custom Shell Command (user-configurable)
  5. Send Notification (user-facing alert)
  6. Activate Window (Accessibility API with scoring)
  7. Copy Working Directory (clipboard)
- Thread-safe command execution
- Error handling and logging
- 20+ unit tests

**WindowDiscoveryView.swift** & **WindowDiscoveryViewModel.swift**
- Debug panel for window activation
- Shows all visible windows with Accessibility attributes
- Scoring logic for window matching
- Used to tune window activation behavior

### Services & Infrastructure

**AIRequestBuilder.swift** (300+ lines)
- Multi-provider HTTP request builder
- Providers: Anthropic, OpenAI, Google, Custom
- API key management (Keychain)
- Request serialization/deserialization
- Error handling
- 15+ unit tests

**NotificationManager.swift** (300+ lines)
- UNUserNotificationCenter integration
- Per-event-type notification preferences
- Session event notifications (start, end, stale)
- 15+ unit tests

**KeychainHelper.swift**
- Secure storage/retrieval of API keys
- Used for AI provider credentials

**LaunchAtLoginManager.swift** (150+ lines)
- SMAppService wrapper
- Launch at login registration
- Permission request handling
- 10+ unit tests

**Log.swift**
- Centralized os.Logger with 10+ named categories:
  - app, database, ingestion, hooks, actions, notifications, settings, ui, ai, lifecycle

### Testing

**14 test files** with 100+ test cases covering:
- Database CRUD, migrations, schema validation
- Event ingestion, JSON parsing, error handling
- Hook installation, detection, merge logic
- Session list display, grouping, sorting
- Settings persistence and UI updates
- Action execution and window activation
- Notification generation
- AI request building and response handling
- Integration scenarios (file drop → DB ingestion)

## Claude Configuration

### settings.local.json

Contains local permissions for automated recipe copying from the agentic-cookbook:
```json
{
  "permissions": {
    "allow": [
      "Bash(cp /Users/mfullerton/projects/active/cookbook/rules/authoring-ground-rules.md /Users/mfullerton/projects/active/Whippet/.claude/rules/)",
      "Bash(cp /Users/mfullerton/projects/active/cookbook/rules/cookbook.md /Users/mfullerton/projects/active/Whippet/.claude/rules/)",
      "Bash(cp /Users/mfullerton/projects/active/cookbook/rules/auto-lint.md /Users/mfullerton/projects/active/Whippet/.claude/rules/)"
    ]
  }
}
```

### CLAUDE.md (Project Conventions)

**Platform**: macOS 14+
**Language**: Swift
**UI**: AppKit (NSPanel, NSStatusItem) + SwiftUI via NSHostingController
**Storage**: SQLite
**Architecture**: Menu bar app (LSUIElement) with floating session monitor window

**Key Conventions**:
- Use native SwiftUI/AppKit controls before building custom equivalents
- All lengthy tasks must be asynchronous (never block main thread)
- Always use PRs and git worktrees (directory: `.claude/worktrees/`)
- Commit and push immediately after each batch of changes
- No commits directly to main

**Build Command**:
```bash
xcodebuild -scheme Whippet -configuration Debug build
```

## Planning & Research Documents

### CreateApp-Roadmap.md

**Status**: 11 of 12 steps complete

**Feature Definition**: Build Whippet, a standalone macOS menu bar app that monitors all active Claude Code sessions in real time with a floating window showing sessions grouped by project, configurable click actions, notifications, and always-on behavior.

**Architecture Decisions**:
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Event transport | File-based drop directory | Hooks are shell commands; files simpler than SQLite from bash |
| Data storage | SQLite | Structured queries, built into macOS |
| Window system | NSPanel + NSHostingController | Control over window level/transparency + SwiftUI bridge |
| Menu bar | NSStatusItem | Full AppKit control |
| App lifecycle | LSUIElement + SMAppService | No dock icon, proper login item handling |

**12 Implementation Steps**:
1. ✅ Project Scaffold & Menu Bar Shell
2. ✅ SQLite Database Layer
3. ✅ Drop Directory & Event Ingestion
4. ✅ Hook Auto-Installation
5. ✅ Floating Window Shell (NSPanel)
6. ✅ Session List UI
7. ✅ Session Liveness Detection
8. ✅ Settings UI
9. ✅ Click Actions System
10. ✅ Launch at Login
11. ✅ Notifications
12. ⏳ CreateApp Feature (in progress)

**Verification Strategy**:
- Build: `xcodebuild -scheme Whippet -configuration Debug build`
- Test: `xcodebuild -scheme Whippet -configuration Debug test`
- Manual: Launch app, create Claude Code session, verify session appears, test actions and settings

### Whippet-cookbook/

**Type**: Agentic-cookbook project metadata and component documentation

**Purpose**: Structured component library documenting all major features using cookbook recipe patterns

**Contents**:
- `app/` — Recipe documentation for all major components
- `context/` — Research documents: architecture-map.md, scope-report.md, generation-summary.md, lifecycle-reviews.md
- `cookbook-project.json` — Component index with dependency graph

**Key Component Groups**:
- **App Lifecycle**: Single-instance guard, subsystem initialization, shutdown
- **Menu Bar**: NSStatusItem with SF Symbol icon (dog.fill)
- **Session Panel**: NSPanel floating utility window with real-time list
- **Settings**: Desktop app preferences with 7 sidebar categories
- **Actions**: 7 configurable click actions with executor pattern
- **Infrastructure**: 8 components (logging, settings keys, window persistence, event ingestion, hooks, liveness, AI summarizer, notifications, launch-at-login)
- **Services**: AI request builder (multi-provider)
- **Data**: SQLite persistence with WAL mode

## Git History & Current State

### Recent Activity

**Latest commits** (last 5):
- `f0cdd3a` (2026-04-06 16:18) chore: standardize worktree directory to `.claude/worktrees/`
- `eb5f062` (2026-03-27 11:12) Update CLAUDE.md: litterbox → agentic-cookbook
- `caa388c` (2026-03-27 08:01) feat: AI session summarization, frontmost window tracking, minimal UI
- `15a6a1b` (2026-03-26 11:10) fix: snapshot app metadata on main thread, enumerate windows on background
- `e3926b8` (2026-03-25 12:46) docs: update CLAUDE.md with litterbox component spec instructions

### Branch Status

**Current branch**: `main`
**Remote status**: Up to date with `origin/main`
**Uncommitted changes**: None
**Untracked files**:
- `Roadmaps/repair.log`
- `Scripts/` (test scripts)
- `Whippet-build/` (build artifacts)
- `Whippet-cookbook/` (documentation subproject)

### Commit History (30 most recent)

The repository shows active development with focused, atomic commits. Major feature areas visible in history:
- AI session summarization (3 commits)
- Window activation and Accessibility API integration (4 commits)
- Settings UI with inspector drawer (6 commits)
- Session liveness detection (3 commits)
- Click actions system (3 commits)
- Notifications (2 commits)
- Settings UI and persistence (2 commits)
- Hook installation (3 commits)
- Initial floating window implementation (2 commits)

**Total commits**: 100+ (feature development very active)

## Build & Test Commands

### Build

```bash
# Debug build
xcodebuild -scheme Whippet -configuration Debug build

# Release build
xcodebuild -scheme Whippet -configuration Release build
```

### Test

```bash
# All tests
xcodebuild -scheme Whippet -configuration Debug test

# Specific test class
xcodebuild -scheme Whippet -configuration Debug test -only-testing WhippetTests/DatabaseManagerTests
```

### Run

```bash
# Launch the app (development)
xcodebuild -scheme Whippet -configuration Debug run
```

### Project Settings

- **Xcode Format**: Modern (objectVersion: 56)
- **Framework Phases**: Empty (uses system frameworks only)
- **Deployment Target**: macOS 14.0
- **Swift Version**: 5.0
- **Bundle Identifier**: com.mikefullerton.Whippet

## Notes

### Architecture Highlights

1. **Event-Driven Architecture**: Claude Code hooks produce events via file drop; Whippet ingests via FSEvents
2. **Decoupled Subsystems**: AppDelegate initializes independent managers (database, ingestion, notifications, liveness, summarizer)
3. **Async-First**: All I/O operations on background queues; main thread reserved for UI
4. **Persistence Layers**: Settings in SQLite (key-value), window frame in UserDefaults, API keys in Keychain
5. **Multi-Provider AI Support**: Abstracted via AIRequestBuilder (Anthropic, OpenAI, Google, Custom)
6. **Accessibility Integration**: Uses macOS Accessibility API for window activation with scoring/matching logic

### Security Considerations

- API keys stored in Keychain (not plaintext)
- Command injection hardened (uses Process API, not shell expansion)
- SQLite prepared statements (SQL injection prevention)
- Accessibility permissions requested on first launch
- Entitlements defined in Whippet.entitlements

### Notable Features

- **AI Session Summarization**: Automatically generates 3-8 word session names via Claude API
- **Window Activation**: Scores windows by process name, window title, role to activate the correct window
- **Staleness Detection**: Combines PID checking + timeout-based marking for dead sessions
- **Settings Inspector**: Slide-out drawer UI with real-time updates
- **Multi-Turn Chat**: Embedded AI chat in settings for interactive configuration
- **Launch at Login**: Proper permission handling via SMAppService
- **Debug Panel**: Window discovery panel for troubleshooting activation

### Dependencies

**System Frameworks** (macOS built-in):
- AppKit
- SwiftUI
- Foundation
- CoreServices (FSEvents)
- ServiceManagement (SMAppService)
- UserNotifications
- Security (Keychain)
- ApplicationServices (Accessibility)

**External Package Dependencies**: None (self-contained Swift implementation)

### Known Risks & Unknowns (from roadmap)

- **High event volume**: Busy sessions produce 30-50 tool events/minute; FSEvents + file deletion must keep pace
- **Hook installation conflicts**: Must merge with existing hooks in settings.json, not overwrite
- **Stale session false positives**: 1-minute timeout might be aggressive if user is reading Claude's output
- **Multiple Claude Code versions**: Hook payload format could change between versions

### Active Development

- Latest work focuses on AI session summarization and window tracking
- Recent refactoring to use native NSSplitViewController for settings inspector
- Heavy testing coverage (100+ test cases across 14 test files)
- Using agentic-cookbook for component documentation and recipe patterns

---

*Last Updated: 2026-04-06*
*Analyzed from repository at: /Users/mfullerton/projects/active/Whippet*
