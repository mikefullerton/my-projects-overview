# Catnip Terminal

## Project Summary

Catnip Terminal is a native macOS terminal emulator built with SwiftUI/AppKit and Swift, featuring AI-powered session summarization that automatically tracks what the user is doing in each terminal session. Supports multiple AI providers (Claude, OpenAI, Google Gemini) and customizable terminal profiles.

## Type & Tech Stack

- **Project Type:** Native macOS GUI Application
- **Language:** Swift 5.0
- **UI:** SwiftUI + Native AppKit (hybrid, AppKit conversion in progress via worktree)
- **Terminal Emulation:** SwiftTerm v1.2.0+
- **Project Tool:** XcodeGen (`project.yml`)
- **IDE:** Xcode 16.0
- **Deployment Target:** macOS 14.0 (Sonoma)
- **Bundle ID:** com.catnip.CatnipTerminal v1.0.0
- **Category:** Developer Tools

## GitHub URL

`git@github.com:mikefullerton/catnip-terminal.git`

## Directory Structure

```
catnip-terminal/
├── .claude/
│   ├── settings.local.json          # Permissions: git commit/push, gh pr, lint-skill
│   └── worktrees/
│       └── appkit-conversion/       # Full AppKit rewrite worktree (in progress)
├── CatnipTerminal/                   # 21 Swift source files
│   ├── CatnipTerminalApp.swift       # SwiftUI @main entry point
│   ├── AppDelegate.swift             # App lifecycle
│   ├── ContentView.swift             # Main window: split view (session list + terminal)
│   ├── TerminalViewRepresentable.swift # SwiftUI wrapper for SwiftTerm
│   ├── SessionManager.swift          # Multi-session lifecycle, coordinates summarization
│   ├── TerminalSession.swift         # Single PTY session, OSC escape handling
│   ├── SessionSummarizer.swift       # AI-powered session title generation
│   ├── SummarizationCoordinator.swift # Orchestrates when summarization runs
│   ├── AIProvider.swift              # Multi-provider: Anthropic, OpenAI, Google, Custom
│   ├── AIRequestBuilder.swift        # HTTP request building for AI APIs
│   ├── AISettingsView.swift          # AI configuration UI
│   ├── TerminalProfile.swift         # Color palettes, cursor styles, fonts
│   ├── ProfilesSettingsView.swift    # Terminal profile management
│   ├── SettingsView.swift            # Settings window (General, Profiles, AI tabs)
│   ├── GeneralSettingsView.swift     # General preferences
│   ├── KeychainHelper.swift          # Secure API key storage
│   ├── Logging.swift                 # Unified os.log subsystems
│   ├── SessionLayoutState.swift      # Layout persistence
│   ├── SessionListView.swift         # Session list sidebar
│   ├── SettingsKeys.swift            # UserDefaults constants
│   └── WindowAccessor.swift          # Window frame persistence
├── CatnipTerminal.xcodeproj/
├── CLAUDE.md                         # Minimal project marker
└── project.yml                       # XcodeGen configuration
```

## Key Files & Components

**AI Session Summarization:**
- `SessionSummarizer.swift` -- Reads scrollback buffer, queries AI provider for short summary
- `SummarizationCoordinator.swift` -- Orchestrates when summarization runs; detects topic changes
- `AIProvider.swift` -- Multi-provider support: Claude (Haiku/Sonnet/Opus), OpenAI (GPT-4), Google (Gemini), Custom
- `AIRequestBuilder.swift` -- Builds HTTP requests for each AI provider's API
- Debounced 5s on directory/process change, periodic 60s refresh
- Min: 5 lines/100 chars. Max output: 32 tokens. Timeout: 60s

**Terminal Features:**
- `TerminalViewRepresentable.swift` -- SwiftUI wrapper for SwiftTerm library
- `TerminalSession.swift` -- PTY management, spawns actual shell processes, OSC escape support (OSC 7: working dir, OSC 2: title)
- `SessionManager.swift` -- Multi-session lifecycle management
- `TerminalProfile.swift` -- Customizable color palettes, fonts, cursor styles

**Settings:**
- `SettingsView.swift` -- Sidebar navigation layout with General, Profiles, AI tabs
- `KeychainHelper.swift` -- Secure API key storage in macOS Keychain

## Claude Configuration

- **`CLAUDE.md`** -- Minimal (just project name)
- **`.claude/settings.local.json`** -- Permissions for git commit, push, lint-skill skill, and gh pr commands
- Active worktree at `.claude/worktrees/appkit-conversion/` for SwiftUI-to-AppKit port

## Planning & Research Documents

None found in the repository.

## Git History & Current State

- **Branch:** `feature/ai-session-summarization` (not on main)
- **Total commits:** 7
- **Working tree:** Clean
- **Recent activity (2026-04-06):** Add CLAUDE.md, standardize worktree directory

Recent commits:
```
d3bb5de chore: add CLAUDE.md
50cdef8 chore: standardize worktree directory to .claude/worktrees/
a634235 feat: AI-powered session summarization with multi-provider support
35505c0 fix: remove sidebar toggle button from settings window
714ce30 refactor: switch settings to sidebar layout per litterbox spec
5de22f2 fix: apply litterbox specs for window frame persistence and titles
26a612e feat: initial Catnip Terminal project
```

## Build & Test Commands

```bash
# Build via Xcode
xcodebuild -project CatnipTerminal.xcodeproj -scheme CatnipTerminal -configuration Debug build
xcodebuild -project CatnipTerminal.xcodeproj -scheme CatnipTerminal -configuration Release build

# Generate project from project.yml (requires XcodeGen)
xcodegen generate

# Open in Xcode
open CatnipTerminal.xcodeproj
```

No test suite configured yet. ~2500 lines of Swift source code.

## Notes

- Currently on `feature/ai-session-summarization` branch -- not yet merged to main
- AppKit conversion is in progress via a worktree at `.claude/worktrees/appkit-conversion/` containing a full rewrite of all SwiftUI views to AppKit (TerminalWindowController, SettingsWindowController, SessionListViewController, etc.)
- Uses SwiftTerm (external package from Miguel de Icaza) for terminal emulation
- AI summarization supports multiple providers through an abstraction layer
- Settings follow a "litterbox spec" for sidebar layout, window frame persistence, and titles
- Product name: "Catnip Terminal"
- Recommended AI provider for summarization: Haiku 4.5 (~$0.80/M tokens)
