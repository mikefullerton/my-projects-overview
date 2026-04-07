# Social Media Bot

## Project Summary

Social Media Bot is an AI-powered autonomous content pipeline that analyzes development work (git commits), identifies compelling topics, researches them, and drafts social media posts across X, LinkedIn, Bluesky, and Substack. Uses a Python coordinator to orchestrate 12 specialized Claude Code agents that run sequentially through the pipeline.

## Type & Tech Stack

- **Project Type:** Python CLI tool + Agent-driven content platform
- **Language:** Python 3.12+
- **Agent Framework:** claude-agent-sdk (spawns Claude Code agents)
- **CLI:** click
- **Config:** pyyaml
- **Platform Integrations:** tweepy (X/Twitter), atproto (Bluesky), python-substack, requests (LinkedIn)
- **Storage:** SQLite3 (operational state), macOS Keychain (credentials via keyring)
- **Testing:** pytest, pytest-asyncio

## GitHub URL

`https://github.com/mikefullerton/social-media-bot`

## Directory Structure

```
social-media-bot/
├── .claude/
│   ├── settings.local.json
│   └── skills/start-run/SKILL.md      # Pipeline run skill
├── config/
│   ├── config.yaml                     # Bot schedules, platform settings, budgets
│   ├── interests.md                    # Topics to track/exclude
│   └── voice.md                        # Brand voice guidelines (TBD)
├── coordinator/                        # Python orchestration (3,563 LOC)
│   ├── cli.py (1238 LOC)              # Click CLI: run, status, queue, approve, reject, show, setup-credentials
│   ├── run_manager.py (790 LOC)       # Run context, manifest, HTML dashboard generation
│   ├── db.py (454 LOC)               # SQLite: bot_runs, drafts, posts, metrics, reading_list, commit_analyses
│   ├── activity_scanner.py            # Recursive repo discovery, commit filtering
│   ├── commit_analyzer.py             # Calls deep-commit-analyzer agent
│   ├── spawner.py                     # claude-agent-sdk wrapper
│   ├── json_extract.py                # Robust JSON extraction from LLM outputs
│   ├── keychain.py                    # macOS Keychain wrapper
│   ├── scheduler.py, health.py, search.py, config.py
├── platforms/                          # Platform clients (317 LOC)
│   ├── base.py, x.py, linkedin.py, bluesky.py, substack.py, mock.py
├── bots/                               # Claude Code agent prompts (markdown)
│   ├── research/                       # deep_commit_analyzer, activity_aggregator, topic_organizer, topic_researcher, online_researcher, live_event_tracker, competitor_tracker, engagement_analyst, interview_extractor
│   └── interaction/                    # draft_post_creator, reading_list_creator, dev_process_advisor, interviewer, auto_poster.py
├── templates/                          # HTML dashboards (index, overview, config, actionable)
├── tests/                              # 134+ unit tests (1,329 LOC)
│   ├── test_cli.py, test_db.py, test_activity_scanner.py, test_bot_prompts.py, etc.
│   └── test_platforms/                 # Per-platform tests
├── docs/superpowers/
│   ├── specs/2026-04-01-social-media-bot-system-design.md
│   └── plans/2026-04-01-phase1-content-pipeline.md
├── pyproject.toml
└── README.md
```

## Key Components

**12-Bot Pipeline (sequential):**
1. deep-commit-analyzer → Analyzes git diffs for WHY (motivations, decisions, trade-offs)
2. activity-aggregator → Scans repos for interesting commits
3. topic-organizer → Groups analyses into narratives
4. topic-researcher → Web research on selected topics
5. online-researcher → Trending AI/agentic dev news
6. live-event-tracker → Conferences, launches, events
7. competitor-tracker → Monitors prominent AI builders
8. engagement-analyst → Analyzes metrics on posted content
9. interview-extractor → Extracts topics from transcripts
10. draft-post-creator → Transforms research into platform-specific drafts
11. reading-list-creator → Curates articles worth reading
12. auto-poster → Posts approved drafts to platforms

**CLI Commands:** `smbot run`, `status`, `queue`, `approve <id>`, `reject <id>`, `show <id>`, `setup-credentials`

**Data:** iCloud storage at `~/Library/Mobile Documents/com~apple~CloudDocs/social-media-bot/` with per-run artifact directories and live HTML dashboards

**Rate Limits:** X: 2/day, LinkedIn: 1/day, Bluesky: 2/day, Substack Notes: 1/day, Newsletter: 1/week

## Claude Configuration

- `/start-run` skill reads run config, executes pipeline, opens live dashboard
- Permissions: pdftotext, file ops, git, pip install, web search (specific domains)

## Planning & Research Documents

- **system-design.md** — Goals, architecture, platform targets, data flow
- **phase1-content-pipeline.md** — Implementation plan with task breakdown and acceptance criteria

## Git History & Current State

- **Branch:** main (up to date with origin)
- **Working tree:** Clean
- **Recent (2026-04-06):** iCloud data migration, actionable items page, pipeline improvements, worktree standardization, interview system, per-run data storage

## Build & Test Commands

```bash
pip install -e .                       # Install
smbot run                              # Full pipeline
smbot run --bot deep-commit-analyzer   # Single bot
smbot queue                            # Review drafts
pytest tests/ -x -q                    # 134+ tests
/start-run                             # Claude Code skill
```

## Notes

- Python coordinator + Claude Code agents: Python owns scheduling/state/health; agents are stateless workers
- Deep commit analysis extracts WHY, not just WHAT changed
- Per-run isolated artifact directories with live HTML dashboards (5s auto-refresh)
- Keychain-based secrets (not env vars)
- Self-teaching loop: engagement metrics feed back into draft creation
