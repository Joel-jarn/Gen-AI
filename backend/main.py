from fastapi import FastAPI
from pydantic import BaseModel
from agents.graph import review_workflow
from backend.models import DocumentDraft, ReviewCriticism

app = FastAPI(
    title="Agentic AI Document Reviewer",
    description="API for the LangGraph-powered document review system",
    version="0.1.0"
)

@app.get("/")
async def healthcheck():
    return {"status": "ok", "message": "API is running"}


# Request model for /review endpoint
class ReviewRequest(BaseModel):
    content: str

# Response model for /review endpoint
class ReviewResponse(BaseModel):
    draft: str
    feedback: str
    is_approved: bool
    iteration_count: int

@app.post("/review", response_model=ReviewResponse)
async def review_document(request: ReviewRequest):
    # Initial state for the workflow
    state = {
        "content": request.content,
        "draft": "",
        "feedback": "",
        "iteration_count": 0,
        "is_approved": False
    }
    result = review_workflow.invoke(state)
    return ReviewResponse(
        draft=result["draft"],
        feedback=result["feedback"],
        is_approved=result["is_approved"],
        iteration_count=result["iteration_count"]
    )
