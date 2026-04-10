# Hairball

## Project Summary

Hairball is a native macOS menu bar application for managing window-level task contexts across parallel development workstreams. It enables developers to group arbitrary windows (not entire apps) into named task contexts, switch between them instantly via off-screen parking using only public Accessibility APIs, and persist window arrangements across system restarts. The app uses heuristic-based window matching for robust reconciliation after reboot and includes visual context grids, work groups, and configurable global hotkeys.

## Type & Tech Stack

**Type:** macOS Desktop Application (Menu Bar App)

**Tech Stack:**
- **Language:** Swift 5.9+
- **Frameworks:** SwiftUI (MenuBarExtra, Settings, Window scenes), AppKit
- **Window Management:** AXUIElement, Accessibility APIs, CGWindowListCopyWindowInfo
- **Build System:** Swift Package Manager + Xcode
- **State Persistence:** JSON files in `~/.config/hairball/`
- **Key Dependency:** KeyboardShortcuts (Sindre Sorhus 2.x) for global hotkeys
- **Target OS:** macOS 14+

## GitHub URL

https://github.com/mikefullerton/Hairball

## Directory Structure

```
Hairball/
├── Sources/Hairball/
│   ├── App/              # @main app, MenuBarExtra, AppDelegate
│   ├── Core/             # WindowManager, ContextManager, WindowMatcher, WindowObserver
│   ├── Models/           # TaskContext, WindowSnapshot, AppHeuristic
│   ├── Window/           # Window management, parking, restoration
│   ├── Fingerprint/      # Window identity & matching after reboot
│   ├── Persistence/      # State store (JSON serialization)
│   └── Shortcuts/        # Keyboard shortcuts integration
├── Tests/HairballTests/  # Unit tests
├── Roadmaps/             # Roadmap files
├── docs/                 # Project documentation
├── Package.swift         # SPM configuration
├── Package.resolved      # Dependency lock file
├── PLAN.md              # Detailed architecture & roadmap
├── CLAUDE.md            # Claude Code configuration
├── project.yml          # Project metadata
└── .build/              # Build artifacts
```

## Key Files & Components

- **CLAUDE.md** - Claude Code configuration; build instructions via `swift build` or Xcode
- **Package.swift** - Swift Package Manager configuration with KeyboardShortcuts dependency
- **PLAN.md** - Comprehensive architecture document covering core mechanism (off-screen window parking), window identity fingerprinting, heuristic matching strategies, and full 12-step roadmap with 11 steps complete
- **Roadmaps/** - Roadmap tracking progress toward feature completion
- **Sources/Hairball/** - Core implementation:
  - **Core/ContextManager.swift** - CRUD for contexts, switching logic, state persistence
  - **Core/WindowManager.swift** - AXUIElement wrapper for window enumeration, positioning, resizing, focus
  - **Core/WindowMatcher.swift** - Fingerprint system for window identity across reboots
  - **Fingerprint/** - Window fingerprinting logic (app name, title, class, role, bounds heuristics)
  - **Models/** - Data models (TaskContext, WindowSnapshot, AppHeuristic)
  - **Window/** - Window state management and restoration logic

## Claude Configuration

Stored in `.claude/` directory (does not exist at root, but project uses Claude Code for development). Settings and worktree management are documented in PLAN.md.

## Planning & Research Documents

- **docs/project/description.md** - Complete project description, purpose, key features, tech stack, architecture overview, related projects, and status
- **PLAN.md** - 80+ lines of detailed architecture document including design rationale, component breakdown, core mechanism explanation (window parking), window identity & matching strategy, context switching algorithm, and 12-step roadmap with progress tracking

## Git History & Current State

- **Remote:** git@github.com:mikefullerton/Hairball.git
- **Current Branch:** main
- **Status:** Clean working tree (no uncommitted changes)
- **Recent Activity:**
  - Latest: docs: add standardized project description (223b406)
  - AppState, WindowExplorer, WorkGroups views refactored (814e3a3)
  - Help window, Discovery window, oslog logging, contexts renamed to Hairballs (5ef2245)
  - User-configurable heuristic rules with Settings UI and persistence (e916260)
  - Last 15 commits include feature additions for context picker, visualization grid, settings window with multiple tabs

## Build & Test Commands

```bash
swift build                    # Build the project
open Hairball.xcodeproj        # Open in Xcode for development

# Or use xcodegen if needed for Xcode project generation
```

## Notes

- **Status:** Active development — 11 of 12 roadmap steps complete
- **Architecture:** Central `ContextManager` with `WindowManager` for AXUIElement control and `WindowMatcher` for fingerprint-based reconciliation
- **Key Innovation:** Off-screen window parking via `AXUIElementSetAttributeValue(kAXPositionAttribute, x: -30000)` — public API, per-window, fast (~5ms per window), proven approach used by FlashSpace
- **Dependencies:** Minimal — only KeyboardShortcuts external package; all window management via public macOS APIs
- **Related Projects:** Whippet (menu bar Claude Code monitor), Scratching Post (Catnip IDE)
