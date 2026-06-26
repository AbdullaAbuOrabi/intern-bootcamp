from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# Try to find vector_store in the same folder first
CHROMA_PATH = BASE_DIR / "vector_store"

# If not found, try to find vector_store in the parent folder
if not CHROMA_PATH.exists():
    CHROMA_PATH = BASE_DIR.parent / "vector_store"


# --------------------------------------------------
# Load embedding model
# --------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------------------
# Connect to Chroma vector database
# --------------------------------------------------

client = chromadb.PersistentClient(path=str(CHROMA_PATH))


def get_collection():
    """
    Get the first collection stored inside Chroma.
    """

    collections = client.list_collections()

    if not collections:
        raise ValueError(
            "No collections found inside the vector_store folder."
        )

    first_collection = collections[0]

    # Works for different Chroma versions
    collection_name = (
        first_collection.name
        if hasattr(first_collection, "name")
        else first_collection
    )

    return client.get_collection(name=collection_name)


collection = get_collection()


# --------------------------------------------------
# Embedding retrieval
# --------------------------------------------------

def retrieve(query, top_k=3):
    """
    Search the vector database using semantic similarity.
    It returns the top matching chunks.
    """

    # Convert the user question into an embedding
    query_embedding = model.encode(query).tolist()

    # Search Chroma for the most similar chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    retrieved_chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    ids = results["ids"][0]

    for i in range(len(documents)):
        distance = distances[i]

        # Smaller distance means better match.
        # This converts distance into an easier relevance score.
        relevance_score = 1 / (1 + distance)

        retrieved_chunks.append({
            "rank": i + 1,
            "id": ids[i],
            "content": documents[i],
            "metadata": metadatas[i],
            "distance": distance,
            "relevance_score": relevance_score
        })

    return retrieved_chunks


# --------------------------------------------------
# Keyword retrieval
# --------------------------------------------------

def keyword_retrieve(query, top_k=3):
    """
    Search chunks using simple keyword matching.
    This helps when the user query contains exact important words.
    """

    stop_words = {
        "what", "is", "a", "an", "the", "of", "to", "and", "or",
        "in", "on", "for", "with", "by", "how", "why", "does", "do"
    }

    all_results = collection.get(include=["documents", "metadatas"])

    documents = all_results["documents"]
    metadatas = all_results["metadatas"]
    ids = all_results["ids"]

    query_words = [
        word.lower().strip(".,?!")
        for word in query.split()
        if word.lower().strip(".,?!") not in stop_words
    ]

    keyword_results = []

    if not query_words:
        return keyword_results

    for i, document in enumerate(documents):
        document_lower = document.lower()

        match_count = 0

        for word in query_words:
            if word in document_lower:
                match_count += 1

        if match_count > 0:
            keyword_score = match_count / len(query_words)

            keyword_results.append({
                "id": ids[i],
                "content": document,
                "metadata": metadatas[i],
                "keyword_score": keyword_score,
                "matched_words": match_count
            })

    keyword_results = sorted(
        keyword_results,
        key=lambda x: x["keyword_score"],
        reverse=True
    )

    return keyword_results[:top_k]


# --------------------------------------------------
# Hybrid retrieval
# --------------------------------------------------

def hybrid_retrieve(query, top_k=3, embedding_weight=0.7, keyword_weight=0.3):
    """
    Combine semantic retrieval and keyword retrieval into one final ranking.
    This is the function used by rag_pipeline.py.
    """

    embedding_results = retrieve(query, top_k=top_k * 2)
    keyword_results = keyword_retrieve(query, top_k=top_k * 2)

    combined_results = {}

    # Add embedding results
    for item in embedding_results:
        chunk_id = item["id"]

        combined_results[chunk_id] = {
            "id": chunk_id,
            "content": item["content"],
            "metadata": item["metadata"],
            "embedding_score": item["relevance_score"],
            "keyword_score": 0,
            "final_score": item["relevance_score"] * embedding_weight
        }

    # Add keyword results
    for item in keyword_results:
        chunk_id = item["id"]

        if chunk_id in combined_results:
            combined_results[chunk_id]["keyword_score"] = item["keyword_score"]
            combined_results[chunk_id]["final_score"] += (
                item["keyword_score"] * keyword_weight
            )
        else:
            combined_results[chunk_id] = {
                "id": chunk_id,
                "content": item["content"],
                "metadata": item["metadata"],
                "embedding_score": 0,
                "keyword_score": item["keyword_score"],
                "final_score": item["keyword_score"] * keyword_weight
            }

    final_results = sorted(
        combined_results.values(),
        key=lambda x: x["final_score"],
        reverse=True
    )

    return final_results[:top_k]


# --------------------------------------------------
# Test the retriever
# --------------------------------------------------

if __name__ == "__main__":
    query = "What is semantic search?"

    print(f"\nQuery: {query}\n")

    print("\nHYBRID RETRIEVAL RESULTS")
    hybrid_results = hybrid_retrieve(query, top_k=3)

    for rank, item in enumerate(hybrid_results, start=1):
        print("=" * 80)
        print(f"Rank: {rank}")
        print(f"Embedding Score: {item['embedding_score']:.4f}")
        print(f"Keyword Score: {item['keyword_score']:.4f}")
        print(f"Final Hybrid Score: {item['final_score']:.4f}")

        print("\nContent:")
        print(item["content"][:500])
        print()
