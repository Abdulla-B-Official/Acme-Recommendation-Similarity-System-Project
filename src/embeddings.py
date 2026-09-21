import os
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_PATH = os.path.join("model_artifacts", "embedding_model")

model = SentenceTransformer(MODEL_PATH)

def create_embedding(text):
    embedding = model.encode([text], normalize_embeddings=True)
    return np.asarray(embedding, dtype="float32")