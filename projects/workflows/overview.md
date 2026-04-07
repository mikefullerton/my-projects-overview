# workflows

## Project Summary

A shared repository of reusable GitHub Actions workflows for Claude-powered CI/CD automation. Implements a three-layer architecture (Consumer -> Wrapper -> Core) with 11 named agent personas (Thorin, Dwalin, Oin, Dori, Gloin, Balin, Bifur, Nori, and Anthropic) that handle code review, performance analysis, safety/security scanning, test review, automated fixes, merge gating, and autonomous test generation. Used by multiple consumer repos (code-review-pipeline-test, QualityTime, etc.) via GitHub Actions `uses:` references.

## Type & Tech Stack

- **Type**: Reusable GitHub Actions workflow library
- **Primary**: YAML (GitHub Actions workflow definitions)
- **Scripts**: Python 3.11 (inline Anthropic API calls), JavaScript (actions/github-script), Bash (git operations)
- **AI**: Anthropic SDK (Claude) for code review, fixes, and test generation
- **Tools**: Semgrep + GitLeaks (safety reviews), claude-code-action
- **Authentication**: GitHub App tokens (create-github-app-token@v1) or GITHUB_TOKEN

## GitHub URL

`git@github.com:Shared-Project-Helpers/workflows.git`

## Directory Structure

```
workflows/
├── .github/
│   └── workflows/
│       ├── anthropic-code-review.yml         # Anthropic wrapper
│       ├── thorin-code-review.yml            # Thorin code review wrapper (claude-code-action)
│       ├── thorin-review.yml                 # Thorin code review wrapper (Python SDK, deprecated)
│       ├── dwalin-perf-review.yml            # Dwalin performance wrapper
│       ├── oin-safety-review.yml             # Oin safety wrapper
│       ├── dori-test-review.yml              # Dori test review wrapper
│       ├── gloin-fix.yml                     # Gloin fix wrapper
│       ├── gloin-issue-fix.yml               # Gloin issue fix wrapper
│       ├── balin-merge-check.yml             # Balin merge check wrapper
│       ├── bifur-combined-review.yml         # Bifur combined review wrapper
│       ├── nori-test-runner.yml              # Nori test runner wrapper
│       ├── claude-code-review.yml            # Core: code review (claude-code-action)
│       ├── claude-review.yml                 # Core: general reviewer (Python SDK, deprecated)
│       ├── claude-perf-review.yml            # Core: performance reviewer
│       ├── claude-safety-review.yml          # Core: safety reviewer
│       ├── claude-test-review.yml            # Core: test reviewer
│       ├── claude-fix.yml                    # Core: fix agent
│       ├── claude-issue-fix.yml              # Core: issue fix agent
│       ├── claude-merge-check.yml            # Core: merge checker
│       ├── claude-combined-review.yml        # Core: combined review (Sonnet 4.5)
│       └── claude-test-runner.yml            # Core: test runner
├── CLAUDE.md                                 # Project structure and conventions
└── README.md                                 # Comprehensive usage docs
```

## Key Files & Components

- `CLAUDE.md` -- Three-layer architecture overview, agent personas, tech stack, key patterns, related repos
- `README.md` -- Comprehensive documentation: architecture diagram, agent roster table, pipeline flow, wrapper and core workflow reference, consumer setup guide, configuration options
- Agent wrappers (11 files) -- Embed agent persona, guidelines, and settings; consumers only provide app_id and secrets
- Core workflows (10 files) -- Reusable implementation workflows called via `uses:` from wrappers
- Pipeline flow: PR opened -> 5 parallel reviewers -> Fix agents on REQUEST_CHANGES -> Merge check on APPROVE -> auto-merge

## Claude Configuration

- `CLAUDE.md` -- Documents project structure (wrappers vs core), tech stack (YAML, Python, JS, Bash), key patterns (three-layer architecture, formal GitHub reviews), related repos, working instructions
- No `.claude/` directory or settings files

## Planning & Research Documents

- `README.md` -- Serves as comprehensive reference documentation for the entire pipeline system
- Related: `~/projects/deprecated/dotfiles/docs/code-review-pipeline.md` -- Pipeline architecture docs (agent roles, flow diagrams, branch protection, design decisions)

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-07 -- "Update dotfiles path reference to deprecated/dotfiles"
- **Working tree**: Clean
- **Total commits**: 15+ (viewed)
- **Recent activity**: Cost optimization (Mar 2026), Anthropic code reviewer addition, agent wrapper system, dotfiles path updates (Apr 2026)
- **Key evolution**: Started with Python SDK reviews, added agent wrappers (#10), added claude-code-action (#11), added Anthropic reviewer (#12), cost optimization with max_turns and cheaper models (#13)

## Build & Test Commands

```bash
# No build step -- all code lives in workflow YAML files
# Test changes by referencing a branch in a consumer repo's uses: directive
# Example: uses: Shared-Project-Helpers/workflows/.github/workflows/thorin-code-review.yml@feature-branch
```

## Notes

- Owned by "Shared-Project-Helpers" GitHub org (shared across projects)
- Agent personas use Tolkien dwarf names (Thorin, Dwalin, Balin, etc.) for code review roles
- The Python SDK-based Thorin review (thorin-review.yml) is deprecated in favor of claude-code-action (thorin-code-review.yml)
- Bifur combined review runs perf/safety/test in a single API call (Sonnet 4.5) for cost savings
- Gloin Issue Fix creates GitHub Issues for deferred items outside PR scope
- Project is paused but functional and in active use by consumer repos
