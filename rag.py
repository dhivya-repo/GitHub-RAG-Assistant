from ingest import load_files

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from sentence_transformers import (
    SentenceTransformer
)

from dotenv import load_dotenv

import google.generativeai as genai
import chromadb
import os


# -------------------------
# Load Repository Files
# -------------------------

texts = load_files(
    "repositories/fastapi"
)

print("Files Loaded:", len(texts))


# -------------------------
# Chunk Documents
# -------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.create_documents(
    texts
)

# Limit chunks for testing
chunks = chunks[:500]

print("Chunks Created:", len(chunks))


# -------------------------
# Create Embeddings
# -------------------------

print("Loading Embedding Model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Creating Embeddings...")

embeddings = model.encode(
    [
        chunk.page_content
        for chunk in chunks
    ],
    show_progress_bar=True
)

print("Embedding Shape:")
print(embeddings.shape)


# -------------------------
# Create ChromaDB
# -------------------------

client = chromadb.PersistentClient(
    path="chroma_db"
)

try:
    client.delete_collection(
        "repo_docs"
    )
except:
    pass

collection = client.get_or_create_collection(
    "repo_docs"
)

print("Storing Documents in ChromaDB...")

collection.add(
    ids=[
        str(i)
        for i in range(len(chunks))
    ],
    documents=[
        chunk.page_content
        for chunk in chunks
    ],
    embeddings=embeddings.tolist()
)

print("Documents Stored:")
print(collection.count())


# -------------------------
# Ask Question
# -------------------------

query = "How authentication works"

print("\nQuestion:")
print(query)

query_embedding = model.encode(
    query
).tolist()

results = collection.query(
    query_embeddings=[
        query_embedding
    ],
    n_results=5
)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(
    results["documents"][0],
    start=1
):
    print(f"Chunk {i}")
    print(doc[:300])
    print("\n" + "=" * 80 + "\n")


# -------------------------
# Gemini Setup
# -------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model_gemini = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# -------------------------
# Build Context
# -------------------------

context = "\n\n".join(
    results["documents"][0]
)

prompt = f"""
You are a helpful GitHub repository assistant.

Use only the context below to answer.

Context:
{context}

Question:
{query}

Answer:
"""


# -------------------------
# Generate Answer
# -------------------------

print("Generating Gemini Response...")

response = model_gemini.generate_content(
    prompt
)

print("\n")
print("=" * 80)
print("GEMINI ANSWER")
print("=" * 80)

print(response.text)