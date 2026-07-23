from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.parser import extract_resume_text

router = APIRouter(prefix="/api/resume", tags=["resume"])

MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file is None:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    file_bytes = await file.read()

    if len(file_bytes) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    if len(file_bytes) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(status_code=400, detail="File too large. Max size is 10MB.")

    resume_text = extract_resume_text(file.filename, file.content_type, file_bytes)

    return {
        "filename": file.filename,
        "resume_text": resume_text,
        "message": "Resume uploaded and parsed successfully.",
    }
