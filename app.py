from fastapi import FastAPI

from github_loader import clone_repo

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "GitHub RAG Running"
    }


@app.post("/ingest")
def ingest_repo(repo_url: str):

    repo_path = clone_repo(
        repo_url
    )

    return {
        "status": "success",
        "repo_path": repo_path
    }


@app.post("/ask")
def ask(question: str):

    return {
        "answer": f"You asked: {question}"
    }