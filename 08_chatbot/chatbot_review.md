# Day 5 — Testing, Fine-Tuning & Demo

## Task Overview

The purpose of this task was to test and improve the final RAG chatbot. The chatbot was tested using different types of questions, including normal document-based questions, follow-up questions, memory questions, off-topic questions, and unclear inputs.

This task helped confirm that the chatbot can answer from project documents, show retrieved sources, remember previous user questions, and handle unsupported questions in a safer way.

## What Was Tested

The chatbot was tested using the Streamlit interface. The main test scenarios included:

- Basic RAG question: asking what RAG means.
- Follow-up question: asking the chatbot to explain the answer more simply.
- Memory question: asking what the user asked before.
- Off-topic question: asking about the weather.
- Unclear input: entering symbols such as question marks.

## Improvements Made

Several improvements were added to the chatbot interface:

- Added simple memory handling using Streamlit session state.
- Added support for questions like “what did I ask before?”
- Added follow-up handling for simple explanations.
- Added graceful fallback responses for off-topic questions.
- Added fallback handling for unclear or empty inputs.
- Kept the source display option for retrieved document chunks.

## Test Results

The chatbot correctly answered RAG-related questions using the project documents. It also displayed the retrieved document sources, which helps show where the answer came from.

The chatbot was improved to handle memory questions. When the user asked what they had asked before, the chatbot returned the previous user questions from the current chat session.

The chatbot was also improved to handle off-topic and unclear questions. Instead of forcing every question into document retrieval, it now gives a fallback message when the question is not related to the available project documents.

## Key Learnings

This task showed that building a chatbot is not only about making it answer questions. It is also important to test how it behaves in different situations.

I learned that a RAG chatbot should answer from the provided documents, but it also needs memory, clear prompt behavior, and fallback handling to feel more complete and reliable.

I also learned that testing helps find weak parts in the chatbot. For example, the chatbot originally repeated retrieved text for follow-up questions and answered off-topic questions using unrelated document chunks. These issues were improved during this task.

## Final Status

The final chatbot is working inside the `08_chatbot/` folder. It includes a Streamlit interface, document-based answering, source display, simple memory handling, follow-up support, and graceful fallback responses.

The chatbot is ready for screenshots, demo recording, and final Git submission.