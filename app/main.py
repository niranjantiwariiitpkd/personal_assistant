# app/main.py
from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.health import router as health_router

app = FastAPI(title="Personal Assistant")

app.include_router(health_router)
app.include_router(chat_router)
