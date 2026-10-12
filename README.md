# Acme Product Recommendation Similarity System

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-blue?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<p align="center">
  <b>A full-stack Natural Language Processing (NLP) product recommendation engine designed to search, retrieve, and match similar items across product catalogs using a Python Flask backend, FAISS vector indexing, and a web UI.</b>
</p>

---

## Overview

The **Acme Product Recommendation Similarity System** is an end-to-end semantic retrieval and personalization pipeline built to process large e-commerce catalogs, matching natural language queries and item descriptions to similar products based on contextual intent.

The system features a structured backend pipeline located in `src/` for text preprocessing, sentence embedding generation, FAISS indexing, and similarity ranking, paired with a dynamic frontend dashboard:

* **Text Preprocessing (`preprocessing.py`):** Normalizes and cleans product metadata to create unified text strings.
* **Vector Embeddings (`embeddings.py`):** Transforms textual features into dense vector spaces to capture contextual semantics.
* **Retrieval & Recommendation (`retrieval.py`, `recommendation.py`):** Handles FAISS vector search indexing (`faiss_index.bin`) and fast similarity lookup across product records (`products_df.pkl`).
* **Web Interface (`app.py`):** A Flask web application rendering interactive HTML templates (`templates/index.html`) and handling asynchronous API requests via `static/js/script.js`.

---

## Repository Structure

```text
Product-Recommendation-Similarity-System/
├── model_artifacts/
│   ├── embedding_model/       # Trained transformer embedding weights
│   ├── faiss_index.bin        # Serialized FAISS vector search index
│   └── products_df.pkl        # Processed product catalog dataframe
├── src/
│   ├── __pycache__/
│   ├── embeddings.py          # Embedding generation logic
│   ├── preprocessing.py       # Data normalization & text cleaning
│   ├── recommendation.py      # Recommendation orchestration
│   └── retrieval.py           # FAISS search query execution
├── static/
│   ├── css/
│   │   └── style.css          # Dashboard styling and layout
│   └── js/                    # Frontend Fetch API & event handling
├── templates/
│   └── index.html             # User interface web template
├── venv/                      # Local virtual environment
├── .gitignore                 # Git exclusion rules
├── app.py                     # Flask web server entry point
├── Procfile                   # Cloud deployment server configuration
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies

```

---

## System Architecture

$$\text{User Query} \longrightarrow \text{Preprocessing (`preprocessing.py`)} \longrightarrow \text{Dense Embedding (`embeddings.py`)} \longrightarrow \text{FAISS Search (`retrieval.py`)} \longrightarrow \text{Flask Web UI}$$

1. **User Input:** Search query or product criteria submitted through the web frontend.
2. **Preprocessing:** Text normalized and mapped into dense vector representation.
3. **Vector Retrieval:** FAISS index efficiently scans high-dimensional space for nearest neighbor matches.
4. **Dashboard Presentation:** Ranked product recommendations and similarity scores are displayed dynamically on the interface.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Abdulla-B-Official/Acme-Recommendation-Similarity-System-Project.git](https://github.com/Abdulla-B-Official/Acme-Recommendation-Similarity-System-Project.git)
cd Acme-Recommendation-Similarity-System-Project

```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Activate on Windows PowerShell:
venv\Scripts\Activate.ps1
# Activate on Linux/macOS:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Web Application

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000` to interact with the recommendation engine.

```

```
