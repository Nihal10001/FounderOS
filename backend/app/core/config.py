from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_KEY: str = ""

    GEMINI_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    # Every agent group has an explicit primary + fallback (provider, model)
    # pair. Primary and fallback can be different providers entirely.

    RESEARCH_MANAGER_PRIMARY_PROVIDER: str = "gemini"
    RESEARCH_MANAGER_PRIMARY_MODEL: str = "gemini-flash-lite-latest"
    RESEARCH_MANAGER_FALLBACK_PROVIDER: str = "gemini"
    RESEARCH_MANAGER_FALLBACK_MODEL: str = "gemini-3.5-flash"

    FINANCE_MARKETING_PRIMARY_PROVIDER: str = "groq"
    FINANCE_MARKETING_PRIMARY_MODEL: str = "llama-3.3-70b-versatile"
    FINANCE_MARKETING_FALLBACK_PROVIDER: str = "groq"
    FINANCE_MARKETING_FALLBACK_MODEL: str = "llama-3.3-70b-versatile"

    CODEGEN_PRIMARY_PROVIDER: str = "gemini"
    CODEGEN_PRIMARY_MODEL: str = "gemini-3.1-flash-lite"
    CODEGEN_FALLBACK_PROVIDER: str = "groq"
    CODEGEN_FALLBACK_MODEL: str = "llama-3.1-8b-instant"

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()