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
    Lazy import the chatbot backend.

    This helps Streamlit show the UI first instead of becoming a blank page
    if the backend takes time to load.
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
            chatbot_answer, retrieved_sources = get_chatbot_response(
                user_question)

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
