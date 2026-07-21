from supabase import create_client, Client
from .config import settings

_supabase_client: Client | None = None


def get_supabase() -> Client | None:
    """
    Returns a Supabase client, or None if credentials aren't configured yet.
    Kept optional on purpose: during early hackathon days you may not have
    a Supabase project wired up, and the agent graph should still run.
    """
    global _supabase_client
    if not settings.SUPABASE_URL or not settings.SUPABASE_SERVICE_KEY:
        return None
    if _supabase_client is None:
        _supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_KEY)
    return _supabase_client
