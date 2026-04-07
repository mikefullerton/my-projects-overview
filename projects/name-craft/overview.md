# Name-Craft

## Project Summary

Name-Craft is a whimsical web-based character name generator for children's books that creates silly, genre-specific names through an interactive 9-question questionnaire. Uses Claude AI (with mock mode fallback) to generate names based on sound symbolism, alliteration, and genre templates, combined with a deterministic word-builder system.

## Type & Tech Stack

- **Project Type:** Full-stack web application with Claude AI integration
- **Backend:** Python 3, Flask
- **Frontend:** HTML/CSS/JavaScript (static, served via Flask)
- **AI:** Anthropic Claude API (claude-sonnet-4-20250514)
- **Database:** SQLite3 with WAL mode (word persistence)
- **Streaming:** Server-Sent Events (SSE) for real-time name generation
- **Dependencies:** flask>=3.0, anthropic>=0.40

## GitHub URL

Not a git repository — local development project only.

## Directory Structure

```
name-craft/
├── .claude/
│   ├── settings.json                  # superpowers plugin enabled
│   ├── settings.local.json
│   └── skills/name-craft/
│       ├── SKILL.md                   # Name-Craft skill definition
│       └── references/
│           └── name-components.md     # Genre templates, sound symbolism, word pools
├── CLAUDE.md
├── index.html                         # Single-page app with full UI
├── requirements.txt                   # flask, anthropic
├── docs/
│   ├── tolkien-style-dwarf-names.md   # Khuzdul naming reference
│   └── superpowers/specs/
│       └── 2026-04-03-word-builder-scaffolding-design.md
├── services/server/
│   ├── __main__.py                    # Entry point (port 8765)
│   ├── app.py                         # Flask app factory
│   ├── api.py                         # /api/generate, /api/events/stream, /api/health
│   ├── claude_client.py               # Claude API + mock mode
│   └── sse.py                         # SSE broadcast system
└── scripts/word_builder/
    ├── __main__.py                    # CLI: python -m scripts.word_builder
    ├── seed_db.py                     # Markdown → SQLite parser
    ├── schema.sql                     # words, word_attributes tables
    └── words.db                       # 269+ words (~119KB)
```

## Key Components

**Questionnaire:** 9 questions (genre, creature type, traits, situational, smell) → Claude generates names

**11 Genre Templates:** Fantasy (5 sub-types), Sci-Fi (5), Pirate, Superhero, Fairy Tale, Western, Steampunk, Gothic, Mythology (5), Spy, Ninja

**Sound Symbolism:** Bouba-kiki effect, personality trait sound mappings for evil/intelligence/silliness/sociability axes

**Word Builder:** Markdown → SQLite pipeline. 269+ words with prefix/root/suffix categorization. Designed for multiple future name generators.

**Mock Mode:** Works without API key using canned responses for testing/demo.

## Claude Configuration

- superpowers plugin enabled
- `/name-craft` custom skill for interactive use
- Skill loads system prompt from SKILL.md + name-components.md reference data

## Planning & Research Documents

- **word-builder-scaffolding-design.md** — SQLite-backed word pool architecture for extensibility
- **tolkien-style-dwarf-names.md** — Khuzdul naming rules reference (not yet integrated)

## Git History & Current State

- **Not a git repo** — no version control
- **Most recent files:** April 2-5, 2026
- **Status:** Active development (word builder scaffolding phase)

## Build & Test Commands

```bash
python -m services.server              # Start Flask on :8765
python -m scripts.word_builder         # Show word pool stats
python scripts/word_builder/seed_db.py # Rebuild words.db from markdown
pip install -r requirements.txt
```

**Environment:** `ANTHROPIC_API_KEY` (required for real generation), `NAME_CRAFT_PORT` (default 8765)

## Notes

- Streaming generation via SSE with client isolation per unique ID
- Flask + explicit threading for async generation tasks
- Markdown + SQLite duality: markdown for Claude readability, SQLite for programmatic access
- No database for persisting generated names (ephemeral per session)
