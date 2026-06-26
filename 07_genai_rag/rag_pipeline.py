import json
from datetime import datetime
from retriever import hybrid_retrieve


def build_context(retrieved_chunks):
    """
    Combine retrieved chunks into one context text.
    """

    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"Context {i}:\n{chunk['content']}"
        )

    return "\n\n".join(context_parts)


def build_prompt(query, context):
    """
    Build the final prompt that would be sent to the LLM.
    """

    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using only the context below.

Rules:
- Use only the provided context.
- Do not invent information.
- If the answer is not found in the context, say:
  "I could not find enough information in the provided documents."
- Keep the answer clear and simple.

Context:
{context}

User question:
{query}

Answer:
"""

    return prompt


def simple_llm_response(prompt):
    """
    Temporary simple LLM placeholder.

    This version tries to answer using the line after the most relevant heading.
    It avoids returning headings as final answers.
    """

    if "Context:" not in prompt or "User question:" not in prompt:
        return "I could not find enough information in the provided documents."

    context = prompt.split("Context:")[1].split("User question:")[0].strip()
    query = prompt.split("User question:")[1].split("Answer:")[0].strip()

    if not context:
        return "I could not find enough information in the provided documents."

    # Remove context labels
    for i in range(1, 10):
        context = context.replace(f"Context {i}:", "")

    # Clean query words
    stop_words = {
        "what", "is", "a", "an", "the", "of", "to", "and", "or",
        "in", "on", "for", "with", "by", "how", "why", "does", "do", "we"
    }

    query_words = [
        word.lower().strip(".,?!")
        for word in query.split()
        if word.lower().strip(".,?!") not in stop_words
    ]

    lines = context.splitlines()
    clean_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Keep headings, but remove markdown ##
        if line.startswith("##"):
            line = line.replace("##", "").strip()

        clean_lines.append(line)

    if not clean_lines:
        return "I could not find enough information in the provided documents."

    # First try: find the heading that best matches the question,
    # then return the useful line after it.
    for i, line in enumerate(clean_lines):
        line_lower = line.lower()

        matched_words = 0
        for word in query_words:
            if word in line_lower:
                matched_words += 1

        if matched_words >= 2 or (query_words and matched_words == len(query_words)):
            # Look for the next real answer line after the heading
            for next_line in clean_lines[i + 1:]:
                next_lower = next_line.lower()

                # Skip question headings
                if next_line.endswith("?"):
                    continue

                if next_lower.startswith("what is"):
                    continue

                if next_lower.startswith("why do"):
                    continue

                if next_lower.startswith("how does"):
                    continue

                if next_lower.startswith("#"):
                    continue

                if len(next_line.split()) >= 5:
                    return next_line

    # Second try: find any non-heading sentence that matches the query words
    best_line = None
    best_score = 0

    for line in clean_lines:
        line_lower = line.lower()

        # Do not return question headings
        if line.endswith("?"):
            continue

        score = 0
        for word in query_words:
            if word in line_lower:
                score += 1

        if score > best_score:
            best_score = score
            best_line = line

    if best_line and best_score > 0:
        return best_line

    return "I could not find enough information in the provided documents."


def evaluate_context_relevance(retrieved_chunks):
    """
    Give a simple relevance label based on the top retrieval score.
    """

    if not retrieved_chunks:
        return "No context found"

    top_score = retrieved_chunks[0].get("final_score", 0)

    if top_score >= 0.7:
        return "High"
    elif top_score >= 0.4:
        return "Medium"
    else:
        return "Low"


def rag_answer(query, top_k=3):
    """
    Full RAG pipeline:

    Step 1: Retrieve relevant context
    Step 2: Assemble prompt
    Step 3: Send prompt to LLM/generator
    Step 4: Return formatted answer
    """

    retrieved_chunks = hybrid_retrieve(query, top_k=top_k)

    if not retrieved_chunks:
        return {
            "query": query,
            "answer": "I could not find enough information in the provided documents.",
            "context_relevance": "No context found",
            "response_quality": "Poor",
            "retrieved_context": [],
            "status": "no_context_found",
            "timestamp": datetime.now().isoformat()
        }

    context = build_context(retrieved_chunks)
    prompt = build_prompt(query, context)
    answer = simple_llm_response(prompt)

    context_relevance = evaluate_context_relevance(retrieved_chunks)

    if answer == "I could not find enough information in the provided documents.":
        response_quality = "Poor"
    elif context_relevance == "High":
        response_quality = "Good"
    else:
        response_quality = "Needs review"

    return {
        "query": query,
        "answer": answer,
        "context_relevance": context_relevance,
        "response_quality": response_quality,
        "retrieved_context": retrieved_chunks,
        "status": "success",
        "timestamp": datetime.now().isoformat()
    }


def save_results(results, output_file="rag_results.json"):
    """
    Save RAG test results into a JSON file.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    test_queries = [
        "What is semantic search?",
        "What is a vector store?",
        "Why do we use chunking?",
        "What does a vector store save?",
        "How does semantic search find text?"
    ]

    all_results = []

    for query in test_queries:
        result = rag_answer(query)
        all_results.append(result)

        print("=" * 80)
        print("QUESTION:")
        print(result["query"])

        print("\nANSWER:")
        print(result["answer"])

        print("\nCONTEXT RELEVANCE:")
        print(result["context_relevance"])

        print("\nRESPONSE QUALITY:")
        print(result["response_quality"])

        print("\nSTATUS:")
        print(result["status"])
        print()

    save_results(all_results)

    print("=" * 80)
    print("RAG results saved to rag_results.json")
