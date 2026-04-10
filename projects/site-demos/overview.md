# Site Demos

## Project Summary

A repository for demo websites showcasing UI components and interaction patterns. Currently features a persona chat demo with multi-pane layout showing chat, detail pane, and topics sidebar. Serves as test bed for shared website components and design exploration.

## Type & Tech Stack

**Project Type:** Demo website/showcase

**Core Technologies:**
- **React** — Component framework
- **TypeScript** — Type-safe development
- **HTML/CSS** — Markup and styling
- **Vite** — Build tool and dev server
- **shared-website-components** — Submodule dependency for chat widgets

**Architecture:**
- React-based demo applications
- Multi-pane layout system
- Git submodule dependency on shared-website-components

## GitHub URL

`git@github.com:agentic-cookbook/site-demos.git`

https://github.com/agentic-cookbook/site-demos

## Directory Structure

```
site-demos/
├── .claude/                             # Claude Code configuration
├── docs/                                # Documentation
├── persona-chat/                        # Chat demo application
│   ├── src/                             # React source code
│   │   ├── components/                  # UI components
│   │   ├── App.tsx                      # Root component
│   │   ├── styles/                      # CSS styling
│   │   └── [other source files]
│   ├── public/                          # Static assets
│   ├── package.json                     # Dependencies
│   ├── vite.config.ts                   # Vite configuration
│   └── tsconfig.json                    # TypeScript config
├── .gitignore
└── README.md
```

## Key Files & Components

**Demo Application:**
- `persona-chat/` — Main demo showcasing persona chat widget
  - Multi-pane layout: chat transcript, detail pane, topics sidebar
  - Arrow key navigation between messages
  - Click-to-select message topics
  - Responsive layout with flexible panning

**Layout System:**
- Separated three-pane layout with chat, details, and topics
- SVG connector lines between related panes
- Full-width topic and detail panes
- Arrow key navigation support

**Configuration:**
- `.claude/` — Claude Code configuration
- `docs/` — Documentation and design notes

## Claude Configuration

**Configuration Files:**
- `.claude/` — Project settings for Claude Code

## Planning & Research Documents

No dedicated planning/research directories. Documentation provided via:
- `docs/` — Design documentation

## Git History & Current State

**Recent Activity:**
- `4213bca` fix: remove pc-has-detail class, rows now full-width
- `c2c0a4f` feat: arrow keys navigate all messages, not just topics
- `5449b45` fix: rebalance pane flex ratios
- `3fc67ad` fix: pin detail arrow to right edge, fix arrow navigation
- `610e56c` fix: redirect printable keystrokes to chat input when unfocused
- `9bb4223` feat: arrow keys, selected highlight, separated layout
- `18341f1` Click transcript message to select topic and details
- `bba7e28` Add separated layout with SVG connector lines
- `61d4eb2` Fix detail arrow: append to message row, not bubble
- `3962dd1` Style detail arrow: right-aligned in bubble
- `1ceafa2` Move topics index to far right
- `a35dad6` Show images in detail pane, add arrow to messages
- `25641f5` Make detail pane 2x wider than chat pane
- `032cc11` Default to topic+details view, narrow topics column
- `70e2cc6` Keep same frame size for both modes

**Pattern:** Active UI development with layout refinement, keyboard navigation, and interaction improvements.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Install Dependencies:**
```bash
cd persona-chat && npm install
```

**Development Server:**
```bash
cd persona-chat && npm run dev
```

**Build:**
```bash
cd persona-chat && npm run build
```

**Preview:**
```bash
cd persona-chat && npm run preview
```

## Notes

**Architecture Highlights:**

1. **Multi-Pane Layout** — Three-pane system (chat, detail, topics) with flexible sizing
2. **Keyboard Navigation** — Arrow keys for message navigation and pane selection
3. **SVG Connectors** — Visual lines connecting related messages across panes
4. **Responsive Design** — Flexible layout that adapts to screen size
5. **Shared Components** — Uses shared-website-components for chat functionality

**Layout System:**

- **Chat Pane** — Transcript of messages with optional detail arrow
- **Detail Pane** — Content related to selected message (2x width of topics)
- **Topics Pane** — Index of topics on far right with selectable items
- **Separated View** — Optional separated layout mode with connector lines
- **Full-Width Rows** — Messages expand full width with proper alignment

**Keyboard Interactions:**

- **Arrow Keys** — Navigate between messages and across panes
- **Enter** — Send message (when focused on input)
- **Escape** — Deselect current item
- **Typing** — Printable keystrokes redirect to chat input when unfocused

**UI Features:**

- **Selected Highlight** — Visual indication of selected message
- **Detail Arrow** — Icon on messages with associated details
- **Responsive Panes** — Flex-based layout with configurable ratios
- **Input Focus** — Smart focus management for keyboard interaction
- **Visual Feedback** — Transitions and hover states

**Development Workflow:**

Serves as test bed for shared-website-components designs. Changes to layout, interaction patterns, and UI components are validated here before promotion to shared library.

**Purpose:**

Acts as showcase and development environment for:
- Multi-pane chat interface patterns
- Keyboard navigation improvements
- Layout responsiveness
- Integration of shared components
- UI/UX experimentation
