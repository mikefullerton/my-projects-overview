# QualityTime

## Project Summary

A cross-platform desktop, mobile, and web application built with Kotlin Multiplatform (KMP). Targets Apple (iOS, macOS, watchOS, tvOS, visionOS via SwiftUI), Android (Jetpack Compose), Windows (Compose Multiplatform), and Web (React + TypeScript). Backend is Ktor Server with PostgreSQL. Includes a full Claude-powered CI/CD pipeline with code review agents, fix agents, and merge gating via GitHub Actions. Early-stage project with scaffolding complete across all platforms.

## Type & Tech Stack

- **Type**: Cross-platform application (mobile, desktop, web)
- **Shared core**: Kotlin Multiplatform (KMP) -- business logic, persistence (SQLDelight), networking (Ktor Client)
- **Apple UI**: SwiftUI (iOS, macOS, watchOS, tvOS, visionOS)
- **Android UI**: Jetpack Compose
- **Windows UI**: Compose Multiplatform (desktop/JVM)
- **Web UI**: React + TypeScript
- **Backend**: Ktor Server + PostgreSQL (via Exposed ORM)
- **Database**: PostgreSQL 16 (Docker Compose), SQLDelight (client-side)
- **Build**: Gradle (Kotlin DSL), XcodeGen (Apple), npm (web)
- **CI/CD**: GitHub Actions with Claude-powered agent pipeline
- **Plugins**: kotlinMultiplatform, androidLibrary, androidApplication, composeCompiler, sqldelight, skie, ktorServer, composeMultiplatform, kotlinSerialization

## GitHub URL

`git@github.com:QualityTimeStudios/QualityTime.git`

## Directory Structure

```
QualityTime/
├── .claude/
│   ├── settings.local.json          # Permission allowlists
│   └── worktrees/                   # Git worktrees (untracked)
├── .github/
│   └── workflows/
│       ├── anthropic-review.yml     # Anthropic code review
│       ├── ci.yml                   # CI pipeline
│       ├── claude-fix.yml           # Claude fix agent
│       ├── claude-merge-check.yml   # Merge readiness check
│       └── claude-review.yml        # Claude code review
├── backend/
│   ├── build.gradle.kts             # Backend build config
│   └── src/                         # Ktor server source
├── clients/
│   ├── android/                     # Android app (Jetpack Compose)
│   ├── apple/                       # SwiftUI apps (all Apple platforms)
│   ├── web/                         # React + TypeScript frontend
│   └── windows/                     # Compose Multiplatform desktop app
├── shared/
│   ├── build.gradle.kts             # KMP shared module
│   └── src/
│       ├── commonMain/kotlin/       # Shared business logic
│       ├── commonTest/kotlin/       # Shared tests
│       ├── androidMain/kotlin/      # Android-specific implementations
│       ├── appleMain/kotlin/        # Shared Apple implementations
│       ├── iosMain/kotlin/          # iOS-specific implementations
│       ├── jvmMain/kotlin/          # JVM implementations
│       └── jsMain/kotlin/           # JS/WASM implementations
├── build.gradle.kts                  # Root build config (plugin declarations)
├── CLAUDE.md                         # Project conventions and commands
├── docker-compose.yml                # PostgreSQL 16 (dev)
├── gradle.properties                 # Gradle settings
├── gradlew / gradlew.bat            # Gradle wrapper
└── settings.gradle.kts               # Module includes (shared, backend, android, windows)
```

## Key Files & Components

- `CLAUDE.md` -- Comprehensive project overview covering tech stack, project structure, architecture conventions, coding standards, and build commands for all platforms
- `build.gradle.kts` -- Root Gradle build declaring all KMP plugins (kotlinMultiplatform, compose, sqldelight, skie, ktor, serialization)
- `settings.gradle.kts` -- Module includes: shared, backend, clients:android, clients:windows
- `docker-compose.yml` -- PostgreSQL 16-alpine dev database (qualitytime DB, port 5432)
- `shared/` -- KMP shared module with expect/actual pattern for platform-specific code
- `backend/` -- Ktor Server with PostgreSQL via Exposed
- `clients/apple/` -- SwiftUI apps for all Apple platforms (XcodeGen)
- `clients/android/` -- Jetpack Compose Android app (compileSdk 34, minSdk 26)
- `clients/windows/` -- Compose Multiplatform desktop app
- `clients/web/` -- React + TypeScript web client

## Claude Configuration

- `CLAUDE.md` -- Architecture conventions (shared-first KMP, native UI, backend shares models, ADRs), coding standards (Kotlin conventions, Swift API guidelines, strict TypeScript), full build/test commands for all platforms
- `.claude/settings.local.json` -- Permission allowlists for git operations
- `.github/workflows/` -- 5 workflow files: CI, Anthropic review, Claude review, Claude fix, merge check

## Planning & Research Documents

- `CLAUDE.md` -- Serves as both Claude configuration and architecture documentation
- Architecture Decision Records planned in `docs/decisions/` (directory structure defined but not populated)

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-03-12 -- "fix: make code reviews on-demand only, not automatic on PR open (#13)"
- **Working tree**: 1 untracked item (.claude/worktrees/)
- **Total commits**: 10
- **Recent activity**: CI/CD pipeline evolution (Mar 2026) -- switched from Python SDK to claude-code-action, added agent wrappers, added Anthropic code reviewer, made reviews on-demand
- **Key commits**: Initial setup, workflow additions (#1-#3), code review pipeline refinements (#10-#13)

## Build & Test Commands

```bash
# Shared module
./gradlew :shared:build
./gradlew :shared:allTests
./gradlew :shared:assembleSharedReleaseXCFramework

# Backend
docker compose up -d                          # Start PostgreSQL
./gradlew :backend:build
./gradlew :backend:run
./gradlew :backend:run -Pdevelopment          # Dev mode
./gradlew :backend:buildFatJar

# Android
./gradlew :clients:android:assembleDebug
./gradlew :clients:android:installDebug

# Windows
./gradlew :clients:windows:run
./gradlew :clients:windows:packageMsi

# Apple (requires Xcode)
cd clients/apple && xcodegen generate
open clients/apple/QualityTime.xcodeproj

# Web
cd clients/web && npm install && npm run dev
```

## Notes

- Project is paused -- scaffolding is complete across all platforms but feature development hasn't started
- Owned by "QualityTimeStudios" GitHub org (not mikefullerton personal)
- The CI/CD pipeline underwent significant evolution through PRs #1-#13, moving from Python SDK reviews to claude-code-action
- PostgreSQL dev database uses simple credentials (qualitytime/qualitytime) -- dev-only
- Prerequisites: JDK 17+, Docker, xcodegen, Android SDK
