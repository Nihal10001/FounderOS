import json
import re

from .gemini import generate

CODEGEN_SYSTEM_PROMPT = """You are a code-generation engine. Given a product idea, generate a
single-page React landing site.

Output ONLY a valid JSON object — no markdown fences, no commentary, no explanation.
The JSON keys are file paths, values are the full file contents as strings.

Required keys:
- "/App.js": a default-exported React functional component. Use plain CSS class
  names (defined in styles.css) — do NOT use Tailwind or any external UI library,
  since the sandbox has no build step for CSS frameworks.
- "/styles.css": plain CSS backing the class names used in App.js.

Keep it to one landing page: hero section, 2-3 feature blocks, and a call-to-action.
Make the copy specific to the idea given, not generic placeholder text.
"""


def _extract_json(raw: str) -> str:
    """Strips markdown fences if the model added them despite instructions."""
    cleaned = raw.strip()
    fence_match = re.match(r"^```(?:json)?\s*(.*?)\s*```$", cleaned, re.DOTALL)
    if fence_match:
        return fence_match.group(1)
    return cleaned


async def generate_website(idea: str) -> dict[str, str]:
    raw = await generate(CODEGEN_SYSTEM_PROMPT, f"Product idea: {idea}")
    try:
        files = json.loads(_extract_json(raw))
    except json.JSONDecodeError as e:
        raise ValueError(f"Model did not return valid JSON: {e}\nRaw output: {raw[:500]}")

    if "/App.js" not in files:
        raise ValueError("Generated output is missing required '/App.js' file")

    return files
