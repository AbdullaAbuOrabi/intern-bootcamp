# Day 5 — Mini Prompt Engineering Project

## 1. Project Overview

This mini project focused on designing and improving prompts for a small generative AI task.

The selected use case was:

**Summarize customer feedback and highlight the top issues.**

The goal was to create a prompt that can analyze multiple customer feedback comments, summarize the overall sentiment, identify positive and negative points, rank the main customer issues, and provide useful recommendations.

## 2. Why This Use Case Was Selected

This use case is useful because companies often receive many customer reviews and feedback messages.

Instead of reading every comment manually, a well-designed prompt can help summarize the main problems quickly and clearly.

This can help a business understand what customers like, what problems customers face, and what improvements should be made.

## 3. Prompt Iterations

Three prompt versions were tested.

### Prompt Version 1 — Simple Prompt

The first prompt was a basic prompt that asked the model to summarize customer feedback and highlight the main issues.

This version produced a useful basic summary, but the answer was not very structured.

### Prompt Version 2 — Structured Prompt

The second prompt added a clear role and required output sections:

- Overall sentiment
- Positive points
- Negative points
- Top customer issues
- Recommendations

This made the response easier to read and more organized.

### Prompt Version 3 — Final Improved Prompt

The third prompt was the best version.

It included:

- A clear analyst role
- Detailed task requirements
- A fixed output format
- Ranked top issues
- Practical recommendations
- Simple evaluation scores

This version produced the most complete and business-focused response.

## 4. Evaluation Method

The prompt outputs were evaluated using four quality dimensions:

| Dimension | Meaning |
|---|---|
| Accuracy | Whether the response correctly understood the feedback |
| Clarity | Whether the response was easy to read |
| Completeness | Whether the response included all important points |
| Conciseness | Whether the response was clear without being too long |

## 5. Evaluation Results

| Prompt Version | Accuracy | Clarity | Completeness | Conciseness | Total Score |
|---|---:|---:|---:|---:|---:|
| Version 1 | 4/5 | 3/5 | 3/5 | 5/5 | 15/20 |
| Version 2 | 4/5 | 4/5 | 4/5 | 4/5 | 16/20 |
| Version 3 | 5/5 | 5/5 | 5/5 | 4/5 | 19/20 |

## 6. Best-Performing Prompt

The best-performing prompt was **Prompt Version 3**.

It was selected because it gave the model clear instructions, a clear structure, and a business-focused output format.

It also ranked the top customer issues and gave practical recommendations.

## 7. Key Learning

The main lesson from this task is that prompt quality improves when the prompt includes more control, context, and structure.

A simple prompt can produce a basic answer, but a structured and detailed prompt produces a clearer, more useful, and more complete response.

This project showed how prompt engineering is an iterative process:

1. Start with a simple prompt.
2. Review the output.
3. Improve the instructions.
4. Evaluate the result.
5. Select the best-performing prompt.