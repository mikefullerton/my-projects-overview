# social-media-bot-tests

## Project Summary

An external test harness for the social-media-bot project, using Vitest and TypeScript. Contains integration and functional test specs covering the bot's core features: activity aggregation, approval flow, auto-posting, draft creation, full pipeline, health/backoff, and smoke tests. Includes test fixtures (config, research data) and shared test utilities (runner, assertions, fixtures). Configured with long timeouts (10 min per test) and single-threaded execution for reliable integration testing.

## Type & Tech Stack

- **Type**: Test harness (external, for social-media-bot)
- **Language**: TypeScript (ES modules)
- **Test framework**: Vitest 3.2.1
- **Database**: better-sqlite3 11.0.0 (for test fixture data)
- **Runtime**: Node.js
- **Build**: npm (package.json, private)
- **Target project**: `/Users/mfullerton/projects/active/social-media-bot`

## GitHub URL

None (no git repository initialized)

## Directory Structure

```
social-media-bot-tests/
├── fixtures/
│   ├── config/
│   │   └── test-config.yaml         # Test configuration
│   └── research/
│       ├── voice.md                 # Voice/tone research fixture
│       └── sample-activity-summary.md  # Sample activity data
├── lib/
│   ├── assertions.ts               # Custom test assertions
│   ├── fixtures.ts                 # Fixture loading utilities
│   └── runner.ts                   # Test runner helpers
├── specs/
│   ├── activity-aggregator.test.ts  # Activity aggregation tests
│   ├── approval-flow.test.ts       # Approval workflow tests
│   ├── auto-poster.test.ts         # Auto-posting tests
│   ├── draft-creator.test.ts       # Draft creation tests
│   ├── full-pipeline.test.ts       # Full pipeline integration tests
│   ├── health-backoff.test.ts      # Health check and backoff tests
│   └── smoke.test.ts               # Smoke tests
├── node_modules/                    # Dependencies
├── package.json                     # Project config
├── package-lock.json               # Lock file
├── tsconfig.json                   # TypeScript config
├── vitest.config.ts                # Vitest configuration
├── .python-path                     # Points to social-media-bot venv
└── .repo-dir                        # Points to social-media-bot repo
```

## Key Files & Components

- `package.json` -- Name: "social-media-bot-test-harness", private, ES modules, Vitest 3.2.1, better-sqlite3 11.0.0
- `vitest.config.ts` -- Configured with 10-minute test timeout, 1-minute hook timeout, single-threaded (maxThreads: 1), verbose reporter, specs/**/*.test.ts pattern
- `.python-path` -- Points to social-media-bot Python venv: `/Users/mfullerton/projects/active/social-media-bot/.venv/bin/python`
- `.repo-dir` -- Points to target repo: `/Users/mfullerton/projects/active/social-media-bot`
- `specs/full-pipeline.test.ts` -- End-to-end pipeline integration test
- `specs/approval-flow.test.ts` -- Tests for the post approval workflow
- `specs/auto-poster.test.ts` -- Tests for automated posting behavior
- `specs/health-backoff.test.ts` -- Tests for health checking and exponential backoff
- `lib/runner.ts` -- Test runner utilities for executing bot commands
- `fixtures/config/test-config.yaml` -- Test configuration fixture
- `fixtures/research/voice.md` -- Voice/tone research fixture data

## Claude Configuration

None -- no `.claude/` directory, CLAUDE.md, or Claude settings.

## Planning & Research Documents

- `fixtures/research/voice.md` -- Voice and tone research data (used as test fixture)
- `fixtures/research/sample-activity-summary.md` -- Sample activity summary fixture

## Git History & Current State

- **Git**: Not initialized (no `.git/` directory)
- **Working tree**: All files are local only, not version controlled
- **Status**: Development in progress, no commits

## Build & Test Commands

```bash
# Install dependencies
npm install

# Run all tests
npm test              # vitest run

# Run specific test suites
npm run test:smoke    # vitest run --grep smoke
npm run test:fast     # vitest run --grep 'approval|poster|health'

# Watch mode
npm run test:watch    # vitest

# Clean temp files
npm run clean         # rm -rf /tmp/smbot-test-*
```

## Notes

- No git repository -- all files exist only locally
- Tests are designed to run against the live social-media-bot project (referenced via .python-path and .repo-dir files)
- Long timeouts (10 minutes per test) suggest these are integration tests that may invoke the actual bot
- Single-threaded execution (maxThreads: 1) prevents test interference
- Uses better-sqlite3 for test fixture data management
- The test harness is separate from the bot repo to keep test infrastructure independent
- 7 test spec files covering the full bot feature surface
