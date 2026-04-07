# Whippet

## Project Summary

A macOS menu bar application that monitors Claude Code sessions in real time. Consumes session events produced by Claude Code global hooks via a file-based event queue (JSON files in `~/.claude/session-events/`), ingests them into a local SQLite database, and displays active sessions in a floating NSPanel window grouped by project. Features include configurable click actions (open terminal, open transcript, copy session ID, custom shell command, notification), AI-powered session summarization, Accessibility API-based window activation, staleness detection, macOS notifications, and launch-at-login support. 11 of 12 roadmap implementation steps are complete (only manual integration testing remains).

## Type & Tech Stack

- **Type**: macOS menu bar application (LSUIElement)
- **Language**: Swift
- **Platform**: macOS 14+
- **UI**: AppKit (NSPanel, NSStatusItem, NSHostingController) + SwiftUI via NSHostingController
- **Storage**: SQLite3 (C API with Swift wrapper, WAL mode)
- **Event monitoring**: DispatchSource (file system watching)
- **Notifications**: UNUserNotificationCenter
- **Login**: SMAppService (launch at login)
- **AI**: Multi-provider AI request builder (Anthropic, OpenAI, Google, Custom) for session summarization
- **Build**: Xcode project (Whippet.xcodeproj)
- **Testing**: XCTest (14 test files)

## GitHub URL

`git@github.com:mikefullerton/Whippet.git`

## Directory Structure

```
Whippet/
├── .claude/
│   └── settings.local.json            # Permission allowlists
├── Roadmaps/
│   ├── CreateApp-Roadmap.md           # Feature roadmap (12 steps, 11 complete)
│   └── repair.log                     # Repair log (untracked)
├── Scripts/
│   ├── test_click_activation.swift    # Click activation test script
│   └── test_window_activation.swift   # Window activation test script
├── Whippet/                           # Xcode project source
│   ├── Whippet/                       # App source code
│   │   ├── Actions/
│   │   │   ├── SessionActionHandler.swift     # Click action executor (30K)
│   │   │   ├── SessionClickAction.swift       # Action enum definition
│   │   │   └── ActivationTestLog.swift        # Activation testing
│   │   ├── Database/
│   │   │   ├── DatabaseManager.swift          # SQLite wrapper (30K)
│   │   │   └── Models.swift                   # Data models
│   │   ├── Hooks/
│   │   │   └── HookInstaller.swift            # Claude hook auto-installation (14K)
│   │   ├── Ingestion/
│   │   │   ├── EventIngestionManager.swift    # File watcher + DB ingestion (16K)
│   │   │   ├── SessionSummarizer.swift        # AI session summarization (13K)
│   │   │   ├── SessionLivenessMonitor.swift   # Staleness detection (6K)
│   │   │   ├── GitMetadataResolver.swift      # Git repo metadata
│   │   │   └── EventFile.swift                # Event file model
│   │   ├── Notifications/
│   │   │   └── NotificationManager.swift      # macOS notifications (10K)
│   │   ├── Settings/
│   │   │   ├── SettingsView.swift             # SwiftUI settings form (19K)
│   │   │   ├── SettingsViewModel.swift        # Settings state (22K)
│   │   │   ├── SettingsWindowController.swift # Window management
│   │   │   ├── AIRequestBuilder.swift         # Multi-provider AI HTTP client (8K)
│   │   │   ├── MiniChatView.swift             # Embedded AI chat UI
│   │   │   ├── MiniChatViewModel.swift        # Chat state
│   │   │   ├── KeychainHelper.swift           # Keychain storage
│   │   │   └── LaunchAtLoginManager.swift     # SMAppService wrapper
│   │   ├── Window/
│   │   │   ├── SessionContentView.swift       # SwiftUI session list
│   │   │   ├── SessionListViewModel.swift     # Session list state (17K)
│   │   │   ├── SessionPanel.swift             # NSPanel subclass
│   │   │   ├── SessionPanelController.swift   # Panel management (7K)
│   │   │   ├── WindowDiscoveryView.swift      # Window discovery UI
│   │   │   ├── WindowDiscoveryViewModel.swift # Window discovery state
│   │   │   └── SummarizerDebugWindowController.swift
│   │   ├── AppDelegate.swift                  # App entry point (10K)
│   │   ├── Log.swift                          # Centralized logging
│   │   ├── main.swift                         # App bootstrap
│   │   ├── Info.plist
│   │   └── Whippet.entitlements
│   ├── Whippet.xcodeproj/            # Xcode project file
│   └── WhippetTests/                  # 14 test files
│       ├── DatabaseManagerTests.swift
│       ├── EventIngestionManagerTests.swift
│       ├── HookInstallerTests.swift
│       ├── NotificationManagerTests.swift
│       ├── SessionActionHandlerTests.swift
│       ├── SessionListViewModelTests.swift
│       ├── SessionLivenessMonitorTests.swift
│       ├── SessionPanelControllerTests.swift
│       ├── SessionSummarizerTests.swift
│       ├── SettingsViewModelTests.swift
│       ├── LaunchAtLoginManagerTests.swift
│       ├── AIRequestBuilderTests.swift
│       ├── IngestionIntegrationTests.swift
│       └── WhippetTests.swift
├── Whippet-build/                     # Build artifacts (untracked)
├── Whippet-cookbook/                   # Cookbook project definition
│   ├── cookbook-project.json           # Component manifest (28 components)
│   ├── app/                           # Component recipes
│   ├── context/                       # Research context
│   └── resources/                     # Additional resources
├── CLAUDE.md                          # Project instructions
└── .gitignore
```

## Key Files & Components

- `CLAUDE.md` -- Project overview: macOS 14+, Swift, AppKit+SwiftUI, SQLite, menu bar app architecture, build command, conventions (native controls, async-first, PRs+worktrees, commit frequently)
- `Whippet/Whippet/AppDelegate.swift` -- App entry point: NSStatusItem setup, subsystem initialization, menu bar dropdown
- `Whippet/Whippet/Database/DatabaseManager.swift` -- SQLite3 C API wrapper with WAL mode, schema migrations, CRUD for sessions/events/settings tables
- `Whippet/Whippet/Ingestion/EventIngestionManager.swift` -- DispatchSource file watcher consuming JSON event files from `~/.claude/session-events/`
- `Whippet/Whippet/Hooks/HookInstaller.swift` -- Auto-installs Claude Code hooks into `~/.claude/settings.json` (merge, not overwrite)
- `Whippet/Whippet/Actions/SessionActionHandler.swift` -- 5+ configurable click actions with iTerm2/Terminal fallback
- `Whippet/Whippet/Ingestion/SessionSummarizer.swift` -- AI-powered session name generation (debounced, 3-8 words)
- `Whippet/Whippet/Settings/AIRequestBuilder.swift` -- Multi-provider AI HTTP client (Anthropic, OpenAI, Google, Custom)
- `Whippet-cookbook/cookbook-project.json` -- Detailed component manifest with 28 components, recipe references, and dependency graph
- `Roadmaps/CreateApp-Roadmap.md` -- 12-step implementation roadmap (11 complete)

## Claude Configuration

- `CLAUDE.md` -- Conventions: native SwiftUI/AppKit controls first, async-first, PRs+worktrees (`.claude/worktrees/`), commit frequently
- **Settings (local)**: Permission allowlists for copying cookbook rules to `.claude/rules/`
- No project-level settings.json

## Planning & Research Documents

- `Roadmaps/CreateApp-Roadmap.md` -- Comprehensive 12-step feature roadmap with acceptance criteria, verification strategies, and implementation notes. 11/12 steps complete. Each step documents GitHub issue number, complexity, dependencies, and test coverage.
- `Whippet-cookbook/context/` -- Research context for cookbook integration
- `Whippet-cookbook/cookbook-project.json` -- Component architecture manifest listing all 28 components with recipes, dependencies, and source references

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: standardize worktree directory to .claude/worktrees/"
- **Working tree**: 4 untracked items (Roadmaps/repair.log, Scripts/, Whippet-build/, Whippet-cookbook/)
- **Recent activity**: Active development through late March 2026, maintenance commits in April
- **Key recent changes**: AI session summarization + frontmost window tracking, snapshot app metadata threading fix, CLAUDE.md updates, roadmap migration, settings inspector layout refactoring (NavigationSplitView then NSSplitViewController), CreateApp feature completion

## Build & Test Commands

```bash
# Build
xcodebuild -scheme Whippet -configuration Debug build

# Test
xcodebuild -scheme Whippet -configuration Debug test

# Open in Xcode
open Whippet/Whippet.xcodeproj
```

## Notes

- Menu bar app with no dock icon (LSUIElement = YES), using SF Symbol `dog.fill` for the menu bar icon
- Event pipeline: Claude Code hooks write JSON files to `~/.claude/session-events/` -> DispatchSource watches directory -> files parsed and inserted into SQLite -> files deleted after ingestion
- Hook auto-installation uses `# whippet-hook` marker comments to identify its hooks, supports merge with existing hooks and clean uninstallation
- Sessions grouped by repository/project, with visual status indicators (green=active, orange=stale, hollow=ended)
- Staleness detection via configurable timeout (default 60s) with DispatchSourceTimer on utility QoS queue
- AI session summarization is debounced and supports 4 providers (Anthropic, OpenAI, Google, Custom) with Keychain-stored API keys
- The Whippet-cookbook directory contains an agentic-cookbook project definition with 28 components mapped to recipes
- 14 test files covering all major subsystems (200+ tests total across DatabaseManager, EventIngestion, HookInstaller, Notifications, Actions, SessionList, Liveness, Panel, Summarizer, Settings, LaunchAtLogin, AIRequestBuilder)
- Part of a broader tool ecosystem referenced alongside "Catnip IDE" (scratching-post) project
