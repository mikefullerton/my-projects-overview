# agenticwebtoolkit

## Project Summary

Shared React + TypeScript component library providing an Agentic design system (theme tokens, ThemeProvider, ThemeToggle) and a full-featured chat widget with three display modes (inline, three-pane, mobile), a typed backend contract, and 10 CSS themes. Consumed as a git submodule by other Agentic Cookbook family sites.

## Type & Tech Stack

- **Type:** Shared React component library, private (`"private": true`), distributed as a git submodule -- not published to npm
- **Language:** TypeScript, CSS
- **Framework:** React 19 (peer dependency; consuming sites provide React)
- **Styling:** CSS custom properties (design tokens), mode-specific CSS files, 10 chat theme CSS files
- **Build:** No library build step -- consumers import TypeScript source directly through their own bundler. Example app uses Vite.
- **Testing:** Vitest + @testing-library/react + jsdom (61 tests across 8 files per README)
- **TypeScript:** target ES2020, ESNext modules, bundler module resolution, JSX `react-jsx`, strict

## GitHub URL

- SSH: `git@github.com:agentic-cookbook/agenticwebtoolkit.git`
- Web: https://github.com/agentic-cookbook/agenticwebtoolkit

## Directory Structure

```
agenticwebtoolkit/
├── package.json                 # Multi-path exports, peer dep on React 19
├── tsconfig.json
├── vitest.config.ts
├── vitest.setup.ts
├── README.md
├── .claude/
│   ├── CLAUDE.md                # Tech stack + architecture notes
│   └── settings.json            # Enables superpowers plugin
├── src/
│   ├── index.ts                 # Barrel export
│   └── theme/
│       ├── index.ts
│       ├── tokens.css           # Core design tokens
│       ├── tokens-light.css     # Opt-in light mode overrides
│       ├── base.css             # Reset, body, selection, grain overlay
│       ├── layout.css
│       ├── components.css
│       ├── markdown.css
│       ├── ThemeProvider.tsx    # Context + useTheme hook
│       └── ThemeToggle.tsx      # Three-way toggle (auto/dark/light)
├── chat/
│   ├── index.ts                 # Chat barrel export
│   ├── types.ts                 # ChatMessage, ChatParticipant, PopoverData, ...
│   ├── persona-chat.js          # DEPRECATED vanilla JS class (back-compat)
│   ├── persona-chat.d.ts        # DEPRECATED type declarations
│   ├── base.css                 # DEPRECATED (replaced by css/base.css)
│   ├── backends/
│   │   ├── types.ts             # ChatBackend interface
│   │   ├── MockBackend.ts       # Canned responses for dev/tests
│   │   └── FetchBackend.ts      # HTTP POST backend
│   ├── components/
│   │   ├── ChatInput.tsx
│   │   ├── InlinePopover.tsx
│   │   ├── MessageBubble.tsx
│   │   ├── RichContent.tsx
│   │   ├── SendIcon.tsx
│   │   ├── Transcript.tsx
│   │   └── TypingIndicator.tsx
│   ├── modes/
│   │   ├── InlineChat.tsx       # Simple centered chat
│   │   ├── ThreePaneChat.tsx    # Chat + detail + topics sidebar
│   │   ├── MobileChat.tsx       # Full-screen slide-in overlay
│   │   ├── PersonaChat.tsx      # Convenience wrapper delegating via mode prop
│   │   └── three-pane/          # Three-pane sub-components
│   ├── hooks/
│   │   ├── useChatSession.ts    # Core state: messages, send queue, typing
│   │   └── useScrollToBottom.ts
│   ├── css/
│   │   ├── base.css             # Shared structural styles
│   │   └── modes/
│   │       ├── inline.css
│   │       ├── three-pane.css
│   │       └── mobile.css
│   ├── themes/                  # 10 CSS themes
│   │   ├── agenticcookbookweb.css
│   │   ├── dev-team.css
│   │   ├── mikefullerton.css
│   │   ├── myprojectsoverview.css
│   │   ├── myprojects.css
│   │   ├── professional.css
│   │   ├── techy.css
│   │   ├── terminal-split.css
│   │   ├── terminal.css
│   │   └── whimsical.css
│   └── __tests__/
├── examples/
│   └── chat/                    # React/Vite example app w/ theme switcher
│       ├── index.html
│       ├── package.json
│       ├── tsconfig.json
│       ├── vite.config.ts
│       └── src/
└── docs/
    ├── usage.md                 # Chat usage & API
    ├── theming.md               # Chat theming guide
    ├── message-layout.md        # Message layout spec
    ├── project-guidelines.md
    ├── planning/
    │   └── planning.md          # Placeholder (TBD)
    └── project/
        └── description.md       # Short standardized description
```

## Key Files & Components

**Theme system (`src/theme/`):**
- `ThemeProvider.tsx` -- React context providing theme state and `useTheme` hook.
- `ThemeToggle.tsx` -- Three-way control (auto / dark / light).
- `tokens.css` -- Core CSS custom properties for colors, fonts, status colors.
- `tokens-light.css` -- Opt-in light-mode token overrides (split for selective import).
- `base.css`, `layout.css`, `components.css`, `markdown.css` -- Shared style layers.

**Chat library (`chat/`):**
- `types.ts` -- `ChatMessage`, `ChatParticipant`, `PopoverData`, etc.
- `backends/types.ts` -- `ChatBackend` interface defining the contract between UI and transport.
- `backends/MockBackend.ts` -- Canned-response backend for demos/tests.
- `backends/FetchBackend.ts` -- HTTP POST backend for real APIs.
- `hooks/useChatSession.ts` -- Core state hook: messages, send queue, typing indicators.
- `hooks/useScrollToBottom.ts` -- Auto-scroll helper for the transcript.
- `components/Transcript.tsx`, `MessageBubble.tsx`, `ChatInput.tsx`, etc. -- Shared UI building blocks.
- `modes/InlineChat.tsx` -- Simple centered chat.
- `modes/ThreePaneChat.tsx` -- Chat + detail pane + topics sidebar layout.
- `modes/MobileChat.tsx` -- Full-screen slide-in overlay.
- `modes/PersonaChat.tsx` -- Convenience wrapper that picks a mode via prop.

**Package exports (`package.json`):**
Fine-grained export paths for `"."`, `"./chat"`, `"./theme"`, plus individual CSS files under `./chat/css/...` and `./theme/...css`, so consumers can import only what they need.

## Claude Configuration

- `.claude/CLAUDE.md` -- Documents tech stack (React 19, TypeScript, Tailwind CSS 4, Vite), architecture overview of `src/theme/` and `chat/`, and an explicit list of deprecated files kept for backward compatibility (`chat/persona-chat.js`, `chat/persona-chat.d.ts`, `chat/base.css`).
- `.claude/settings.json` -- Enables the `superpowers` plugin: `{"enabledPlugins": {"superpowers@claude-plugins-official": true}}`.
- No `.claude/rules/` directory and no commands/hooks configured.

## Planning & Research Documents

- `docs/project/description.md` -- One-line standardized description: "PersonaChat -- A React/TypeScript chat component library for AI persona conversations, with three display modes (inline, three-pane, mobile), a typed backend contract, and 10 CSS themes."
- `docs/planning/planning.md` -- Placeholder (`(to be determined)`).
- `docs/project-guidelines.md` -- Project-level guidelines.
- `docs/usage.md` -- Chat widget usage & API reference.
- `docs/theming.md` -- Guide for applying and authoring chat themes.
- `docs/message-layout.md` -- Message layout specification.

## Git History & Current State

- **Remote:** `origin` -> `git@github.com:agentic-cookbook/agenticwebtoolkit.git`
- **Branch:** `main`
- **Working tree:** clean

**Recent commits (last 15):**
- `ea9fcc9` docs: update all docs for React component library
- `78f81b8` refactor: convert examples to React/Vite, deprecate vanilla JS
- `718af02` chore: add chat exports to package.json, include chat in tsconfig
- `7998d77` feat: add InlineChat, MobileChat, ThreePaneChat modes with CSS
- `670eaed` feat: add shared React chat components
- `af3c41e` feat: add chat types, backend abstraction, and core session hook
- `37b6a27` refactor: split light mode tokens into separate opt-in file
- `206b504` feat: add TypeScript type declaration for persona-chat
- `b80c163` feat: add shared layout, components, and markdown CSS
- `34a92b1` refactor: convert to React + TypeScript component library
- `f934aaa` feat: add three-way theme toggle control and light mode tokens
- `a5b207e` feat: add agentic theme with shared design tokens and base styles
- `4b054b4` refactor: restructure repo for git submodule consumption
- `5fdd4b7` feat: canned responses, mobile support, mikefullerton theme refresh
- `8791d1d` docs: comprehensive project guidelines and updated layout spec

**Trajectory:** started as a vanilla-JS `persona-chat` widget, restructured for submodule consumption, then converted to a full React + TypeScript component library with a chat backend abstraction, three display modes, and a shared Agentic theme system.

## Build & Test Commands

`package.json` defines no `scripts` block -- there is no `npm run build` or `npm run dev` at the library root. Consumers import source directly.

```bash
# Install dev dependencies (library)
npm install

# Run the Vitest test suite (library)
npx vitest run          # one-shot
npx vitest              # watch mode

# Run the React/Vite example app
cd examples/chat
npm install
npx vite                # dev server
npx vite build          # production build of the example
```

## Notes

- **Submodule-first design:** the library is not published; consuming sites add it via `git submodule add git@github.com:agentic-cookbook/agenticwebtoolkit.git` and import source files directly.
- **No build step at the library level** -- `tsconfig.json` has `declaration: true` but there is no output emit configured, and `package.json` exports point at `.ts`/`.tsx` source. The consuming site's bundler is responsible for compilation.
- **PersonaChat wrapper** acts as a single entry point that delegates to `InlineChat`, `ThreePaneChat`, or `MobileChat` based on a `mode` prop, simplifying adoption.
- **Theming** is pure CSS custom properties -- 10 drop-in theme files in `chat/themes/` with no JS coupling, making it easy to add new looks.
- **Backward-compat surface:** the deprecated vanilla JS files (`chat/persona-chat.js`, `chat/persona-chat.d.ts`, `chat/base.css`) are intentionally retained per `.claude/CLAUDE.md` so existing submodule consumers don't break during the React migration.
- **Peer dependency:** React 19 (and `react-dom` 19) must be provided by the consumer.
- **Superpowers plugin** is the only Claude tooling enabled; no custom commands, hooks, or rules directories.
