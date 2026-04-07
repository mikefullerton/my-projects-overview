# Code Review Pipeline - Project Overview

## Project Summary

An automated code review pipeline that runs as a macOS launchd daemon, polls configured GitHub repositories for open pull requests, reviews them using the Claude Code CLI with agentic cookbook guidelines, and posts reviews back via a GitHub App bot identity. The system tracks review state in SQLite and provides both continuous polling and on-demand review modes.

## Type & Tech Stack

**Project Type:** Python CLI tool + automated daemon service

**Languages & Frameworks:**
- **Python 3.11+** (primary language)
- **Claude Code CLI** (external code review engine via subprocess)
- **GitHub API** (via `gh` CLI and direct REST API)
- **SQLite** (state management with WAL mode)

**Key Dependencies:**
- `pyyaml>=6.0` (config parsing)
- `PyJWT>=2.8` (GitHub App JWT generation)
- `cryptography>=41.0` (RSA key handling for GitHub App authentication)

**Testing:**
- `pytest` (unit testing framework)
- Fixtures for temporary configs and SQLite databases

## GitHub URL

`git@github.com:agentic-cookbook/code-review-pipline.git` (or `https://github.com/agentic-cookbook/code-review-pipline.git`)

## Directory Structure

```
code-review-pipline/
├── src/                          # All source modules
│   ├── __init__.py
│   ├── main.py                   # Entry point: daemon, once, status, review-now commands
│   ├── config.py                 # Configuration loading & validation
│   ├── poller.py                 # GitHub PR polling via `gh` CLI
│   ├── reviewer.py               # Claude Code subprocess orchestration
│   ├── poster.py                 # GitHub API review posting
│   ├── workspace.py              # Git clone & PR checkout management
│   ├── state.py                  # SQLite review state tracking
│   ├── github_auth.py            # GitHub App JWT & installation token handling
│   ├── prompts.py                # System & user prompt construction (6-phase review)
│   └── log.py                    # Logging setup (JSON file + console)
├── tests/                        # pytest unit tests
│   ├── __init__.py
│   ├── conftest.py               # pytest fixtures (tmp_config, tmp_db_path)
│   ├── test_config.py            # Config loading & validation
│   ├── test_poller.py            # PR fetching & filtering
│   ├── test_reviewer.py          # Claude output parsing & decision extraction
│   ├── test_poster.py            # Review posting
│   ├── test_github_auth.py       # JWT & token generation
│   ├── test_state.py             # SQLite state management
│   └── test_workspace.py         # Git operations
├── .claude/                      # Claude Code harness configuration
│   └── settings.local.json       # Permissions (allows Bash(gh browse:*))
├── .git/                         # Git repository
├── .gitignore                    # Ignores state/ and logs/ dirs
├── CLAUDE.md                     # Project documentation (this file)
├── config.yaml                   # Pipeline configuration (repos, GitHub App, review settings)
├── requirements.txt              # Python dependencies
├── state/                        # Runtime directory (gitignored)
│   └── reviews.db               # SQLite database with review history
└── logs/                         # Runtime directory (gitignored)
    └── review-pipeline.log      # Rotating JSON log file
```

## Key Files & Components

### **src/main.py** — Entry Point & Command Dispatcher
- **Commands:**
  - `daemon` — Run continuous poll loop with SIGTERM/SIGINT handling
  - `once` — Single poll cycle, then exit
  - `status` — Print JSON summary of review history (last 24h)
  - `review-now owner/repo#N` — Immediately review a specific PR
- **State Management:** Creates `ReviewState` and `GitHubAppAuth` instances
- **Cycle Logic:** Polls repos, filters PRs, reviews needed PRs, writes heartbeat

### **src/config.py** — Configuration & Validation
- **Dataclasses:**
  - `PipelineConfig` — Top-level configuration
  - `RepoConfig` — Per-repository settings (owner, name, platform, guidelines, filters)
  - `GitHubAppConfig` — GitHub App credentials (app_id, private_key_path, installation_id)
  - `ReviewConfig` — Claude model & max turns
  - `RepoFilters` — PR filtering rules (skip_drafts, skip_labels, require_labels)
- **Validation:** Enforces required keys, validates platform names (swift, kotlin, csharp)
- **Path Resolution:** Uses `Path.expanduser().resolve()` for all paths

### **src/poller.py** — GitHub PR Discovery
- **PRInfo Dataclass:** number, title, author, head_ref, head_sha, base_ref, is_draft, labels
- **Functions:**
  - `get_open_prs(repo)` — Queries GitHub for open PRs using `gh pr list`
  - `_apply_filters()` — Filters by draft status, labels, base branch
- **Integration:** Uses `gh` CLI (read-only, no API costs)

### **src/reviewer.py** — Claude Code Orchestration
- **ReviewResult:** decision (APPROVE/REQUEST_CHANGES/COMMENT), body (full review text)
- **Functions:**
  - `review()` — Runs Claude via `claude --print --model X --system-prompt ... user_prompt`
  - `_parse_decision()` — Extracts decision from Claude output
  - `_extract_review_body()` — Formats review markdown
  - `_parse_claude_output()` — Handles JSON or plain text responses
- **Execution:** Allows Read, Grep, Glob, Bash(git diff/log/gh pr view) tools only
- **Timeout:** 300 seconds (5 minutes) per review

### **src/state.py** — SQLite Review Tracking
- **Schema:**
  ```sql
  CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    repo_owner, repo_name, pr_number, head_sha,
    review_status (in_progress/completed/failed),
    review_decision (APPROVE/REQUEST_CHANGES/COMMENT),
    retry_count, started_at, completed_at, error_message
  );
  ```
- **Key Methods:**
  - `needs_review()` — Check if PR at commit SHA needs review
  - `mark_in_progress()`, `mark_completed()`, `mark_failed()` — State transitions
  - `get_retry_count()` — Enforce max_retries limit
  - `get_status_summary()` — Last 24h summary for `/status` command
- **Features:** WAL mode for concurrent access, ISO8601 timestamps

### **src/prompts.py** — Review Prompt Construction
- **build_system_prompt()** — Constructs system context with 6-phase review structure:
  1. Diff Review (debug code, credentials, conflicts)
  2. Code Quality (complexity, YAGNI, naming, readability)
  3. Security (OWASP Top 10, input validation, TLS)
  4. Testing (coverage, unit/integration tests)
  5. Performance (optimizations, caching, unnecessary allocations)
  6. Final Decision (structured decision output)
- **build_user_prompt()** — Includes PR metadata, diff, and project-specific guidelines
- **Platform Names:** Maps swift/kotlin/csharp to human-readable descriptions

### **src/github_auth.py** — GitHub App Authentication
- **GitHubAppAuth Class:**
  - Generates JWT from app_id and private key
  - Requests installation token (valid ~58 min)
  - Caches token with expiry buffer
  - Makes authenticated API requests
- **Methods:**
  - `_generate_jwt()` — RS256 JWT with 10 min expiry
  - `_request_installation_token()` — GitHub API call for installation token
  - `get_token()` — Cached token with refresh logic
  - `api_request()` — Authenticated POST/GET/etc. to GitHub API

### **src/workspace.py** — Git Repository Management
- **Functions:**
  - `ensure_clone()` — Clone repo if needed, fetch latest
  - `checkout_pr()` — Uses `gh pr checkout` to fetch PR and create branch
  - `get_diff()` — Runs `git diff origin/base_branch...HEAD`
- **Integration:** Subprocess wrappers around `git` and `gh` CLI commands

### **src/poster.py** — GitHub Review Posting
- **post_review()** — Posts review result to GitHub API
  - Maps decision (APPROVE/REQUEST_CHANGES/COMMENT) to GitHub event
  - Includes full review body
  - Returns posted review ID
- **Integration:** Uses `GitHubAppAuth` for authentication

### **src/log.py** — Structured Logging
- **JSONFormatter:** Outputs ISO 8601 timestamps, log level, logger name, message, exceptions as JSON
- **setup_logging():**
  - RotatingFileHandler (10 MB, 5 backups) to `logs/review-pipeline.log`
  - StreamHandler (stderr) with human-readable format
  - Root logger initialized to INFO level

## Claude Configuration

### **.claude/settings.local.json**
```json
{
  "permissions": {
    "allow": ["Bash(gh browse:*)"]
  }
}
```
- Restricts Bash tool to only `gh browse:*` commands (safety constraint)
- Other Bash commands (git, python, etc.) would need explicit permission

## Configuration (config.yaml)

**Top-level Keys:**
- `poll_interval_seconds` — Poll frequency (e.g., 300 = 5 min)
- `clone_base_dir` — Where to clone repos (e.g., `/tmp/review-clones`)
- `state_db_path` — SQLite database path (e.g., `./state/reviews.db`)
- `log_dir` — Log directory (e.g., `./logs`)
- `max_retries` — Max retry attempts per PR

**github_app Section:**
- `app_id` — GitHub App ID (create at github.com/settings/apps)
- `private_key_path` — Path to app private key PEM file
- `installation_id` — GitHub App installation ID

**review Section:**
- `model` — Claude model (e.g., `claude-opus-4-6`)
- `max_turns` — Max agentic turns per review

**global_guidelines:**
- List of markdown files with general code review guidelines
- Paths can use `~` (expanded to home dir)
- Current: empty in example, but typically includes:
  - `~/.claude/guidelines/general.md`
  - `~/.claude/guidelines/engineering-principles.md`
  - `~/.claude/guidelines/testing.md`
  - `~/.claude/guidelines/security.md`

**repos Array:**
- **owner** — GitHub org/user
- **name** — Repository name
- **platform** — `swift`, `kotlin`, or `csharp`
- **guidelines** — Platform-specific markdown guidelines
- **extra_review_instructions** — Project-specific notes
- **branches.base** — Base branch name (default: `main`)
- **filters.skip_drafts** — Skip draft PRs (default: true)
- **filters.skip_labels** — Skip PRs with these labels
- **filters.require_labels** — Only review PRs with these labels

## Planning & Research Documents

No dedicated planning or research directories found. Architecture and design decisions are documented in:
- **CLAUDE.md** — This file (architecture, layout, conventions)
- **src/prompts.py** — 6-phase review methodology (referenced from `~/projects/active/cookbook/workflows/code-review.md`)
- Code comments in Python modules

## Git History & Current State

**Current Branch:** `main`
**Remote Origin:** `git@github.com:agentic-cookbook/code-review-pipline.git`
**Remote Status:** Upstream is gone (detached from remote tracking)

**Recent Commits:**
```
59fc63c (2026-04-06 18:43:42 -0700) chore: add .gitignore
```

**Uncommitted Changes:**
All files (CLAUDE.md, config.yaml, requirements.txt, src/, tests/) are currently untracked:
```
Untracked files:
  CLAUDE.md
  config.yaml
  requirements.txt
  src/
  tests/
```

This indicates the repository may be in an initial setup state after cloning, or files were recently staged/committed but the working tree state hasn't been synchronized.

## Build & Test Commands

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

**Run Tests:**
```bash
pytest tests/
pytest tests/test_config.py -v              # Test config parsing
pytest tests/test_poller.py -v              # Test PR fetching
pytest tests/test_reviewer.py -v            # Test Claude integration
pytest tests/test_state.py -v               # Test SQLite state
pytest tests/test_github_auth.py -v         # Test GitHub App auth
```

**Run Pipeline:**
```bash
# Continuous daemon (polls every N seconds)
python3 src/main.py --daemon

# Single poll cycle
python3 src/main.py --once

# Check current state
python3 src/main.py --status

# Immediate review of specific PR
python3 src/main.py --review-now owner/repo#123

# Custom config file
python3 src/main.py --config /path/to/config.yaml --daemon
```

**Example Systemd/Launchd Integration:**
Create `/Library/LaunchDaemons/com.example.review-pipeline.plist` to run as daemon:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.example.review-pipeline</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/python3</string>
    <string>/path/to/src/main.py</string>
    <string>--config</string>
    <string>/path/to/config.yaml</string>
    <string>daemon</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
```

## Conventions & Best Practices

**Python:**
- Python 3.11+ with `from __future__ import annotations` for forward compatibility
- `pathlib.Path` for all file path operations
- `logging` module with module-level loggers per file
- No external ORMs — direct SQL for SQLite queries

**Database:**
- SQLite with WAL (Write-Ahead Logging) mode
- ISO 8601 timestamps (`datetime.datetime.isoformat()`)
- Unique constraints on (repo_owner, repo_name, pr_number, head_sha)
- Explicit SQL transactions

**Testing:**
- `pytest` with fixtures for temporary configs/databases
- Mocking of external subprocess calls (git, gh, Claude CLI)
- Isolation: each test has independent tmp_path, tmp_db_path

**Logging:**
- Structured JSON logging to file (machine-readable)
- Human-readable console logging (development-friendly)
- Log rotation: 10 MB per file, 5 backups
- Module-level loggers for context

## Notes & Key Design Decisions

1. **Claude Code CLI (not API):** Uses `claude --print --output-format json` subprocess instead of Anthropic API, avoiding API costs and enabling read-only review mode.

2. **6-Phase Review Structure:** Follows structured methodology from agentic cookbook:
   - Diff review, code quality, security, testing, performance, decision
   - Severity levels: CRITICAL, WARNING, INFO
   - Extensible via YAML-based guidelines

3. **GitHub App Isolation:** Reviews posted under bot identity, not personal account. Enables audit trail and permission control.

4. **SQLite + WAL:** Enables multiple processes (daemon + CLI commands) without file locks. State DB is primary source of truth.

5. **Configurable Filtering:** Label-based, draft status, base branch checks prevent reviewing unintended PRs.

6. **Retry Logic:** Tracks retry_count per PR commit SHA; fails gracefully after max_retries (default 3).

7. **Heartbeat File:** `state/heartbeat.json` tracks last poll time, repos checked, reviews pending — useful for monitoring/alerting.

8. **Path Resolution:** All paths use `Path.expanduser()` to support `~` in config, enabling portable configuration across machines.

9. **Subprocess Safety:** All external commands (claude, git, gh) run with explicit timeout and error handling; output captured for parsing.

10. **Architectural Separation:**
    - **Poller** — discovers PRs (reads GitHub API via `gh`)
    - **Reviewer** — analyzes code (runs Claude via subprocess)
    - **Poster** — submits review (writes GitHub API)
    - **State** — tracks progress (SQLite, persistent)
    - Each module independently testable

## Setup Checklist

- [ ] Create GitHub App (github.com/settings/apps/new)
- [ ] Install app on target repositories
- [ ] Download private key, place at `~/.config/review-pipeline/app-private-key.pem`
- [ ] Update config.yaml with app_id, installation_id
- [ ] Configure repos list with owner, name, platform, guidelines
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create `~/.claude/guidelines/` directory with review guidelines
- [ ] Test with: `python3 src/main.py --once`
- [ ] Review state: `python3 src/main.py --status`
- [ ] Set up launchd daemon for continuous polling
- [ ] Monitor logs: `tail -f logs/review-pipeline.log`
