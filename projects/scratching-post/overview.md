# Scratching Post

## Project Summary

Scratching Post is a macOS application hosting the Catnip IDE — a document-based, multi-window IDE for managing projects and workspaces with integrated terminal sessions, notes, file browsing, and AI-powered session summarization.

## Type & Tech Stack

- **Project Type:** Native macOS SwiftUI/AppKit Application
- **Language:** Swift 5+
- **UI:** SwiftUI with AppKit interop
- **Database:** SQLite3 (custom SQLiteHelpers wrapper)
- **Terminal:** SwiftTerm
- **Code Editing:** CodeEditSourceEditor, CodeEditLanguages
- **File Monitoring:** FSEvents (FileSystemWatcher)
- **Document Types:** `.catnip-proj`, `.catnip-workspace`

## GitHub URL

`git@github.com:mikefullerton/scratching-post.git`

## Directory Structure

```
scratching-post/
├── .claude/
│   ├── settings.local.json           # Permissions: xcodebuild, git, gh
│   └── worktrees/
├── Catnip/                            # 60 Swift source files
│   ├── App: CatnipApp.swift, AppDelegate.swift, ContentView.swift
│   ├── Documents: ProjectDocument.swift, WorkspaceDocument.swift, CatnipProject.swift, CatnipWorkspace.swift
│   ├── UI - Projects: ProjectWindowView.swift (4-pane layout), ProjectSessionListView, ProjectTerminalPaneView, ProjectSettingsView, ProjectInspectorView
│   ├── UI - Workspaces: WorkspaceWindowView, WorkspaceSidebarView, WorkspaceEntryRow, WorkspaceWelcomeView
│   ├── UI - File Browser: FileTreeView, FileTreeNode, FileTreeManager, FileTreeCache, FileEditorView
│   ├── UI - Terminal: TerminalViewRepresentable, TerminalSession
│   ├── UI - Notes: NotesWindowView, NotesSettingsView, QuickNotePanel (floating NSPanel)
│   ├── UI - Settings: SettingsView (5 tabs: General, Profiles, AI, Notes, File Types)
│   ├── Data: SQLiteProjectStore, SQLiteWorkspaceStore, SQLiteNotesStore, SQLiteHelpers, SessionLayoutState
│   ├── File System: FileSystemWatcher, DirectoryWatchCoordinator, GitStatusProvider, LanguageDetection
│   ├── IDE: IDEDetector (Xcode, VS Code, IntelliJ, SPM)
│   ├── Notes: Note.swift, NotesManager.swift
│   ├── AI: AIProvider (multi-provider), AIRequestBuilder, SessionSummarizer, SummarizationCoordinator, KeychainHelper
│   ├── Menu Bar: MenuBarManager (NSStatusItem), QuickNotePanel
│   └── Core: SessionManager, Logging, SettingsKeys, WindowAccessor, UTType+Catnip
├── Catnip.xcodeproj/
├── Roadmaps/
│   ├── CatnipIDEEnhancements-Roadmap.md  # Complete (16/16 steps)
│   ├── ProjectFiles-Roadmap.md
│   ├── SessionMetadata-Roadmap.md
│   ├── SettingsWindow-Roadmap.md
│   └── TerminalSessionHost-Roadmap.md
├── CLAUDE.md
└── .gitignore
```

## Key Components

**Document-based Architecture:** ProjectDocument (`.catnip-proj`) and WorkspaceDocument (`.catnip-workspace`) with separate window controllers

**4-Pane Project Window:** Sessions sidebar, terminal, file tree, inspector

**File Browser:** FSEvents monitoring, git status overlay, IDE detection (Xcode/VS Code/IntelliJ), file tree caching

**Notes System:** Full CRUD, pinning, markdown editing, search, dedicated SQLiteNotesStore

**Menu Bar:** NSStatusItem with project/workspace listing, Quick Note floating panel

**AI Summarization:** Multi-provider (Claude/OpenAI/Google), triggered on topic change, debounced

**Persistence:** Per-concern SQLite stores (Project, Workspace, Notes), layout state in DB

## Claude Configuration

- Permissions: xcodebuild, git operations, gh CLI
- Worktrees for feature branches

## Planning & Research Documents

**CatnipIDEEnhancements Roadmap (Complete, 16/16 steps):**
Window title fix, file browser toggle, resize-to-fit, IDE detection/caching, IDE inspector, open-in-IDE, notes window, SQLiteNotesStore, notes settings, file types settings, quick note panel, menu bar, AI summarization, dynamic pane layout, IDE sub-items, settings redesign

**4 additional roadmaps:** ProjectFiles, SessionMetadata, SettingsWindow, TerminalSessionHost

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Working tree:** Clean
- **Recent (2026-04-06):** Standardize worktree directory
- **Key milestones:** Full CatnipIDEEnhancements feature set (PR #98), AI summarization, AppKit interop

## Build & Test Commands

```bash
xcodebuild -project Catnip.xcodeproj -scheme Catnip -destination 'platform=macOS' build
open Catnip.xcodeproj
```

No XCTest suite — manual integration testing. 60 Swift files total.

## Notes

- Modular persistence through per-concern SQLite stores
- AppKit integration: NSStatusItem, NSPanel, NSWindow title manipulation
- FSEvents + DirectoryWatchCoordinator for real-time file tree updates
- IDE detection scans for .xcodeproj, .vscode, .idea, Package.swift
- MVVM pattern with @ObservedObject/@StateObject, async/await for background tasks
