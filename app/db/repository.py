# app/db/repository.py
from app.db.base import SessionLocal
from app.db.models import Note
from app.db.base import SessionLocal
from app.db.models import Note
from app.services.embeddings import embed_text
from app.services.similarity import cosine_similarity

def save_note(text: str):
    db = SessionLocal()
    try:
        note = Note(content=text)
        db.add(note)
        db.commit()
        db.refresh(note)
        return note
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def semantic_search_with_scores(query: str, limit: int = 5):
    db = SessionLocal()
    try:
        q_vec = embed_text(query)
        notes = db.query(Note).filter(Note.embedding.isnot(None)).all()

        scored = []
        for n in notes:
            score = cosine_similarity(q_vec, n.embedding)
            scored.append((score, n.content))

        scored.sort(reverse=True, key=lambda x: x[0])
        return scored[:limit]
    finally:
        db.close()

def keyword_search(query: str, limit: int = 5):
    db = SessionLocal()
    try:
        results = (
            db.query(Note)
            .filter(Note.content.ilike(f"%{query}%"))
            .limit(limit)
            .all()
        )
        return [n.content for n in results]
    finally:
        db.close()

def hybrid_search(query: str, limit: int = 3):
    semantic_results = semantic_search_with_scores(query)

    # If we have ANY semantic results, return the top ones
    if semantic_results:
        return [content for _, content in semantic_results[:limit]]

    # Only if semantic results are empty, try keyword search
    return keyword_search(query)
