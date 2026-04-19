# Agentic Daemon

## Project Summary

A macOS user-space daemon that watches a jobs directory for Swift scripts, auto-compiles them, and runs them on configurable schedules. Drop a Swift script into the jobs directory and it compiles and runs automatically. The daemon is managed by launchd, starts at login, and keeps itself alive. Useful for automating recurring tasks written in Swift without manual build steps.

## Type & Tech Stack

**Type:** System Daemon / Task Scheduler

**Tech Stack:**
- **Language:** Swift 6, strict concurrency
- **Platform:** macOS 14+
- **Bundle ID:** `com.agentic-cookbook.daemon`
- **Process Management:** launchd (`com.agentic-cookbook.daemon.plist`)
- **Logging:** os.log (subsystem: `com.agentic-cookbook.daemon`)
- **Testing:** Swift XCTest, Python e2e tests

## GitHub URL

https://github.com/agentic-cookbook/agenticdaemon

## Directory Structure

```
.
├── .claude/              # Claude Code configuration
│   ├── CLAUDE.md
│   └── worktrees/
├── AgenticDaemon/        # Swift package
│   ├── Package.swift
│   ├── Sources/
│   │   ├── main.swift                 # Entry point, signal handling
│   │   ├── DaemonController.swift      # Wires watcher + scheduler
│   │   ├── DirectoryWatcher.swift      # DispatchSource file system watcher
│   │   ├── JobDiscovery.swift          # Scans jobs/, reads config.json
│   │   ├── SwiftCompiler.swift         # Compiles .swift to .job-bin
│   │   ├── Scheduler.swift             # Timer loop, per-job scheduling
│   │   ├── Models/
│   │   │   ├── JobConfig.swift         # Codable config struct
│   │   │   └── JobDescriptor.swift     # Job metadata struct
│   │   ├── AgenticJobKit/              # Plugin calling convention module
│   │   ├── CrashTracker.swift          # Plugin crash detection
│   │   ├── JobLoader.swift             # @objc protocol bridge
│   │   ├── CrashReporter.swift         # PLCrashReporter integration
│   │   ├── StatusWriter.swift          # Daemon observability
│   │   ├── Scheduler.swift             # Actor with async/await
│   │   └── (more components)
│   └── Tests/
│       ├── SchedulerTests.swift
│       ├── JobConfigTests.swift
│       ├── BackoffTests.swift
│       ├── CrashTrackerTests.swift
│       ├── (more test files)
│       └── TestHelpers.swift
├── tests/
│   └── e2e.py            # End-to-end test harness
├── docs/
│   ├── research/
│   │   └── launchd-research.md
│   └── project/
│       └── description.md
├── install.sh            # Build, install binary + plist, start daemon
├── uninstall.sh          # Stop daemon, remove binary + plist
├── README.md
├── com.agentic-cookbook.daemon.plist  # launchd plist
└── .gitignore
```

## Key Files & Components

**Core Components:**
- `main.swift` — Entry point with signal handling
- `DaemonController.swift` — Orchestrates watcher and scheduler
- `DirectoryWatcher.swift` — File system monitoring with debounce
- `JobDiscovery.swift` — Job directory scanning and config parsing
- `SwiftCompiler.swift` — Swift source compilation with mtime caching
- `Scheduler.swift` — Actor-based async/await timer loop and job scheduling
- `StatusWriter.swift` — Observability and status reporting

**Plugin Architecture:**
- `AgenticJobKit/` — Module with plugin calling convention
- `JobLoader.swift` — Dynamic job loading with @objc protocol bridge
- `CrashTracker.swift` — Plugin crash detection and blacklisting

**Crash Reporting:**
- `CrashReporter.swift` — PLCrashReporter integration
- `CrashReportCollector.swift` — Collection and reporting utilities

**Configuration:**
- `com.agentic-cookbook.daemon.plist` — launchd property list
- `Package.swift` — Swift package configuration

**Testing:**
- Comprehensive XCTest suite (12+ test files)
- `e2e.py` — Python-based end-to-end test harness

## Claude Configuration

**Location:** `.claude/CLAUDE.md`

Contains quick reference including:
- Build commands (swift build, swift build -c release)
- Project structure and language details
- Platform target (macOS 14+) and bundle ID
- Logging configuration (os.log subsystem)
- Installation and testing procedures
- Architecture overview with per-file responsibilities

## Planning & Research Documents

**Research:**
- `docs/research/launchd-research.md` — launchd integration research

**Project Documentation:**
- `docs/project/description.md` — Project purpose, key features, tech stack, and status

## Git History & Current State

**Current Branch:** main

**Remote:** git@github.com:agentic-cookbook/agenticdaemon.git

**Recent Commits:**
- `5e239f6` — Add crash reporting: PLCrashReporter + DiagnosticReports (#1)
- `5fbde65` — docs: add standardized project description
- `cae015f` — Update E2E test for plugin architecture
- `d33b948` — Update install.sh for plugin architecture, remove JobRunner
- `09d8069` — Rewrite Scheduler for in-process plugin architecture
- `dda928e` — Add CrashTracker for plugin crash detection and blacklisting
- `8e8e4f4` — Add in-process JobLoader with @objc protocol bridge
- `f6410aa` — Update SwiftCompiler to emit dylibs linking against AgenticJobKit
- `8dea31b` — Add AgenticJobKit module with plugin calling convention
- (15 more commits showing active development of scheduler, analytics, crash handling, etc.)

**Status:** Active development.

## Build & Test Commands

```bash
# Build the daemon
cd AgenticDaemon
swift build              # Debug build
swift build -c release   # Release build (optimized)

# Install and manage the daemon
./install.sh             # Build, install binary to ~/Library/Application Support/, install launchd plist
./uninstall.sh           # Stop daemon, remove binary and plist

# Run tests
cd AgenticDaemon
swift test               # Run Swift XCTest suite

# End-to-end testing
python tests/e2e.py      # Run Python-based end-to-end tests

# Monitor logs
log stream --predicate 'subsystem == "com.agentic-cookbook.daemon"'
log stream --predicate 'subsystem == "com.agentic-cookbook.daemon" AND category == "Scheduler"'
```

## Notes

- No UI — headless daemon with no SwiftUI or AppKit
- Uses Swift 6 with strict concurrency for thread safety
- Scheduler implemented as an actor using async/await
- File system watcher uses DispatchSource with debouncing
- Jobs stored in ~/Library/Application Support/com.agentic-cookbook.daemon/jobs/
- Each job is a directory containing job.swift and optional config.json
- Compiled jobs are cached as .job-bin with mtime-based invalidation
- Configuration per job: intervalSeconds, enabled, timeout, runAtWake, backoffOnFailure
- Exponential backoff on consecutive job failures
- Crash detection and reporting via PLCrashReporter
- In-process plugin architecture with AgenticJobKit module
- Logs via os.log (subsystem, categories for each component)
- Stdout/stderr also written to ~/Library/Logs/com.agentic-cookbook.daemon/
- Integrated with macOS launchd for auto-start at login and keep-alive
