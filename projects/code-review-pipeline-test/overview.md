# code-review-pipeline-test

## Project Summary

A test project for exercising the AI-powered code review pipeline defined in the `workflows` repo (Shared-Project-Helpers/workflows). Uses eight Claude-based agents to automate PR review, fixing, test generation, and merge gating via GitHub Actions. The project itself is a Kotlin Multiplatform (KMP) application scaffolded across all target platforms (Apple/SwiftUI, Android/Jetpack Compose, Windows/Compose Multiplatform, Web/Kotlin JS) to provide realistic code for the review pipeline to analyze.

## Type & Tech Stack

- **Type**: Test project / CI/CD pipeline validation
- **Shared core**: Kotlin Multiplatform (KMP)
- **Build**: Gradle (Kotlin DSL)
- **Clients**: Android (Jetpack Compose), Apple (SwiftUI via XcodeGen), Windows (Compose Multiplatform), Web (Kotlin/JS)
- **CI/CD**: GitHub Actions with 8 Claude-powered agent workflows
- **Frameworks**: Compose Multiplatform, Ktor, kotlinx.serialization

## GitHub URL

`git@github.com:Shared-Project-Helpers/code-review-pipeline-test.git`

## Directory Structure

```
code-review-pipeline-test/
├── .github/
│   └── workflows/
│       ├── anthropic-review.yml            # Anthropic code review
│       ├── claude-combined-review.yml      # Combined perf/safety/test
│       ├── claude-fix.yml                  # Fix agent
│       ├── claude-issue-fix.yml            # Issue fix agent
│       ├── claude-merge-check.yml          # Merge readiness check
│       ├── claude-review.yml               # General code review
│       └── claude-test-runner.yml          # Test runner
├── clients/
│   ├── android/                            # Android client
│   ├── apple/                              # SwiftUI client (all Apple platforms)
│   ├── web/                                # Kotlin/JS web client
│   └── windows/                            # Compose Multiplatform desktop
├── shared/                                 # KMP shared module
├── kotlin-js-store/                        # Kotlin JS artifacts
├── gradle/                                 # Gradle wrapper
├── build.gradle.kts                        # Root build config
├── CLAUDE.md                               # Project documentation
├── README.md                               # Pipeline docs and agent roster
├── settings.gradle.kts                     # Module includes
├── gradlew / gradlew.bat                   # Gradle wrapper scripts
└── .gitignore
```

## Key Files & Components

- `CLAUDE.md` -- Comprehensive documentation: purpose (pipeline test project), project structure, pipeline architecture with 8 agents, pipeline flow diagram, related repos, current status
- `README.md` -- Agent pipeline documentation: reviewer agents (General, Performance, Safety, Test), fixer agents (Fix, Issue Fix), merge gate (Merge Checker), test runner (Test Runner), consumer setup guide
- `build.gradle.kts` -- Root Gradle build for KMP project
- `settings.gradle.kts` -- Module includes for shared and client subprojects
- `.github/workflows/` -- 7 workflow files wiring up the review pipeline from Shared-Project-Helpers/workflows
- `clients/` -- 4 platform clients providing realistic code for review pipeline testing

## Claude Configuration

- `CLAUDE.md` -- Documents purpose, structure, 8-agent pipeline (General Reviewer, Performance Reviewer, Safety Reviewer, Test Reviewer, Fix Agent, Issue Fix Agent, Merge Checker, Test Runner), pipeline flow, related repos, current status
- No `.claude/` settings directory

## Planning & Research Documents

- `CLAUDE.md` -- Includes current status section: "Pipeline wired up -- all platform clients and shared module are scaffolded. Next step: create intentionally imperfect PRs to test review/fix/merge cycle"
- `README.md` -- Comprehensive agent pipeline reference

## Git History & Current State

- **Branch**: feature/cost-optimization
- **Last commit**: 2026-04-07 -- "Update dotfiles path reference to deprecated/dotfiles"
- **Working tree**: Clean
- **Total commits**: 15+ (viewed)
- **Recent activity**: Cost optimization (Mar 2026) -- combined reviews, on-demand-only reviews, Anthropic reviewer addition, worktree standardization (Apr 2026)
- **Key evolution**: Initial KMP scaffold, workflow wiring, switched to agent wrappers (#62), claude-code-action (#68), Anthropic reviewer (#70), cost optimization (#71)

## Build & Test Commands

```bash
# Build shared module
./gradlew :shared:build

# Build specific clients
./gradlew :clients:android:assembleDebug
./gradlew :clients:windows:run

# Apple client
cd clients/apple && xcodegen generate
open clients/apple/*.xcodeproj
```

## Notes

- Owned by "Shared-Project-Helpers" GitHub org (same as the workflows repo)
- Currently on `feature/cost-optimization` branch (not main)
- Mirrors QualityTime's project structure (KMP multiplatform) to provide realistic test scenarios
- The pipeline is wired up but intentionally imperfect PRs for testing haven't been created yet
- Related repos: workflows (reusable workflows), QualityTime (similar structure), deprecated/dotfiles (pipeline architecture docs)
- Required secret: `ANTHROPIC_API_KEY` in repository settings
