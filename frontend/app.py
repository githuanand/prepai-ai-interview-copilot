import streamlit as st
import requests
import re
from report_generator import generate_report

# ==========================================
# CONFIG
# ==========================================

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="PrepAI",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.skill-badge {
    display:inline-block;
    background:#0e7490;
    color:white;
    padding:8px 14px;
    border-radius:15px;
    margin:5px;
    font-size:14px;
    font-weight:600;
}

.hero-box {
    background: linear-gradient(90deg,#1e3a8a,#0f766e);
    padding:25px;
    border-radius:15px;
    color:white;
}

.footer {
    text-align:center;
    padding:15px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "skills" not in st.session_state:
    st.session_state.skills = []

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🚀 PrepAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "📄 Resume Analysis",
        "🤖 Question Generation",
        "📊 Answer Evaluation"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
### AI Interview Copilot

Powered By:

- FastAPI
- Google Gemini
- Streamlit
"""
)

# ==========================================
# HEADER
# ==========================================

st.title("🚀 PrepAI - AI Interview Copilot")

st.markdown("""
<div class='hero-box'>

### 🎯 Prepare Smarter with AI

Analyze resumes, generate interview questions,
and receive AI-powered answer evaluations.

Built using FastAPI + Gemini AI + Streamlit.

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# KPI SECTION
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Resumes Analyzed",
        "100+"
    )

with col2:
    st.metric(
        "Questions Generated",
        "1000+"
    )

with col3:
    st.metric(
        "AI Evaluation Accuracy",
        "95%"
    )

st.divider()

# ==========================================
# RESUME ANALYSIS
# ==========================================

if page == "📄 Resume Analysis":

    st.header("📄 Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button("Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf"
                    )
                }

                response = requests.post(
                    f"{BACKEND_URL}/upload-resume",
                    files=files
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.skills = data["skills"]

                    st.success(
                        "Resume Analyzed Successfully"
                    )

                    c1, c2 = st.columns(2)

                    with c1:
                        st.metric(
                            "Characters",
                            data["total_characters"]
                        )

                    with c2:
                        st.metric(
                            "Skills Found",
                            data["total_skills"]
                        )

                    st.subheader(
                        "Detected Skills"
                    )

                    badges = ""

                    for skill in data["skills"]:
                        badges += (
                            f"<span class='skill-badge'>{skill}</span>"
                        )

                    st.markdown(
                        badges,
                        unsafe_allow_html=True
                    )

                else:
                    st.error("Failed to analyze resume")

# ==========================================
# QUESTION GENERATION
# ==========================================

elif page == "🤖 Question Generation":

    st.header("🤖 Interview Question Generator")

    detected_skills = st.session_state.skills

    if detected_skills:

        st.success(
            "Skills imported from Resume Analysis"
        )

        st.write(
            ", ".join(detected_skills)
        )

        default_skills = ", ".join(
            detected_skills
        )

    else:

        default_skills = (
            "Python, FastAPI, Machine Learning, RAG"
        )

    skills = st.text_input(
        "Skills",
        value=default_skills
    )

    if st.button("Generate Questions"):

        skill_list = [
            s.strip()
            for s in skills.split(",")
        ]

        with st.spinner(
            "Generating Questions..."
        ):

            response = requests.post(
                f"{BACKEND_URL}/generate-questions",
                json={
                    "skills": skill_list
                }
            )

            if response.status_code == 200:

                st.success(
                    "Questions Generated Successfully"
                )

                st.markdown(
                    response.json()["questions"]
                )

            else:

                st.error(
                    "Failed to Generate Questions"
                )

# ==========================================
# ANSWER EVALUATION
# ==========================================

elif page == "📊 Answer Evaluation":

    st.header("📊 AI Answer Evaluation")

    question = st.text_area(
        "Interview Question",
        height=120
    )

    answer = st.text_area(
        "Your Answer",
        height=220
    )

    if st.button("Evaluate Answer"):

        with st.spinner(
            "Evaluating Answer..."
        ):

            response = requests.post(
                f"{BACKEND_URL}/evaluate-answer",
                json={
                    "question": question,
                    "answer": answer
                }
            )

            if response.status_code == 200:

                evaluation = response.json()["evaluation"]

                st.success(
                    "Evaluation Completed"
                )

                score = None

                match = re.search(
                    r"(\d+)/10",
                    evaluation
                )

                if match:
                    score = int(
                        match.group(1)
                    )

                if score:

                    st.subheader(
                        "Interview Score"
                    )

                    st.progress(
                        score / 10
                    )

                    st.metric(
                        "Score",
                        f"{score}/10"
                    )

                st.markdown(
                    evaluation
                )

                # ==========================================
                # PDF REPORT GENERATION
                # ==========================================

                generate_report(
                    "PrepAI_Report.pdf",
                    question,
                    answer,
                    evaluation,
                    score if score else 0
                )

                with open(
                    "PrepAI_Report.pdf",
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="📄 Download Interview Report",
                        data=pdf_file,
                        file_name="PrepAI_Report.pdf",
                        mime="application/pdf"
                    )

            else:

                st.error(
                    "Evaluation Failed"
                )

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    """
<div class='footer'>

🚀 PrepAI | Built by Anand Mohan Jha

FastAPI • Gemini AI • Streamlit

</div>
""",
    unsafe_allow_html=True
)