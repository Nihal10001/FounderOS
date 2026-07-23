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


async def generate(system_prompt: str, context: str, model: str) -> str:
    """
    Single-model call with retry-with-backoff for transient errors (like a
    503 UNAVAILABLE spike). Cross-model/cross-provider fallback is handled
    one level up, in llm_router.py — this function only owns retrying the
    one model it's given.
    """
    client = _get_client()
    last_error: Exception | None = None

    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=model,
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
            print(f"[gemini:{model}] attempt {attempt + 1} failed ({e}); retrying in {delay}s")
            await asyncio.sleep(delay)

    raise last_error
