from fastapi import APIRouter

from models.request_models import AnalysisRequest

from services.llm_service import analyze_resume

from services.validator import validate_response



router=APIRouter()



@router.post("/analyze")
def analyze(
    request:AnalysisRequest
):


    result=analyze_resume(

        request.resume_text,

        request.job_description

    )


    validated=validate_response(
        result
    )


    return validated