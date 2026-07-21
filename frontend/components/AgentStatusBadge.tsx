import { AGENT_META, AgentKey } from "@/lib/agents";

export function AgentStatusBadge({ agent, active }: { agent: AgentKey; active: boolean }) {
  const meta = AGENT_META[agent];
  return (
    <div className="flex items-center gap-2 rounded-full bg-surface-container-high px-3 py-1 text-xs text-on-surface-variant">
      <span
        className={`h-2 w-2 rounded-full ${meta.dot} ${active ? "status-pulse" : "opacity-40"}`}
      />
      <span>{meta.label}</span>
      <span className="text-outline">{active ? "· Processing" : "· Idle"}</span>
    </div>
  );
}
