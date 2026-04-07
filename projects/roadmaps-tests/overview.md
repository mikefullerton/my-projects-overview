# roadmaps-tests

## Project Summary

A test repository for the roadmaps system, containing roadmap fixture files in various states (AllAuto3Step, SingleStep, PartialComplete, WithDependencies) along with Python test files and markdown test documents (smoke tests, atomic batch tests, dashboard verification). Used for validating roadmap parsing, state transitions, and the flat-file roadmap format. Includes multiple roadmap fixture types exercising different scenarios.

## Type & Tech Stack

- **Type**: Test repository (for roadmaps system)
- **Languages**: Python (test files), Markdown (roadmap fixtures and test docs)
- **Testing**: Python (pytest-style test files)
- **Format**: Flat-file roadmap format (markdown with state tracking)

## GitHub URL

`git@github.com:agentic-cookbook/roadmaps-tests.git`

## Directory Structure

```
roadmaps-tests/
├── .claude/
│   └── settings.json                # Permissions for .claude/Features/ editing
├── Roadmaps/
│   ├── AllAuto3Step/                # 3-step auto-completion fixture
│   ├── SingleStep/                  # Single-step roadmap fixture
│   ├── PartialComplete/             # Partially completed roadmap fixture
│   ├── WithDependencies/            # Roadmap with step dependencies
│   ├── AtomicBatchTest-Roadmap.md   # Atomic batch test roadmap
│   ├── AtomicBatchTest2-Roadmap.md  # Atomic batch test 2 roadmap
│   ├── DashboardVerify-Roadmap.md   # Dashboard verification roadmap
│   ├── GreetingModule-Roadmap.md    # Greeting module roadmap
│   ├── MissionWhiskerReconnaissance-Roadmap.md  # Mission roadmap
│   └── QuickSmokeTest-Roadmap.md    # Quick smoke test roadmap
├── atomic-batch-test.md             # Atomic batch test doc
├── atomic-test-2.md                 # Atomic test 2 doc
├── dashboard-verify.md              # Dashboard verification doc
├── greeting.py                      # Python greeting module
├── README.md                        # Minimal readme ("cat-herding-tests")
├── roadmap-test.md                  # Roadmap test specification
├── smoke-test.md                    # Smoke test doc
├── test_greeting.py                 # Python test file for greeting
└── .gitignore
```

## Key Files & Components

- `.claude/settings.json` -- Permissions: Edit and Write access to `.claude/Features/**`
- `Roadmaps/` -- Roadmap fixtures in various states: AllAuto3Step (3-step auto-completion), SingleStep, PartialComplete, WithDependencies
- `roadmap-test.md` -- Roadmap test specification document
- `greeting.py` -- Simple Python module used as test subject
- `test_greeting.py` -- pytest-style tests for the greeting module
- `smoke-test.md` -- Quick smoke test document
- `atomic-batch-test.md` / `atomic-test-2.md` -- Atomic operation test documents
- `dashboard-verify.md` -- Dashboard verification test

## Claude Configuration

- `.claude/settings.json` -- Allows Edit and Write operations on `.claude/Features/**` paths
- No CLAUDE.md or settings.local.json

## Planning & Research Documents

- `roadmap-test.md` -- Roadmap test specification
- Various test documents (smoke-test.md, atomic-batch-test.md, dashboard-verify.md)

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: add .gitignore"
- **Working tree**: Clean
- **Total commits**: 15+ (viewed)
- **Recent activity**: Active fixture creation (Mar 2026) -- adding roadmap fixtures of various types (AllAuto3Step, SingleStep, PartialComplete, WithDependencies), flat file format migration, gitignore added (Apr 2026)
- **Key changes**: Migration to flat file format (#305b1db), Complete state file fixes, numerous fixture additions

## Build & Test Commands

```bash
# Python tests
python -m pytest test_greeting.py

# No formal build process -- test fixtures are markdown files
```

## Notes

- Owned by "agentic-cookbook" GitHub org
- README says "cat-herding-tests" (alternate name / internal codename)
- The repo primarily serves as a fixture collection for testing roadmap parsing and state machine behavior
- Roadmap fixtures exercise different scenarios: auto-completion, single-step, partial completion, dependency chains
- The flat-file roadmap format was migrated from an earlier format (commit 305b1db)
