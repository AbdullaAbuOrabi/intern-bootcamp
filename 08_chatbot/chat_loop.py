# 08_chatbot/chat_loop.py

"""
Simple loop-based chatbot for Week 7 Day 1.

This chatbot:
- Runs in the terminal
- Stores conversation history
- Uses a simple persona
- Replies to the user in a loop
- Shows conversation history when requested
- Stops when the user types 'exit'
"""


SYSTEM_PROMPT = """
You are a helpful data assistant.
You explain things clearly, simply, and in a friendly tone.
You help users understand data, AI, RAG, and chatbot concepts.
"""


conversation_history = []


def format_history(history):
    """
    Format the stored conversation history into readable text.
    """

    if not history:
        return "There is no conversation history yet."

    formatted_history = "Here is the conversation history so far:\n"

    for item in history:
        role = item["role"]
        message = item["message"]
        formatted_history += f"- {role}: {message}\n"

    return formatted_history


def generate_response(user_message, history):
    """
    Generate a simple chatbot response.

    This is a rule-based response function.
    Later, it can be replaced with an LLM or RAG-based response.
    """

    user_message_lower = user_message.lower().strip()
    words = user_message_lower.split()

    if user_message_lower == "show history":
        return format_history(history)

    if "rag" in words:
        return (
            "RAG stands for Retrieval-Augmented Generation. "
            "It helps an AI system answer questions using external documents or data."
        )

    if "history" in words or "memory" in words:
        return (
            "Conversation history is the chatbot's short-term memory. "
            "It stores what the user and chatbot said during the current session."
        )

    if "chatbot" in words:
        return (
            "A chatbot is a system that receives user messages, keeps track of the conversation, "
            "and generates replies based on the user input and context."
        )

    if "hello" in words or "hi" in words:
        return "Hello! I am your helpful data assistant. How can I help you today?"

    return (
        "I understand your message. Since I am a simple chatbot for now, "
        "I can explain basic topics like RAG, chatbot architecture, memory, and conversation flow."
    )


def main():
    """
    Main chatbot loop.
    """

    print("Chatbot: Hello! I am your helpful data assistant.")
    print("Chatbot: Type 'exit' to stop the chat.")
    print("Chatbot: Type 'show history' to view the conversation history.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        conversation_history.append({
            "role": "user",
            "message": user_input
        })

        bot_response = generate_response(user_input, conversation_history)

        conversation_history.append({
            "role": "assistant",
            "message": bot_response
        })

        print(f"Chatbot: {bot_response}\n")


if __name__ == "__main__":
    main()
