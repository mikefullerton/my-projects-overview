# Agentic Toolkit

## Project Summary
A cross-platform toolkit for agentic development workflows with Swift implementations for Apple platforms (macOS, iOS, tvOS, watchOS). Provides reusable UI components and utilities for building agentic applications.

## Type & Tech Stack
- **Type**: Cross-platform toolkit library
- **Primary Stack**: Swift 6.0 (strict concurrency), Xcode project with XCGen
- **Platforms**: macOS 14+, iOS 17+, tvOS 17+, watchOS 10+ (Swift)
- **Secondary**: Android (TBD), Windows (TBD)
- **Modules**: 
  - `AgenticToolkit` — Foundation-only, cross-platform
  - `AgenticAppKit` — macOS AppKit UI
  - `AgenticUIKit` — iOS/tvOS UIKit (header files only, full support deferred)
- **Build System**: XCGen-generated Xcode project (was SPM, converted in recent commit)

## GitHub URL
https://github.com/agentic-cookbook/agentic-toolkit

## Directory Structure
```
.
├── apple/                      # Swift package & Xcode project
│   ├── Sources/
│   │   ├── AgenticToolkit/     # Core Foundation-only module
│   │   ├── AgenticAppKit/      # macOS AppKit components
│   │   └── AgenticUIKit/       # iOS/tvOS UIKit headers
│   ├── Tests/
│   │   ├── AgenticToolkitTests/
│   │   ├── AgenticAppKitTests/
│   │   └── AgenticUIKitTests/
│   ├── TestApp/                # Test application
│   ├── AgenticToolkit.xcodeproj/
│   └── project.yml             # XCGen configuration
├── android/                    # Placeholder, not yet implemented
├── windows/                    # Placeholder, not yet implemented
├── docs/
│   ├── planning/               # Planning documentation (TBD)
│   ├── project/                # Project description
│   └── toolkit-checklist.md    # Code review checklist for toolkit code
├── .claude/
│   ├── CLAUDE.md              # Architecture guide
│   ├── settings.json          # Claude Code configuration with graphify hook
│   └── worktrees/             # Active worktrees
├── graphify-out/              # Code knowledge graph output
└── README.md                  # Quick start guide
```

## Key Files & Components
- **apple/Sources/AgenticToolkit/** — Core modules (cross-platform logic)
- **apple/Sources/AgenticAppKit/** — macOS UI toolkit (AppKit only, no SwiftUI except widgets)
- **apple/Sources/AgenticUIKit/** — iOS/tvOS UI stubs
- **apple/project.yml** — XCGen project spec with Swift 6 strict concurrency
- **apple/TestApp/** — Integration test application
- **docs/toolkit-checklist.md** — 4-section code review checklist for toolkit standards
- **graphify-out/** — Knowledge graph for architecture questions

## Claude Configuration
- **CLAUDE.md**: Architecture overview, build commands, conventions
  - Specifies Swift 6.0, SPM root symlink, per-platform structure
  - Documents conventions: AppKit-only for macOS UI, PRs/worktrees required, no direct commits to main
  - References graphify knowledge graph (read GRAPH_REPORT.md before architecture questions)
  - Post-code-change: run graphify rebuild command to keep graph current
- **settings.json**: Superpowers plugin enabled, PreToolUse hook alerts about graphify

## Planning & Research Documents
- **docs/planning/planning.md** — TBD placeholder
- **docs/project/description.md** — Brief toolkit description
- **docs/toolkit-checklist.md** — Comprehensive 49-point checklist covering principles, Swift code standards, toolkit conventions, and client code expectations

## Git History & Current State
- **Remote**: git@github.com:agentic-cookbook/agentic-toolkit.git
- **Current Branch**: main (up to date with origin/main)
- **Working Tree**: Clean
- **Last 10 Commits**:
  1. ecd44cc — Move KeychainHelper into AgenticToolkit; add selectPanel to SettingsViewController (#10)
  2. 5bd4215 — Convert to Xcode project (no SPM) (#9)
  3. fce663a — Move chat UI classes from agentic-plugins into AgenticAppKit (#7)
  4. 9622540 — Round-two review fixes: polish + testability (#6)
  5. 210ec1b — Code review fixes: correctness, concurrency, duplication (#5)
  6. 52c356c — Remove plugin SDK and built-in plugins (#4)
  7. 3a70ac7 — Make plugin panels editable with model selector and authentication
  8. 346d416 — Fix plugins tab showing empty in settings
  9. 22d0b62 — Fix plugins not appearing in settings (discoverPlugins() overwriting built-ins)
  10. 9dd4035 — Swift 6 concurrency fixes for TestApp

## Build & Test Commands
```bash
cd apple && swift build
cd apple && swift test
xcodebuild -scheme AgenticToolkit build
xcodebuild -scheme AgenticAppKit build
xcodebuild -scheme AgenticUIKit build
```

## Notes
- **Recent conversion**: Switched from SPM to Xcode project in commit 5bd4215 to support iOS/tvOS TestApp builds
- **SPM compatibility**: Root `Package.swift` symlink maintained for remote SPM resolution (clients can still pull via SPM)
- **Multi-module architecture**: Clear layering (AppKit/UIKit depend on core Toolkit; Toolkit is Foundation-only)
- **Strict Swift 6**: Entire codebase runs with `SWIFT_STRICT_CONCURRENCY: complete`
- **No direct main commits**: All changes must go through PRs; worktrees stored in `.claude/worktrees/`
- **Graphify enabled**: Knowledge graph tracks architecture; rebuild after code changes
