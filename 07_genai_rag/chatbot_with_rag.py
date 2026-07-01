import json
from datetime import datetime
from pathlib import Path

from rag_pipeline import rag_answer


CHAT_HISTORY_FILE = Path(__file__).parent / "chat_history.json"

chat_history = []


def save_chat_history():
    """
    Save chat history to a JSON file.
    """
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(chat_history, file, indent=4, ensure_ascii=False)


def build_context_aware_query(user_question):
    """
    If the user asks a follow-up question, include the previous question and answer.
    If it is a direct question, use the question alone.
    """

    follow_up_words = [
        "it",
        "this",
        "that",
        "them",
        "more",
        "explain",
        "simpler",
        "again",
    ]

    question_lower = user_question.lower()
    question_words = question_lower.split()

    is_follow_up = any(word in question_words for word in follow_up_words)

    if not chat_history or not is_follow_up:
        return user_question

    last_turn = chat_history[-1]

    previous_question = last_turn.get("question", "")
    previous_answer = last_turn.get("answer", "")

    context_aware_query = f"""
Previous question:
{previous_question}

Previous answer:
{previous_answer}

Current follow-up question:
{user_question}
"""

    return context_aware_query.strip()


def ask_chatbot(user_question):
    """
    Main chatbot function used by the Streamlit UI.

    It returns:
    answer, retrieved_sources
    """

    context_aware_query = build_context_aware_query(user_question)

    rag_result = rag_answer(context_aware_query)

    if isinstance(rag_result, dict):
        answer = rag_result.get("answer", "No answer generated.")
        retrieved_sources = rag_result.get("retrieved_context", [])
    else:
        answer = str(rag_result)
        retrieved_sources = []

    chat_entry = {
        "timestamp": datetime.now().isoformat(),
        "question": user_question,
        "context_aware_query": context_aware_query,
        "answer": answer,
        "retrieved_sources": retrieved_sources,
    }

    chat_history.append(chat_entry)
    save_chat_history()

    return answer, retrieved_sources


def main():
    """
    Terminal version of the chatbot.
    This is useful for testing without Streamlit.
    """

    print("RAG Chatbot is running.")
    print("Ask a question, or type 'exit' to stop.\n")

    while True:
        user_question = input("You: ")

        if user_question.lower() in ["exit", "quit", "stop"]:
            print("Chatbot stopped.")
            break

        answer, retrieved_sources = ask_chatbot(user_question)

        print("\nBot:")
        print(answer)

        print("\nRetrieved Sources:")
        if retrieved_sources:
            for i, source in enumerate(retrieved_sources, start=1):
                print(f"{i}. {source}")
        else:
            print("No sources found.")

        print("-" * 50)


if __name__ == "__main__":
    main()
