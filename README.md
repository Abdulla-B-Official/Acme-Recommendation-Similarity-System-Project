# Acme Product Recommendation Similarity System

![Python](https://img.shields.io/badge/Python-45.7%25-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-23.6%25-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSS](https://img.shields.io/badge/CSS-16.9%25-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-13.8%25-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)

<p align="center">
  <b>A full-stack Natural Language Processing (NLP) product recommendation engine designed to search, retrieve, and match similar items across a 70,000-product catalog using a Python Flask backend, FAISS vector search, and a glassmorphic web UI.</b>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Algorithm-FAISS_Vector_Search-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-SentenceTransformers_all--MiniLM--L6--v2-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Metrics-Precision%405_95.10%25-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Metrics-MRR%405_0.9679-red?style=for-the-badge" />
</p>

---

## Overview

**Acme Product Recommendation Similarity System** is an end-to-end NLP semantic retrieval and personalization pipeline built to process large-scale e-commerce product catalogs, automatically matching natural language queries or item descriptions to similar products based on contextual intent.

The system leverages a modular Python backend for high-performance dense vector embedding and sub-millisecond retrieval, paired with an interactive HTML/CSS/JS frontend for seamless user interaction:

* **Text Preprocessing & Feature Fusion:** Normalization and concatenation of product metadata (`name`, `main_category`, and `sub_category`) into unified feature strings.
* **Dense Embedding Generation:** Transforming textual product features into dense vector representations using `all-MiniLM-L6-v2` to capture contextual semantics rather than relying on exact keyword overlaps.
* **Sub-Millisecond Vector Search:** Utilizing Facebook AI Similarity Search (`FAISS` `IndexFlatIP` / `IndexIVFFlat`) to perform efficient similarity queries across 70,000+ vector spaces.
* **Interactive User Interface:** A dynamic dark-mode web application allowing users to input search queries, select top-$N$ recommendation bounds, and view percentage-based similarity match scores in real time.

The system transforms raw unstructured product metadata into high-dimensional vector spaces, bridging the gap between customer search intent and relevant product discovery.

---

### Language Breakdown

| Language | Percentage | Primary Usage |
| :--- | :--- | :--- |
| **Python** | **45.7%** | Core NLP pipeline, Sentence-Transformers embedding, FAISS indexing, and Flask RESTful API routing |
| **JavaScript** | **23.6%** | Asynchronous Fetch API requests, dynamic DOM rendering, match score calculations, and status updates |
| **CSS** | **16.9%** | Glassmorphism dashboard styling, ambient lighting effects, responsive grid layouts, and typography |
| **HTML** | **13.8%** | Structural layout for search forms, top-$N$ recommendation controls, and product card result containers |

---

### Application Features

* **Full-Stack Architecture:** Modular separation between the vector retrieval backend (`src/`) and the client-facing web application (`templates/` and `static/`).
* **Semantic Search Engine:** Understands underlying query intent to retrieve relevant alternatives (e.g., matching *"noise cancellation earplugs"* with *"wireless bluetooth headphones"*).
* **Sub-Millisecond Retrieval:** Powered by FAISS vector indexing, returning ranked recommendations across tens of thousands of catalog items instantly.
* **Quantitative Evaluation Metrics:** Rigorously benchmarked on catalog test sets, achieving a **Precision@5 of 95.10%** and an **MRR@5 of 0.9679**.
* **Cloud-Ready Deployment:** Configured with dynamic weight loading, `.gitignore` isolation rules for large binaries, Gunicorn server setup, and Render deployment compatibility.

---

## Project Objective

The primary objective is to build a scalable, production-grade product recommendation system that can:

* Clean, normalize, and combine multi-field product metadata across 70,000+ catalog items.
* Eliminate search friction caused by traditional exact keyword match constraints.
* Generate dense text embeddings to capture subtle semantic relationships between catalog SKUs.
* Deliver sub-millisecond vector retrieval for real-time e-commerce user queries.
* Provide an intuitive web interface for non-technical users to query the catalog and visualize top match confidence scores.
* Maintain a clean repository structure adhering to modern software development standards.

---

## Problem Statement

Navigating vast e-commerce product catalogs using traditional keyword searches frequently fails when customers use synonyms, descriptive features, or phrasing that differs from seller product titles.

Standard baseline solutions frequently suffer from:

* An inability to recognize semantic equivalency between different vocabularies describing identical product capabilities.
* Latency bottlenecks ($O(N)$ pairwise comparisons) when calculating cosine similarity across large catalog sizes.
* A lack of user-friendly front-end tools, making backend machine learning models inaccessible to shoppers or business operations.

### Proposed Solution

This project introduces a robust full-stack NLP retrieval pipeline executing:

$$\text{Product Query} \longrightarrow \text{Text Normalization} \longrightarrow \text{Transformer Embedding} \longrightarrow \text{FAISS Vector Retrieval} \longrightarrow \text{Ranked Products \& Scores}$$

For every query processed through the web application, the system produces:

```text
Normalized Query Vector
Ranked List of Top-N Matched Products
Percentage-Based Similarity Match Badges
Interactive Dark-Mode Visual Dashboard Output
