# RAG Document Q&A System

A simple Retrieval-Augmented Generation (RAG) application built using Python and LangChain. This project allows users to ask questions about a local text document and retrieve relevant information using semantic search.

## Features

- Load documents from local text files.
- Split documents into smaller chunks.
- Generate embeddings using HuggingFace.
- Store and search embeddings using FAISS.
- Retrieve relevant document chunks based on user queries.
- Generate answers using an LLM.

## Technologies Used

- Python
- LangChain
- HuggingFace Sentence Transformers
- FAISS
- Groq / LLM API 

## How RAG Works

1. **Document Loading:** Load the source text using a document loader.
2. **Text Splitting:** Divide the document into smaller chunks.
3. **Embedding Generation:** Convert each chunk into numerical vectors.
4. **Vector Storage:** Store embeddings in a FAISS index.
5. **Retrieval:** Find the most relevant chunks for a user's question.
6. **Answer Generation:** Use the retrieved context to generate an answer.

## Installation

Clone the repository and navigate to this project folder.

```bash
cd W3L1/rag-document
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Project Structure

```text
rag-document/
├── main.py
├── notes.txt
├── requirements.txt
└── README.md
```

## Learning Outcomes

- Understanding the RAG architecture.
- Understanding chunks versus tokens.
- Learning semantic search and embeddings.
- Working with vector databases using FAISS.
- Building a document-based question-answering pipeline.

