from langgraph.graph import StateGraph, START, END

from .state import AgentState
from .prompts import RESEARCH_PROMPT, MARKETING_PROMPT, FINANCE_PROMPT, MANAGER_PROMPT
from ..services.gemini import generate

MAX_REVISIONS = 1  # caps the Marketing<->Finance back-and-forth so the graph can't loop forever


def _build_transcript(state: AgentState) -> str:
    lines = [f"Founder's request: {state['user_request']}", ""]
    for m in state["messages"]:
        lines.append(f"{m['display_name']}: {m['content']}")
    return "\n".join(lines)


def _append(state: AgentState, agent: str, display_name: str, content: str) -> list:
    return state["messages"] + [
        {"agent": agent, "display_name": display_name, "content": content, "round": state["round"]}
    ]


async def research_node(state: AgentState) -> dict:
    context = f"Founder's request: {state['user_request']}"
    content = await generate(RESEARCH_PROMPT, context)
    return {
        "messages": _append(state, "research", "Research Agent", content),
        "round": state["round"] + 1,
    }


async def marketing_node(state: AgentState) -> dict:
    content = await generate(MARKETING_PROMPT, _build_transcript(state))
    return {
        "messages": _append(state, "marketing", "Marketing Agent", content),
        "round": state["round"] + 1,
    }


async def finance_node(state: AgentState) -> dict:
    content = await generate(FINANCE_PROMPT, _build_transcript(state))
    decision_lines = [l for l in content.splitlines() if l.strip().upper().startswith("DECISION:")]
    approved = bool(decision_lines) and "APPROVE" in decision_lines[-1].upper()
    return {
        "messages": _append(state, "finance", "Finance Agent", content),
        "round": state["round"] + 1,
        "finance_approved": approved,
        "revision_count": state["revision_count"] + (0 if approved else 1),
    }


async def manager_node(state: AgentState) -> dict:
    content = await generate(MANAGER_PROMPT, _build_transcript(state))
    return {
        "messages": _append(state, "manager", "Manager Agent", content),
        "finished": True,
    }


def _route_after_finance(state: AgentState) -> str:
    if state["finance_approved"] or state["revision_count"] > MAX_REVISIONS:
        return "manager"
    return "marketing"


def build_workflow():
    workflow = StateGraph(AgentState)

    workflow.add_node("research", research_node)
    workflow.add_node("marketing", marketing_node)
    workflow.add_node("finance", finance_node)
    workflow.add_node("manager", manager_node)

    workflow.add_edge(START, "research")
    workflow.add_edge("research", "marketing")
    workflow.add_edge("marketing", "finance")
    workflow.add_conditional_edges(
        "finance",
        _route_after_finance,
        {"marketing": "marketing", "manager": "manager"},
    )
    workflow.add_edge("manager", END)

    return workflow.compile()


_compiled_graph = None


def get_graph():
    global _compiled_graph
    if _compiled_graph is None:
        _compiled_graph = build_workflow()
    return _compiled_graph


async def run_workflow(user_request: str, session_id: str) -> AgentState:
    initial_state: AgentState = {
        "user_request": user_request,
        "session_id": session_id,
        "messages": [],
        "round": 0,
        "revision_count": 0,
        "finance_approved": False,
        "finished": False,
    }
    graph = get_graph()
    result = await graph.ainvoke(initial_state)
    return result
