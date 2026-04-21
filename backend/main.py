from fastapi import FastAPI

app = FastAPI(
    title="Agentic AI Document Reviewer",
    description="API for the LangGraph-powered document review system",
    version="0.1.0"
)

@app.get("/")
async def healthcheck():
    return {"status": "ok", "message": "API is running"}
