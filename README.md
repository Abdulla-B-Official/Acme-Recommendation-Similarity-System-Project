# Acme Product Recommendation Similarity System

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_API-000000?style=for-the-badge&logo=flask&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Sentence_Transformers-orange?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

<p align="center">
  <b>An end-to-end semantic product recommendation and similarity search system designed to index large-scale item catalogs, generate dense vector embeddings, and retrieve relevant recommendations using Facebook AI Similarity Search (FAISS) over a modular web application backend.</b>
</p>

---

## Overview

Acme Recommendation Similarity System is an advanced machine learning and information retrieval application designed to deliver fast and accurate item recommendations based on semantic textual similarity.

The system incorporates deep embedding models and dense vector indexing to process catalog records:
- **Sentence Transformers:** Generates high-dimensional dense vector embeddings that capture deep semantic meaning from product descriptions and metadata.
- **FAISS (Facebook AI Similarity Search):** Implements efficient dense vector indexing and approximate nearest neighbor search across large product catalogs (e.g., 70,000+ items) for instantaneous similarity queries.

Instead of computing pairwise similarities on the fly, the application loads pre-computed vector indexes and model artifacts, ensuring high-speed retrieval performance and responsive web interactions.

---

## Features

- **Semantic Similarity Search:** Input any product description or query to retrieve the top-k most relevant item recommendations based on dense vector alignment.
- **Large-Scale Indexing:** Capable of searching across extensive item catalogs with sub-millisecond query latencies using FAISS vector indexes.
- **Interactive REST API:** Serves structured endpoints for similarity lookups, item recommendations, and system health checks.
- **Responsive Web UI:** Single-page user interface for seamless query input and visual recommendation inspection.
- **Containerised Deployment:** Fully configured with Docker, Render, and Railway deployment blueprints.
- **Automated Testing Suite:** Built-in test coverage using `pytest` to validate vector matching logic, embedding generation, and API endpoints.

---

## How It Works

```text
                  USER QUERY
                      │
                      ▼
         ┌─────────────────────────┐
         │  Web UI / Flask REST    │
         └────────────┬────────────┘
                      │
                      ▼
         ┌─────────────────────────┐
         │  Sentence Transformer   │
         │  (Dense Vector Embedding│
         └────────────┬────────────┘
                      │
                      ▼
         ┌─────────────────────────┐
         │      FAISS Index        │
         │ (Approximate Nearest    │
         │     Neighbor Search)    │
         └────────────┬────────────┘
                      │
                      ▼
         ┌─────────────────────────┐
         │   JSON API Response     │
         │ (Ranked Recommendations)│
         └─────────────────────────┘

```

---

## Project Architecture & Layout

```text
acme_recommendation_system/
├── app/
│   ├── main.py              # Application entrypoint
│   ├── routes/              # API route handlers (/recommend, /health, /search)
│   ├── services/            # Recommender logic and embedding pipelines
│   ├── models/              # Model loaders, FAISS index loader, and schemas
│   ├── utils/               # Text cleaning and normalisation utilities
│   └── config/              # Application settings and environment variables
├── static/                  # Frontend assets (CSS stylesheets, client-side JS)
├── templates/               # HTML single-page interface (index.html)
├── notebooks/               # Training/indexing scripts and artifact export utilities
├── saved_models/            # Directory for FAISS index, embedding models, and metadata
├── data/                    # Catalog data files (e.g., product CSV datasets)
├── tests/                   # Pytest automated test suite
├── requirements.txt         # Pinned python dependencies
├── Dockerfile               # Container build instructions
├── Procfile                 # Railway process configuration
├── render.yaml              # Render cloud deployment blueprint
└── README.md                # Project documentation

```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Abdulla-B-Official/Acme-Recommendation-Similarity-System-Project.git](https://github.com/Abdulla-B-Official/Acme-Recommendation-Similarity-System-Project.git)
cd Acme-Recommendation-Similarity-System-Project

```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## Running Locally

Start the development server:

```bash
python app/main.py

```

* **Web Interface:** [http://localhost:8000/](http://localhost:8000/)
* **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

## API Endpoints & Usage

### `POST /recommend`

Retrieve similar product recommendations based on input text or item ID.

**Request Body:**

```json
{
  "query": "wireless noise-cancelling headphones with long battery life",
  "top_k": 5
}

```

**Response:**

```json
{
  "query": "wireless noise-cancelling headphones with long battery life",
  "recommendations": [
    { "item_id": "PRD-1092", "title": "Apex Pro Wireless Headphones", "similarity_score": 0.89 },
    { "item_id": "PRD-4481", "title": "SoundWave Active ANC Over-Ear", "similarity_score": 0.85 }
  ]
}

```

### `GET /health`

Returns system status and index readiness.

```json
{
  "status": "ok",
  "index_loaded": true,
  "catalog_size": 70000
}

```

**cURL Example:**

```bash
curl -X POST http://localhost:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query":"ergonomic office chair for lumbar support","top_k":3}'

```

---

## Model Training & Indexing

To generate embeddings and build the FAISS index from scratch using your catalog data:

```bash
python notebooks/build_faiss_index.py --data data/catalog.csv --out saved_models

```

### Artifact Specifications

* **FAISS Index:** Saved as `faiss.index`, storing dense vector coordinates.
* **Metadata Mapping:** Serialised lookup tables linking vector IDs to product details.
* **Configuration:** `config.json` stores embedding dimension and distance metrics.

---

## Testing

Run the automated test suite using `pytest`:

```bash
pytest

```

The tests validate embedding generation, FAISS vector retrieval, similarity scoring logic, and web route status schemas.

---

## Deployment

### Docker Containerisation

```bash
docker build -t acme-recommender .
docker run -p 8000:8000 acme-recommender

```

*(The container automatically detects the `$PORT` environment variable).*

### Render & Railway

* **Render:** Connect your GitHub repository and configure using `render.yaml`.
* **Railway:** Deploy directly using the provided `Procfile`:
```text
web: python app/main.py

```



---

## Technology Stack

| Technology | Purpose |
| --- | --- |
| **Python** | Core Programming Language |
| **Flask** | Web Application & REST API Routing |
| **Sentence Transformers** | Dense Text Embeddings & Semantic Representation |
| **FAISS** | High-Performance Vector Similarity Search |
| **Bootstrap 5** | Responsive Frontend UI Framework |
| **Docker** | Containerisation & Environment Isolation |
| **Pytest** | Automated Testing Framework |
| **Git / GitHub** | Version Control & Collaboration |

---

## Project Outcomes

* Successfully integrated dense vector embeddings with FAISS indexing for large-scale product catalogs.
* Developed a high-speed semantic similarity search pipeline.
* Built an intuitive, responsive single-page web interface for real-time recommendations.
* Exposed clean, validated API routes for seamless integration.
* Successfully packaged and containerised the application for cloud deployment.

---

### Search Smarter. Recommend Faster. Automate Similarity Discovery.

If you found this project useful, consider giving the repository a star!

---
```
