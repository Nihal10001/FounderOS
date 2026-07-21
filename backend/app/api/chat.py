from fastapi import APIRouter, HTTPException

from ..schemas.chat import ChatRequest, ChatResponse, AgentTurn
from ..agents.graph import run_workflow
from ..services.persistence import save_run

router = APIRouter()


@router.post("/invoke", response_model=ChatResponse)
async def invoke_agent(request: ChatRequest):
    try:
        final_state = await run_workflow(request.message, request.session_id)
        await save_run(final_state)

        turns = [AgentTurn(**m) for m in final_state["messages"]]
        final_plan = turns[-1].content if turns else ""

        return ChatResponse(
            session_id=request.session_id,
            turns=turns,
            final_plan=final_plan,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
