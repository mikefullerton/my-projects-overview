# Hairball — Project Overview

## Project Summary

Hairball is a native macOS menu bar application that manages window-level task contexts. It allows developers to group arbitrary windows (not apps) into named task contexts representing parallel workstreams (e.g., "iOS app" = specific Xcode project + terminal + browser), switch between contexts instantly, and persist window arrangements across app and system restarts using only public macOS Accessibility APIs.

## Type & Tech Stack

**Project Type:** macOS Desktop Application (Menu Bar App)  
**Target OS:** macOS 14+ (Sonoma and later)  
**Architecture:** Apple Silicon native (arm64)

**Technology Stack:**
- **Language:** Swift 5.9+
- **UI Framework:** SwiftUI (MenuBarExtra, Settings scenes)
- **Window Management:** AXUIElement & Accessibility APIs, CGWindowListCopyWindowInfo
- **App Lifecycle:** NSWorkspace notifications
- **Global Hotkeys:** KeyboardShortcuts library (Sindre Sorhus 2.4.0)
- **Build System:** Swift Package Manager + Xcode 16.0
- **State Persistence:** JSON files + Codable
- **Code Signing:** Automatic, Development Team K2NA732JAX

**Key Dependencies:**
- `KeyboardShortcuts` (https://github.com/sindresorhus/KeyboardShortcuts @ 2.4.0) — user-configurable global keyboard shortcuts

## GitHub URL

`git@github.com:mikefullerton/Hairball.git`  
https://github.com/mikefullerton/Hairball

## Directory Structure

```
Hairball/
├── .build/                                    # Swift build artifacts
├── .git/                                      # Git repository
├── .gitignore                                 # Ignores .claude/worktrees/, .build/, etc.
├── .swiftpm/                                  # Swift Package Manager config
├── Hairball.xcodeproj/                        # Xcode project (generated via xcodegen)
├── Sources/
│   └── Hairball/
│       ├── App/                               # Application entry point & UI scenes
│       │   ├── HairballApp.swift              # @main app struct with MenuBarExtra
│       │   ├── AppDelegate.swift              # Accessibility permission check
│       │   ├── AppState.swift                 # Shared application state container
│       │   ├── MenuBarView.swift              # Dropdown menu bar UI
│       │   ├── SettingsView.swift             # Settings window (tabbed)
│       │   ├── ReconcileView.swift            # Post-reboot window re-matching UI
│       │   ├── ContextVisualizationView.swift # Visual overview of contexts
│       │   ├── ContextPickerView.swift        # Floating context picker panel
│       │   ├── WindowExplorerView.swift       # View all windows across contexts
│       │   ├── WorkGroupsView.swift           # Manage work groups (new feature)
│       │   ├── DiscoveryView.swift            # Discovery/tutorial window
│       │   ├── HelpView.swift                 # Help/documentation window
│       │   └── HeuristicsSettingsTab.swift    # Custom heuristic rules UI
│       ├── Core/
│       │   ├── ContextManager.swift           # Brain: manages contexts, switching, parking
│       │   ├── ContextManagerError.swift      # Error types for context operations
│       │   └── Log.swift                      # Centralized logging (os.log)
│       ├── Models/
│       │   ├── TaskContext.swift              # Context model: name, color, windows, lastFocused
│       │   ├── WindowSnapshot.swift           # Persisted window state & fingerprint
│       │   ├── WindowFingerprint.swift        # Window identity: app, title pattern, display
│       │   ├── MatchStrategy.swift            # Enum: how to match windows (exact, substring, etc.)
│       │   └── GlobalState.swift              # Global persistent state model
│       ├── Window/
│       │   ├── WindowManager.swift            # Enumerate, move, resize, focus windows
│       │   ├── WindowInfo.swift               # Current window struct (app, title, frame, id)
│       │   ├── WindowObserver.swift           # Observe AX notifications & NSWorkspace events
│       │   ├── AXWindowHelper.swift           # AXUIElement utility functions
│       │   ├── WindowManipulating.swift       # Protocol for window manipulation
│       │   └── WindowManipulationError.swift  # Error types for window operations
│       ├── Fingerprint/
│       │   ├── WindowMatcher.swift            # Score windows against fingerprints
│       │   ├── AppHeuristic.swift             # Protocol for per-app matching heuristics
│       │   ├── HeuristicRegistry.swift        # Registry of built-in heuristics
│       │   ├── XcodeHeuristic.swift           # Extract project name from Xcode titles
│       │   ├── WarpHeuristic.swift            # Extract directory/branch from Warp
│       │   ├── BraveHeuristic.swift           # Extract page title from Brave
│       │   ├── VSCodeHeuristic.swift          # Extract workspace from VS Code
│       │   ├── TerminalHeuristic.swift        # Extract directory from Terminal
│       │   ├── CustomHeuristic.swift          # User-defined heuristic model
│       │   ├── CustomHeuristicRule.swift      # Rule structure for custom heuristics
│       │   └── CustomHeuristicStore.swift     # Persist/load custom heuristic rules
│       ├── Shortcuts/
│       │   ├── ShortcutManager.swift          # Manages global keyboard shortcuts
│       │   └── ShortcutNames.swift            # Shortcut identifier constants
│       └── Persistence/
│           └── StateStore.swift               # Read/write JSON to ~/.config/hairball/
├── Tests/
│   └── HairballTests/                         # Unit tests (Swift Testing framework)
├── Roadmaps/
│   └── HairballV1-Roadmap.md                  # Feature roadmap with acceptance criteria
├── Package.swift                              # Swift package manifest
├── Package.resolved                           # Locked dependency versions
├── project.yml                                # Xcodegen project config
├── Info.plist                                 # Bundle configuration
├── CLAUDE.md                                  # Development notes & architecture
├── PLAN.md                                    # Detailed implementation design document
└── GITIGNORE                                  # Excludes .build/, xcuserdata/, .claude/worktrees/
```

## Key Files & Components

**Entry Point:**
- `Sources/Hairball/App/HairballApp.swift` — Main app struct, initializes shared state, sets up menu bar UI

**Core Logic:**
- `Sources/Hairball/Core/ContextManager.swift` — Orchestrates context switching, window parking/restoration, state persistence
- `Sources/Hairball/Window/WindowManager.swift` — Wrapper around Accessibility APIs and CGWindow for window enumeration and manipulation
- `Sources/Hairball/Fingerprint/WindowMatcher.swift` — Scores live windows against fingerprints to find matches after reboot

**Data Models:**
- `Sources/Hairball/Models/TaskContext.swift` — Represents a named context with windows and settings
- `Sources/Hairball/Models/WindowSnapshot.swift` — Persisted window state (fingerprint, saved position, windowID)
- `Sources/Hairball/Models/WindowFingerprint.swift` — Window identity (app name, title pattern, display)

**Persistence:**
- `Sources/Hairball/Persistence/StateStore.swift` — Saves/loads JSON to `~/.config/hairball/` (contexts, windows, settings, heuristics)

**UI:**
- `Sources/Hairball/App/MenuBarView.swift` — Dropdown menu showing contexts, active indicator, quick actions
- `Sources/Hairball/App/SettingsView.swift` — Multi-tab settings (Contexts, Windows, Heuristics, General)
- `Sources/Hairball/App/ReconcileView.swift` — Post-reboot: assigns unmatched windows to contexts
- `Sources/Hairball/App/ContextVisualizationView.swift` — Visual grid showing contexts and their window arrangements

**Window Matching Heuristics:**
- `Sources/Hairball/Fingerprint/AppHeuristic.swift` — Protocol for per-app matching logic
- `Sources/Hairball/Fingerprint/HeuristicRegistry.swift` — Registry of all heuristics
- Built-in heuristics for Xcode, Warp, Brave, VS Code, Terminal (extract meaningful identifiers from window titles)
- `Sources/Hairball/Fingerprint/CustomHeuristic.swift` — User-defined rules for matching

**Testing:**
- `Tests/HairballTests/` — Unit tests (framework TBD)

## Claude Configuration

**No `.claude/` directory found.** The project has a `.gitignore` that excludes `.claude/worktrees/`, but no CLAUDE.md settings, rules, or plugins are configured in a `.claude/` directory at this time.

**CLAUDE.md exists** (at root) with brief technical notes:
- Mentions architecture is in PLAN.md
- Notes tech stack and build commands
- References core mechanism: off-screen window parking via AXUIElement

## Planning & Research Documents

**PLAN.md** (1,900+ lines)
- **Purpose:** Comprehensive implementation design document
- **Contents:**
  - Context: problem statement (macOS Spaces/Stage Manager operate at app level, not window level)
  - Full architecture design with tech stack rationale
  - Core mechanism: off-screen parking via `AXUIElement.setPosition(x: -30000)` — proven by FlashSpace
  - Detailed component breakdown with data structures
  - Context switching algorithm (save frames, park, restore)
  - Window identity & matching strategy (fingerprints, heuristics, scoring)
  - State persistence structure (`~/.config/hairball/`)
  - UI specifications (menu bar dropdown, settings tabs, reconcile sheet, visualization grid)
  - Keyboard shortcuts specification (⌃⌥1-9 for switch, ⌃⌥A to add, etc.)
  - Window observation via AX notifications and NSWorkspace
  - Permissions required: Accessibility only
  - **5-phase implementation plan** (Foundation, Menu Bar UI, Shortcuts, Matching & Persistence, Settings & Polish)
  - Post-plan cleanup checklist (disable yabai, re-enable SIP, etc.)
  - Verification checklist

**Roadmaps/HairballV1-Roadmap.md** (1,200+ lines)
- **Format:** Flat markdown roadmap file with metadata header
- **Created:** 2026-03-24, last modified 2026-03-24
- **Status:** All 15 implementation steps marked complete (as of 2026-04-06)
- **Contents:**
  - Feature definition: goal, platform, technologies, resources
  - Extended description with workflow examples
  - **Acceptance criteria** (all implementation features)
  - Dependencies & prerequisites (macOS 14+, Accessibility permission)
  - Risks & mitigations (off-screen parking edge cases, re-matching false positives, title changes)
  - Architecture decisions (why off-screen parking, why no SIP, why standalone vs yabai)
  - 15 implementation steps (foundation, window management, menu bar UI, shortcuts, matching, settings, polish, etc.)
  - Each step marks current progress/completion

**Notes from CLAUDE.md:**
```
# Hairball

Native macOS menu bar app for window-level task context management.

## Tech Stack
- Swift 5.9+ / SwiftUI, macOS 14+
- Public Accessibility APIs only (no SIP required)
- KeyboardShortcuts library (Sindre Sorhus) for global hotkeys

## Build
```
swift build
open Hairball.xcodeproj  # or use xcodegen if needed
```

## Architecture
See PLAN.md for full design. Core mechanism: off-screen window parking via AXUIElement.
```

## Git History & Current State

**Recent Commits (Last 5):**
```
2026-04-06 18:39:36 -0700  feat: add AppState, WindowExplorer, WorkGroups views and refactor app structure
2026-04-06 16:18:01 -0700  chore: standardize worktree directory to .claude/worktrees/
2026-03-27 11:12:21 -0700  Update CLAUDE.md: litterbox → agentic-cookbook
2026-03-25 12:41:21 -0700  feat: add Help window, Discovery window, oslog logging, rename contexts to Hairballs
2026-03-25 12:22:27 -0700  refactor: migrate 1 roadmaps to flat file format
```

**30-Commit Log Summary:**
- Phase 1-4 implementation (foundation, window management, menu bar UI, shortcuts, matching, persistence)
- Step-by-step PR-based development with numbered steps
- Recent additions: AppState refactor, WindowExplorer view, WorkGroups, Help/Discovery windows, oslog logging
- Renamed "contexts" terminology to "Hairballs" internally
- All 15 roadmap steps marked complete (merged into main)

**Current State:**
- **Branch:** main
- **Status:** 1 commit ahead of origin/main (not yet pushed)
- **Working Tree:** Clean (no uncommitted changes)
- **Bundle Version:** 1.0 (Info.plist)

**Git Remote:**
- origin: `git@github.com:mikefullerton/Hairball.git`

## Build & Test Commands

**Build:**
```bash
swift build
xcodebuild -scheme Hairball build
```

**Open Xcode:**
```bash
open Hairball.xcodeproj
# or regenerate via xcodegen:
xcodegen generate -s project.yml
```

**Build Settings Available:**
- Scheme: Hairball
- Target Platform: macOS (arm64 and x86_64)
- Code Signing: Automatic
- Development Team: K2NA732JAX
- Bundle Identifier: com.mikefullerton.Hairball
- Deployment Target: macOS 14.0

**Testing:**
- Unit test target: HairballTests (path: Tests/HairballTests)
- Framework: Standard Swift testing (specific framework not yet configured in codebase review)

## Notes & Context

**Architecture Highlights:**

1. **Off-Screen Window Parking:** The core technique for hiding windows uses only public APIs:
   - Save window position when deactivating context
   - Move to x: -30,000 via `AXUIElement.setPosition()`
   - Restore to saved position when re-activating
   - Imperceptible to users (~5ms per window, ~50ms for 10 windows)
   - Proven technique used by FlashSpace for PiP workaround

2. **Window Matching via Heuristics:** After app/system restart:
   - Each window gets a fingerprint: app name + title pattern + display
   - Per-app heuristics extract meaningful identifiers (Xcode: project name, Warp: directory/branch, Brave: page title, etc.)
   - Scoring algorithm matches running windows to dormant fingerprints
   - High-confidence matches (≥80 score) auto-assign; ambiguous matches surface in Reconcile UI

3. **State Persistence:**
   - Location: `~/.config/hairball/`
   - Format: JSON with Codable
   - Survives app restarts, system reboots, app updates
   - Includes contexts, window snapshots with saved positions, global settings, custom heuristic rules

4. **Keyboard Shortcuts:**
   - ⌃⌥1-9: Switch to context by index
   - ⌃⌥A: Add focused window to active context
   - ⌃⌥X: Remove focused window from context
   - ⌃⌥N/P: Next/previous context
   - ⌃⌥Space: Context picker popup
   - All configurable via Settings UI

5. **Recent Refactoring (2026-04-06):**
   - Introduced AppState for centralized state management
   - New WindowExplorer view to see all windows across contexts
   - New WorkGroups view (feature still being developed)
   - Standardized worktree directory to `.claude/worktrees/`
   - Added oslog logging throughout for debugging
   - Renamed "contexts" terminology to "Hairballs" in some UI areas

6. **Permissions:** Accessibility only (no SIP changes required)
   - Prompt on first launch via `AXIsProcessTrustedWithOptions`

7. **Development Workflow:**
   - Feature branches with numbered PRs (e.g., #16, #15, etc.)
   - Git worktrees supported (per .gitignore comment)
   - Xcodegen used to manage project configuration
   - Ready for production v1.0

**Status:** Feature complete for v1.0. All roadmap acceptance criteria implemented. Current focus: refinement (help UI, discovery window, appstate refactoring, workgroups exploration).
