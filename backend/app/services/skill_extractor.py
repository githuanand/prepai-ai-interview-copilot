AI_ML_SKILLS = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Scikit-Learn",
    "FastAPI",
    "Django",
    "Flask",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "Docker",
    "Git",
    "GitHub",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "OpenCV",
    "NLP",
    "LLM",
    "Generative AI",
    "LangChain",
    "RAG",
    "Data Science",
    "Statistics",
    "AWS"
]

def extract_skills(text):
    found_skills = []

    text_lower = text.lower()

    for skill in AI_ML_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills