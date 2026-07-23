from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.analyzer import analyze_resume

router = APIRouter(prefix="/api", tags=["analyze"])


class AnalyzeRequest(BaseModel):
    resume_text: str = Field(..., min_length=1)
    job_description: str = Field(..., min_length=1)


@router.post("/analyze")
async def analyze(payload: AnalyzeRequest):
    if not payload.resume_text.strip():
        raise HTTPException(status_code=400, detail="resume_text cannot be empty.")
    if not payload.job_description.strip():
        raise HTTPException(status_code=400, detail="job_description cannot be empty.")

    result = analyze_resume(payload.resume_text, payload.job_description)
    return result
