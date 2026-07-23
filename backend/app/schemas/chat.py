from pydantic import BaseModel
from typing import List, Optional


class AgentTurn(BaseModel):
    agent: str          # "founder" | "research" | "marketing" | "finance" | "manager"
    display_name: str   # "Founder", "Research Agent", "Finance Agent", etc.
    content: str
    round: int


class ChatRequest(BaseModel):
    message: str
    session_id: str
    history: Optional[List[AgentTurn]] = None  # prior turns, sent back for a follow-up round


class ChatResponse(BaseModel):
    session_id: str
    turns: List[AgentTurn]
    final_plan: str
