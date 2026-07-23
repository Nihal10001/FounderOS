import { AGENT_META, AgentKey } from "@/lib/agents";
import type { AgentTurn } from "@/lib/api";

export function AgentBubble({ turn }: { turn: AgentTurn }) {
  const meta = AGENT_META[turn.agent as AgentKey];
  const isManager = turn.agent === "manager";
  const isFounder = turn.agent === "founder";

  return (
    <div
      className={`rounded-md border-l-4 ${meta.border} bg-surface-container-low p-4 ${
        isManager ? "ring-1 ring-primary-container/50" : ""
      } ${isFounder ? "ml-auto max-w-[85%] bg-surface-container-high" : ""}`}
    >
      <div className="mb-1 flex items-center justify-between">
        <span className="text-sm font-semibold" style={{ color: meta.color }}>
          {meta.label}
        </span>
        {isManager && (
          <span className="rounded-full bg-primary-container/20 px-2 py-0.5 text-[10px] uppercase tracking-wide text-primary">
            Final Plan
          </span>
        )}
      </div>
      <p className="text-sm leading-relaxed text-on-surface-variant whitespace-pre-wrap">
        {turn.content}
      </p>
    </div>
  );
}
