from app.core.config import EXECUTION_MODE
import webbrowser
import re
import urllib.parse

KNOWN_SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
}

COMMAND_WORDS = ["open", "launch", "visit", "go", "to", "please"]

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    words = [w for w in text.split() if w not in COMMAND_WORDS]
    return " ".join(words)

def open_website(text: str) -> str:
    normalized = normalize(text)

    print("OPEN_WEBSITE NORMALIZED:", normalized)  # debug

    for site, url in KNOWN_SITES.items():
        if site in normalized:
            if EXECUTION_MODE == "local":
                webbrowser.open(url)
                return f"Opening {site.capitalize()} 🚀"
            else:
                return f"Here’s the link to {site.capitalize()}:\n{url}"

    return "I don’t know which website you want to open."


def web_search(text: str) -> str:
    query = urllib.parse.quote(text)
    url = f"https://www.google.com/search?q={query}"

    if EXECUTION_MODE == "local":
        webbrowser.open(url)
        return f"Searching the web for: {text}"
    else:
        return f"Search link:\n{url}"
