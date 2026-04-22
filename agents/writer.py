import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Use ChatGroq as requested initially or fallback to OpenAI/Anthropic based on env keys
# Let's import initially configured models or we can set it up to be dynamic
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

def get_llm():
    if os.getenv("GROQ_API_KEY"):
        return ChatGroq(model="llama3-70b-8192", temperature=0.2)
    return ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

WRITER_SYSTEM_PROMPT = """You are an expert technical writer and product manager.
Your task is to take the user's rough notes, ideas, or feedback, and draft a structured Product Requirements Document (PRD).

A successful PRD must include the following sections:
1. Overview & Objective: What is this project and why are we doing it?
2. Target Audience: Who is this for?
3. Core Features: List of features to be implemented.
4. Out of Scope: What are we explicitly NOT doing?
5. Success Metrics: How do we know if this is successful?

If you are provided with Feedback from a reviewer, incorporate their suggestions and fix the missing sections.

Format your output in Markdown.
"""

def generate_draft(content: str, feedback: str = None) -> str:
    llm = get_llm()
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", WRITER_SYSTEM_PROMPT),
        ("user", "Draft Content/Notes:\n{content}\n\nReviewer Feedback (if any):\n{feedback}")
    ])
    
    chain = prompt_template | llm | StrOutputParser()
    return chain.invoke({
        "content": content,
        "feedback": feedback or "None"
    })
