from pathlib import Path

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


# ----------------------------------------------------
# 1. Set up file paths
# ----------------------------------------------------

BASE_DIR = Path("07_genai_rag")

MARKDOWN_FILE = BASE_DIR / "sample_markdown_doc.md"
PRODUCT_FILE = BASE_DIR / "product_description.txt"

OUTPUT_DIR = BASE_DIR / "reports" / "llm_outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------
# 2. Set up the LLM
# ----------------------------------------------------
# If your Ollama model has a different name, change it here.
# You can check your models by running: ollama list

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.2
)


# ----------------------------------------------------
# 3. Prompt template for markdown summarization
# ----------------------------------------------------

summary_template = PromptTemplate(
    input_variables=["document_title", "markdown_text"],
    template="""
You are a helpful AI assistant.

Your task is to summarize the following markdown document.

Document title:
{document_title}

Markdown content:
{markdown_text}

Return the answer in this format:

Summary:
- Point 1
- Point 2
- Point 3

Main idea:
Write one short sentence explaining the main idea of the document.
"""
)


# ----------------------------------------------------
# 4. Prompt template for keyword extraction
# ----------------------------------------------------

keyword_template = PromptTemplate(
    input_variables=["product_name", "product_description"],
    template="""
You are a product analysis assistant.

Your task is to extract useful keywords from the product description.

Product name:
{product_name}

Product description:
{product_description}

Return the answer in this format:

Keywords:
- keyword 1
- keyword 2
- keyword 3
- keyword 4
- keyword 5

Product category:
Write the most likely product category.

Short explanation:
Briefly explain why these keywords are useful.
"""
)


# ----------------------------------------------------
# 5. Function to read a file
# ----------------------------------------------------

def read_file(file_path):
    """
    Reads a text or markdown file and returns its content.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


# ----------------------------------------------------
# 6. Function to run a prompt and save output
# ----------------------------------------------------

def run_prompt_and_save(prompt_template, input_data, output_file):
    """
    This function does the full mini-pipeline:

    input data
    -> fill prompt template
    -> send final prompt to LLM
    -> receive output
    -> save output to text file
    """

    final_prompt = prompt_template.format(**input_data)

    response = llm.invoke(final_prompt)

    output_path = OUTPUT_DIR / output_file

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(response.content)

    print(f"Output saved to: {output_path}")
    print("-" * 50)
    print(response.content)
    print("-" * 50)

    return response.content


# ----------------------------------------------------
# 7. Main program
# ----------------------------------------------------

def main():
    # --------------------------------------------
    # Use case 1: Summarization of a markdown file
    # --------------------------------------------

    markdown_text = read_file(MARKDOWN_FILE)

    markdown_input = {
        "document_title": "Prompt Templates in LangChain",
        "markdown_text": markdown_text
    }

    run_prompt_and_save(
        prompt_template=summary_template,
        input_data=markdown_input,
        output_file="markdown_summary_output.txt"
    )

    # -------------------------------------------------
    # Use case 2: Keyword extraction from product text
    # -------------------------------------------------

    product_description = read_file(PRODUCT_FILE)

    product_input = {
        "product_name": "Wireless Noise-Cancelling Headphones",
        "product_description": product_description
    }

    run_prompt_and_save(
        prompt_template=keyword_template,
        input_data=product_input,
        output_file="keyword_extraction_output.txt"
    )


if __name__ == "__main__":
    main()
