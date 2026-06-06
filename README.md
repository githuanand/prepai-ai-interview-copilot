# 🚀 PrepAI - AI Interview Copilot

AI-powered interview preparation platform built using **FastAPI**, **Google Gemini AI**, and **Python**.

PrepAI helps candidates prepare for technical interviews by:

- Analyzing resumes
- Extracting technical skills
- Generating personalized interview questions
- Evaluating answers with AI feedback

---

## 📌 Project Overview

PrepAI is designed to simulate a smart interview preparation assistant.

The system accepts a resume in PDF format, extracts the content, identifies technical skills, and generates interview questions tailored to the candidate's profile. It can also evaluate answers and provide detailed feedback using Generative AI.

---

## ✨ Features

### 📄 Resume Analysis

- Upload PDF resumes
- Extract text using PyMuPDF
- Analyze candidate profile

### 🧠 Skill Extraction

- Detect technical skills automatically
- AI/ML-focused skill identification
- Resume keyword analysis

### 🤖 Interview Question Generation

- Personalized interview questions
- Domain-specific questions
- AI-generated technical assessments

### 📊 Answer Evaluation

- AI-powered answer analysis
- Score candidate responses
- Detailed feedback generation
- Ideal answer suggestions

### 📚 Interactive API Documentation

- Swagger UI support
- OpenAPI documentation
- Easy API testing

---

## 🏗️ System Architecture

```text
          Resume PDF
               │
               ▼
      Resume Parser
        (PyMuPDF)
               │
               ▼
      Skill Extractor
               │
               ▼
        Google Gemini
         /         \
        /           \
       ▼             ▼
Interview       Answer
Questions      Evaluation
```

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Backend Framework | FastAPI |
| AI Model | Google Gemini |
| PDF Processing | PyMuPDF |
| Validation | Pydantic |
| Server | Uvicorn |
| Documentation | Swagger UI |
| API Standard | OpenAPI |

---

## 📌 API Endpoints

### 1️⃣ Upload Resume

```http
POST /upload-resume
```

Upload a PDF resume and extract skills.

#### Sample Response

```json
{
  "filename": "resume.pdf",
  "total_characters": 3861,
  "skills": [
    "Python",
    "Machine Learning",
    "FastAPI",
    "SQL",
    "Git"
  ],
  "total_skills": 5
}
```

---

### 2️⃣ Generate Questions

```http
POST /generate-questions
```

Generate AI-powered interview questions based on extracted skills.

#### Request

```json
{
  "skills": [
    "Python",
    "FastAPI",
    "Machine Learning",
    "RAG"
  ]
}
```

---

### 3️⃣ Evaluate Answer

```http
POST /evaluate-answer
```

Evaluate candidate answers using Google Gemini.

#### Request

```json
{
  "question": "What is Overfitting in Machine Learning?",
  "answer": "Overfitting happens when a model learns the training data too well and performs poorly on unseen data."
}
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/githuanand/prepai-ai-interview-copilot.git
```

### Move Into Project

```bash
cd prepai-ai-interview-copilot/backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

### Run Application

```bash
uvicorn app.main:app --reload
```

---

## 📖 Swagger Documentation

After running the server:

```text
http://127.0.0.1:8000/docs
```

Interactive API documentation will be available through Swagger UI.

---

## 📂 Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   │   ├── resume.py
│   │   ├── questions.py
│   │   └── evaluate.py
│   │
│   ├── services/
│   │   ├── resume_parser.py
│   │   ├── skill_extractor.py
│   │   └── gemini_service.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── uploads/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🎯 Skills Demonstrated

This project demonstrates:

- FastAPI Development
- REST API Design
- Python Backend Development
- Generative AI Integration
- Prompt Engineering
- PDF Parsing
- NLP Concepts
- OpenAPI Documentation
- Git & GitHub
- Software Architecture Design

---

## 🚀 Future Enhancements

- Mock Interview Sessions
- Voice-Based Interviews
- Authentication & Authorization
- Interview Analytics Dashboard
- Resume Improvement Suggestions
- RAG-Based Knowledge Base
- Candidate Performance Tracking
- AI Career Guidance

---

## 💼 Resume Project Description

**PrepAI – AI Interview Copilot**

Built an AI-powered interview preparation platform using FastAPI and Google Gemini. Implemented PDF resume parsing, automated skill extraction, AI-driven interview question generation, and answer evaluation. Designed REST APIs with Swagger documentation and integrated Generative AI for personalized interview preparation.

---

## 👨‍💻 Author

### Anand Mohan Jha

- GitHub: https://github.com/githuanand
- LinkedIn: [https://linkedin.com/in/anand-mohan-jha](https://www.linkedin.com/in/anand-mohan-jha-55843924a/)

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star.
