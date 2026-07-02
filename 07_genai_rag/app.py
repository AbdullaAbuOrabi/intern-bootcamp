import json
from datetime import datetime

import streamlit as st


st.set_page_config(
    page_title="RAG Chatbot UI",
    page_icon="🤖",
    layout="centered",
)

st.title("RAG Chatbot Interface")

st.write(
    "Ask questions and receive answers from the RAG chatbot using project documents."
)


def format_source(source):
    """
    Format source output for Streamlit display.
    """

    if isinstance(source, dict):
        text = source.get("text", "")
        metadata = source.get("metadata", {})
        score = source.get("score", None)

        st.write(text)

        if metadata:
            st.caption(f"Metadata: {metadata}")

        if score is not None:
            st.caption(f"Score: {score}")

    else:
        st.write(source)


def get_chatbot_response(user_question):
    """
    Connect Streamlit UI to the chatbot backend.
    """

    try:
        from chatbot_with_rag import ask_chatbot

        answer, retrieved_sources = ask_chatbot(user_question)
        return answer, retrieved_sources

    except Exception as error:
        error_message = f"""
An error happened while connecting the Streamlit UI to the chatbot backend.

Error type: {type(error).__name__}

Error message:
{error}

Check the VS Code terminal for the full error details.
"""
        return error_message, []


def get_previous_user_questions():
    """
    Return previous user questions from the current chat session.
    """

    return [
        message["content"]
        for message in st.session_state.messages
        if message["role"] == "user"
    ]


def get_last_assistant_answer():
    """
    Return the most recent assistant answer from the current chat session.
    """

    assistant_messages = [
        message["content"]
        for message in st.session_state.messages
        if message["role"] == "assistant"
    ]

    if assistant_messages:
        return assistant_messages[-1]

    return None


def handle_memory_question(user_question):
    """
    Handle questions that ask about previous conversation history.
    """

    question_lower = user_question.lower().strip()

    memory_keywords = [
        "what did i ask before",
        "what was my previous question",
        "previous question",
        "chat history",
        "conversation history",
        "what did i say before",
    ]

    if any(keyword in question_lower for keyword in memory_keywords):
        previous_questions = get_previous_user_questions()

        # Remove the current question from the list
        previous_questions = previous_questions[:-1]

        if not previous_questions:
            return "You have not asked any previous questions yet."

        formatted_questions = "\n".join(
            [f"- {question}" for question in previous_questions]
        )

        return f"You previously asked:\n\n{formatted_questions}"

    return None


def handle_simplify_question(user_question):
    """
    Handle follow-up questions that ask for a simpler explanation.
    """

    question_lower = user_question.lower().strip()

    simplify_keywords = [
        "can you explain it more simple",
        "can you explain it more simply",
        "explain it more simple",
        "explain it more simply",
        "make it simple",
        "make it simpler",
        "simplify it",
        "in simple words",
        "explain simply",
        "explain simpler",
    ]

    is_simplify_question = any(
        keyword in question_lower for keyword in simplify_keywords
    )

    # Extra flexible check
    if "explain" in question_lower and "simple" in question_lower:
        is_simplify_question = True

    if is_simplify_question:
        last_answer = get_last_assistant_answer()

        if not last_answer:
            return "There is no previous answer to simplify yet."

        if "RAG" in last_answer or "Retrieval-Augmented Generation" in last_answer:
            return (
                "In simple words, RAG means the chatbot searches the project documents first, "
                "finds the useful information, and then uses that information to answer your question."
            )

        return (
            "In simple words, the chatbot uses the previous answer as context "
            "and explains the idea in an easier way."
        )

    return None


def handle_fallback_question(user_question):
    """
    Handle unclear or off-topic questions before sending them to RAG.
    """

    question_lower = user_question.lower().strip()

    unclear_inputs = [
        "???",
        "????",
        "?????",
        "??????",
        "...",
        ".",
        "!",
        "??",
        "?",
    ]

    off_topic_keywords = [
        "weather",
        "temperature",
        "today's weather",
        "news",
        "sports",
        "stock price",
        "time now",
        "current time",
        "football",
        "movie",
    ]

    if question_lower in unclear_inputs or len(question_lower) < 3:
        return (
            "I could not understand the question clearly. "
            "Please ask a clear question related to the project documents."
        )

    if any(keyword in question_lower for keyword in off_topic_keywords):
        return (
            "I do not have enough information in the project documents to answer this question. "
            "Please ask a question related to the RAG chatbot, documents, chunking, vector store, or retrieval."
        )

    return None


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar options
with st.sidebar:
    st.header("Options")

    show_sources = st.checkbox("Show sources", value=True)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    transcript = json.dumps(
        st.session_state.messages,
        indent=4,
        ensure_ascii=False,
    )

    st.download_button(
        label="Save Transcript",
        data=transcript,
        file_name=f"chat_transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json",
    )


# Display old chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

        if (
            message["role"] == "assistant"
            and show_sources
            and message.get("sources")
        ):
            with st.expander("Show Sources"):
                for i, source in enumerate(message["sources"], start=1):
                    st.write(f"Source {i}")
                    format_source(source)


# User input
user_question = st.chat_input("Ask a question:")

if user_question:
    user_question = user_question.strip()

    if not user_question:
        st.warning("Please enter a question before sending.")

    else:
        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_question,
            }
        )

        # Display user message
        with st.chat_message("user"):
            st.write(user_question)

        # Generate chatbot answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                memory_answer = handle_memory_question(user_question)
                simplify_answer = handle_simplify_question(user_question)
                fallback_answer = handle_fallback_question(user_question)

                if memory_answer:
                    chatbot_answer = memory_answer
                    retrieved_sources = []

                elif simplify_answer:
                    chatbot_answer = simplify_answer
                    retrieved_sources = []

                elif fallback_answer:
                    chatbot_answer = fallback_answer
                    retrieved_sources = []

                else:
                    chatbot_answer, retrieved_sources = get_chatbot_response(
                        user_question
                    )

            st.write(chatbot_answer)

            if show_sources and retrieved_sources:
                with st.expander("Show Sources"):
                    for i, source in enumerate(retrieved_sources, start=1):
                        st.write(f"Source {i}")
                        format_source(source)

        # Save assistant message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": chatbot_answer,
                "sources": retrieved_sources,
            }
        )
