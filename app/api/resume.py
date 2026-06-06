from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills
import os

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # Save uploaded PDF
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract resume text
    text = extract_text_from_pdf(file_path)

    # Extract skills
    skills = extract_skills(text)

    # Return response
    return {
        "filename": file.filename,
        "total_characters": len(text),
        "skills": skills,
        "total_skills": len(skills)
    }