# GitHub Repository RAG Assistant

An AI-powered GitHub Repository RAG (Retrieval-Augmented Generation) Assistant that enables developers to analyze, search, and understand source code repositories using semantic search, vector databases, and Large Language Models.

## Features

* Clone public GitHub repositories
* Extract source code and documentation files
* Intelligent code chunking
* Generate embeddings using Sentence Transformers
* Store vectors in ChromaDB
* Semantic code search
* Repository question-answering system
* FastAPI REST APIs
* MCP (Model Context Protocol) integration
* Docker support
* Gemini LLM integration

## Tech Stack

* Python
* FastAPI
* LangChain
* ChromaDB
* Sentence Transformers
* Gemini API
* GitPython
* Docker
* MCP

## Project Architecture

GitHub Repository
↓
Repository Cloning
↓
Code Extraction
↓
Chunking
↓
Embeddings Generation
↓
ChromaDB Vector Storage
↓
Semantic Retrieval
↓
Gemini LLM
↓
AI Generated Answers

## Folder Structure

```text
github-rag-assistant/

├── app.py
├── rag.py
├── ingest.py
├── github_loader.py
├── mcp_server.py
│
├── chroma_db/
├── repositories/
│
├── requirements.txt
├── Dockerfile
└── .env
```

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd github-rag-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

## Running the Application

```bash
uvicorn app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Ingest Repository

POST `/ingest`

Request:

```json
{
  "repo_url": "https://github.com/user/repository"
}
```

### Ask Questions

POST `/ask`

Request:

```json
{
  "question": "Explain authentication flow"
}
```

Response:

```json
{
  "answer": "Authentication is implemented using..."
}
```

## Example Questions

* Explain the project architecture
* Where is authentication implemented?
* How does the database connection work?
* Summarize app.py
* List all API endpoints
* Explain middleware configuration
* Describe repository structure

## Docker Support

Build image:

```bash
docker build -t github-rag .
```

Run container:

```bash
docker run -p 8000:8000 github-rag
```

## Future Improvements

* Multi-repository support
* GitHub OAuth integration
* Incremental indexing
* Hybrid search
* Agentic workflows
* Repository visualization
* Multi-LLM support
* CI/CD pipeline integration

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Code Intelligence
* FastAPI Development
* MCP Integration
* Dockerization
* LLM Application Development
* AI Engineering Best Practices


```
```
