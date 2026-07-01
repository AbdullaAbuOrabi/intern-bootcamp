from typing import Any, Dict, List
import re


try:
    from retriever import hybrid_retrieve, retrieve
except ImportError:
    from .retriever import hybrid_retrieve, retrieve


def _flatten(value):
    """
    Chroma sometimes returns nested lists like [[doc1, doc2, doc3]].
    This converts them into a simple list.
    """
    if isinstance(value, list) and value and isinstance(value[0], list):
        return value[0]

    if isinstance(value, list):
        return value

    return []


def _extract_text(item: Any) -> str:
    """
    Extract text from different possible retriever output formats.
    """
    if item is None:
        return ""

    if isinstance(item, str):
        return item

    if isinstance(item, dict):
        return (
            item.get("text")
            or item.get("content")
            or item.get("page_content")
            or item.get("document")
            or str(item)
        )

    if hasattr(item, "page_content"):
        return item.page_content

    return str(item)


def _extract_metadata(item: Any) -> Dict:
    """
    Extract metadata if available.
    """
    if isinstance(item, dict):
        return item.get("metadata", {})

    if hasattr(item, "metadata"):
        return item.metadata

    return {}


def _normalize_results(raw_results: Any) -> List[Dict]:
    """
    Convert retriever results into a clean list of dictionaries.
    Each source will have:
    - text
    - metadata
    - score
    """

    normalized = []

    if raw_results is None:
        return normalized

    # Chroma-style dictionary output
    if isinstance(raw_results, dict) and "documents" in raw_results:
        documents = _flatten(raw_results.get("documents"))
        metadatas = _flatten(raw_results.get("metadatas"))
        distances = _flatten(raw_results.get("distances"))

        for i, doc in enumerate(documents):
            normalized.append(
                {
                    "text": doc,
                    "metadata": metadatas[i] if i < len(metadatas) else {},
                    "score": distances[i] if i < len(distances) else None,
                }
            )

        return normalized

    # Already contains retrieved context
    if isinstance(raw_results, dict) and "retrieved_context" in raw_results:
        return _normalize_results(raw_results["retrieved_context"])

    # Single dictionary result
    if isinstance(raw_results, dict):
        normalized.append(
            {
                "text": _extract_text(raw_results),
                "metadata": _extract_metadata(raw_results),
                "score": raw_results.get("score") or raw_results.get("distance"),
            }
        )
        return normalized

    # List of strings/dicts/documents
    if isinstance(raw_results, list):
        for item in raw_results:
            normalized.append(
                {
                    "text": _extract_text(item),
                    "metadata": _extract_metadata(item),
                    "score": item.get("score") if isinstance(item, dict) else None,
                }
            )

        return normalized

    # Fallback
    normalized.append(
        {
            "text": str(raw_results),
            "metadata": {},
            "score": None,
        }
    )

    return normalized


def retrieve_context(user_question: str, top_k: int = 3) -> List[Dict]:
    """
    Retrieve the most relevant document chunks for the question.
    """

    try:
        raw_results = hybrid_retrieve(user_question, top_k=top_k)
    except Exception:
        raw_results = retrieve(user_question, top_k=top_k)

    return _normalize_results(raw_results)


def _clean_question(text: str) -> str:
    """
    Normalize a question for easier matching.
    Example:
    'WHAT IS RAG ?' -> 'what is rag'
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _is_question_line(line: str) -> bool:
    """
    Detect if a line looks like a new question.
    """
    line = line.strip().lower()

    question_starts = (
        "what ",
        "why ",
        "how ",
        "when ",
        "where ",
        "who ",
        "which ",
        "can ",
        "does ",
        "do ",
        "is ",
        "are ",
    )

    return line.endswith("?") or line.startswith(question_starts)


def _extract_direct_answer(user_question: str, retrieved_context: List[Dict]) -> str:
    """
    Try to extract a clean direct answer from the retrieved document chunks.
    This is useful for FAQ-style documents.
    """

    cleaned_user_question = _clean_question(user_question)

    for source in retrieved_context:
        text = source.get("text", "")
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        for i, line in enumerate(lines):
            cleaned_line = _clean_question(line)

            # Find the matching question line inside the retrieved document
            if cleaned_user_question == cleaned_line:
                answer_lines = []

                # Take the lines after the question until another question starts
                for next_line in lines[i + 1:]:
                    if _is_question_line(next_line):
                        break

                    answer_lines.append(next_line)

                if answer_lines:
                    return " ".join(answer_lines)

    return ""


def _fallback_answer(user_question: str, retrieved_context: List[Dict]) -> str:
    """
    If no exact FAQ-style answer is found, create a simple answer
    using the most relevant retrieved source.
    """

    if not retrieved_context:
        return "I could not find relevant information in the project documents."

    first_source_text = retrieved_context[0].get("text", "")

    return (
        "Based on the retrieved project documents, the most relevant information is:\n\n"
        f"{first_source_text}"
    )


def rag_answer(user_question: str) -> Dict:
    """
    Main RAG function.

    Flow:
    1. Receive user question
    2. Retrieve relevant document chunks
    3. Extract or generate a clean answer
    4. Return answer and sources
    """

    retrieved_context = retrieve_context(user_question, top_k=3)

    if not retrieved_context:
        return {
            "answer": "I could not find relevant information in the project documents.",
            "retrieved_context": [],
        }

    direct_answer = _extract_direct_answer(user_question, retrieved_context)

    if direct_answer:
        final_answer = direct_answer
    else:
        final_answer = _fallback_answer(user_question, retrieved_context)

    return {
        "answer": final_answer,
        "retrieved_context": retrieved_context,
    }
