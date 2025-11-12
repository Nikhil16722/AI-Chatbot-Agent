import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load the model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, top_k=3):
    # Load the FAISS index and stored documents
    index = faiss.read_index("app/kb.index")

    with open("app/kb_docs.pkl", "rb") as f:
        docs = pickle.load(f)

    # Encode query
    query_vector = model.encode([query])
    D, I = index.search(np.array(query_vector).astype("float32"), top_k)

    # Return top matching context texts (not dicts!)
    return [docs[i]["text"] for i in I[0]]
