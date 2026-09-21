# Acme Product Recommendation Similarity System

![Python](https://img.shields.io/badge/Python-45.7%25-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-23.6%25-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSS](https://img.shields.io/badge/CSS-16.9%25-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-13.8%25-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)

<p align="center">
  <b>A production-grade, full-stack Natural Language Processing (NLP) product recommendation engine designed to search, retrieve, and match similar items from a 70,000-product e-commerce catalog using a Python Flask backend and an interactive glassmorphic web UI.</b>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Algorithm-FAISS_Vector_Search-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-SentenceTransformers_all--MiniLM--L6--v2-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Metrics-Precision%405_95.10%25-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MRR%405-0.9679-red?style=for-the-badge" />
</p>

---

## Overview

**Acme Product Recommendation Similarity System** is an end-to-end NLP semantic retrieval and personalization system built to scale across extensive retail catalogs. By mapping product metadata—including title, main category, and subcategory—into dense multi-dimensional vector spaces, the system processes natural language queries or product descriptions to instantly deliver top-$N$ relevant recommendations.

The architecture combines deep transformer-based semantic embeddings with optimized vector search indices, surfaced through a modern web UI:

* **Text Preprocessing & Metadata Fusion:** Concatenation and normalization of multi-field metadata (`name`, `main_category`, `sub_category`) into a unified `combined_features` text field.
* **Dense Embedding Extraction:** Leveraging `Sentence-Transformers` (`all-MiniLM-L6-v2`) to capture context, intent, and subtle product characteristics far beyond traditional keyword search.
* **Sub-Millisecond Retrieval:** Utilizing Facebook AI Similarity Search (`FAISS` `IndexFlatIP` / `IndexIVFFlat`) for ultra-low latency cosine similarity queries across 70,000+ vector spaces.
* **Glassmorphic Web Interface:** A responsive Flask-driven web app featuring dynamic top-$N$ selection, percentage match badges, and real-time backend API consumption.

---

### Language Breakdown

| Language | Percentage | Primary Usage |
| :--- | :--- | :--- |
| **Python** | **45.7%** | Core NLP pipeline, FAISS vector indexing, Sentence-Transformers embeddings, and Flask RESTful API |
| **JavaScript** | **23.6%** | Asynchronous Fetch API requests, dynamic DOM rendering, score formatting, and status handling |
| **CSS** | **16.9%** | Glassmorphism dashboard styling, ambient lighting backgrounds, flex/grid layouts, and responsive design |
| **HTML** | **13.8%** | Structured Web UI layouts, accessible input forms, top-$N$ selector controls, and card grids |

---

### Application Features

* **Full-Stack Architecture:** Clean modular design separating the NLP vector retrieval pipeline (`src/`) from the client interface (`templates/` and `static/`).
* **True Semantic Understanding:** Matches search queries based on conceptual intent rather than exact word overlaps (e.g., matching *"noise cancelling earplugs"* with *"wireless bluetooth headphones"*).
* **Sub-Millisecond Vector Search:** Powered by FAISS index structures, capable of searching tens of thousands of catalog items instantly.
* **Production Evaluation Metrics:** Validated quantitatively on historical data, achieving a **Precision@5 of 95.10%** and an **MRR@5 of 0.9679**.
* **Cloud-Ready Deployment:** Engineered with `.gitignore` rules for weight isolation, HuggingFace auto-caching, Gunicorn server setup, and Render cloud compatibility.

---

## Project Objective

The primary objective is to build a high-performance, real-time product discovery engine for Acme Retail that can:

* Structure and vectorize multi-category product catalog metadata containing over 70,000 entries.
* Eliminate search bounce rates caused by rigid `CTRL+F` or exact SQL string matches.
* Compute vector cosine similarity in sub-millisecond windows to recommend highly relevant alternative items.
* Provide non-technical retail users and e-commerce shoppers with an intuitive web UI.
* Deploy cleanly to cloud infrastructure using automated build processes.

---

## Problem Statement

Traditional keyword search engines rely on exact token matching. When e-commerce customers query a retail catalog using synonyms, broad features, or colloquial phrases, standard keyword systems fail to return relevant results—leading to dead ends and dropped conversions.

Standard baseline solutions frequently suffer from:
* **Synonym Blindness:** Inability to recognize that words like *"beverage container"* and *"water bottle"* share the same semantic intent.
* **Latency Bottlenecks:** Naive pairwise cosine similarity calculations scale poorly ($O(N)$) as product catalogs grow to tens or hundreds of thousands of SKUs.
* **Lack of Visual Tooling:** Technical backend vector models that remain inaccessible to business managers or shoppers due to the absence of a modern frontend interface.

### Proposed Solution

This project implements an end-to-end semantic vector pipeline executing:

$$\text{User Search Query} \longrightarrow \text{Text Normalization} \longrightarrow \text{Transformer Embedding} \longrightarrow \text{FAISS Vector Retrieval} \longrightarrow \text{Ranked Products \& Match Scores}$$

For every query processed through the web application, the system delivers:

```text
Normalized Query Embedding
Ranked List of Top-N Matched Products
Percentage-Based Similarity Match Badges
Interactive Dark-Mode Visual Dashboard Output
