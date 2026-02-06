# app/core/intent.py
def detect_intent(text: str) -> str:
    text = text.lower()

    if "note" in text or "remember" in text:
        return "CREATE_NOTE"

    return "UNKNOWN"
