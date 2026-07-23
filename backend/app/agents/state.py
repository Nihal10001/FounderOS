from typing import TypedDict, List


class AgentMessage(TypedDict):
    agent: str
    display_name: str
    content: str
    round: int


class AgentState(TypedDict):
    session_id: str
    messages: List[AgentMessage]
    round: int
    revision_count: int
    finance_approved: bool
    finished: bool
