# Conversation Flow and Memory Logic Summary

## Task Overview

In Week 7 Day 1, I implemented a simple loop-based chatbot in Python.  
The chatbot runs in the terminal, accepts user messages, stores the conversation history, follows a defined assistant persona, and generates basic responses.

The goal of this task was to understand the basic architecture of a chatbot before connecting it to an LLM, RAG system, API, or external tools.

---

## Conversation Flow

The chatbot follows this flow:

```text
User message
→ Terminal input
→ Message handling
→ Store user message in conversation history
→ Generate chatbot response
→ Store chatbot response in conversation history
→ Print response in terminal
→ Repeat until user types exit

---

## Terminal Testing

The chatbot was tested in the terminal using multi-turn interaction.

Example test:

```text
You: hello
Chatbot: Hello! I am your helpful data assistant. How can I help you today?

You: what is chatbot memory
Chatbot: Conversation history is the chatbot's short-term memory. It stores what the user and chatbot said during the current session.

You: show history
Chatbot: Here is the conversation history so far:
- user: hello
- assistant: Hello! I am your helpful data assistant. How can I help you today?
- user: what is chatbot memory
- assistant: Conversation history is the chatbot's short-term memory. It stores what the user and chatbot said during the current session.
- user: show history

You: exit
Chatbot: Goodbye!