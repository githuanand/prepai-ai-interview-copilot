from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.gemini_service import generate_response

router = APIRouter(
    tags=["Answer Evaluation"]
)


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

Evaluate the answer professionally.

Return in the following format:

## Score
(X/10)

## Strengths
- Point 1
- Point 2

## Weaknesses
- Point 1
- Point 2

## Suggestions for Improvement
- Point 1
- Point 2

## Ideal Answer
Provide an ideal interview-quality answer.
"""

    try:
        evaluation = generate_response(prompt)

        return {
            "success": True,
            "evaluation": evaluation
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Evaluation failed: {str(e)}"
        )