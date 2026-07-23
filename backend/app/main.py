from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.website import router as website_router
from app.core.config import settings

app = FastAPI(title="FounderOS — Multi-Agent Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/v1/chat")
app.include_router(website_router, prefix="/api/v1/website")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
