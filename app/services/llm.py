from app.core.intents import Intent

def classify_intent(user_text: str) -> dict:
    text = user_text.lower()
    if any(p in text for p in ["what can you do","what all can you do","help","features","capabilities"]):
        return {"intent": Intent.CAPABILITIES, "text": user_text}

    if any(w in text for w in ["open", "launch", "visit", "go to"]):
        return {"intent": Intent.OPEN_WEBSITE, "text": user_text}

    if any(w in text for w in ["search", "google"]):
        return {"intent": Intent.WEB_SEARCH, "text": user_text}

    if any(w in text for w in ["remember", "remind", "note"]):
        return {"intent": Intent.CREATE_NOTE, "text": user_text}

    if any(w in text for w in ["what", "tell", "show", "about"]):
        return {"intent": Intent.SEARCH_NOTES, "text": user_text}

    return {"intent": Intent.CHAT, "text": user_text}
