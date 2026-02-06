from app.db.base import SessionLocal
from app.db.models import Note
from app.services.embeddings import embed_text

def reembed_all_notes():
    db = SessionLocal()
    try:
        notes = db.query(Note).all()
        print(f"Found {len(notes)} notes")

        for note in notes:
            note.embedding = embed_text(note.content)

        db.commit()
        print(" Re-embedding complete")

    finally:
        db.close()

if __name__ == "__main__":
    reembed_all_notes()
