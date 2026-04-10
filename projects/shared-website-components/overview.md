# Shared Website Components

## Project Summary

A reusable React + TypeScript component library providing theme system, chat widgets, and design tokens for Agentic Cookbook family websites. Designed as a git submodule for consistent UI/UX across multiple sites. Includes multiple chat modes (inline, three-pane, mobile), theme provider with dark/light/auto modes, and comprehensive CSS styling system.

## Type & Tech Stack

**Project Type:** React component library (npm package)

**Core Technologies:**
- **React 19** — Modern component framework
- **TypeScript** — Type-safe development
- **Tailwind CSS 4** — Utility-first styling
- **Vite** — Build tool and dev server
- **Vitest** — Unit testing framework
- **CSS** — Structural and theme styling
- **npm** — Package management

**Architecture:**
- Modular component exports with TypeScript
- CSS-based theming system with custom properties
- Functional components with hooks
- Backend abstraction for chat functionality
- Multiple layout modes for different contexts

## GitHub URL

`git@github.com:agentic-cookbook/shared-website-components.git`

https://github.com/agentic-cookbook/shared-website-components

## Directory Structure

```
shared-website-components/
├── src/                                 # Core library exports
│   ├── index.ts                         # Barrel export
│   └── theme/
│       ├── tokens.css                   # Design tokens (colors, fonts)
│       ├── base.css                     # Reset, body, selection, grain
│       ├── ThemeProvider.tsx            # React context + useTheme hook
│       └── ThemeToggle.tsx              # Three-way toggle (auto/dark/light)
├── chat/                                # Chat widget system
│   ├── index.ts                         # Chat barrel export
│   ├── types.ts                         # ChatMessage, ChatParticipant, etc.
│   ├── backends/
│   │   ├── types.ts                     # ChatBackend interface
│   │   ├── MockBackend.ts               # Canned responses
│   │   └── FetchBackend.ts              # HTTP POST backend
│   ├── components/
│   │   ├── Transcript.tsx               # Message list + typing
│   │   ├── MessageBubble.tsx            # Single message rendering
│   │   ├── ChatInput.tsx                # Input + send button
│   │   ├── InlinePopover.tsx            # Collapsible popover
│   │   ├── RichContent.tsx              # Links/images in bubbles
│   │   ├── SendIcon.tsx                 # Paper plane SVG
│   │   └── TypingIndicator.tsx          # Animated dots
│   ├── modes/
│   │   ├── InlineChat.tsx               # Simple centered chat
│   │   ├── ThreePaneChat.tsx            # Chat + detail + topics
│   │   ├── MobileChat.tsx               # Full-screen overlay
│   │   ├── PersonaChat.tsx              # Convenience wrapper
│   │   └── three-pane/                  # Sub-components
│   ├── hooks/
│   │   ├── useChatSession.ts            # Core state management
│   │   └── useScrollToBottom.ts         # Auto-scroll behavior
│   ├── css/
│   │   ├── base.css                     # Structural styles
│   │   └── modes/
│   │       ├── inline.css               # Inline mode positioning
│   │       ├── three-pane.css           # Three-pane layout
│   │       └── mobile.css               # Mobile overlay
│   └── themes/                          # 10 theme files (colors, fonts)
├── examples/                            # React/Vite example app
│   └── chat/                            # Chat demo with theme switcher
├── docs/                                # Documentation
│   ├── usage.md                         # Chat Usage & API
│   └── theming.md                       # Chat Theming Guide
├── package.json                         # npm configuration & exports
├── package-lock.json
├── tsconfig.json                        # TypeScript configuration
├── vitest.config.ts                     # Vitest configuration
├── vitest.setup.ts                      # Test setup
├── .claude/                             # Claude Code configuration
└── README.md
```

## Key Files & Components

**Theme System:**
- `src/theme/tokens.css` — Design tokens (colors, fonts, status colors)
- `src/theme/base.css` — Reset, body styles, selection, grain overlay
- `src/theme/ThemeProvider.tsx` — React context for theme management
- `src/theme/ThemeToggle.tsx` — Three-way toggle UI component

**Chat Widget System:**
- `chat/types.ts` — Type definitions (ChatMessage, ChatParticipant, PopoverData)
- `chat/backends/types.ts` — ChatBackend interface for extensibility
- `chat/components/` — Reusable UI components (Transcript, MessageBubble, ChatInput)
- `chat/modes/` — Layout modes (Inline, ThreePane, Mobile, PersonaChat)
- `chat/hooks/` — State management (useChatSession, useScrollToBottom)
- `chat/css/` — CSS styling for structural and mode-specific layouts
- `chat/themes/` — 10 pre-built color themes

**Example Application:**
- `examples/chat/` — React/Vite demo app with theme switcher

**Testing:**
- `vitest.config.ts` — Test runner configuration
- `vitest.setup.ts` — Test environment setup
- 61 tests across 8 test files

**Configuration:**
- `package.json` — npm exports, peer dependencies, dev dependencies
- `tsconfig.json` — TypeScript strict mode
- `.claude/` — Claude Code configuration

## Claude Configuration

**Configuration Files:**
- `.claude/` — Project settings for Claude Code

## Planning & Research Documents

No dedicated planning/research directories. Documentation provided via:
- `docs/usage.md` — Chat Widget Usage & API
- `docs/theming.md` — Chat Theming Guide

## Git History & Current State

**Recent Activity:**
- `ea9fcc9` docs: update all docs for React component library
- `78f81b8` refactor: convert examples to React/Vite, deprecate vanilla JS
- `718af02` chore: add chat exports to package.json, include chat in tsconfig
- `7998d77` feat: add InlineChat, MobileChat, ThreePaneChat modes with CSS
- `670eaed` feat: add shared React chat components
- `af3c41e` feat: add chat types, backend abstraction, core session hook
- `37b6a27` refactor: split light mode tokens into separate opt-in file
- `206b504` feat: add TypeScript type declaration for persona-chat
- `b80c163` feat: add shared layout, components, and markdown CSS
- `34a92b1` refactor: convert to React + TypeScript component library
- `f934aaa` feat: add three-way theme toggle and light mode tokens
- `a5b207e` feat: add agentic theme with design tokens and base styles
- `4b054b4` refactor: restructure repo for git submodule consumption
- `5fdd4b7` feat: canned responses, mobile support, mikefullerton theme
- `8791d1d` docs: comprehensive project guidelines

**Pattern:** Major refactoring to React/TypeScript, comprehensive feature development for chat system, consistent documentation.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Install Dependencies:**
```bash
npm install
```

**Development Server:**
```bash
npm run dev
```

**Build:**
```bash
npm run build
```

**Run Tests:**
```bash
npx vitest run          # Run all tests
npx vitest             # Watch mode
npx vitest --ui        # Web UI
```

**Test Coverage:**
```bash
npx vitest run --coverage
```

## Notes

**Architecture Highlights:**

1. **Modular Exports** — Fine-grained exports for theme, chat components, and modes
2. **Backend Abstraction** — ChatBackend interface allows MockBackend or custom implementations
3. **CSS-Based Theming** — Custom properties for easy theme switching without JS
4. **Multiple Chat Modes** — Inline, ThreePane, Mobile, and PersonaChat layouts
5. **Type-Safe** — Full TypeScript with strict mode enabled
6. **Submodule-Ready** — Designed to be included as git submodule in other projects

**Chat Widget Features:**

- **Modes:** Inline (simple centered), ThreePane (chat + detail + topics), Mobile (overlay), PersonaChat (wrapper)
- **Typing Indicators** — Animated dots while waiting for responses
- **Reactions & Rich Content** — Links and images in message bubbles
- **Auto-Scroll** — Transcript scrolls to latest message
- **Backend Flexibility** — MockBackend for demos, FetchBackend for real APIs
- **10 Themes** — Pre-built color schemes for different contexts

**Theme System:**

- **Design Tokens** — Centralized colors, fonts, status colors in CSS
- **Three-Way Toggle** — Auto (system), Dark, Light modes
- **Light Mode Opt-In** — Split tokens for selective inclusion
- **Grain Overlay** — Optional texture for visual depth
- **Custom Properties** — CSS variables for dynamic theming

**Testing:**

- 61 tests covering backends, hooks, components, and all three modes
- Integration-focused testing with Vitest and Testing Library
- Mock backend for isolated component testing

**Submodule Usage:**

```bash
git submodule add git@github.com:agentic-cookbook/shared-website-components.git
```

Then import components:
```typescript
import { InlineChat, MockBackend } from './shared-website-components/chat'
import './shared-website-components/chat/css/base.css'
import './shared-website-components/chat/css/modes/inline.css'
```

**Documentation:**

- `docs/usage.md` — Complete API reference for chat widget
- `docs/theming.md` — Theming guide with examples
- `examples/chat/` — Working demo application
