# Catnip Terminal

## Project Summary

Catnip Terminal is a native macOS terminal emulator built with SwiftUI/AppKit and Swift, featuring AI-powered session summarization that automatically tracks what the user is doing in each terminal session.

## Type & Tech Stack

- **Project Type:** Native macOS GUI Application
- **Language:** Swift 5.0
- **UI:** SwiftUI + Native AppKit (hybrid, recently converted from full SwiftUI)
- **Terminal Emulation:** SwiftTerm v1.12.0
- **Dependencies:** SwiftTerm, swift-argument-parser v1.7.1
- **Deployment Target:** macOS 14.0 (Sonoma)
- **Bundle ID:** com.catnip.CatnipTerminal v1.0.0

## GitHub URL

`git@github.com:mikefullerton/catnip-terminal.git`

## Directory Structure

```
catnip-terminal/
├── .claude/
│   ├── settings.local.json          # Permissions: git commit/push, gh pr, lint-skill
│   └── worktrees/appkit-conversion/
├── CatnipTerminal/                   # 21 Swift source files
│   ├── CatnipTerminalApp.swift       # SwiftUI @main entry point
│   ├── AppDelegate.swift             # App lifecycle
│   ├── ContentView.swift             # Main window: split view (session list + terminal)
│   ├── SessionManager.swift          # Multi-session lifecycle, coordinates summarization
│   ├── TerminalSession.swift         # Single PTY session, OSC escape handling
│   ├── TerminalViewRepresentable.swift # SwiftUI wrapper for SwiftTerm
│   ├── SessionSummarizer.swift       # AI-powered session title generation
│   ├── SummarizationCoordinator.swift # Orchestrates when summarization runs
│   ├── AIProvider.swift              # Multi-provider: Anthropic, OpenAI, Google, Custom
│   ├── AIRequestBuilder.swift        # HTTP request building for AI APIs
│   ├── AISettingsView.swift          # AI configuration UI
│   ├── TerminalProfile.swift         # Color palettes, cursor styles, fonts
│   ├── ProfilesSettingsView.swift    # Terminal profile management
│   ├── SettingsView.swift            # Settings window (General, Profiles, AI tabs)
│   ├── GeneralSettingsView.swift
│   ├── KeychainHelper.swift          # Secure API key storage
│   ├── Logging.swift                 # Unified os.log subsystems
│   ├── SessionLayoutState.swift      # Layout persistence
│   ├── SessionListView.swift         # Session list sidebar
│   ├── SettingsKeys.swift            # UserDefaults constants
│   └── WindowAccessor.swift          # Window frame persistence
├── CatnipTerminal.xcodeproj/
├── CLAUDE.md
└── project.yml                       # XcodeGen configuration
```

## Key Components

**AI Session Summarization:**
- Reads scrollback buffer, queries AI provider for short summary
- Detects topic changes (UNCHANGED vs new summary)
- Multi-provider: Claude (Haiku/Sonnet/Opus), OpenAI (GPT-4), Google (Gemini)
- Debounced 5s on directory/process change, periodic 60s refresh
- Min: 5 lines/100 chars. Max output: 32 tokens. Timeout: 60s
- Recommended: Haiku 4.5 (~$0.80/M tokens)

**Terminal Features:**
- Split-view layout (sidebar sessions + terminal)
- Multi-window with independent session lists
- PTY management spawning actual shell processes
- OSC escape sequence support (OSC 7: working dir, OSC 2: title, OSC 7770: custom)
- Customizable profiles with color palettes, fonts, cursor styles

## Claude Configuration

- Permissions: git commit/push, gh pr, lint-skill
- Worktrees for feature branches

## Git History & Current State

- **Branch:** feature/ai-session-summarization (1 commit ahead)
- **Working tree:** Clean
- **Recent (2026-04-06):** Add CLAUDE.md, standardize worktree directory
- **Key milestones:** Initial project, full AppKit conversion, AI session summarization

## Build & Test Commands

```bash
xcodebuild -scheme CatnipTerminal -configuration Debug
xcodebuild -scheme CatnipTerminal -configuration Release
open CatnipTerminal.xcodeproj
```

No test suite configured yet. ~2500 lines of Swift source code.
