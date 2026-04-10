# Search Helper

## Project Summary

A native macOS application for managing and automating web searches with customizable search terms, database persistence, and Finder integration. Provides a desktop client (BrowsingPal) with global hotkey shortcuts for quick searches, browser-specific routing, and a Finder Sync extension for right-click access. Designed to streamline research workflows and URL management.

## Type & Tech Stack

**Project Type:** Native macOS application suite (main app + Finder extension)

**Core Technologies:**
- **Swift** — Native application code
- **SwiftUI** — Modern UI framework
- **Xcode** — Project generation via xcodegen
- **project.yml** — XcodeGen configuration for project structure
- **SQLite/GRDB** — Persistent database for search terms
- **KeyboardShortcuts** — Global hotkey management
- **Finder Sync Framework** — Right-click context menu integration
- **AppKit** — Native macOS features

**Architecture:**
- Main BrowsingPal application for search management
- Finder Sync extension for context menu integration
- SearchTermsApp for configuration UI
- SQLite backend for search term and URL tracking
- Global hotkey support for quick access

## GitHub URL

`git@github.com:mikefullerton/search-helper.git`

https://github.com/mikefullerton/search-helper

## Directory Structure

```
search-helper/
├── .github/                             # GitHub Actions CI/CD workflows
├── docs/                                # Documentation
├── SearchHelper/                        # Finder extension source
│   └── [FinderSync implementation]
├── SearchHelper.xcodeproj/              # Generated Xcode project
├── SearchHelperFinder/                  # Finder extension bundle
│   └── [FinderSync extension]
├── SearchTermsApp/                      # Main BrowsingPal application
│   ├── main.swift                       # Entry point
│   ├── [UI views and models]
│   ├── SearchTermsApp.entitlements      # App sandboxing/permissions
│   └── Info.plist                       # App manifest
├── project.yml                          # XcodeGen project definition
├── .gitignore
└── README.md
```

## Key Files & Components

**Project Configuration:**
- `project.yml` — XcodeGen configuration defining all targets, settings, and dependencies

**Main Application (BrowsingPal):**
- `SearchTermsApp/` — Main application source code
- Global hotkey for quick search access
- Search term entry and editing UI
- Links tracker window for URL management
- Browser selection and routing
- Deep linking support via `browsingpal://` URL scheme

**Finder Extension:**
- `SearchHelper/` — FinderSync extension implementation
- Right-click context menu in Finder
- Integrated search workflow

**Database:**
- SQLite backend via GRDB for:
  - Search term storage
  - Hotkey/browser mapping
  - URL history and tracking

**Configuration:**
- `SearchTermsApp.entitlements` — Sandbox permissions for hotkeys and file access
- Settings tabs for behavior customization
- Browser selection configuration

## Claude Configuration

**CI/CD:**
- `.github/` — GitHub Actions workflows for code review and testing
- Automated code signing configuration

## Planning & Research Documents

**Documentation:**
- `docs/` — Design documentation and usage guides

**Feature Development:**
- No dedicated planning directory found
- Features tracked via GitHub issues

## Git History & Current State

**Recent Activity:**
- `084634a` chore: standardize worktree directory to .claude/worktrees/
- `c99e7a2` Add deep linking URL scheme (browsingpal://)
- `3331cc9` Add Links Tracker window for saving/browsing URLs
- `c88fb95` Move search terms into Settings tabs
- `da1ea57` Add browser switch setting, autocomplete, history editing
- `955f6b5` Improve Search Builder UX: hotkey, autocomplete, history
- `f7509a4` Add explicit code signing settings
- `56e693c` Add SQLite database via GRDB
- `47b85df` Rename app to BrowsingPal, pin input, remember window
- `da8756f` Disable app sandbox to allow global hotkey
- `d71429d` Enable automatic code signing
- `d1ac95f` Track generated Xcode project in version control
- `93bbef6` Add global hotkey, search/filter, sorting, space-prepend
- `dc842dc` Add code review pipeline workflows
- `64c9f62` Add term entry and edit/delete to SearchTermsApp

**Pattern:** Active development with features for search management, browser integration, and Finder extension.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Generate Xcode Project:**
```bash
xcodegen generate
```

**Build:**
```bash
xcodebuild -project SearchHelper.xcodeproj -scheme SearchTermsApp build
```

**Open in Xcode:**
```bash
open SearchHelper.xcodeproj
```

**Run:**
```bash
xcodebuild -project SearchHelper.xcodeproj -scheme SearchTermsApp run
```

## Notes

**Architecture Highlights:**

1. **XcodeGen Project Generation** — project.yml defines all targets and configuration
2. **Multi-Target Structure** — Main app, Finder extension, and search terms app
3. **SQLite Persistence** — GRDB backend for search terms, hotkeys, and history
4. **Global Hotkey Integration** — KeyboardShortcuts framework for system-wide shortcuts
5. **Finder Integration** — FinderSync extension for right-click workflows
6. **Deep Linking** — Custom browsingpal:// URL scheme for automation

**Key Features:**

- **Global Hotkey** — Quick access from anywhere on system
- **Search Term Management** — Entry, editing, deletion with persistence
- **Browser Routing** — Configure preferred browsers for searches
- **Links Tracker** — Save and manage research URLs
- **Finder Context Menu** — Right-click access in Finder
- **URL Autocomplete** — Smart suggestions from history
- **Settings Tabs** — Organized configuration UI
- **Keyboard Shortcuts** — Customizable hotkey binding

**Permissions Model:**

- Code signing via automatic certificate management
- Sandbox entitlements for macOS security
- Global hotkey monitoring (requires accessibility permission)

**Development Workflow:**

- XcodeGen-based project management for maintainability
- Automatic code signing in GitHub Actions
- Code review pipeline configured via GitHub Actions
- Feature branches for development

**User Experience:**

The application streamlines research and URL management through:
- Quick hotkey access for searches
- Browser-specific search routing
- Native Finder integration
- Persistent URL/search history
- Keyboard-driven workflow
