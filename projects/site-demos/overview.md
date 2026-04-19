# site-demos

## Project Summary

A collection of static HTML/CSS/JS demo sites used as a scratchpad for UI prototyping. The current contents are a set of **PersonaChat** widget themes — a reusable vanilla-JS chat component rendered against many distinct CSS themes and layout variants, browsable from a single theme browser page.

## Type & Tech Stack

- **Type:** Static website / frontend prototype collection (no build step)
- **Languages:** HTML, CSS, vanilla JavaScript (ES6 classes)
- **Dependencies:** None (no `package.json`, no bundler). Uses Google Fonts via CDN (`Inter`, `Nunito`, `JetBrains Mono`, `IBM Plex Mono`, `Instrument Serif`, `Manrope`, `DM Mono`).
- **Runtime:** Browser only — served as plain files (works with the local Caddy server or any static host).

## GitHub URL

https://github.com/agentic-cookbook/site-demos

Remote: `git@github.com:agentic-cookbook/site-demos.git`

## Directory Structure

```
site-demos/
├── .claude/
│   ├── CLAUDE.md                 # minimal placeholder (tech stack TBD)
│   └── settings.json             # enables superpowers plugin
├── .gitignore
├── README.md                     # placeholder stub
├── docs/
│   ├── planning/
│   │   └── planning.md           # stub
│   └── project/
│       └── description.md        # stub ("Demo websites for anything I need")
└── persona-chat/
    ├── index.html                # theme browser (main entry point, ~28KB)
    ├── shared/
    │   └── persona-chat.js       # the PersonaChat JS class (shared widget)
    ├── professional/             # theme + demo page
    │   ├── index.html
    │   ├── style.css
    │   └── DESIGN.md
    ├── techy/                    # theme + demo page
    │   ├── index.html
    │   ├── style.css
    │   └── DESIGN.md
    ├── whimsical/                # theme + demo page
    │   ├── index.html
    │   ├── style.css
    │   └── DESIGN.md
    ├── mikefullerton/            # single-theme demo (references themes/*.css)
    │   └── index.html
    ├── terminal/                 # terminal-styled demo
    │   └── index.html
    ├── terminal-split/           # right-justified user variant
    │   └── index.html
    ├── agenticcookbookweb/             # site-matched theme demo
    │   └── index.html
    ├── dev-team/                 # site-matched theme demo
    │   └── index.html
    ├── myprojects/              # site-matched theme demo
    │   └── index.html
    └── myprojectsoverview/     # site-matched theme demo
        └── index.html
```

## Key Files & Components

- **`persona-chat/shared/persona-chat.js`** — The core `PersonaChat` class (~200 lines). Builds transcript, input, send button, typing indicator, and message bubbles entirely via `document.createElement`. Accepts `{container, persona, user, welcomeMessage, onSend}` and exposes `addMessage`, `addTypingIndicator`, `removeTypingIndicator`. Has a built-in default responder that returns canned replies with simulated latency.
- **`persona-chat/index.html`** — The main "theme browser" (main entry). Sidebar lists themes, preview pane renders the same widget against each. Recent commits added a chat pane + detail pane + topics-index pane layout with keyboard navigation (arrow keys over messages), SVG connector lines in a "separated" layout, click-to-select topic from transcript, and full-width rows.
- **Per-theme `DESIGN.md` files** (`professional`, `techy`, `whimsical`) — Document the concept, visual language, palette, typography, and reusability notes for each theme. The shared-JS / CSS-only-theming pattern is a core architectural decision.
- **Per-theme `style.css`** — Theme-specific styling. The JS component emits class names like `pc-transcript`, `pc-message`, `pc-persona`, `pc-user`, `pc-bubble`, `pc-avatar`, `pc-sender`, `pc-text`, `pc-time`, `pc-dots`, `pc-typing`, `pc-input`, `pc-send-btn`, so themes restyle via those hooks.
- **Site-matched theme demos** (`agenticcookbookweb`, `dev-team`, `myprojects`, `myprojectsoverview`, `mikefullerton`) — Small `index.html` files demonstrating PersonaChat styled to blend into specific sister projects.
- **Note:** `mikefullerton/index.html` and the theme browser reference a `persona-chat/themes/` directory (e.g. `themes/base.css`, `themes/mikefullerton.css`) that does not exist in the current tree — likely missing/untracked assets or a broken link.

## Claude Configuration

- **`.claude/CLAUDE.md`** — 164-byte placeholder. Only says the tech stack, build, and architecture are "to be determined". Needs updating.
- **`.claude/settings.json`** — Enables the `superpowers@claude-plugins-official` plugin. Nothing else configured.
- **`.gitignore`** — Ignores `.DS_Store`, `.claude/worktrees/`, `.claude/settings.local.json`, `.env`, `.superpowers/`.
- No project-level skills, rules, hooks, or agents.

## Planning & Research Documents

- **`docs/project/description.md`** — One-line stub: "Demo websites for anything I need going forward."
- **`docs/planning/planning.md`** — Stub: "(to be determined)".
- No research documents, no implementation plans, no ADRs. Documentation footprint is minimal — this is a sandbox project.

## Git History & Current State

- **Branch:** `main`
- **Status:** clean (nothing staged, nothing unstaged, no untracked)
- **Commits:** 27 total, starting from `68f9216 Initial project scaffolding`
- **Evolution:** Began as generic scaffolding, then grew `persona-chat` through three themed variants → adding 5 site-matched themes → terminal and terminal-split → an index navigation page → replacement with a single theme browser → topic+details mode with settings popup. Recent work focuses on interaction polish: arrow-key navigation, detail-pane arrows, click-to-select transcript messages, pane flex ratio tuning, SVG connector lines for a "separated" layout.
- **Recent commits (most recent first):**
  - `4213bca fix: remove pc-has-detail class, rows are now full-width by default`
  - `c2c0a4f feat: arrow keys navigate all messages, not just topics`
  - `5449b45 fix: rebalance pane flex ratios so topics pane is visible`
  - `3fc67ad fix: pin detail arrow to right edge, fix arrow key navigation`
  - `610e56c fix: redirect printable keystrokes to chat input when not focused`
  - `9bb4223 feat: arrow keys, selected highlight, separated default, transparent gaps`
  - `18341f1 Click transcript message to select its topic and details`
  - `bba7e28 Add separated layout with SVG connector lines`
  - `61d4eb2 Fix detail arrow: append to message row, not bubble`
  - `3962dd1 Style detail arrow: right-aligned in bubble, theme highlight color`

## Build & Test Commands

There is no build step, no package manager, no test runner. To work on it:

- **Serve locally:** Copy `persona-chat/` into `~/.local-server/sites/` (Caddy auto-serves at `http://localhost:2080/persona-chat/`), or open `persona-chat/index.html` directly in a browser. Relative paths (`../../persona-chat/themes/base.css`) assume serving from the repo root, so a static server is preferred over `file://`.
- **Lint / format / test:** None configured.

## Notes

- This is a **sandbox / prototype repo**, not a product. The README, CLAUDE.md, planning, and description files are all placeholder stubs — the real documentation is inline in per-theme `DESIGN.md` files and git commit messages.
- The core architectural idea worth preserving: **one shared vanilla-JS component, many CSS-only themes**. `persona-chat.js` emits a stable `pc-*` class vocabulary, and every theme is purely a restyle. No framework, no build, drop-in friendly.
- Despite the plural "site-demos" name and README ("for anything I need going forward"), the repo currently only contains the `persona-chat/` family. Future demos would live as sibling top-level directories.
- The theme browser (`persona-chat/index.html`) and `mikefullerton/index.html` both reference a `persona-chat/themes/` directory that is **not present in the committed tree** — this is a likely broken reference worth investigating before working on those pages.
- The remote is hosted under the `agentic-cookbook` GitHub org, suggesting this repo is a companion to other "agentic cookbook" material rather than a personal scratchpad.
- The `agenticcookbookweb`, `dev-team`, `myprojects`, and `myprojectsoverview` theme variants appear to correspond to sister sites — the chat widget is being designed to be dropped into each of those projects.
