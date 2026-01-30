# app/core/assistant.py
from app.core.intent import detect_intent

def handle_input(text: str) -> str:
    intent = detect_intent(text)

    # For now, simple response
    return f"I detected intent: {intent}"
