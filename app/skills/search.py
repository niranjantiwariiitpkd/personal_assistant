from app.db.base import SessionLocal
from app.db.models import Note

from app.db.repository import hybrid_search

def search_notes(query: str) -> str:
    results = hybrid_search(query)

    if not results:
        return "I couldn’t find anything related to that."

    response = "Here’s what I found:\n"
    for r in results:
        response += f"- {r}\n"

    return response

