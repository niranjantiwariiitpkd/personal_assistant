from sentence_transformers import SentenceTransformer

# lightweight, fast, CPU-friendly
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list[float]:
    embedding = _model.encode(text)
    return embedding.tolist()
