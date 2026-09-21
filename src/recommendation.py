import os
import pickle
import pandas as pd

from src.preprocessing import prepare_query
from src.embeddings import create_embedding
from src.retrieval import search_index

PRODUCTS_PATH = os.path.join("model_artifacts", "products_df.pkl")

with open(PRODUCTS_PATH, "rb") as f:
    products_df = pickle.load(f)

def get_recommendations(query, top_n=5):
    if isinstance(query, (int, float)) or (isinstance(query, str) and query.strip().isdigit()):
        query_id = str(query).strip()
        matched = products_df[products_df["product_id"].astype(str) == query_id]

        if matched.empty:
            return {"error": "Product ID not found"}

        query_text = matched.iloc[0]["combined_features"]
        query_product_id = query_id

    elif isinstance(query, dict):
        query_text = prepare_query(query)
        query_product_id = None

    else:
        query_text = prepare_query(query)
        query_product_id = None

    if not query_text.strip():
        return {"error": "No usable product text was provided"}

    query_vector = create_embedding(query_text)

    distances, indices = search_index(query_vector, top_n)

    results = []

    for score, index in zip(distances, indices):
        if index < 0:
            continue

        row = products_df.iloc[int(index)]

        if query_product_id is not None and str(row["product_id"]) == query_product_id:
            continue

        results.append({
            "product_id": str(row["product_id"]),
            "name": str(row["name"]),
            "main_category": str(row["main_category"]),
            "sub_category": str(row["sub_category"]),
            "similarity_score": round(float(score), 4)
        })

        if len(results) >= top_n:
            break

    return {
        "query": query_text,
        "recommendations": results
    }