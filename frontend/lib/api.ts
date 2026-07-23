const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export type AgentTurn = {
  agent: "founder" | "research" | "marketing" | "finance" | "manager";
  display_name: string;
  content: string;
  round: number;
};

export type ChatResponse = {
  session_id: string;
  turns: AgentTurn[];
  final_plan: string;
};

export async function invokeAgents(
  message: string,
  sessionId: string,
  history: AgentTurn[] = []
): Promise<ChatResponse> {
  const res = await fetch(`${API_BASE}/api/v1/chat/invoke`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, session_id: sessionId, history }),
  });

  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`Agent workflow failed: ${detail}`);
  }

  return res.json();
}
