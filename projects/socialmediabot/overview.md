# Social Media Bot

## Project Summary

An AI-powered autonomous content pipeline that analyzes development work from git commits, identifies compelling topics, researches them, and drafts social media posts across X, LinkedIn, Bluesky, and Substack. Orchestrated pipeline of 12 sequential bots with live HTML dashboard, configurable bot selection UI, and approval workflow before publishing.

## Type & Tech Stack

**Project Type:** Python CLI application with Claude Code agents and platform integrations

**Core Technologies:**
- **Python 3.12+** — CLI orchestration and coordination
- **Claude Agent SDK** — AI-powered bot agents
- **Flask/Click** — CLI interface and configuration
- **SQLite** — Operational state database
- **Tweepy** — X (Twitter) API client
- **atproto** — Bluesky protocol client
- **python-substack** — Substack API client
- **PyYAML** — Configuration management
- **Keyring** — Secure credential storage
- **pytest** — 134+ unit tests
- **HTML/CSS/JavaScript** — Live dashboard UI

**Architecture:**
- Python coordinator orchestrates sequential bot pipeline
- Claude Code agents (subprocess-spawned) handle analysis and creation
- Platform clients provide thin wrappers for API access
- SQLite-backed state management for runs and drafts
- Per-run data storage outside repo for isolation

## GitHub URL

`git@github.com:mikefullerton/socialmediabot.git`

https://github.com/mikefullerton/socialmediabot

## Directory Structure

```
socialmediabot/
├── .claude/                             # Claude Code configuration
├── .pytest_cache/                       # Pytest artifacts
├── .venv/                               # Python virtual environment
├── bots/                                # Claude Code agent prompts
│   ├── deep-commit-analyzer.md          # Analyzes git diffs
│   ├── topic-organizer.md               # Groups analyses into narratives
│   ├── topic-researcher.md              # Web research on selected topic
│   ├── online-researcher.md             # Trending AI/agentic news
│   ├── live-event-tracker.md            # Conferences, launches, events
│   ├── competitor-tracker.md            # Monitor prominent builders
│   ├── interview-extractor.md           # Topics from transcripts
│   ├── draft-post-creator.md            # Platform-specific posts
│   ├── reading-list-creator.md          # Curate articles
│   └── dev-process-advisor.md           # Process improvements
├── config/                              # Configuration files
│   ├── config.yaml                      # Bot schedules, settings, platform config
│   ├── interests.md                     # Topics and exclusion filters
│   └── voice.md                         # Brand voice guidelines
├── coordinator/                         # Python CLI orchestrator
│   ├── cli.py                           # Command-line interface
│   ├── [coordinator modules]
│   └── agent_runner.py
├── platforms/                           # Platform API clients
│   ├── x_platform.py                    # X (Twitter) client
│   ├── bluesky_platform.py              # Bluesky client
│   ├── substack_platform.py             # Substack client
│   ├── linkedin_platform.py             # LinkedIn client
│   └── __init__.py
├── templates/                           # HTML templates
│   ├── index.html                       # Run history dashboard
│   ├── config.html                      # Bot selection UI
│   └── overview.html                    # Live run dashboard
├── tests/                               # Unit tests (134+ tests)
│   ├── test_coordinator.py
│   ├── test_platforms.py
│   ├── test_bots.py
│   └── [other test files]
├── Mike Fullerton/                      # Profile-specific configuration
├── docs/                                # Documentation
│   ├── bot-architecture.md
│   ├── pipeline-flow.md
│   └── [other docs]
├── pyproject.toml                       # Python project configuration
├── README.md                            # Project documentation
├── CLAUDE.md                            # Claude Code project rules
├── .gitignore
└── socialmediabot.egg-info/           # Package metadata
```

## Key Files & Components

**CLI & Orchestration:**
- `coordinator/cli.py` — Command-line interface with commands: run, status, queue, approve, reject, show, setup-credentials
- Main coordination logic for sequential pipeline execution
- Per-run data storage and manifest management

**Bot Agents (Claude Code):**
- `bots/deep-commit-analyzer.md` — Python + Agent: analyzes git diffs for motivations, decisions, patterns
- `bots/topic-organizer.md` — Agent: groups analyses into compelling narratives, selects best topic
- `bots/topic-researcher.md` — Agent: web research on selected topic
- `bots/online-researcher.md` — Agent: searches for trending AI/agentic news
- `bots/live-event-tracker.md` — Agent: finds conferences, launches, events
- `bots/competitor-tracker.md` — Agent: monitors prominent AI builder posts
- `bots/interview-extractor.md` — Agent: extracts topics from transcripts
- `bots/draft-post-creator.md` — Agent: writes platform-specific posts
- `bots/reading-list-creator.md` — Agent: curates articles
- `bots/dev-process-advisor.md` — Agent: suggests workflow improvements
- `platforms/` — auto-poster (Python) and engagement-analyst (Agent)

**Configuration:**
- `config/config.yaml` — Bot schedules, settings, platform configuration
- `config/interests.md` — Topics to track and exclusion filters
- `config/voice.md` — Brand voice guidelines (TBD)
- `Mike Fullerton/` — Profile-specific settings

**Platform Clients:**
- `platforms/x_platform.py` — Tweepy-based X client
- `platforms/bluesky_platform.py` — atproto-based Bluesky client
- `platforms/substack_platform.py` — Substack API client
- `platforms/linkedin_platform.py` — LinkedIn client

**Data Management:**
- Per-run storage: `~/Library/Mobile Documents/com~apple~CloudDocs/socialmediabot/bot-runs/run-YYYY-MM-DD-HH-MM-SS/`
  - `manifest.json` — Bot statuses, timing, artifacts
  - `overview.html` — Live-updating dashboard
  - `[bot-name]/` — Per-bot output directories
- `arch-maps/` — Cached repository architecture maps
- `socialmediabot.db` — SQLite operational state

**Dashboard & UI:**
- `templates/index.html` — Run history with status tracking
- `templates/config.html` — Bot selection and configuration UI
- `templates/overview.html` — Live 5-second-refresh dashboard during runs

## Claude Configuration

**Configuration Files:**
- `.claude/` — Claude Code project settings
- `CLAUDE.md` — Project rules, bot coordination patterns

## Planning & Research Documents

**Documentation:**
- `docs/` — Architecture, bot workflow, and integration guides

## Git History & Current State

**Recent Activity:**
- `8c4aab1` docs: add standardized project description
- `cfc7878` feat: iCloud data dir migration, actionable items page
- `6377a50` chore: standardize worktree directory
- `1436d82` docs: add README and Claude Code skills
- `0bd80cb` feat: interview system and updated bot config
- `6721dbc` feat: per-run data storage with live HTML dashboard
- `10fb707` feat: deep activity pipeline with commit-by-commit analysis
- `83759e2` fix: activity scanner recursive discovery, better filtering
- `4d34e70` feat: move data directory to ~/socialmediabot
- `d56ef59` feat: deterministic activity scanner, JSON extraction
- `ee1aa31` fix: make data directory configurable via SMBOT_DATA_DIR
- `e962de3` fix: e2e test harness uses venv Python
- `ec2d4d2` test: 41 new tests for Phase 2/3 code
- `126be97` feat: self-teaching feedback loop from engagement data
- `bbb8a62` feat: dev process advisor bot

**Pattern:** Active feature development with bot enhancements, dashboard improvements, and state management refinement.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Install Dependencies:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Run Tests:**
```bash
python -m pytest tests/ -x -q          # Run all tests
python -m pytest tests/ -v             # Verbose
python -m pytest tests/test_coordinator.py  # Specific test file
```

**Setup Credentials:**
```bash
smbot setup-credentials
```

**Run Pipeline:**
```bash
smbot run                                    # Full pipeline
smbot run --bot deep-commit-analyzer         # Single bot
smbot run --run-id run-2026-04-02-13-36-59  # Continue existing run
smbot run --skip auto-poster,engagement     # Skip specific bots
```

**View Status & Queue:**
```bash
smbot status                                 # Show recent runs
smbot queue                                  # List pending drafts
smbot show <id>                              # Display draft content
smbot approve <id> | --all                   # Approve for posting
smbot reject <id>                            # Reject draft
```

## Notes

**Architecture Highlights:**

1. **Sequential Bot Pipeline** — 12 bots run in order, each feeding output to next
2. **Git-Based Content Source** — Deep commit analyzer extracts motivations from diffs
3. **Live Dashboard** — 5-second refresh during active runs with pulsing bot status
4. **Per-Run Isolation** — Each pipeline execution gets isolated data directory
5. **Approval Workflow** — Human approval gate before platform publishing
6. **Multi-Platform Output** — Single analysis generates platform-specific posts

**Bot Pipeline:**

```
commit-analyzer → topic-organizer → draft-post-creator → auto-poster
topic-organizer → live-event-tracker
topic-researcher → online-researcher
↓
draft-post-creator → reading-list-creator
                  → dev-process-advisor
                  → engagement-analyst
```

**Key Features:**

- **Commit Analysis** — Diffs analyzed for motivations, design decisions, patterns
- **Topic Grouping** — Analyses grouped into compelling narratives
- **Web Research** — Automatic research on selected topic and trending news
- **Event Tracking** — Discovers conferences, product launches
- **Competitor Monitoring** — Tracks posts from prominent builders
- **Interview Extraction** — Derives topics from podcast/interview transcripts
- **Platform Adaptation** — Posts rewritten for each platform's style
- **Reading Lists** — Curated articles based on research
- **Process Advice** — Weekly workflow improvement suggestions
- **Live Metrics** — Engagement analysis on published content

**Configuration:**

- `config.yaml` — Per-platform API config, bot scheduling, timing
- `interests.md` — Topics to track (AI, agentic development, etc.), exclusion filters
- `voice.md` — Brand voice guidelines for post styling
- Platform API keys stored securely via keyring

**Data Storage:**

- Per-run directory structure with manifest.json
- manifest.json tracks: bot statuses, timing, artifacts, errors
- HTML dashboard auto-refreshes every 5 seconds
- Architecture maps cached for reuse
- SQLite database for run history and draft queue

**Testing:**

- 134+ unit tests covering coordinator, platforms, bots
- Health-backoff test design for resilience
- Deterministic activity scanner with JSON validation

**Development Workflow:**

The project follows Claude Code best practices:
- Bot implementations as agent prompts
- Coordinator in Python for deterministic orchestration
- Per-run data isolation
- Live progress tracking via HTML dashboard
- Approval workflow for safety
