# app/api/chat.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.assistant import handle_input

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = handle_input(request.message)
    return ChatResponse(response=reply)
