# Retrieval Findings

## Task Overview

This task focused on building and testing the retriever component of a RAG pipeline.

In the previous step, document chunks and embeddings were already stored inside a Chroma vector database. In this task, the goal was to search those stored chunks more accurately and return the most relevant results for a user query.

The retriever was tested using embedding retrieval, keyword retrieval, and hybrid retrieval.

## Retrieval Methods Used

### 1. Embedding Retrieval

Embedding retrieval searches based on meaning. The user query is converted into an embedding, then compared with the embeddings stored in the Chroma vector database.

This method is useful when the question and the document chunk have similar meaning, even if they do not use the exact same words.

### 2. Keyword Retrieval

Keyword retrieval searches based on exact word matches. The query is split into important words, and common words such as "what", "is", "the", and "a" are ignored.

This method is useful for exact terms, such as technical words, document names, dates, codes, or specific phrases.

### 3. Hybrid Retrieval

Hybrid retrieval combines embedding retrieval and keyword retrieval.

The final score was calculated using:

* 70% embedding score
* 30% keyword score

This approach gives more importance to meaning-based search while still using exact keyword matches to improve retrieval accuracy.
