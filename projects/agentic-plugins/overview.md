# Agentic Plugins

## Project Summary
A framework for building and distributing LLM provider plugins across agentic tools and workflows. Built with Swift/AppKit, it provides a plugin SDK, built-in plugins for major LLM providers, and reusable UI components.

## Type & Tech Stack
- Language: Swift 5.9+
- Platform: macOS 14+
- UI Framework: AppKit (no SwiftUI)
- Build System: Swift Package Manager + Xcode
- Project Type: Plugin framework + SDK

## GitHub URL
https://github.com/agentic-cookbook/agentic-plugins

## Directory Structure
```
agentic-plugins/
├── Apple/                        # Xcode projects and Swift sources
│   ├── AgenticPlugins.xcworkspace
│   ├── Plugins/                 # 5 built-in plugin implementations
│   │   ├── ClaudeAPIPlugin
│   │   ├── ClaudeLocalPlugin
│   │   ├── GooglePlugin
│   │   ├── OpenAIPlugin
│   │   ├── OpenAICompatiblePlugin
│   │   └── Tests/
│   ├── PluginSDK/              # Core SDK library
│   │   ├── Source/             # WhippetLLMPlugin protocol, PluginManager
│   │   └── Tests/
│   └── TestApp/                # Standalone test application
├── Sources/
│   └── AgenticUI/              # Reusable AppKit chat and settings views
├── TestApp/                    # Test application workspace
├── agentic-toolkit/            # Git submodule (AgenticAppKit)
├── docs/
│   ├── planning/               # Planning documents
│   └── project/                # Project description
├── .claude/
│   ├── CLAUDE.md               # Architecture and conventions
│   └── settings.json           # Claude Code configuration
├── graphify-out/               # Knowledge graph output
├── README.md
└── .gitmodules
```

## Key Files & Components
- **Apple/PluginSDK/Source** — Core `WhippetLLMPlugin` protocol and `PluginManager` for plugin discovery and registration
- **Apple/Plugins/** — Five built-in LLM provider plugins (Anthropic, OpenAI, Google, Claude CLI, OpenAI-compatible)
- **Sources/AgenticUI/** — Reusable AppKit components for chat UI and settings panels
- **Apple/TestApp/** — Standalone macOS application (AgenticPluginTester) for testing plugins
- **agentic-toolkit** — Submodule containing AgenticAppKit shared components

## Claude Configuration
- **CLAUDE.md** — Detailed architecture notes, build commands, and conventions
- **settings.json** — Enabled superpowers plugin, includes graphify hooks for PreToolUse
- **graphify-out/** — Knowledge graph for architecture reference (GRAPH_REPORT.md available)

## Planning & Research Documents
- **docs/planning/planning.md** — To be determined
- **docs/project/description.md** — Brief project description

## Git History & Current State
- **Remote:** origin https://github.com/agentic-cookbook/agentic-plugins.git
- **Current Branch:** main
- **Status:** Clean (no uncommitted changes)
- **Last 10 Commits:**
  1. 5941c3d — Restore AI Chat window with a stub backend (#12)
  2. 126bdfe — Flip AgenticLLMPlugin to settingsPanelViewController() (#10)
  3. b6c23f2 — Bump agentic-toolkit submodule to latest main (#11)
  4. 51dade2 — Reorganize: Sources/Plugins/<Name>/ per-plugin directories (#9)
  5. d8de685 — Move chat UI into toolkit (AgenticAppKit) (#8)
  6. cf7c2e9 — Cookbook review: fix force-unwraps, narrow API surface (#7)
  7. 623ecd3 — Pick up round-two toolkit fixes + PluginChatBackend multicast (#5)
  8. b6028e1 — Pick up toolkit review fixes (#4)
  9. a19d4ef — Add agentic-toolkit submodule (#3)
  10. c877d20 — chore: merge graphify section into .claude/CLAUDE.md, remove root CLAUDE.md

## Build & Test Commands
```bash
swift build
swift test
```

## Notes
- Plugin architecture supports both built-in plugins (registered via `PluginManager.registerBuiltIns()`) and external plugins as `.bundle` files
- All UI must be AppKit; SwiftUI is not permitted
- Project includes graphify knowledge graph; run `python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` to keep graph current after code modifications
- Active development with regular integration of agentic-toolkit updates
