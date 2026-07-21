from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    message: str
    session_id: str


class AgentTurn(BaseModel):
    agent: str          # "research" | "marketing" | "finance" | "manager"
    display_name: str   # "Research Agent", "Finance Agent", etc.
    content: str
    round: int


class ChatResponse(BaseModel):
    session_id: str
    turns: List[AgentTurn]
    final_plan: str
