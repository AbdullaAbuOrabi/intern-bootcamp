from pathlib import Path
import shutil

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Paths
document_path = Path("07_genai_rag/source_documents/faq.md")
vector_store_path = Path("07_genai_rag/vector_store")

# Read the markdown file
text = document_path.read_text(encoding="utf-8")

print("Document loaded successfully")
print("--------------------------------")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40
)

chunks = text_splitter.split_text(text)

print(f"Number of chunks created: {len(chunks)}")
print("--------------------------------")

# Convert chunks into LangChain Document objects with metadata
documents = []

for i, chunk in enumerate(chunks, start=1):
    document = Document(
        page_content=chunk,
        metadata={
            "source": "faq.md",
            "chunk_number": i,
            "document_type": "FAQ"
        }
    )
    documents.append(document)

print("Documents with metadata created successfully")
print("--------------------------------")

# Clear old vector store if it already exists
if vector_store_path.exists():
    shutil.rmtree(vector_store_path)

# Create embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded successfully")
print("--------------------------------")

# Create and save Chroma vector store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=str(vector_store_path),
    collection_name="project_faq"
)

print("Vector store created successfully")
print(f"Vector store saved at: {vector_store_path}")
print("--------------------------------")
print("Testing semantic retrieval")

query = "Why do we split documents into chunks?"

results = vector_store.similarity_search(query, k=3)

print(f"Query: {query}")
print("--------------------------------")

for i, result in enumerate(results, start=1):
    print(f"Result {i}:")
    print(result.page_content)
    print("Metadata:")
    print(result.metadata)
    print("--------------------------------")
