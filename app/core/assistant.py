from app.services.llm import classify_intent
from app.core.orchestrator import route_intent

def handle_input(user_text: str) -> str:
    result = classify_intent(user_text)

    intent = result["intent"]
    text = result["text"]   # 👈 THIS WAS MISSING / WRONG

    return route_intent(intent, text)
