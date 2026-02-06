from app.db.repository import save_note

def create_note(text: str) -> str:
    note = save_note(text)
    timestamp = note.created_at.strftime("%Y-%m-%d %H:%M")
    return f"Note saved at {timestamp}: {note.content}"
