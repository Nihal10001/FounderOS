# AI Org Chart — Multi-Agent Startup Team

## What this is
A working multi-agent system: a founder describes a product idea, and Research,
Marketing, and Finance agents discuss it — with Finance able to push back and send
Marketing back to revise — before a Manager agent synthesizes the final plan.
This matches the example flow exactly:

```
Research  -> market/competitor findings
Marketing -> pricing/positioning proposal
Finance   -> APPROVE or REVISE (with reason)
Marketing -> revises if REVISE (max 1 revision loop, prevents infinite loops)
Manager   -> final approved plan
```

## Structure

```
ai-org-chart/
├── backend/            FastAPI + LangGraph multi-agent orchestration
│   └── app/
│       ├── agents/     graph.py = the actual StateGraph, prompts.py = agent personas
│       ├── api/        chat.py = /invoke endpoint
│       ├── core/       config.py, supabase.py
│       ├── schemas/    request/response models (now includes AgentTurn)
│       └── services/   gemini.py (real LLM calls), persistence.py (optional Supabase save)
├── frontend/            Next.js + Tailwind, tokens ported from DESIGN.md
│   ├── app/            page.tsx = the live agent-conversation UI
│   ├── components/      AgentBubble, AgentStatusBadge, ChatComposer
│   └── lib/             api.ts (backend client), agents.ts (per-agent colors)
└── docs/DESIGN.md       original design reference
```

## Running it

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in GEMINI_API_KEY at minimum; Supabase optional
uvicorn app.main:app --reload
```
Runs on `http://localhost:8000`. Check `/health`.

### Frontend
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```
Runs on `http://localhost:3000`.

## What changed from the original skeleton
- `agents_graph.py` was an unused empty stub — replaced with a real LangGraph
  `StateGraph` (`backend/app/agents/graph.py`) with 4 nodes and a conditional edge.
- `chat.py` called Gemini directly, bypassing agents entirely — now it runs the graph.
- `gemini.py` returned a hardcoded string — now makes a real `google-genai` call.
- Added `AgentTurn` to the response schema so the frontend can render each agent's
  turn separately instead of one final blob.
- Added missing `__init__.py` files (the original structure would have failed to
  import as a package).
- Frontend was a static, non-interactive Stitch HTML export — rebuilt as a real
  Next.js app wired to the backend, with the same color tokens/typography from
  `DESIGN.md`.
- Persistence to Supabase is wrapped in try/except and no-ops if unconfigured, so
  a missing Supabase project never breaks the live demo.

## Next steps (suggested order)
1. Drop in your `GEMINI_API_KEY` and run one end-to-end request to confirm the
   graph's conditional routing actually triggers (try a very low price like
   ₹199 to force a Finance REVISE).
2. Wire the Supabase tables (`messages`) if you want session history/replay.
3. Add the org-chart/dashboard/kanban views from the original mockup as
   additional pages once the core agent loop is solid — don't build those before
   the agent loop works, since that's what judges will actually watch.
