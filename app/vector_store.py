
import faiss
import numpy as np

def search_vector_db(query_embedding):
    index = faiss.IndexFlatL2(len(query_embedding))
    index.add(np.array([query_embedding]))
    _, I = index.search(np.array([query_embedding]), k=1)
    return f"Results for embedding index {I}"
