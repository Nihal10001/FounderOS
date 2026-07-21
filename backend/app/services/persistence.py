from ..core.supabase import get_supabase
from ..agents.state import AgentState


async def save_run(state: AgentState) -> None:
    client = get_supabase()
    if client is None:
        return  # no Supabase configured yet — skip silently, don't break the demo
    try:
        client.table("messages").insert(
            [
                {
                    "session_id": state["session_id"],
                    "agent": m["agent"],
                    "display_name": m["display_name"],
                    "content": m["content"],
                    "round": m["round"],
                }
                for m in state["messages"]
            ]
        ).execute()
    except Exception as e:
        # Log and move on — persistence should never take down a live demo
        print(f"[persistence] failed to save run: {e}")
