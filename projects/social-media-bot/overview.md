# social-media-bot

## Project Summary

AI-powered content pipeline that analyzes development work (git commits, diffs), finds compelling topics, researches them via web search and competitor tracking, and drafts social media posts across X, LinkedIn, Bluesky, and Substack. Runs 12 bots sequentially in a pipeline: analysis (commit-analyzer, topic-organizer, topic-researcher) -> research (online-researcher, live-event-tracker, competitor-tracker, interview-extractor) -> output (draft-post-creator, reading-list-creator, dev-process-advisor) -> publishing (auto-poster, engagement-analyst). Includes a self-teaching feedback loop from engagement data back to draft creation. Data is stored in iCloud for cross-device access, with a live HTML dashboard that auto-refreshes during runs.

## Type & Tech Stack

- **Type**: CLI tool / autonomous agent pipeline
- **Language**: Python 3.12+
- **Framework**: Click (CLI), claude-agent-sdk (bot orchestration)
- **Dependencies**: click, pyyaml, keyring, tweepy (X/Twitter), atproto (Bluesky), python-substack, requests, claude-agent-sdk
- **Testing**: pytest, pytest-asyncio (134 unit tests)
- **Build system**: setuptools via pyproject.toml
- **Entry point**: `smbot` CLI command (`coordinator.cli:cli`)
- **Data storage**: SQLite (operational state), JSON files (per-run outputs), iCloud directory for persistent data

## GitHub URL

`git@github.com:mikefullerton/social-media-bot.git`

## Directory Structure

```
social-media-bot/
├── .claude/
│   ├── settings.local.json          # Permission allowlists
│   └── skills/start-run/SKILL.md    # Pipeline run skill
├── bots/
│   ├── interaction/                  # Interview-related bots
│   └── research/                     # Research-related bots
├── config/
│   ├── config.yaml                   # Bot schedules, settings, platform config
│   ├── interests.md                  # Topics to track and exclusion filters
│   └── voice.md                      # Brand voice guidelines
├── coordinator/
│   ├── cli.py                        # Main CLI and pipeline orchestration (63K)
│   ├── run_manager.py                # Per-run state management (31K)
│   ├── db.py                         # SQLite database layer
│   ├── commit_analyzer.py            # Deep commit analysis with diff reading
│   ├── activity_scanner.py           # Recursive repo discovery
│   ├── json_extract.py               # Robust JSON extraction from LLM output
│   ├── config.py                     # Configuration loader
│   ├── health.py                     # Health/backoff system
│   ├── keychain.py                   # Platform credential storage
│   ├── scheduler.py                  # Bot scheduling
│   ├── search.py                     # Search utilities
│   ├── spawner.py                    # Claude agent spawner
│   └── test_logger.py               # Test logging utilities
├── platforms/
│   ├── base.py                       # Platform base class
│   ├── x.py                          # X/Twitter client (tweepy)
│   ├── linkedin.py                   # LinkedIn client
│   ├── bluesky.py                    # Bluesky client (atproto)
│   ├── substack.py                   # Substack client
│   └── mock.py                       # Mock platform for testing
├── templates/
│   ├── index.html                    # Run history dashboard
│   ├── overview.html                 # Per-run live dashboard
│   ├── config.html                   # Bot selection UI
│   └── actionable.html               # Actionable items page
├── tests/                            # 134 unit tests
├── Mike Fullerton/                   # Personal context (resume, etc.)
├── pyproject.toml                    # Project metadata and dependencies
├── README.md                         # Documentation
└── .gitignore
```

## Key Files & Components

- `coordinator/cli.py` -- Main CLI with `smbot run`, `smbot status`, `smbot queue`, `smbot approve`, `smbot reject`, `smbot show`, `smbot setup-credentials` commands
- `coordinator/run_manager.py` -- Per-run data model, manifest management, HTML dashboard generation
- `coordinator/commit_analyzer.py` -- Analyzes actual git diffs to extract motivations, design decisions, patterns, and trade-offs
- `coordinator/activity_scanner.py` -- Discovers and scans git repos for recent activity
- `bots/` -- Markdown prompt files for Claude Code agents (12 bots total)
- `platforms/` -- Thin API wrappers for X, LinkedIn, Bluesky, Substack
- `templates/` -- HTML templates for dashboards (live-updating overview, config UI, run history)
- `config/config.yaml` -- Pipeline configuration
- `config/interests.md` -- Topic filters and interests
- Data stored at: `~/Library/Mobile Documents/com~apple~CloudDocs/social-media-bot/`

## Claude Configuration

- **Skills**: `start-run` -- reads run-config.json, shows bot summary, executes pipeline, opens live overview page
- **Settings (local)**: Permission allowlists for web search, web fetch (GitHub, PyPI, docs sites), file operations, pip, claude agent execution
- **No CLAUDE.md** in the project root (uses README.md for documentation)

## Planning & Research Documents

- `docs/superpowers/` -- Contains planning/superpowers documentation
- `tests/test-design.md` -- Test design methodology document

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "feat: iCloud data dir migration, actionable items page, and pipeline improvements"
- **Working tree**: Clean
- **Recent activity**: Active development (daily commits through early April 2026)
- **Key recent changes**: iCloud data directory migration, actionable items page, interview system, per-run data storage with live HTML dashboard, deep activity pipeline with commit-by-commit analysis

## Build & Test Commands

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e .

# Run pipeline
smbot run                                    # Full pipeline
smbot run --bot deep-commit-analyzer         # Single bot
smbot run --run-id <run-id>                  # Continue existing run
smbot run --skip auto-poster,engagement-analyst  # Skip bots

# CLI commands
smbot status                                 # Recent bot runs
smbot queue                                  # Pending drafts
smbot approve <id> | --all                   # Approve drafts
smbot reject <id>                            # Reject draft
smbot show <id>                              # Display draft
smbot setup-credentials                      # Store API keys

# Tests
python -m pytest tests/ -x -q               # 134 unit tests

# Configure bots
open ~/Library/Mobile\ Documents/com\~apple\~CloudDocs/social-media-bot/config.html
```

## Notes

- The pipeline uses claude-agent-sdk to spawn Claude Code agents for each bot
- Data is stored in iCloud (`~/Library/Mobile Documents/com~apple~CloudDocs/social-media-bot/`) for cross-device access and persistence outside the repo
- The commit analyzer reads actual diffs to understand *why* changes were made, not just *what* changed
- Overview pages auto-refresh every 5 seconds during active runs with pulsing status indicators
- The self-teaching feedback loop feeds engagement data from the engagement-analyst back into the draft-post-creator
- Bot prompts live in `bots/` as markdown files, organized into `interaction/` and `research/` subdirectories
