# app/core/intent.py
def detect_intent(text: str) -> str:
    text = text.lower()

    if "note" in text:
        return "CREATE_NOTE"
    if "remind" in text:
        return "SET_REMINDER"

    return "GENERAL_CHAT"
