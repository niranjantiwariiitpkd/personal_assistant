from app.core.skill_registry import SKILL_REGISTRY
from app.core.intents import Intent


def route_intent(intent: Intent, text: str) -> str:
    handler = SKILL_REGISTRY.get(intent)

    if handler:
        return handler(text)

    return "I’m here 🙂 How can I help you?"
