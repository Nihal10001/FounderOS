import asyncio
import httpx
from ..core.config import settings

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MAX_RETRIES = 3
BASE_DELAY_SECONDS = 2  # doubles each retry: 2s, 4s, 8s


async def generate(system_prompt: str, context: str, model: str) -> str:
    """
    Same shape/contract as services/gemini.generate(), so the router can swap
    providers transparently. Uses Groq's OpenAI-compatible chat completions
    endpoint — no special SDK needed.
    """
    last_error: Exception | None = None

    async with httpx.AsyncClient(timeout=60) as client:
        for attempt in range(MAX_RETRIES):
            try:
                res = await client.post(
                    GROQ_API_URL,
                    headers={
                        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": context},
                        ],
                    },
                )
                if res.status_code >= 400:
                    raise ValueError(f"Groq API error ({res.status_code}): {res.text}")
                data = res.json()
                return data["choices"][0]["message"]["content"].strip()
            except Exception as e:
                last_error = e
                is_last_attempt = attempt == MAX_RETRIES - 1
                if is_last_attempt:
                    break
                delay = BASE_DELAY_SECONDS * (2**attempt)
                print(f"[groq] attempt {attempt + 1} failed ({e}); retrying in {delay}s")
                await asyncio.sleep(delay)

    raise last_error
