# Learn True Facts

## Project Summary

Learn True Facts is a free, public-facing chat application featuring an AI improv comedian persona that blends real historical facts with absurdly plausible fictional details. It's designed as a test bed for a modern tech stack (Cloudflare + Railway) and persona-driven AI applications before scaling to production.

## Type & Tech Stack

- **Project Type:** Full-stack web application with AI chat interface
- **Frontend:** React 19 + Vite + Tailwind CSS 4 + TanStack Router/Query
- **Backend API:** Hono framework + Drizzle ORM + PostgreSQL + Zod validation
- **Admin Portal:** React 19 + Vite + Tailwind CSS 4
- **Dashboard:** React 19 + Vite + Tailwind CSS 4 + D1 SQLite
- **Authentication:** RS256 JWT via shared `agentic-auth-service`
- **Streaming:** Server-Sent Events (SSE) for real-time responses
- **Hosting:** Cloudflare Workers (frontend), Railway (backend/API)
- **LLM Strategy:** Multi-provider abstraction supporting Cloudflare Workers AI, Google Gemini, Groq, Claude (premium)

## GitHub URL

`git@github.com:agentic-cookbook/learntruefacts.git`

## Directory Structure

```
learntruefacts/
├── .git/
└── docs/
    ├── design/
    │   └── initial-idea.md        # Complete product design and architecture
    └── research/
        └── llm-chat-widget-research.md  # Cost analysis, LLM options, infrastructure
```

## Key Files & Components

### `/docs/design/initial-idea.md`
Comprehensive product design document covering:
- Persona design: improv comedian AI making "true facts"
- Core experience: terminal-style chat with typewriter streaming
- Content safety requirements: prompt-level and application-level guards
- Model strategy: abstraction layer for provider switching (free tier, premium tier)
- Architecture: full stack diagram with component breakdown
- Data model: conversations, messages, users, shared_conversations tables
- Authentication: JWT-based with email/password, GitHub OAuth, Google OAuth
- API endpoints: chat, conversation history, sharing, model selection
- Agent registry integration: persona registration in Official Agent Registry
- Test harness: red team testing for character consistency and safety
- Rollout plan: 4 phases from MVP to premium + registry

### `/docs/research/llm-chat-widget-research.md`
Cost analysis and infrastructure research:
- **Claude Haiku pricing:** ~$0.013/conversation at ~6K input tokens + ~1.5K output tokens
- **At 1M conversations:** $13K (standard) → $7.5K (with prompt caching) → $4-5K (both optimizations)
- **Free tier options:** Google Gemini (15 req/min, 1.5K req/day), Groq, OpenRouter, Cloudflare Workers AI
- **Recommended MVP:** Cloudflare Workers AI (zero new infrastructure, zero cost)
- **Self-hosting:** Ollama for local development, vLLM for production GPU deployments

### Key Design Decisions
- Content must be absolutely safe for children (non-negotiable guardrails)
- Persona will have a registered name in the Official Agent Registry
- Model abstraction allows per-user provider selection without UI changes
- Free tier uses Cloudflare Workers AI (Llama 3.1 8B) or Google Gemini
- Premium tier targets Claude models (Haiku/Sonnet/Opus)

## Claude Configuration

No `.claude/` directory exists yet — project is pre-implementation.

## Planning & Research Documents

**Design Phase (Complete):**
- Comprehensive specification including persona behavior, safety guardrails, four-phase rollout, test harness, and agent registry integration

**Research Phase (Complete):**
- Cost analysis showing prompt caching as key optimization ($0.013 → $0.0009 per conversation)
- Free tier economics via Cloudflare Workers AI or Gemini
- Self-hosting vs. API cost tradeoff ($5-10K/month break-even)

**Open Questions from Design:**
- Comedian persona name (required for agent registry)
- Domain availability for `learntruefacts.com`
- Paid tier pricing and gating mechanism
- Apple Sign-In support in auth service
- TTL policy for anonymous conversations
- Rate limits for free anonymous users
- Test harness architecture (separate service vs. admin tooling)

## Git History & Current State

- **Current Branch:** main
- **Commits:** None (fresh repository)
- **Untracked files:** docs/
- **Remote:** origin → `git@github.com:agentic-cookbook/learntruefacts.git`
- **Status:** Ready for initial commit

## Build & Test Commands

Not yet configured — project is in planning phase.

**Planned architecture:**
- Frontend: `npm run build` or `wrangler deploy` for Cloudflare Workers
- Backend: Hono API server deployment to Railway
- Testing: Red team test harness for adversarial content safety testing

## Notes

- **Project Stage:** Design & Research Complete, Implementation Pending
- Part of the "agentic-cookbook" organization with shared infrastructure
- Designed to test new tech stack before scaling to production use with Temporal
- First user-facing AI persona application in the portfolio
- Stress-tests: content safety at scale, model abstraction, conversation recording, persona registration

**Integration Points:**
- Shared auth service (`agentic-auth-service`) for JWT auth
- Official Agent Registry for persona registration
- Cloudflare Workers for frontend hosting
- Railway for backend API

**Next Steps:**
1. Name the comedian persona
2. Verify domain availability
3. Initial git commit with docs
4. Create `.claude/` configuration
5. Begin Phase 1: MVP with Cloudflare Workers AI backend
