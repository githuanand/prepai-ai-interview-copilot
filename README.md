# PrepAI - AI Interview Copilot

## Overview

PrepAI is an AI-powered interview preparation platform that analyzes resumes, extracts technical skills, generates personalized interview questions, and evaluates candidate answers using Google Gemini.

## Features

* Resume PDF Upload
* Resume Text Extraction
* AI/ML Skill Detection
* AI-generated Interview Questions
* AI-powered Answer Evaluation
* Interactive Swagger Documentation

## Tech Stack

* Python
* FastAPI
* Google Gemini API
* PyMuPDF
* Pydantic
* Uvicorn

## API Endpoints

### Upload Resume

POST `/upload-resume`

Upload a PDF resume and extract skills.

### Generate Questions

POST `/generate-questions`

Generate interview questions based on skills.

### Evaluate Answer

POST `/evaluate-answer`

Evaluate candidate answers and provide feedback.

## Installation

```bash
git clone <repo-url>
cd prepai-ai-interview-copilot/backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## Future Enhancements

* Mock Interviews
* Voice-based Interviews
* User Authentication
* Interview Analytics Dashboard
* RAG-based Knowledge Base
