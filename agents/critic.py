import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from backend.models import ReviewCriticism

def get_llm():
    if os.getenv("GROQ_API_KEY"):
        return ChatGroq(model="llama3-70b-8192", temperature=0.1)
    return ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

CRITIC_SYSTEM_PROMPT = """You are a strict Product Management Critic. Your job is to review a drafted Product Requirements Document (PRD).

A successful PRD MUST contain ALL of the following sections strictly separated:
1. Overview & Objective
2. Target Audience
3. Core Features
4. Out of Scope
5. Success Metrics

Check the document carefully. If any of these 5 sections are missing, incomplete, or lack substance, you must flag `is_approved` as false, list the missing sections, and provide constructive `improvement_notes`.
If and ONLY if all 5 sections are present and adequately detailed, set `is_approved` as true and leave `missing_sections` empty.
"""

def evaluate_draft(draft_content: str) -> ReviewCriticism:
    llm = get_llm()
    # Use with_structured_output to force JSON matching the Pydantic model
    structured_llm = llm.with_structured_output(ReviewCriticism)
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", CRITIC_SYSTEM_PROMPT),
        ("user", "Please review the following draft PRD:\n\n{draft_content}")
    ])
    
    chain = prompt_template | structured_llm
    return chain.invoke({"draft_content": draft_content})
