# Market Research

## Project Summary

Market Research is an AI-powered market analysis tool that evaluates indie software project ideas by running 5 specialized analysis agents per project, then synthesizing a cross-project ranking with a clear recommendation on which project to pursue first for the fastest path to revenue. Designed for solo indie developers with multiple project ideas who need objective, data-driven decision-making. Each project is analyzed across five dimensions (Market, Competition, Revenue, Feasibility, Progress) using the Anthropic SDK and Tavily web search, generating detailed per-project reports, comparative rankings, and executive summaries.

## Type & Tech Stack

**Type:** AI-Powered CLI Tool / Market Analysis System

**Tech Stack:**
- **Language:** Python 3.9+
- **AI/LLM:** Anthropic Claude API (Sonnet 4.5 by default, configurable to Opus)
- **Web Search:** Tavily Python SDK
- **Schema Validation:** Pydantic v2
- **CLI:** Rich (progress bars, tables, colored output), argparse
- **Configuration:** python-dotenv for environment variables
- **Package Manager:** pip / setuptools
- **Build System:** setuptools + wheel

## GitHub URL

https://github.com/mikefullerton/market-research.git

## Directory Structure

```
market-research/
├── pyproject.toml          # Project metadata, dependencies, entry point
├── .env.example            # Environment template (ANTHROPIC_API_KEY, TAVILY_API_KEY)
├── README.md               # Project overview, usage, setup
├── src/market_research/    # Main package
│   ├── __init__.py
│   ├── cli.py              # Entry point, orchestration, CLI commands
│   ├── config.py           # Load .env, create API clients
│   ├── schema.py           # Pydantic models (input/output schemas)
│   ├── loader.py           # Load & validate YAML project files
│   ├── search.py           # Tavily wrapper with file-based daily cache
│   ├── report.py           # Markdown report generation
│   └── agents/
│       ├── __init__.py
│       ├── base.py         # Shared Anthropic SDK wrapper, structured output
│       ├── market.py       # Market size, demand signals (uses Tavily)
│       ├── competition.py  # Competitor mapping, saturation (uses Tavily)
│       ├── revenue.py      # Revenue models, pricing, time-to-money (uses Tavily)
│       ├── feasibility.py  # Solo-founder viability, MVP time
│       ├── progress.py     # Leverage existing work, adjust time-to-revenue
│       └── synthesizer.py  # Cross-project ranking, recommendation
├── projects/               # User-authored project YAML files
│   └── _template.yaml      # Template for adding new projects
├── docs/
│   ├── ORIGINAL_SPEC.md    # Initial specification & design
│   ├── ARCHITECTURE.md     # Implementation architecture
│   ├── DESIGN_RATIONALE.md # Key design decisions
│   └── IMPLEMENTATION_LOG.md # Development log
├── .claude/                # Claude Code configuration
│   └── settings.local.json # Local Claude settings
├── reports/                # Generated reports (gitignored)
├── .venv/                  # Virtual environment
└── .gitignore
```

## Key Files & Components

- **pyproject.toml** - Project metadata, setuptools configuration, entry point (`market-research = "market_research.cli:main"`), dependencies (anthropic, tavily-python, pydantic, pyyaml, rich, python-dotenv)
- **README.md** - Complete usage guide, setup instructions, CLI syntax, output format, cost breakdown, tech stack overview
- **src/market_research/cli.py** - Main orchestration: parses CLI args (analyze, list, --project, --skip-cache), runs agent pipeline, generates reports
- **src/market_research/schema.py** - Pydantic models for ProjectInput (YAML schema), agent outputs (scores 1-10), CompositeScore (weighted ranking), ProjectReport
- **src/market_research/agents/base.py** - Shared Anthropic SDK wrapper using tool_use + Pydantic structured output
- **src/market_research/agents/market.py** - Market Agent: TAM/SAM/SOM analysis, growth trends, demand signals via Tavily
- **src/market_research/agents/competition.py** - Competition Agent: competitor mapping, saturation, differentiation gaps
- **src/market_research/agents/revenue.py** - Revenue Agent: revenue model recommendations, pricing, time-to-first-dollar
- **src/market_research/agents/feasibility.py** - Feasibility Agent: solo-founder viability, MVP timeline, maintenance burden
- **src/market_research/agents/progress.py** - Progress Agent: existing work leverage, adjusted time-to-revenue
- **src/market_research/agents/synthesizer.py** - Synthesizer: cross-project comparison, weighted ranking, recommendation
- **src/market_research/search.py** - Tavily wrapper with file-based daily cache (no repeated API calls same day)
- **src/market_research/report.py** - Markdown report generation (per-project, ranking, executive summary)
- **docs/ORIGINAL_SPEC.md** - Original design specification with scoring methodology, architecture overview, analysis pipeline, implementation order
- **docs/ARCHITECTURE.md** - Implementation architecture details
- **projects/_template.yaml** - Template for defining new projects (name, description, target_audience, problem_solved, existing_progress, platforms, revenue_ideas, competitors_known, keywords, constraints)

## Claude Configuration

Stored in **.claude/settings.local.json** - Contains local Claude Code settings for project-specific configuration.

## Planning & Research Documents

- **docs/ORIGINAL_SPEC.md** - Comprehensive original specification (80+ lines) covering architecture, project input schema, analysis pipeline (5 agents + synthesizer), scoring methodology (5 weighted dimensions), output format, CLI usage, dependencies, implementation order, and verification steps
- **docs/ARCHITECTURE.md** - Implementation architecture
- **docs/DESIGN_RATIONALE.md** - Key design decisions (YAML for project input, Pydantic for schema validation, Anthropic SDK directly, Tavily for search, file-based cache, Claude Sonnet 4.5, Markdown reports)
- **docs/IMPLEMENTATION_LOG.md** - Development log of implementation progress

## Git History & Current State

- **Remote:** git@github.com:mikefullerton/market-research.git
- **Current Branch:** main
- **Status:** Clean working tree (no uncommitted changes)
- **Recent Activity:**
  - Latest: Merge remote-tracking branch 'origin/docs/project-history' (806c6e9)
  - chore: standardize worktree directory to .claude/worktrees/ (67b2bcf, 9ba46f4)
  - Add project documentation (#2) (55a318e, fdacaa3)
  - Add market research agent system (#1) (e48a0a7)
  - Initial commit with .gitignore (8163769)

## Build & Test Commands

```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -e .                         # Editable install (development mode)
cp .env.example .env
# Edit .env with ANTHROPIC_API_KEY and TAVILY_API_KEY

# Usage
market-research list                     # List defined projects
market-research analyze                  # Analyze all projects
market-research analyze --project NAME   # Analyze specific project
market-research analyze --skip-cache     # Force fresh web searches

# Running Python directly
python -m market_research.cli analyze
python -m market_research.cli list
```

## Notes

- **Status:** Active development for project evaluation
- **Scoring Dimensions:** Feasibility (0.25 weight - solo dev time constraint), Revenue (0.20 - monetization viability), Progress (0.20 - existing work leverage), Market (0.20 - demand existence), Competition (0.15 - addressable via differentiation)
- **Cost Estimate:** ~$0.12 per full 4-project run using Claude Sonnet 4.5; ~60 Tavily searches per run (~6% of 1,000 free monthly credits)
- **Search Cache:** File-based daily cache prevents re-burning API credits on same-day re-runs
- **Agent Pipeline:** Sequential execution where each agent feeds results to next (Market → Competition → Revenue → Feasibility → Progress → Synthesizer for cross-project ranking)
- **Output Format:** Markdown reports (per-project analysis, comparative ranking table with narrative, executive summary with bottom-line recommendation and timeline)
- **Extensibility:** Easy to add new projects via YAML files; configurable to use Claude Opus instead of Sonnet via ANTHROPIC_MODEL env var
- **Tavily Integration:** Web search with structured results for market research, competitor analysis, revenue model discovery
