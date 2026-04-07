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
├── .gitignore                    # Ignores state/ and logs/ dirs
├── CLAUDE.md                     # Project documentation
├── config.yaml                   # Pipeline configuration (repos, GitHub App, review settings)
├── requirements.txt              # Python dependencies
├── state/                        # Runtime directory (gitignored)
│   └── reviews.db               # SQLite database with review history
└── logs/                         # Runtime directory (gitignored)
    └── review-pipeline.log      # Rotating JSON log file
```

## Key Files & Components

### src/main.py -- Entry Point & Command Dispatcher
- **Commands:** `daemon` (poll loop), `once` (single cycle), `status` (JSON summary), `review-now owner/repo#N` (immediate review)
- Creates `ReviewState` and `GitHubAppAuth` instances, polls repos, filters PRs, reviews needed PRs, writes heartbeat

### src/config.py -- Configuration & Validation
- Dataclasses: `PipelineConfig`, `RepoConfig`, `GitHubAppConfig`, `ReviewConfig`, `RepoFilters`
- Validates platform names (swift, kotlin, csharp), resolves paths with `Path.expanduser()`

### src/poller.py -- GitHub PR Discovery
- `PRInfo` dataclass (number, title, author, head_ref, head_sha, base_ref, is_draft, labels)
- Uses `gh pr list` for read-only polling, filters by draft status and labels

### src/reviewer.py -- Claude Code Orchestration
- Runs Claude via `claude --print --model X --system-prompt ...`
- Parses decision (APPROVE/REQUEST_CHANGES/COMMENT) from output
- 300-second timeout, read-only tool permissions (Read, Grep, Glob, git diff/log)

### src/prompts.py -- Review Prompt Construction
- 6-phase review structure: Diff Review, Code Quality, Security, Testing, Performance, Final Decision
- Injects platform guidelines from `~/.claude/guidelines/`

### src/state.py -- SQLite Review Tracking
- Schema: reviews table with repo_owner, repo_name, pr_number, head_sha, review_status, review_decision
- WAL mode, ISO8601 timestamps, unique constraint on (owner, name, pr_number, sha)

### src/github_auth.py -- GitHub App Authentication
- RS256 JWT generation, installation token caching with refresh, authenticated API requests

### src/poster.py -- GitHub Review Posting
- Posts review via GitHub App identity, maps decision to GitHub event type

### src/workspace.py -- Git Repository Management
- Clone management, PR checkout via `gh pr checkout`, diff generation

### src/log.py -- Structured Logging
- JSON formatter for file output (10 MB rotating, 5 backups), human-readable console output

## Claude Configuration

### .claude/settings.local.json
```json
{
  "permissions": {
    "allow": ["Bash(gh browse:*)"]
  }
}
```
No rules or skills configured. No `.claude/CLAUDE.md` (project docs in root `CLAUDE.md`).

## Planning & Research Documents

No dedicated planning or research directories. Architecture and design decisions are documented in:
- **CLAUDE.md** -- Architecture, layout, conventions
- **src/prompts.py** -- 6-phase review methodology (referenced from `~/projects/active/cookbook/workflows/code-review.md`)

## Git History & Current State

**Current Branch:** `main`
**Remote Origin:** `git@github.com:agentic-cookbook/code-review-pipline.git`

**Recent Commits:**
```
59fc63c (2026-04-06) chore: add .gitignore
```

**Uncommitted/Untracked Files:**
All substantive files are currently untracked (CLAUDE.md, config.yaml, requirements.txt, src/, tests/). The repository has only one commit (the .gitignore). This indicates the project is in early setup -- code has been written locally but not yet committed to the repository.

## Build & Test Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run pipeline
python3 src/main.py --daemon          # Continuous daemon
python3 src/main.py --once            # Single poll cycle
python3 src/main.py --status          # JSON state summary
python3 src/main.py --review-now owner/repo#123  # Immediate review
```

## Notes

1. **Claude Code CLI (not API):** Uses `claude --print` subprocess instead of Anthropic API, avoiding API costs and enabling read-only review mode.

2. **6-Phase Review Structure:** Follows structured methodology from agentic cookbook -- diff review, code quality, security, testing, performance, decision. Severity levels: CRITICAL, WARNING, INFO.

3. **GitHub App Isolation:** Reviews posted under bot identity, not personal account. Enables audit trail and permission control.

4. **SQLite + WAL:** Enables multiple processes (daemon + CLI) without file locks. State DB is primary source of truth.

5. **Configurable Filtering:** Label-based, draft status, base branch checks prevent reviewing unintended PRs. Max 3 retries per PR commit SHA.

6. **config.yaml Structure:** Top-level settings (poll_interval, clone_base_dir, state_db_path, max_retries), github_app credentials, review model settings (claude-opus-4-6, max_turns: 10), global_guidelines paths, and repos array with per-repo platform/guidelines/filters.

7. **Conventions:** Python 3.11+, pathlib.Path for all paths, module-level loggers, direct SQL (no ORM), ISO 8601 timestamps.

8. **Project State:** Early stage -- code written but mostly uncommitted. Only the .gitignore has been committed to the repository.
