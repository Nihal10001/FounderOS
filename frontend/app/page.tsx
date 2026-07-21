"use client";

import { useState } from "react";
import { invokeAgents, AgentTurn } from "@/lib/api";
import { AGENT_META, AgentKey } from "@/lib/agents";
import { AgentBubble } from "@/components/AgentBubble";
import { AgentStatusBadge } from "@/components/AgentStatusBadge";
import { ChatComposer } from "@/components/ChatComposer";

const AGENT_ORDER: AgentKey[] = ["research", "marketing", "finance", "manager"];
const REVEAL_DELAY_MS = 900; // spaces out turns so it reads like a live discussion, not a wall of text

export default function Home() {
  const [visibleTurns, setVisibleTurns] = useState<AgentTurn[]>([]);
  const [activeAgent, setActiveAgent] = useState<AgentKey | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [sessionId] = useState(() => crypto.randomUUID());

  async function handleSubmit(message: string) {
    setError(null);
    setVisibleTurns([]);
    setLoading(true);
    setActiveAgent("research");

    try {
      const result = await invokeAgents(message, sessionId);

      // Reveal turns sequentially for a "watch the team discuss it live" effect.
      for (let i = 0; i < result.turns.length; i++) {
        const turn = result.turns[i];
        setActiveAgent(turn.agent as AgentKey);
        await new Promise((r) => setTimeout(r, REVEAL_DELAY_MS));
        setVisibleTurns((prev) => [...prev, turn]);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
      setActiveAgent(null);
    }
  }

  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col gap-6 px-6 py-10">
      <header>
        <h1 className="text-2xl font-semibold text-on-surface">Your Virtual Startup Team</h1>
        <p className="mt-1 text-sm text-on-surface-variant">
          Describe what you want to launch. Research, Marketing, Finance, and your Manager will
          work it out together — live.
        </p>
      </header>

      <div className="flex flex-wrap gap-2">
        {AGENT_ORDER.map((agent) => (
          <AgentStatusBadge key={agent} agent={agent} active={activeAgent === agent} />
        ))}
      </div>

      <ChatComposer onSubmit={handleSubmit} disabled={loading} />

      {error && (
        <div className="rounded-md border border-error/40 bg-error-container/10 p-3 text-sm text-error">
          {error}
        </div>
      )}

      <section className="flex flex-col gap-3">
        {visibleTurns.map((turn, i) => (
          <AgentBubble key={i} turn={turn} />
        ))}

        {loading && activeAgent && (
          <div className="flex items-center gap-2 text-xs text-outline">
            <span
              className={`h-2 w-2 rounded-full ${AGENT_META[activeAgent].dot} status-pulse`}
            />
            {AGENT_META[activeAgent].label} is thinking...
          </div>
        )}

        {!loading && visibleTurns.length === 0 && !error && (
          <div className="rounded-md border border-dashed border-outline-variant p-8 text-center text-sm text-outline">
            Your team is idle. Send a request above to kick off the discussion.
          </div>
        )}
      </section>
    </main>
  );
}
