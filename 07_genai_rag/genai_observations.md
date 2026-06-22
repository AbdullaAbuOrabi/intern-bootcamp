# Generative AI Observations

## Task Overview

In this task, I learned the basics of Generative AI and Large Language Models. I used Ollama to run a local LLM model and tested how the model generates text from different prompts and settings.

The main goal of this task was to understand how LLMs respond to prompts and how settings such as temperature and max tokens affect the output.

## What I Did

I used the local model `llama3.2:1b` through Ollama. I tested simple text generation by sending prompts from a Python notebook and printing the model responses.

I also created experiments to compare:

* Different temperature values
* Different max token values
* Creative prompts and factual prompts

## Temperature Observations

I tested the same prompt using different temperature values.

Lower temperature values, such as `0.1`, produced more direct, stable, and predictable answers. The response was focused and less creative.

Medium temperature values, such as `0.7`, produced balanced answers. The response was still clear, but the wording was more natural and flexible.

Higher temperature values, such as `1.0`, produced more creative and varied answers. The response was less predictable and more expressive.

## Max Token Observations

I tested different max token values to understand how response length changes.

Smaller max token values produced shorter answers. Sometimes the response was less detailed or stopped earlier.

Larger max token values allowed the model to generate longer and more complete answers.

This showed me that max tokens are useful for controlling the length of the model output.

## Creative vs Factual Outputs

I tested one creative prompt and one factual prompt.

The creative prompt asked the model to write a short story. The output was more imaginative, expressive, and story-like.

The factual prompt asked the model to explain a technical concept. The output was more direct, educational, and serious.

This showed me that the wording of the prompt can guide the model toward different types of responses.

## Open Models vs API-Based Models

Using Ollama means the model runs locally on my laptop. This is useful for learning, testing, and experimenting without needing an API key.

API-based models, such as OpenAI models, are accessed online through code. They are usually stronger and easier to connect to production applications, but they require an API key and internet connection.

In this task, I used Ollama because it allowed me to practice LLM experiments locally.

## Key Learning

I learned that I am not training the model in this task. The model is already trained.

Instead, I am learning how to use the model through Python code, send prompts to it, change settings, and compare the outputs.

This is different from chatting with ChatGPT because Python allows me to use the model inside my own project, save outputs, repeat experiments, and later connect the model to applications such as FastAPI, Streamlit, RAG systems, or chatbots.

## Conclusion

This task helped me understand the basic workflow of using an LLM programmatically. I learned how prompts, temperature, and max tokens affect the model response.

This is an important foundation before moving to more advanced Generative AI tasks such as Retrieval-Augmented Generation and chatbot development.
