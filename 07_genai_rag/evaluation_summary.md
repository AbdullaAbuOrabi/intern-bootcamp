# Day 4 — Evaluating and Refining LLM Outputs

## Task Objective

The objective of this task was to evaluate the quality of LLM outputs instead of only generating responses.

In previous tasks, the focus was on writing prompts and using prompt templates. In this task, the focus was on checking whether the LLM output is good, complete, clear, and reliable.

The evaluation was based on quality dimensions such as faithfulness, coherence, completeness, conciseness, and relevance.

---

## Input Used

The same product review was used for all prompt versions:

The wireless headphones are very comfortable and the sound quality is great, but the battery drains faster than expected.

---

## Prompt Versions Tested

Four prompt versions were tested:

1. Vague prompt  
2. Structured prompt  
3. Few-shot prompt  
4. Overly constrained prompt  

Each prompt was used to generate an LLM output for the same product review.

---

## Evaluation Method

A simple Python evaluator was created to score each output.

The evaluator checked:

- Whether the output included important keywords such as mixed, comfortable, sound, battery, and recommendation.
- Whether the output followed the required format.
- Whether the output was concise.
- Whether the output avoided hallucinated information.
- The total score for each prompt output.

The results were saved in a CSV file named:

prompt_evaluation_scores.csv

---

## Main Findings

The structured prompt and few-shot prompt performed better than the vague and overly constrained prompts.

The vague prompt gave a basic answer, but it did not include all required sections clearly.

The structured prompt performed well because it asked for sentiment, positive points, negative points, and recommendation.

The few-shot prompt also performed well because it gave the LLM an example to follow.

The overly constrained prompt was short and clear, but it missed important details such as sentiment and recommendation.

---

## What I Learned

From this task, I learned that LLM outputs should not be accepted without evaluation.

A good LLM answer should be:

- Faithful: it should not make up information.
- Coherent: it should be clear and logical.
- Complete: it should include all required parts.
- Concise: it should be short and focused.
- Relevant: it should answer the actual question.

I also learned that prompt quality affects output quality. Clear and structured prompts usually produce better responses than vague prompts.

---

## Improvement Guidelines

Based on the evaluation, better prompts should:

1. Clearly explain the task.
2. Include the required output format.
3. Mention the key information that should be included.
4. Avoid being too vague.
5. Avoid being too restrictive.
6. Use examples when consistency is important.

---

## Conclusion

This task showed how to evaluate and refine LLM outputs using simple manual and rule-based methods.

The best outputs came from structured and few-shot prompts because they were more complete, organized, and useful.

This task helped me understand that in real LLM applications, evaluation is important because AI answers can look correct but still be incomplete, irrelevant, or hallucinated.