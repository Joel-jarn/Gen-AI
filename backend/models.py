from pydantic import BaseModel
from typing import List, Optional

class DocumentDraft(BaseModel):
    content: str
    feedback: Optional[str] = None
    iteration: int = 0

class ReviewCriticism(BaseModel):
    is_approved: bool
    missing_sections: List[str]
    improvement_notes: str
