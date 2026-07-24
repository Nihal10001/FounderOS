# FounderOS — Multi-Agent Startup Team


## Structure

```
ai-org-chart/
├── backend/            FastAPI + LangGraph multi-agent orchestration
│   └── app/
│       ├── agents/     graph.py = the actual StateGraph, prompts.py = agent personas
│       ├── api/        chat.py = /invoke (agents), website.py = /generate + /deploy
│       ├── core/       config.py, supabase.py
│       ├── schemas/    chat.py, website.py
│       └── services/   gemini.py, groq.py (same generate() contract, swappable),
│                        llm_router.py (per-group primary/fallback routing),
│                        codegen.py, github_deploy.py, persistence.py
├── frontend/            Next.js + Tailwind, tokens ported from DESIGN.md
│   ├── app/
│   │   ├── page.tsx        the agent-team chat UI
│   │   └── website/page.tsx  standalone "Idea → Website" builder
│   ├── components/
│   │   ├── (agent chat components)
│   │   └── website/     IdeaForm, WebsitePreview (Sandpack), DeployPanel
│   └── lib/             api.ts (agent client), website-api.ts (builder client)
└── docs/DESIGN.md       original design reference
```


## Two features

1. **Virtual Startup Team** (`/`) — Research→Marketing→Finance→Manager multi-agent
   discussion. Finance can force a Marketing revision (capped at 1 loop). Follow-up
   messages continue the same transcript rather than starting over.
2. **Idea → Website** (`/website`) — standalone. Generates a live, sandboxed
   (Sandpack) React landing page from an idea, with an optional one-hop deploy:
   push to a new GitHub repo (user-supplied PAT, never stored) → Vercel's own
   `/new/clone` import link finishes the deploy on Vercel's side.

## LLM setup

Each of 3 agent groups (`research_manager`, `finance_marketing`, `codegen`) has an
independent **primary + fallback** provider/model pair, configured entirely via env
vars — see `backend/.env.example`. Currently running fully on **Groq** (free, no
card) across 4 separate model quota buckets, since the Gemini key is on hold pending
a billing-verification prepayment we're not doing right now. Any group can be
flipped back to `gemini` later with zero code changes if that gets resolved.

## Running it

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in GROQ_API_KEY at minimum; Gemini/Supabase optional
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

## Persistence

Supabase is connected (`messages` table: session_id, agent, display_name, content,
round). `services/persistence.py` no-ops silently if `SUPABASE_URL`/
`SUPABASE_SERVICE_KEY` are ever unset, so a misconfigured Supabase project never
breaks a live run — it just won't log that run.

## Deployment plan

- **Frontend → Vercel** (root dir `frontend`, env `NEXT_PUBLIC_API_URL` = backend URL)
- **Backend → Render free tier** (root dir `backend`, build `pip install -r
  requirements.txt`, start `uvicorn app.main:app --host 0.0.0.0 --port $PORT`).
  Free tier sleeps after 15 min idle — hit `/health` to warm it up before a live demo.
- After both are up: update backend's `CORS_ORIGINS` env var on Render to include
  the real Vercel URL, not just `localhost:3000`, or the deployed frontend can't
  reach the deployed backend.
  
## Roadmap

Ideas for extending this further: org-chart/dashboard/kanban views on top of the
existing agent data, session history/replay from the Supabase-backed transcript,
and richer tool access for agents (live web search, calendar, etc.) beyond pure
text generation.