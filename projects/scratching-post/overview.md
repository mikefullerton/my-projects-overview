# Scratching Post

## Project Summary

A native macOS IDE enhancement application that provides AI-powered development assistance with session management, real-time file monitoring, intelligent project discovery, and Claude AI integration. Designed as a productivity tool that sits alongside native development environments, offering features like session summarization, layout persistence, and AI-powered notes.

## Type & Tech Stack

**Project Type:** Native macOS desktop application

**Core Technologies:**
- **Swift & SwiftUI** — Modern native macOS UI framework
- **Xcode Project (.xcodeproj)** — Swift Package Manager integration
- **Core Data/SQLite** — Session state and layout persistence
- **FileSystemWatcher/DirectoryWatcher** — Real-time file monitoring
- **Claude AI SDK** — Integrated AI provider for session summarization and insights
- **AppKit** — Native macOS integration (menu bar, window management)
- **Darwin APIs** — IDE detection, process monitoring

**Architecture Approach:**
- Single window-based IDE as Swift application
- Real-time file system monitoring for project changes
- SQLite persistence for sessions and layout state
- AI-powered session summarization and dynamic pane layouts

## GitHub URL

`git@github.com:mikefullerton/scratching-post.git`

https://github.com/mikefullerton/scratching-post

## Directory Structure

```
scratching-post/
├── .claude/                              # Claude Code configuration
├── Catnip/                               # Main Swift source code (66 files)
│   ├── AIProvider.swift                  # Claude AI integration
│   ├── AIRequestBuilder.swift            # LLM request building
│   ├── AISettingsView.swift              # AI configuration UI
│   ├── CatnipApp.swift                   # Main app entry point
│   ├── CatnipProject.swift               # Project model and management
│   ├── CatnipWorkspace.swift             # Workspace management
│   ├── ContentView.swift                 # Main content view
│   ├── FileEditorView.swift              # File editing interface
│   ├── FileTreeManager.swift             # Project tree state
│   ├── FileSystemWatcher.swift           # Real-time file monitoring
│   ├── DirectoryWatchCoordinator.swift   # Directory watching coordination
│   ├── [40+ additional Swift files]      # Various UI/business logic components
│   └── Assets.xcassets                   # App icons and images
├── Catnip.xcodeproj/                     # Xcode project configuration
├── Roadmaps/                             # Feature development roadmaps
├── docs/                                 # Documentation
├── CLAUDE.md                             # Project rules
├── .gitignore
└── README.md
```

## Key Files & Components

**Application Core:**
- `Catnip/CatnipApp.swift` — Main application entry point and initialization
- `Catnip/ContentView.swift` — Root content view container

**AI Integration:**
- `Catnip/AIProvider.swift` — Claude AI integration and provider management
- `Catnip/AIRequestBuilder.swift` — Building and formatting AI requests
- `Catnip/AISettingsView.swift` — AI configuration user interface

**Session Management:**
- `Catnip/CatnipProject.swift` — Project model, session management
- `Catnip/CatnipWorkspace.swift` — Workspace state and persistence

**File System & Monitoring:**
- `Catnip/FileSystemWatcher.swift` — Real-time file system change detection
- `Catnip/DirectoryWatchCoordinator.swift` — Coordinates directory watching
- `Catnip/FileTreeManager.swift` — Project tree structure caching
- `Catnip/FileTreeCache.swift` — Efficient tree caching

**UI Components:**
- `Catnip/FileEditorView.swift` — File editing interface
- `Catnip/ContentViewerView.swift` — Content viewing/previewing
- `Catnip/AppDelegate.swift` — Application delegate for lifecycle events

**Project Discovery:**
- Project discovery via IDEs (Xcode, VSCode detection)
- Automatic project structure analysis
- IDE-based project sub-item display

## Claude Configuration

**Configuration Files:**
- `.claude/` — Project settings and Claude Code configuration

**Project Conventions:**
- Modern SwiftUI patterns with `@Observable` and `@MainActor`
- Sendable conformance for concurrency safety
- Proper main-thread isolation for UI updates

## Planning & Research Documents

**Feature Roadmaps:**
- `Roadmaps/` — Contains feature development specifications and progress tracking
- Active feature: CatnipIDEEnhancements (window title fix, file browser improvements, IDE detection, notes feature, menu bar status, settings redesign)

**Documentation:**
- `docs/` — Project documentation and design notes

## Git History & Current State

**Recent Activity:**
- `32526dd` docs: add standardized project description
- `763cc12` chore: standardize worktree directory to .claude/worktrees/
- `d48543a` Update CLAUDE.md: litterbox → agentic-cookbook
- `07237d3` fix: only update session summary on topic change
- `431572a` feat: AI-powered session summarization with multi-provider support
- `df6ad28` feat: dynamic pane layout with arrangement picker
- `1243837` feat: show IDE projects as sub-items in session list
- `876baa7` feat: double-click file in browser opens in default app
- `f9ef103` fix: inspector and panel toggles update SwiftUI state properly
- `fbeaca0` feat: add Project menu with Add Terminal and Open IDE actions
- `70d5d6f` feat: per-session layout state with SQLite persistence
- `b303e62` feat: add New Session and Panels toolbar buttons
- `465ec39` refactor: slim menu bar to Quick Note + Quit
- `f7559cb` refactor: replace custom Settings window with native Settings scene
- `6912c7c` fix: resolve build warnings (deprecated onChange, Sendable, main-actor)

**Pattern:** Active development with features for IDE enhancements, session management, AI integration, and UI improvements.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Build:**
```bash
xcodebuild -project Catnip.xcodeproj -scheme Catnip build
```

**Run:**
```bash
xcodebuild -project Catnip.xcodeproj -scheme Catnip run
```

**Open in Xcode:**
```bash
open Catnip.xcodeproj
```

## Notes

**Architecture Highlights:**

1. **Native SwiftUI Application** — Built entirely in Swift with SwiftUI framework
2. **Real-time File Monitoring** — DirectoryWatchCoordinator monitors project changes in real-time
3. **AI-Powered Summaries** — Session summarization via Claude AI for context retention
4. **Persistent Layout** — SQLite-backed session layout state and preferences
5. **IDE Detection** — Automatic discovery of Xcode/VSCode projects with sub-item display
6. **Dynamic Pane Layouts** — Flexible pane arrangement with arrangement picker

**Key Features:**

- Multi-pane IDE interface with collapsible panels
- AI-powered session summarization on topic changes
- IDE project discovery with hierarchical display
- File browser with keyboard shortcuts and double-click actions
- Per-session layout persistence across launches
- Menu bar integration (Quick Note + Quit)
- Native Settings scene with AI configuration
- Proper concurrency and main-thread safety

**Development Workflow:**

The project follows feature branch development with roadmaps documenting enhancements. Currently active: CatnipIDEEnhancements feature branch implementing window title fix, improved file browser, IDE detection, notes feature, menu bar status item, and settings redesign.

**Technology Notes:**

- Uses modern SwiftUI patterns (@Observable, @MainActor)
- Proper Sendable conformance for Swift concurrency
- Native FileSystemWatcher for efficient change detection
- SQLite backend for performant state persistence
