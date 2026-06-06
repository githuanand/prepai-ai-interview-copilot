from fastapi import FastAPI

from app.api.resume import router as resume_router
from app.api.questions import router as question_router
from app.api.evaluate import router as evaluate_router

app = FastAPI(
    title="PrepAI - AI Interview Copilot",
    description="AI-powered interview preparation platform using FastAPI and Google Gemini",
    version="1.0.0"
)

app.include_router(resume_router)
app.include_router(question_router)
app.include_router(evaluate_router)

@app.get("/")
def home():
    return {
        "status": "running"
    }