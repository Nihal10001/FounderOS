from ..core.config import settings
from . import gemini as gemini_provider
from . import groq as groq_provider

# Each group maps to a (provider, model) pair, independently configurable.
# Splitting groups across providers/models gives each its own quota pool.
_GROUP_CONFIG = {
    "research_manager": (settings.RESEARCH_MANAGER_PROVIDER, settings.RESEARCH_MANAGER_MODEL),
    "finance_marketing": (settings.FINANCE_MARKETING_PROVIDER, settings.FINANCE_MARKETING_MODEL),
    "codegen": (settings.CODEGEN_PROVIDER, settings.CODEGEN_MODEL),
}


async def generate_for(group: str, system_prompt: str, context: str) -> str:
    if group not in _GROUP_CONFIG:
        raise ValueError(f"Unknown agent group '{group}'")

    provider, model = _GROUP_CONFIG[group]

    if provider == "groq":
        return await groq_provider.generate(system_prompt, context, model=model)
    if provider == "gemini":
        return await gemini_provider.generate(system_prompt, context, model=model)

    raise ValueError(f"Unknown provider '{provider}' for group '{group}'")