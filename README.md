#  Pizza Review Agent

> An AI-powered NLP agent that lets you query pizza restaurant reviews using natural language — powered by RAG (Retrieval-Augmented Generation).

---

## Overview

**Pizza Review Agent** is a specialized AI agent designed to perform Natural Language Processing (NLP) on customer feedback data. By leveraging a **Retrieval-Augmented Generation (RAG)** architecture, users can ask questions about a dataset of pizza restaurant reviews in plain English and receive accurate, context-aware answers in seconds — grounded strictly in the actual review data.

> Example query: *"What do customers think about the crust?"* or *"Which pizza got the most complaints?"*

---

##  Architecture

```
CSV Reviews Dataset
       │
       ▼
 Document Loader (LangChain)
       │
       ▼
 Text Chunking & Embedding (BGE-Embed via Ollama)
       │
       ▼
 Vector Database (ChromaDB)
       │
       ▼
 User Query ──► Similarity Search ──► Retrieved Chunks
                                             │
                                             ▼
                                    LLM (Llama 3.2 via Ollama)
                                             │
                                             ▼
                                    Contextual Answer
```

---

##  Tech Stack

| Component | Technology |
|---|---|
| **LLM** | Llama 3.2 (via Ollama) |
| **Embedding Model** | BGE-Embed (via Ollama) |
| **Orchestration** | LangChain |
| **Vector Database** | ChromaDB |
| **Data Source** | CSV (Pizza Reviews) |
| **Language** | Python |

---

##  Project Structure

```
Pizza-Review-agent/
├── main.py                          # Main agent logic & query interface
├── vector.py                        # Embedding & vector store setup
├── realistic_restaurant_reviews.csv # Pizza review dataset
└── README.md
```

---

##  Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running locally

### 1. Clone the Repository

```bash
git clone https://github.com/TanishqMishra12/Pizza-Review-agent.git
cd Pizza-Review-agent
```

### 2. Install Dependencies

```bash
pip install langchain langchain-community chromadb ollama
```

### 3. Pull Required Ollama Models

```bash
ollama pull llama3.2
ollama pull bge-m3
```

> Make sure the Ollama server is running before proceeding (`ollama serve`).

### 4. Build the Vector Store

```bash
python vector.py
```

This loads the CSV dataset, chunks the text, generates embeddings, and stores them in a local ChromaDB instance.

### 5. Run the Agent

```bash
python main.py
```

You'll be prompted to enter natural language questions about the pizza reviews.

---

##  Example Queries

```
You: What do customers say about the delivery time?
You: Which menu items are mentioned most positively?
You: Are there any complaints about the sauce?
You: What rating do most customers give?
```

---

##  How It Works

1. **Data Ingestion** — The CSV file containing pizza restaurant reviews is loaded using LangChain's document loaders.
2. **Vectorization** — Text is split into chunks and converted into high-dimensional vectors using the BGE-Embed model. These are stored in ChromaDB.
3. **Retrieval** — When a query is submitted, ChromaDB performs a semantic similarity search to find the most relevant review snippets.
4. **Generation** — The retrieved snippets are passed as context to Llama 3.2, which synthesizes a concise and accurate answer grounded in the reviews.

---

##  Key Features

-  **Natural language querying** over structured review data
-  **RAG pipeline** ensures responses are grounded in real reviews (no hallucinations)
-  **Local-first** — runs entirely on your machine via Ollama
-  **Fast retrieval** using ChromaDB vector similarity search
-  **CSV-based** — easy to swap in your own review dataset

---

##  Customization

To use your own dataset, replace `realistic_restaurant_reviews.csv` with any CSV containing customer reviews, then update the relevant column name in `vector.py` and re-run the vectorization step.

---

##  License

This project is open source. Feel free to fork, modify, and build upon it.

---
