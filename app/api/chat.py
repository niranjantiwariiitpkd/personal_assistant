# app/api/chat.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.assistant import handle_input
from app.core.chat_mode import handle_chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    mode: str = "task"   # "task" or "chat"

class ChatResponse(BaseModel):
    response: str

@router.post("/chat")
def chat(request: ChatRequest):
    if request.mode == "chat":
        return {"response": handle_chat(request.message)}
    else:
        return {"response": handle_input(request.message)}
