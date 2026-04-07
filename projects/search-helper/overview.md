# search-helper

## Project Summary

A macOS application suite for browsing assistance, originally named SearchHelper and later renamed to BrowsingPal. Features include a search builder with autocomplete and history, a links tracker for saving and browsing URLs, a global hotkey for quick access, browser switch settings, and a Finder extension (SearchHelperFinder). Built with SwiftUI/AppKit for macOS 14+, using SQLite (via GRDB) for persistence and KeyboardShortcuts for global hotkeys. Includes a deep linking URL scheme (`browsingpal://`).

## Type & Tech Stack

- **Type**: macOS application (menu bar / utility)
- **Language**: Swift
- **Platform**: macOS 14.0+
- **UI**: SwiftUI + AppKit
- **Storage**: SQLite via GRDB.swift
- **Hotkeys**: KeyboardShortcuts (sindresorhus)
- **Build**: XcodeGen (project.yml) + Xcode
- **Code signing**: Automatic (Team K2NA732JAX)
- **CI/CD**: GitHub Actions workflows

## GitHub URL

`git@github.com:mikefullerton/search-helper.git`

## Directory Structure

```
search-helper/
├── .github/
│   └── workflows/                    # CI/CD workflows
├── docs/
│   ├── architecture.md              # Architecture documentation
│   ├── decisions.md                 # Decision records
│   └── testing.md                   # Testing guide
├── SearchHelper/
│   ├── SearchHelper.entitlements    # App entitlements (sandbox disabled)
│   └── (source files)              # Main app target
├── SearchHelperFinder/              # Finder extension target
├── SearchTermsApp/
│   ├── AppDelegate.swift            # App entry point
│   ├── BrowserActivator.swift       # Browser switching logic
│   ├── DatabaseManager.swift        # GRDB SQLite manager
│   ├── HotkeyNames.swift           # Global hotkey definitions
│   ├── Link.swift                   # Link model
│   ├── LinkPreviewFetcher.swift     # URL preview fetching
│   ├── LinksView.swift             # Links tracker UI
│   ├── Models.swift                 # Data models
│   ├── SearchBuilderView.swift      # Search builder UI
│   ├── SearchTermsApp.swift         # App lifecycle
│   ├── SearchTermsApp.entitlements  # Entitlements
│   ├── SearchTokenizer.swift        # Search term tokenization
│   └── SettingsView.swift           # Settings UI
├── SearchHelper.xcodeproj/          # Generated Xcode project
├── project.yml                      # XcodeGen project definition
└── .gitignore
```

## Key Files & Components

- `project.yml` -- XcodeGen project definition: macOS 14.0 deployment target, GRDB and KeyboardShortcuts dependencies, automatic code signing
- `SearchTermsApp/DatabaseManager.swift` -- GRDB-based SQLite database for search terms and links
- `SearchTermsApp/SearchBuilderView.swift` -- Search builder with autocomplete and history
- `SearchTermsApp/LinksView.swift` -- Links tracker window for saving and browsing URLs
- `SearchTermsApp/BrowserActivator.swift` -- Browser switching and activation logic
- `SearchTermsApp/SettingsView.swift` -- Settings with search terms in tabs
- `docs/architecture.md` -- Architecture documentation
- `docs/decisions.md` -- Architectural decision records
- `docs/testing.md` -- Testing guide

## Claude Configuration

- No CLAUDE.md or `.claude/` settings found in the repository
- GitHub Actions workflows present in `.github/workflows/`

## Planning & Research Documents

- `docs/architecture.md` -- Architecture documentation
- `docs/decisions.md` -- Decision records
- `docs/testing.md` -- Testing documentation

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: standardize worktree directory to .claude/worktrees/"
- **Working tree**: Clean
- **Total commits**: 15+ (viewed)
- **Recent activity**: Deep linking URL scheme (Feb 2026), links tracker, search term UX improvements, worktree standardization (Apr 2026)
- **Key features added**: SQLite via GRDB (#7), search builder (#7), global hotkey (#4), browser switch (#10), links tracker (#11), deep linking (#13), BrowsingPal rename (#6)

## Build & Test Commands

```bash
# Generate Xcode project
xcodegen generate

# Open in Xcode
open SearchHelper.xcodeproj

# Build (via Xcode or xcodebuild)
xcodebuild -scheme SearchHelper -configuration Debug build
```

## Notes

- App was renamed from SearchHelper to BrowsingPal (PR #6) but the repo/project is still named search-helper
- App sandbox is disabled to allow global hotkey monitoring
- The SearchHelperFinder target is a Finder extension (separate from the main app)
- Deep linking via `browsingpal://` URL scheme
- Project is paused but feature-rich with 13+ PRs of development
