# Prompt Design Summary

## Task Overview

In this task, I learned the basic principles of prompt design for Large Language Models (LLMs).

The goal was to understand how different prompt styles affect the quality, structure, and usefulness of the model output.

I tested different prompt formats using a product review summarization task.

The prompt styles tested were:

1. Zero-shot prompting
2. One-shot prompting
3. Few-shot prompting
4. Reasoning-style prompting

---

## What is a Prompt?

A prompt is the instruction given to an LLM.

The prompt tells the model what task to complete, what format to use, what context to follow, and what constraints to respect.

A simple prompt may produce a simple answer, while a clear and structured prompt can produce a more useful and organized response.

---

## Key Principles of Prompt Design

### 1. Clarity

The prompt should clearly explain what the model needs to do.

Example:

Instead of writing:

```text
Summarize this.
```

A clearer prompt would be:

```text
Summarize the product review and identify the sentiment, positive points, negative points, and recommendation.
```

### 2. Structure

The prompt should tell the model how to organize the answer.

Example:

```text
Return the answer using this format:
- Sentiment:
- Positive points:
- Negative points:
- Recommendation:
```

This helps the model produce a clean and consistent output.

### 3. Context

The prompt should provide background information about the role or purpose of the task.

Example:

```text
You are a product review analyst.
```

This helps the model understand the type of answer expected.

### 4. Constraints

The prompt should include limits or rules when needed.

Example:

```text
Use simple language.
Do not add information that is not mentioned in the review.
Keep the answer short.
```

Constraints help control the length, accuracy, and style of the response.

---

## Prompt Styles Tested

### 1. Zero-Shot Prompting

Zero-shot prompting means asking the model to complete a task without giving any example.

In this task, the zero-shot prompt only asked the model to summarize the review.

The output was correct, but it was very simple and similar to the original review.

### Observation

Zero-shot prompting is useful for simple tasks, but it may not produce a structured or detailed answer unless the prompt clearly asks for it.

---

### 2. One-Shot Prompting

One-shot prompting means giving the model one example before asking it to complete the task.

In this task, I gave the model one example of a product review summary, then asked it to summarize a new review using the same format.

The output became more structured and included sentiment, positive points, negative points, and recommendation.

### Observation

One-shot prompting improved the answer because the model followed the example format.

---

### 3. Few-Shot Prompting

Few-shot prompting means giving the model multiple examples before asking it to complete the task.

In this task, I gave the model two examples before asking it to summarize the wireless headphones review.

The output was structured and consistent.

### Observation

Few-shot prompting gives the model more examples to follow, which helps make the output more reliable and consistent.

---

### 4. Reasoning-Style Prompting

Reasoning-style prompting asks the model to briefly explain the reason behind the answer.

In this task, the model was asked to explain why the review sentiment was positive, negative, or mixed.

The output included a brief reasoning section before the final answer.

### Observation

Reasoning-style prompting is useful when the task requires explanation or judgment. It helps the user understand why the model gave a specific answer.

---

## Comparison Table

| Prompt Style    | Description                                                                       | Output Quality   | Main Observation                                                                        |
| --------------- | --------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------- |
| Zero-shot       | The model was given only the task instruction without examples.                   | Basic            | The output was correct but too simple and not structured.                               |
| One-shot        | The model was given one example before the real task.                             | Better           | The output followed the example format and became more organized.                       |
| Few-shot        | The model was given multiple examples before the real task.                       | Strong           | The output was structured and consistent because the model had more examples to follow. |
| Reasoning-style | The model was asked to briefly explain the answer before giving the final result. | Most explainable | The output included a reason for the sentiment, making the answer easier to understand. |

---

## Best Practices Learned

From this task, I learned the following prompt design best practices:

1. Write clear instructions.
2. Give the model enough context.
3. Use a specific output format when needed.
4. Add examples if I want the model to follow a certain style.
5. Use few-shot prompting when consistency is important.
6. Use reasoning-style prompting when the task requires explanation.
7. Add constraints to control length, tone, and accuracy.
8. Avoid vague prompts because they can produce vague answers.

---

## Final Conclusion

This task showed that prompt design is important when working with LLMs.

The same product review produced different outputs depending on the prompt style.

A basic prompt gave a simple answer, while prompts with examples and structure produced better results.

The main lesson is that better prompts lead to better LLM outputs.

This skill will be useful in future GenAI tasks, especially when using LLMs for summarization, analysis, recommendations, and question answering.
