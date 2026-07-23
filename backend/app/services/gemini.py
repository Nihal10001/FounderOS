import asyncio
from google import genai
from ..core.config import settings

_client: genai.Client | None = None

MAX_RETRIES = 3
BASE_DELAY_SECONDS = 2  # doubles each retry: 2s, 4s, 8s


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.GEMINI_API_KEY)
    return _client


async def generate(system_prompt: str, context: str, model: str | None = None) -> str:
    """
    Single shared LLM call used by every agent node.
    `system_prompt` sets the agent's persona/role.
    `context` is the conversation-so-far that this agent needs to read.
    `model` overrides settings.GEMINI_MODEL — lets different agent groups use
    different Gemini models, which have separate quota buckets.
    Retries on transient errors (like Gemini's 503 UNAVAILABLE under load)
    with exponential backoff, since a single flaky call shouldn't kill an
    entire multi-agent run mid-demo.
    """
    client = _get_client()
    use_model = model or settings.GEMINI_MODEL
    last_error: Exception | None = None

    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=use_model,
                contents=context,
                config={"system_instruction": system_prompt},
            )
            return response.text.strip()
        except Exception as e:
            last_error = e
            is_last_attempt = attempt == MAX_RETRIES - 1
            if is_last_attempt:
                break
            delay = BASE_DELAY_SECONDS * (2**attempt)
            print(f"[gemini] attempt {attempt + 1} failed ({e}); retrying in {delay}s")
            await asyncio.sleep(delay)

    raise last_error
