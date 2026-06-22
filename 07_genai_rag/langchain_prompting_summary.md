# Week 5 Day 3 — Prompt Templates and Automation using LangChain

## Task Overview

In this task, I learned how to use LangChain to create reusable prompt templates and automate LLM workflows.

The main goal was to move from writing prompts manually to building structured prompts in Python using variables and placeholders.

Instead of writing a full prompt every time, I created templates that can be reused with different inputs.

## What I Built

I created a Python script named:

`prompt_templates.py`

I also created a notebook named:

`langchain_prompting.ipynb`

The script and notebook both demonstrate two LLM use cases:

1. Summarizing a Markdown document.
2. Extracting keywords from a product description.

## Files Created

The main files created for this task are:

* `prompt_templates.py`
* `langchain_prompting.ipynb`
* `sample_markdown_doc.md`
* `product_description.txt`
* `reports/llm_outputs/markdown_summary_output.txt`
* `reports/llm_outputs/keyword_extraction_output.txt`
* `reports/llm_outputs/notebook_markdown_summary_output.txt`
* `reports/llm_outputs/notebook_keyword_extraction_output.txt`

## Prompt Templates Used

### 1. Markdown Summarization Template

This template reads a Markdown document and asks the LLM to summarize it.

The input file used was:

`sample_markdown_doc.md`

The output was saved to:

`reports/llm_outputs/markdown_summary_output.txt`

### 2. Keyword Extraction Template

This template reads a product description and asks the LLM to extract useful keywords.

The input file used was:

`product_description.txt`

The output was saved to:

`reports/llm_outputs/keyword_extraction_output.txt`

## How the Automation Works

The workflow follows this process:

1. Python reads input text from external files.
2. LangChain fills the prompt template variables.
3. The final prompt is sent to the local Ollama LLM.
4. The LLM generates an answer.
5. The output is saved inside the `reports/llm_outputs/` folder.

## Difference from Previous Tasks

In the previous tasks, I practiced writing prompts manually and comparing different prompt styles.

In this task, I used LangChain to automate prompts in code.

The main difference is:

* Previous tasks: manual prompt writing.
* This task: reusable prompt templates and automated LLM pipelines.

## What I Learned

I learned that prompt templates are useful because they make LLM workflows more organized, reusable, and easier to maintain.

I also learned how to separate input data from the code by storing the Markdown document and product description in external files.

This makes the workflow closer to real-world LLM applications, where documents and user inputs are usually read from files, databases, or APIs.

## Conclusion

This task helped me understand how LangChain can be used to build structured and reusable LLM workflows.

I completed the required script, notebook, and output samples for the two use cases.
