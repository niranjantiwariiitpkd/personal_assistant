from app.services.online_llm import chat_with_llm
from app.services.llm import classify_intent
from app.core.orchestrator import route_intent
from app.core.intents import Intent

def handle_chat(text: str) -> str:
    result = classify_intent(text)

    # Capabilities still handled by rules
    if result["intent"] == Intent.CAPABILITIES:
        return route_intent(result["intent"], text)

    # Everything else → online LLM
    return chat_with_llm(text)
