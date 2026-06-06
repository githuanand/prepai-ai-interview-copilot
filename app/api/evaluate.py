from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_service import model

router = APIRouter()


class EvaluationRequest(BaseModel):
    question: str
    answer: str


@router.post("/evaluate-answer")
def evaluate_answer(data: EvaluationRequest):

    prompt = f"""
    You are a senior AI/ML interviewer.

    Question:
    {data.question}

    Candidate Answer:
    {data.answer}

    Evaluate the answer.

    Return:
    Score out of 10
    Feedback
    Ideal Answer
    """

    response = model.generate_content(prompt)

    return {
        "evaluation": response.text
    }