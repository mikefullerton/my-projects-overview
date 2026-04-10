# persona-creator

## Project Summary

A Python library and Claude Code skill for generating AI personas from minimal seed input (name, role, personality hints), producing fully fleshed-out personas at three tiers (full, lightweight, specialist) with markdown and JSON output. Recently expanded to include **visual character generation** — mapping personality traits to SVG character sheets via pluggable image-generation providers (Recraft, FLUX + VTracer).

## Type & Tech Stack

- **Type**: Python library + Claude Code skill + CLI tool
- **Language**: Python 3.12+
- **Packaging**: setuptools via `pyproject.toml`, src-adjacent layout (`persona_creator/`)
- **Key dependencies**:
  - `pydantic>=2.0` — data models (frozen BaseModel)
  - `pyyaml>=6.0` — YAML frontmatter parsing
  - `httpx>=0.27` — async HTTP for image-gen providers
  - `click>=8.0` — CLI framework
  - `vtracer>=0.6` (optional, `[flux]` extra) — raster-to-SVG vectorization
- **Dev tooling**: pytest, pytest-asyncio, ruff (line length 100, rules E/F/I/UP/B/SIM)
- **CLI entry point**: `persona-creator` (from `persona_creator.cli:main`)

## GitHub URL

https://github.com/agentic-cookbook/persona-creator

## Directory Structure

```
persona-creator/
├── persona_creator/            # Main package
│   ├── __init__.py             # Public API exports
│   ├── cli.py                  # Click CLI: generate, preview, mapping
│   ├── models.py               # Persona dataclasses (full/lightweight/specialist)
│   ├── serializers.py          # to/from markdown + JSON
│   ├── generator.py            # LLM prompt building + response parsing
│   ├── visual_models.py        # Pydantic models for visual generation
│   ├── trait_mapper.py         # Rules engine: personality -> visual params
│   ├── spec_builder.py         # Builds component specs from visual params
│   ├── layout.py               # Character sheet layout/positioning
│   ├── compositor.py           # Layers SVG components into final image
│   ├── prompts/                # Tier-specific generation prompt templates
│   │   ├── full.md
│   │   ├── lightweight.md
│   │   └── specialist.md
│   └── providers/              # Swappable image-gen backends
│       ├── base.py             # ComponentProvider protocol
│       ├── recraft.py          # Direct SVG via Recraft API
│       └── flux_vtrace.py      # FLUX raster + VTracer vectorization
├── skill/                      # Claude Code skill
│   ├── SKILL.md                # /create-persona slash command
│   └── references/
│       └── persona-research.md # Design principles (from cookbook/registry)
├── tests/                      # 46 pytest tests
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_serializers.py
│   ├── test_generator.py
│   ├── test_visual_models.py
│   ├── test_trait_mapper.py
│   ├── test_compositor.py
│   └── test_providers.py
├── docs/
│   ├── project/description.md  # Standardized project description
│   ├── planning/planning.md    # (placeholder)
│   └── superpowers/
│       ├── plans/2026-04-08-persona-creator.md
│       └── specs/2026-04-08-persona-creator-design.md
├── .claude/
│   ├── CLAUDE.md               # Project instructions
│   ├── settings.json           # Enables superpowers plugin
│   └── worktrees/              # (empty)
├── pyproject.toml
└── README.md
```

## Key Files & Components

### Persona generation (text)
- **`persona_creator/models.py`** — Pydantic models for three tiers: `FullPersona` (14 sections), `LightweightPersona` (7 sections), `SpecialistPersona` (4 sections), plus supporting types (`Trait`, `Value`, `Emotion`, `Flaw`, `Voice`, `GrowthArc`, `AntiPattern`, `SampleInteraction`, `Contradiction`, `PersonaSeed`, `PersonaMetadata`).
- **`persona_creator/generator.py`** — `generate_prompt(seed, tier)` builds an LLM prompt from tier templates; `parse_response(text, tier, name)` parses the response back into a model. Library is LLM-agnostic.
- **`persona_creator/serializers.py`** — `to_markdown`, `from_markdown` (YAML frontmatter + headed sections), `to_json`, `from_json` (supports `format="registry"` for official-agent-registry compatibility).
- **`persona_creator/prompts/*.md`** — Tier-specific generation prompt templates encoding persona design research.

### Visual generation
- **`persona_creator/visual_models.py`** — Frozen pydantic models: `PersonaDefinition`, `EnergyLevel` (StrEnum: calm/moderate/intense/playful), `ColorPalette`, `VisualParameters`, `CharacterSheet`.
- **`persona_creator/trait_mapper.py`** — `PERSONALITY_RULES` dict mapping trait strings ("analytical", etc.) to partial visual overrides (eye style, eyebrows, expression, accessories, shape language). `map_traits()` blends multiple trait contributions.
- **`persona_creator/compositor.py`** — `build_character_sheet()` layers SVG components into a final character image.
- **`persona_creator/providers/base.py`** — `ComponentProvider` protocol for swappable generation backends.
- **`persona_creator/providers/recraft.py`** — Direct SVG generation via Recraft API.
- **`persona_creator/providers/flux_vtrace.py`** — FLUX image generation followed by VTracer rasterization to SVG.
- **`persona_creator/cli.py`** — Click CLI with `generate`, `preview`, `mapping` commands and a `_get_provider()` factory.

### Skill
- **`skill/SKILL.md`** — `/create-persona` slash command (v1.0.0, sonnet model). Interactive flow: gathers name/role/tier, asks for 2-3 personality hints, reads research context, generates the persona, iterates, and writes YAML-frontmattered markdown.
- **`skill/references/persona-research.md`** — Design principles extracted from agentic-cookbook and official-agent-registry (structural ingredients, core principles, tier comparison).

## Claude Configuration

- **`.claude/CLAUDE.md`** — Project instructions describing the original text-only architecture (models/serializers/generator/prompts/skill/tests). Note: pre-dates the visual generation additions, so does not mention `visual_models`, `trait_mapper`, `compositor`, `providers/`, or `cli.py`.
- **`.claude/settings.json`** — Enables the `superpowers@claude-plugins-official` plugin.
- **`.claude/worktrees/`** — Directory present but empty.
- **No custom hooks, agents, or slash commands** in `.claude/` beyond the skill shipped in `skill/SKILL.md`.

## Planning & Research Documents

- **`docs/project/description.md`** — Standardized one-paragraph project description (aligns with the my-projects-overview convention).
- **`docs/planning/planning.md`** — Placeholder (`(to be determined)`).
- **`docs/superpowers/specs/2026-04-08-persona-creator-design.md`** — Design spec (Draft, authored 2026-04-08 by Mike Fullerton + Claude). Defines goals, non-goals, tier structures, and library/skill architecture. Full persona tier based on `official-agent-registry/docs/research/ai-persona-template.md`.
- **`docs/superpowers/plans/2026-04-08-persona-creator.md`** — Corresponding implementation plan.
- **`skill/references/persona-research.md`** — Research notes on persona design principles, used by the `/create-persona` skill at runtime.

## Git History & Current State

- **Remote**: `git@github.com:agentic-cookbook/persona-creator.git`
- **Current branch**: `main`
- **Status**: 1 uncommitted change — `docs/feedback/cookbook-review-2026-04-08.md` shows as deleted (the `docs/feedback/` directory no longer exists on disk). This predates the current session.
- **Recent commits** (most recent first):
  - `b9ae9fa` Merge pull request #9 from agentic-cookbook/worktree-visual-generator
  - `d858a59` Integrate visual generation with existing persona library
  - `fd36fb9` Add tag-based guideline filtering proposal to cookbook feedback
  - `f96fb9a` Add cookbook principles feedback from visual generator build
  - `b00d584` Apply cookbook principles: separation of concerns, DI, immutability, linting
  - `fc4f930` Add test harness — 46 tests covering models, trait mapper, compositor, providers
  - `26b02c1` Add CLI with generate, preview, and mapping commands
  - `2b398f2` Add compositor — layers SVG components into final character image
  - `c6c495b` Add FLUX + VTracer provider — image generation with vectorization
  - `602bbc4` Add Recraft provider — direct SVG generation via Recraft API
  - `7b69e1e` Add trait mapper — rules engine connecting personality to appearance
  - `2a7d275` Add ComponentProvider protocol for swappable generation backends
  - `20b7fef` Add core data models for persona visual generation
  - `3dd8a58` Add Python project structure with src layout
  - `e11face` Initial implementation: persona-creator library and skill (#8)

Project started as a text-only persona library/skill (PR #8), then a second arc of work added visual character generation on a `worktree-visual-generator` branch that merged as PR #9.

## Build & Test Commands

```bash
# Install (editable, with dev extras)
pip install -e ".[dev]"

# Install with visual-generation extras
pip install -e ".[dev,flux,recraft]"

# Run tests (46 tests)
pytest -v

# Lint
ruff check .

# CLI
persona-creator generate ...
persona-creator preview ...
persona-creator mapping ...

# Slash command (in Claude Code)
/create-persona
```

## Notes

- **Two architectural layers, one package**: original text-persona generation (models, serializers, generator, prompts, skill) and a later visual-generation layer (visual_models, trait_mapper, spec_builder, layout, compositor, providers, CLI). They share the `persona_creator` namespace but the text API is what's exported from `__init__.py`; visual generation is accessed via the CLI and direct submodule imports.
- **LLM-agnostic by design** — the library produces prompts and parses responses; callers provide the LLM. No provider lock-in for text generation.
- **Output-compatible with official-agent-registry** — `to_json(persona, format="registry")` produces the minimal `config.persona` shape consumed by that project.
- **Provider pattern for visuals** — `ComponentProvider` protocol makes backends swappable; Recraft (direct SVG) and FLUX+VTracer (raster + vectorize) ship in-repo.
- **Frozen pydantic models** in `visual_models.py` (`BaseModel, frozen=True`) enforce immutability — consistent with the `b00d584` commit applying cookbook principles (separation of concerns, DI, immutability, linting).
- **CLAUDE.md is stale** — describes only the text-generation architecture. Does not mention the visual generation additions merged in PR #9. A refresh would help future Claude sessions.
- **Uncommitted deletion** of `docs/feedback/cookbook-review-2026-04-08.md` exists on `main` and is unrelated to this overview task; should be resolved with the user.
- **Superpowers plugin enabled** via `.claude/settings.json`; the design spec and implementation plan live under `docs/superpowers/`, suggesting the project was scaffolded using a superpowers-style plan-then-build workflow.
- **Org**: `agentic-cookbook` GitHub org — part of a cluster of related projects (agentic-cookbook, official-agent-registry) that inform the persona design research.
