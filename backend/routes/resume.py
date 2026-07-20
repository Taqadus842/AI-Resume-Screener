from fastapi import APIRouter, UploadFile, File, HTTPException
from services.file_service import save_file, extract_text



router=APIRouter()



@router.post("/upload")
async def upload_resume(
    file:UploadFile=File(...)
):


    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files allowed"
        )


    path=save_file(file)


    text=extract_text(path)


    return {

        "filename":file.filename,

        "resume_text":text

    }