# chat_memory.py

class SimpleConversationMemory:
    def __init__(self, max_messages=4):
        self.messages = []
        self.max_messages = max_messages
        self.summary = ""

    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

        # If memory becomes too long, summarize the older messages
        if len(self.messages) > self.max_messages:
            old_messages = self.messages[:-self.max_messages]
            self.update_summary(old_messages)

            # Keep only the latest messages
            self.messages = self.messages[-self.max_messages:]

    def update_summary(self, old_messages):
        for message in old_messages:
            if "RAG" in message["content"] or "rag" in message["content"]:
                self.summary = "Earlier, the user asked about RAG and learned that it helps AI answer using external documents."

            elif "useful" in message["content"].lower():
                self.summary = "Earlier, the user discussed why RAG is useful for improving chatbot answers."

    def get_memory(self):
        return self.messages

    def get_context(self):
        context = ""

        if self.summary:
            context += f"Conversation Summary: {self.summary}\n\n"

        for message in self.messages:
            context += f"{message['role']}: {message['content']}\n"

        return context

    def clear_memory(self):
        self.messages = []
        self.summary = ""


def chatbot_without_memory(user_question):
    if "RAG" in user_question or "rag" in user_question:
        answer = "RAG means Retrieval-Augmented Generation. It helps AI answer questions using external documents."

    elif "useful" in user_question.lower():
        answer = "I need more context to know what you are asking about."

    elif "limit" in user_question.lower() and "memory" in user_question.lower():
        answer = "We limit memory size to avoid long conversations becoming too large and exceeding token limits."

    elif "memory" in user_question.lower():
        answer = "Memory helps the chatbot remember previous messages in the same conversation."

    else:
        answer = "I need more context to answer this question clearly."

    return answer


def chatbot_with_memory(user_question, memory):
    conversation_context = memory.get_context()

    if "RAG" in user_question or "rag" in user_question:
        answer = "RAG means Retrieval-Augmented Generation. It helps AI answer questions using external documents."

    elif "useful" in user_question.lower() and "RAG" in conversation_context:
        answer = "It is useful because RAG helps the chatbot give more accurate answers based on stored documents."

    elif "limit" in user_question.lower() and "memory" in user_question.lower():
        answer = "We limit memory size to avoid long conversations becoming too large and exceeding token limits."

    elif "memory" in user_question.lower():
        answer = "Memory helps the chatbot remember previous messages in the same conversation."

    else:
        answer = "I need more context to answer this question clearly."

    memory.add_message("user", user_question)
    memory.add_message("assistant", answer)

    return answer


if __name__ == "__main__":
    print("=== Chatbot WITHOUT Memory ===")

    question_1 = "What is RAG?"
    answer_1 = chatbot_without_memory(question_1)
    print("User:", question_1)
    print("Assistant:", answer_1)

    question_2 = "Why is it useful?"
    answer_2 = chatbot_without_memory(question_2)
    print("\nUser:", question_2)
    print("Assistant:", answer_2)

    print("\n=== Chatbot WITH Memory, Limit, and Summary ===")

    memory = SimpleConversationMemory(max_messages=4)

    questions = [
        "What is RAG?",
        "Why is it useful?",
        "What is memory in chatbots?",
        "Why do we limit memory size?"
    ]

    for question in questions:
        answer = chatbot_with_memory(question, memory)
        print("\nUser:", question)
        print("Assistant:", answer)

    print("\nFinal Conversation Context:")
    print(memory.get_context())
