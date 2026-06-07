from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.gemini_service import generate_response

router = APIRouter(tags=["Question Generation"])


class SkillRequest(BaseModel):
    skills: list[str] = Field(..., min_length=1)


@router.post("/generate-questions")
def generate_questions(data: SkillRequest):

    prompt = f"""
Generate 10 technical interview questions.

Skills:
{", ".join(data.skills)}

Requirements:
- Questions only
- No answers
- Mix beginner, intermediate and advanced
- Number each question
"""

    try:
        result = generate_response(prompt)

        return {
            "success": True,
            "questions": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Question generation failed: {str(e)}"
        )