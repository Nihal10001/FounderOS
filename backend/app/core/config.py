from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_KEY: str = ""
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-3.5-flash"
    GROQ_API_KEY: str = ""

    # Each agent group can use a different provider+model — gives each group
    # its own quota pool instead of all agents competing for one model's limit.
    RESEARCH_MANAGER_PROVIDER: str = "gemini"
    RESEARCH_MANAGER_MODEL: str = "gemini-3.5-flash"
    FINANCE_MARKETING_PROVIDER: str = "groq"
    FINANCE_MARKETING_MODEL: str = "llama-3.3-70b-versatile"
    CODEGEN_PROVIDER: str = "groq"
    CODEGEN_MODEL: str = "llama-3.1-8b-instant"

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()