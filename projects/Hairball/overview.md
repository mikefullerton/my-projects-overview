# Hairball - Project Overview

## Project Summary

Hairball is a native macOS menu bar application that manages window-level task contexts. It allows developers to group arbitrary windows (not apps) into named task contexts representing parallel workstreams (e.g., "iOS app" = specific Xcode project + terminal + browser), switch between contexts instantly via off-screen parking, and persist window arrangements across app and system restarts using only public macOS Accessibility APIs. No SIP changes required.

## Type & Tech Stack

**Project Type:** macOS Desktop Application (Menu Bar App)
**Target OS:** macOS 14+ (Sonoma and later)
**Architecture:** Apple Silicon native (arm64)

**Technology Stack:**
- **Language:** Swift 5.9+
- **UI Framework:** SwiftUI (MenuBarExtra, Settings scenes, Window scenes)
- **Window Management:** AXUIElement & Accessibility APIs, CGWindowListCopyWindowInfo
- **App Lifecycle:** NSWorkspace notifications
- **Global Hotkeys:** KeyboardShortcuts library (Sindre Sorhus 2.x)
- **Build System:** Swift Package Manager + Xcode (xcodegen for project config)
- **State Persistence:** JSON files + Codable in `~/.config/hairball/`
- **Logging:** os.log (macOS unified logging)

**Key Dependencies:**
- `KeyboardShortcuts` (https://github.com/sindresorhus/KeyboardShortcuts from: 2.0.0) -- user-configurable global keyboard shortcuts

## GitHub URL

`git@github.com:mikefullerton/Hairball.git`
https://github.com/mikefullerton/Hairball

## Directory Structure

```
Hairball/
├── Sources/Hairball/
│   ├── App/                          # Application entry point & all UI views
│   │   ├── HairballApp.swift         # @main app struct with MenuBarExtra
│   │   ├── AppDelegate.swift         # Accessibility permission check
│   │   ├── AppState.swift            # Centralized application state (ObservableObject)
│   │   ├── MenuBarView.swift         # Dropdown menu bar UI
│   │   ├── SettingsView.swift        # Settings window (tabbed: Contexts, Shortcuts, General)
│   │   ├── ReconcileView.swift       # Post-reboot window re-matching UI
│   │   ├── ContextVisualizationView.swift  # Visual grid of contexts and window layouts
│   │   ├── ContextPickerView.swift   # Floating search popup (ctrl+opt+Space)
│   │   ├── WindowExplorerView.swift  # View all windows across contexts
│   │   ├── WorkGroupsView.swift      # Work groups management (new feature)
│   │   ├── DiscoveryView.swift       # Discovery/tutorial window
│   │   ├── HelpView.swift            # Help/documentation window
│   │   └── HeuristicsSettingsTab.swift  # Custom heuristic rules UI
│   ├── Core/
│   │   ├── ContextManager.swift      # Brain: context CRUD, switching, parking/restore
│   │   ├── ContextManagerError.swift # Error types
│   │   └── Log.swift                 # Centralized os.log logging
│   ├── Models/
│   │   ├── TaskContext.swift          # Context: name, color, windows, lastFocused
│   │   ├── WindowSnapshot.swift       # Persisted window state & fingerprint
│   │   ├── WindowFingerprint.swift    # Window identity: app, titlePattern, display
│   │   ├── MatchStrategy.swift        # Enum: appAndTitleExact, appAndTitleSubstring, appOnly
│   │   └── GlobalState.swift          # Global persistent state model
│   ├── Window/
│   │   ├── WindowManager.swift        # AXUIElement wrapper: enumerate, move, resize, focus
│   │   ├── WindowInfo.swift           # Current window struct
│   │   ├── WindowObserver.swift       # AX notifications & NSWorkspace events
│   │   ├── AXWindowHelper.swift       # AXUIElement utilities
│   │   ├── WindowManipulating.swift   # Protocol for testability
│   │   └── WindowManipulationError.swift
│   ├── Fingerprint/
│   │   ├── WindowMatcher.swift        # Score windows against fingerprints
│   │   ├── AppHeuristic.swift         # Protocol for per-app matching
│   │   ├── HeuristicRegistry.swift    # Registry of built-in + custom heuristics
│   │   ├── XcodeHeuristic.swift       # Extract project name from Xcode titles
│   │   ├── WarpHeuristic.swift        # Extract directory/branch from Warp
│   │   ├── BraveHeuristic.swift       # Extract page title from Brave
│   │   ├── VSCodeHeuristic.swift      # Extract workspace from VS Code
│   │   ├── TerminalHeuristic.swift    # Extract directory from Terminal
│   │   ├── CustomHeuristic.swift      # User-defined heuristic model
│   │   ├── CustomHeuristicRule.swift  # Rule structure (substring/regex)
│   │   └── CustomHeuristicStore.swift # Persist/load custom rules
│   ├── Shortcuts/
│   │   ├── ShortcutManager.swift      # Global keyboard shortcut registration
│   │   └── ShortcutNames.swift        # Shortcut identifier constants
│   └── Persistence/
│       └── StateStore.swift           # JSON read/write to ~/.config/hairball/
├── Tests/HairballTests/               # 16 unit test files
│   ├── ContextManagerTests.swift, ContextPickerTests.swift
│   ├── CustomHeuristicsTests.swift, DataModelTests.swift
│   ├── HairballTests.swift, KeyboardShortcutTests.swift
│   ├── MenuBarUITests.swift, ReconcileUITests.swift
│   ├── SettingsTests.swift, StateStoreTests.swift
│   ├── WindowFingerprintTests.swift, WindowInfoTests.swift
│   ├── WindowManagerTests.swift, WindowManipulationTests.swift
│   ├── WindowObservationTests.swift, WindowReMatchingTests.swift
├── Roadmaps/
│   └── HairballV1-Roadmap.md          # 15-step roadmap, all steps complete
├── Hairball.xcodeproj/                # Xcode project
├── Package.swift                      # Swift Package Manager manifest
├── Package.resolved                   # Locked dependency versions
├── project.yml                        # Xcodegen project config
├── Info.plist                         # Bundle config (LSUIElement=true for menu bar app)
├── CLAUDE.md                          # Development notes & architecture
└── PLAN.md                            # Comprehensive design document
```

## Key Files & Components

### Core Mechanism: Off-Screen Window Parking
The only public-API method for per-window hiding on macOS:
1. **Deactivate context:** Save each window's position, move to x:-30000 via `AXUIElement.setPosition()`
2. **Activate context:** Restore each window to saved position, focus last-focused window
3. ~5ms per window, ~50ms for 10 windows. Imperceptible. Proven by FlashSpace.

### ContextManager.swift -- The Brain
Orchestrates context switching, window parking/restore, state persistence. Methods: createContext, deleteContext, addWindow, removeWindow, switchContext. Persists state after every mutation.

### WindowMatcher.swift -- Re-Matching Engine
Scores running windows against context fingerprints after reboot. Scoring: app match (required) + title pattern match (80 pts exact, 60 pts substring) + display match (+10). Greedy one-to-one assignment. Auto-assigns at score >= 80. Ambiguous matches surface in Reconcile UI.

### Per-App Heuristics (5 built-in + custom)
| App | Extracts | Example |
|-----|----------|---------|
| Xcode | Project name | "QualityTime -- ContentView.swift" -> "QualityTime" |
| Warp | Directory/branch | "Claude - QualityTime (main) *" -> "QualityTime" |
| Brave | Page title | "Roadmap Dashboard - Brave" -> "Roadmap Dashboard" |
| VS Code | Workspace | "temporal -- api.go" -> "temporal" |
| Terminal | Working dir | "~/projects/temporal" -> "temporal" |

### Keyboard Shortcuts (all user-configurable)
- ctrl+opt+1-9: Switch to context by index
- ctrl+opt+A: Add focused window to active context
- ctrl+opt+X: Remove focused window from context
- ctrl+opt+N/P: Next/previous context
- ctrl+opt+Space: Context picker popup (search + select)

### State Persistence
Location: `~/.config/hairball/` (state.json, contexts/*.json, heuristics.json). JSON with Codable. Survives app restarts and system reboots.

### Window Observation
Subscribes to AX notifications (window created/destroyed/title changed) and NSWorkspace events (app launched/terminated). Auto-tracks new windows, marks closed windows as dormant, re-matches on app relaunch.

## Claude Configuration

**CLAUDE.md** (root): Brief tech notes referencing PLAN.md for full architecture.

No `.claude/` directory with settings, rules, or skills. `.gitignore` excludes `.claude/worktrees/`.

## Planning & Research Documents

### PLAN.md (200+ lines)
Comprehensive implementation design document covering:
- Problem statement (macOS Spaces/Stage Manager are app-level, not window-level)
- Architecture with tech stack rationale
- Core mechanism design (off-screen parking)
- Component breakdown with data structures
- Context switching algorithm, window identity/matching strategy
- State persistence structure, UI specs, keyboard shortcuts
- Window observation via AX notifications
- 5-phase implementation plan
- Verification checklist

### Roadmaps/HairballV1-Roadmap.md
15-step feature roadmap. All 15 steps complete. Covers:
1. Project scaffold
2. Window enumeration
3. AXUIElement manipulation
4. Data models
5. State persistence
6. Context switching
7. Menu bar UI
8. Keyboard shortcuts
9. Window fingerprinting
10. Re-matching engine
11. Reconcile UI
12. Window observation
13. Settings window
14. Context visualization & picker
15. User-configurable heuristics

Extensive unit test coverage at each step (47 context manager tests, 48 fingerprint tests, 33 observation tests, 52 custom heuristic tests, etc.).

## Git History & Current State

**Branch:** `main`
**Working Tree:** Clean (no uncommitted changes)

**Recent Commits:**
```
814e3a3 (2026-04-06) feat: add AppState, WindowExplorer, WorkGroups views and refactor app structure
4273eec (2026-04-06) chore: standardize worktree directory to .claude/worktrees/
b8857de (2026-03-27) Update CLAUDE.md: litterbox -> agentic-cookbook
5ef2245 (2026-03-25) refactor: migrate 1 roadmaps to flat file format
fc0de7b (2026-03-25) Merge pull request #16 from feature/HairballV1
```

**Development History:** Feature branches with numbered PRs (#1-#16). All 15 roadmap steps implemented through PR-based workflow. Most recent work: AppState refactor, WindowExplorer view, WorkGroups view.

## Build & Test Commands

```bash
# Build
swift build
xcodebuild -scheme Hairball build

# Open in Xcode
open Hairball.xcodeproj
# or regenerate project:
xcodegen generate -s project.yml

# Run tests
swift test

# Build settings
# Scheme: Hairball
# Platform: macOS (arm64 + x86_64)
# Deployment Target: macOS 14.0
# Bundle ID: com.mikefullerton.Hairball
# Code Signing: Automatic
```

## Notes

1. **Permissions:** Only Accessibility permission required (System Settings > Privacy & Security > Accessibility). Prompted on first launch via `AXIsProcessTrustedWithOptions`. No SIP changes needed. LSUIElement=true (no dock icon).

2. **Recent Refactoring (Apr 6):** Introduced AppState for centralized state management. Added WindowExplorer (view all windows across contexts) and WorkGroups views. Added os.log logging throughout.

3. **Status:** Feature complete for v1.0. All 15 roadmap acceptance criteria implemented. Current focus: refinement -- AppState refactoring, WindowExplorer, WorkGroups exploration.

4. **Architecture Decisions:**
   - Off-screen parking via AXUIElement (only public-API option, proven by FlashSpace)
   - No SIP/yabai dependency (fragile, overkill)
   - JSON state files (human-readable, git-friendly)
   - KeyboardShortcuts library (well-maintained, SwiftUI-native)
   - MockWindowManager protocol for testable window manipulation

5. **Test Coverage:** 16 test files with hundreds of unit tests covering all major components: context management, window fingerprinting, re-matching, reconciliation, observation, custom heuristics, settings, keyboard shortcuts, data models.
