import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Initialize Groq Llama 3
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# WRITER AGENT
writer_system_prompt = """
You are an expert Document Writer AI specialized in creating highly structured, professional Product Requirement Documents (PRDs).
Your task is to transform raw meeting notes or bullet points into a well-formatted Markdown PRD.

A standard PRD must include the following sections:
1. Executive Summary
2. Business Objectives & Success Metrics
3. User Personas
4. Features and Requirements (User Stories)
5. Edge Cases & Technical Specs
"""

writer_prompt_template = ChatPromptTemplate.from_messages([
    ("system", writer_system_prompt),
    ("user", "Here are the raw notes: {raw_notes}")
])

writer_chain = writer_prompt_template | llm

rough_notes = """
- new feature: user profile picture upload
- need to accept PNG, JPG
- max size 5MB
- should automatically crop to square
"""

print("============== WRITER AGENT DRAFT ==============")
try:
    draft = writer_chain.invoke({"raw_notes": rough_notes})
    print(draft.content)
except Exception as e:
    print(f"API Error: {e}")
    exit(1)


# CRITIC AGENT
critic_system_prompt = """
You are a strict QA Compliance / Reviewer AI.
Your objective is to evaluate the provided document draft against the standard template.

Review Rubric:
- Does it contain 'Business Objectives & Success Metrics'?
- Does it contain 'User Personas'?
- Are there clear 'Edge Cases'?

If the draft is missing any of these elements, reply with specific feedback stating what is missing.
If it is complete and meets all standards, reply with 'APPROVED'.
"""

critic_prompt_template = ChatPromptTemplate.from_messages([
    ("system", critic_system_prompt),
    ("user", "Draft for review:\n\n{draft}")
])

critic_chain = critic_prompt_template | llm

print("\n============== CRITIC AGENT FEEDBACK ==============")
try:
    feedback = critic_chain.invoke({"draft": draft.content})
    print(feedback.content)
except Exception as e:
    print(f"API Error: {e}")
