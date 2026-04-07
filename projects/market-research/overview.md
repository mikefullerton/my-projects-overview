# market-research

## Project Summary

An AI-powered market research tool for evaluating indie software project ideas. Runs 5 sequential analysis agents per project (Market, Competition, Revenue, Feasibility, Progress), then a Synthesizer agent compares all projects with weighted scoring to produce a clear recommendation on which project to pursue first for the fastest path to revenue. Designed for solo indie developers with multiple project ideas who need objective, data-driven prioritization.

## Type & Tech Stack

- **Type**: CLI tool / AI agent system
- **Language**: Python 3.9+
- **AI**: Anthropic SDK (Claude) with structured output via tool_use + Pydantic
- **Search**: Tavily API (web search with file-based daily cache)
- **Validation**: Pydantic v2 (schema validation for all inputs/outputs)
- **CLI**: Rich (progress indicators and tables)
- **Config**: python-dotenv, PyYAML
- **Build**: setuptools (pyproject.toml)
- **Package**: `market-research` CLI entry point

## GitHub URL

`git@github.com:mikefullerton/market-research.git`

## Directory Structure

```
market-research/
├── .claude/
│   └── settings.local.json          # Permission allowlists (git operations)
├── .env.example                      # API key template
├── docs/
│   ├── ARCHITECTURE.md              # System architecture
│   ├── DESIGN_RATIONALE.md          # Design decisions
│   ├── IMPLEMENTATION_LOG.md        # Implementation history
│   └── ORIGINAL_SPEC.md            # Original specification
├── projects/
│   ├── _template.yaml              # Project definition template
│   └── todo-app.yaml               # Example project definition
├── reports/                         # Generated analysis reports (empty)
├── src/
│   └── market_research/            # Python package source
├── pyproject.toml                   # Build config + dependencies
└── README.md                        # Usage docs
```

## Key Files & Components

- `pyproject.toml` -- Dependencies: anthropic>=0.79.0, tavily-python>=0.7.21, pydantic>=2.0, pyyaml, rich, python-dotenv
- `src/market_research/` -- Main package with CLI entry point (`cli:main`), 6 analysis agents
- `projects/_template.yaml` -- YAML schema for defining project ideas to evaluate
- `projects/todo-app.yaml` -- Example project definition
- `docs/ARCHITECTURE.md` -- System architecture documentation
- `docs/DESIGN_RATIONALE.md` -- Design decisions and rationale
- `docs/ORIGINAL_SPEC.md` -- Original specification

## Claude Configuration

- `.claude/settings.local.json` -- Permission allowlists for git init, checkout, remote, fetch, add, commit, push
- No CLAUDE.md or project-level rules

## Planning & Research Documents

- `docs/ARCHITECTURE.md` -- System architecture
- `docs/DESIGN_RATIONALE.md` -- Design decisions
- `docs/IMPLEMENTATION_LOG.md` -- Implementation history
- `docs/ORIGINAL_SPEC.md` -- Original project specification

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: standardize worktree directory to .claude/worktrees/"
- **Working tree**: Clean
- **Total commits**: 4
- **Recent activity**: Initial build (Feb 2026), documentation added, worktree standardization (Apr 2026)
- **Key commits**: Initial commit, market research agent system (#1), project documentation (#2)

## Build & Test Commands

```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# Edit .env with ANTHROPIC_API_KEY and TAVILY_API_KEY

# Usage
market-research list                        # List defined projects
market-research analyze                     # Analyze all projects
market-research analyze --project todo-app  # Analyze single project
market-research analyze --skip-cache        # Force fresh web searches
```

## Notes

- Scoring weights: Feasibility (0.25), Revenue (0.20), Progress (0.20), Market (0.20), Competition (0.15)
- Cost: ~$0.12 per full 4-project run with Claude Sonnet; ~60 Tavily searches per run
- Tavily search cache prevents duplicate API calls on same-day re-runs
- Reports output to `reports/<date>/` with per-project, ranking, and executive summary reports
- Project is paused -- functional but not actively developed
