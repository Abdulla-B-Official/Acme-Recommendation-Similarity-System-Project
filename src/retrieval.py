import os
import faiss

INDEX_PATH = os.path.join("model_artifacts", "faiss_index.bin")

# Load index if file exists
if os.path.exists(INDEX_PATH):
    faiss_index = faiss.read_index(INDEX_PATH)
else:
    faiss_index = None
    print(f"Warning: FAISS index file not found at {INDEX_PATH}.")

def search_index(query_vector, top_n=5):
    if faiss_index is None:
        raise FileNotFoundError("FAISS index is not loaded. Please build or download the index binary.")
    
    distances, indices = faiss_index.search(query_vector, top_n + 1)
    return distances[0], indices[0]