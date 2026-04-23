from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END

from agents.writer import generate_draft
from agents.critic import evaluate_draft

class DocumentReviewState(TypedDict):
    content: str
    draft: str
    feedback: str
    iteration_count: int
    is_approved: bool

def writer_node(state: DocumentReviewState):
    content = state.get("content", "")
    feedback = state.get("feedback", "")
    iteration_count = state.get("iteration_count", 0)
    
    # Generate draft using the writer agent
    draft = generate_draft(content, feedback)
    
    return {
        "draft": draft,
        "iteration_count": iteration_count + 1
    }

def critic_node(state: DocumentReviewState):
    draft = state.get("draft", "")
    
    # Review the draft using the critic agent
    review = evaluate_draft(draft)
    
    return {
        "is_approved": review.is_approved,
        "feedback": review.improvement_notes
    }

def should_continue(state: DocumentReviewState):
    # Check if we should exit the loop
    if state.get("is_approved"):
        return "end"
    
    # Set a maximum iteration count to prevent infinite requests
    if state.get("iteration_count", 0) >= 3:
        return "end"
        
    return "continue"

# Define the graph
workflow_builder = StateGraph(DocumentReviewState)

workflow_builder.add_node("writer", writer_node)
workflow_builder.add_node("critic", critic_node)

# Create the graph wiring
workflow_builder.set_entry_point("writer")
workflow_builder.add_edge("writer", "critic")

workflow_builder.add_conditional_edges(
    "critic",
    should_continue,
    {
        "continue": "writer",
        "end": END
    }
)

# Compile to runnable app
review_workflow = workflow_builder.compile()
