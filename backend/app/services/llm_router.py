from ..core.config import settings
from . import gemini as gemini_provider
from . import groq as groq_provider

# Each group has an independent primary AND fallback (provider, model) pair.
# Primary and fallback can be different providers entirely — e.g. codegen's
# primary is Gemini but its fallback is Groq — so one provider being down or
# low-quality for a task doesn't take out the whole group.
_GROUP_CONFIG = {
    "research_manager": {
        "primary": (settings.RESEARCH_MANAGER_PRIMARY_PROVIDER, settings.RESEARCH_MANAGER_PRIMARY_MODEL),
        "fallback": (settings.RESEARCH_MANAGER_FALLBACK_PROVIDER, settings.RESEARCH_MANAGER_FALLBACK_MODEL),
    },
    "finance_marketing": {
        "primary": (settings.FINANCE_MARKETING_PRIMARY_PROVIDER, settings.FINANCE_MARKETING_PRIMARY_MODEL),
        "fallback": (settings.FINANCE_MARKETING_FALLBACK_PROVIDER, settings.FINANCE_MARKETING_FALLBACK_MODEL),
    },
    "codegen": {
        "primary": (settings.CODEGEN_PRIMARY_PROVIDER, settings.CODEGEN_PRIMARY_MODEL),
        "fallback": (settings.CODEGEN_FALLBACK_PROVIDER, settings.CODEGEN_FALLBACK_MODEL),
    },
}


async def _call(provider: str, model: str, system_prompt: str, context: str) -> str:
    if provider == "groq":
        return await groq_provider.generate(system_prompt, context, model=model)
    if provider == "gemini":
        return await gemini_provider.generate(system_prompt, context, model=model)
    raise ValueError(f"Unknown provider '{provider}'")


async def generate_for(group: str, system_prompt: str, context: str) -> str:
    if group not in _GROUP_CONFIG:
        raise ValueError(f"Unknown agent group '{group}'")

    cfg = _GROUP_CONFIG[group]
    primary_provider, primary_model = cfg["primary"]
    fallback_provider, fallback_model = cfg["fallback"]

    try:
        return await _call(primary_provider, primary_model, system_prompt, context)
    except Exception as primary_error:
        if (primary_provider, primary_model) == (fallback_provider, fallback_model):
            raise  # no distinct fallback configured, nothing more we can do
        print(
            f"[llm_router:{group}] primary {primary_provider}/{primary_model} failed "
            f"entirely ({primary_error}); falling back to {fallback_provider}/{fallback_model}"
        )
        return await _call(fallback_provider, fallback_model, system_prompt, context)
