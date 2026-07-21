from google import genai
from ..core.config import settings

_client: genai.Client | None = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.GEMINI_API_KEY)
    return _client


async def generate(system_prompt: str, context: str) -> str:
    """
    Single shared LLM call used by every agent node.
    `system_prompt` sets the agent's persona/role.
    `context` is the conversation-so-far that this agent needs to read.
    """
    client = _get_client()
    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=context,
        config={"system_instruction": system_prompt},
    )
    return response.text.strip()
