from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_service import model

router = APIRouter(
    tags=["Question Generation"]
)


class SkillRequest(BaseModel):
    skills: list[str]


@router.post("/generate-questions")
def generate_questions(data: SkillRequest):

    prompt = f"""
    Generate 10 technical interview questions.

    Skills:
    {", ".join(data.skills)}

    Return only questions.
    """

    response = model.generate_content(prompt)

    return {
        "questions": response.text
    }