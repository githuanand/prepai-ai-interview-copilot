import re

import requests
import streamlit as st

from report_generator import generate_report


# ==========================================
# CONFIG
# ==========================================

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="PrepAI - AI Interview Copilot",
    page_icon="🚀",
    layout="wide",
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .skill-badge {
        display: inline-block;
        background: #0e7490;
        color: white;
        padding: 8px 14px;
        border-radius: 15px;
        margin: 5px;
        font-size: 14px;
        font-weight: 600;
    }

    .hero-box {
        background: linear-gradient(90deg, #1e3a8a, #0f766e);
        padding: 25px;
        border-radius: 15px;
        color: white;
    }

    .footer {
        text-align: center;
        padding: 15px;
        color: gray;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================
# SESSION STATE
# ==========================================

if "skills" not in st.session_state:
    st.session_state.skills = []

if "resumes_analyzed" not in st.session_state:
    st.session_state.resumes_analyzed = 0

if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = 0

if "answers_evaluated" not in st.session_state:
    st.session_state.answers_evaluated = 0


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🚀 PrepAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "📄 Resume Analysis",
        "🤖 Question Generation",
        "📊 Answer Evaluation",
    ],
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
### AI Interview Copilot

Powered By:

- FastAPI
- Groq AI
- Streamlit
"""
)


# ==========================================
# HEADER
# ==========================================

st.title("🚀 PrepAI - AI Interview Copilot")

st.markdown(
    """
    <div class="hero-box">

    ### 🎯 Prepare Smarter with AI

    Analyze resumes, generate interview questions,
    and receive AI-powered answer evaluations.

    Built using FastAPI + Groq AI + Streamlit.

    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")


# ==========================================
# REAL SESSION METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Resumes Analyzed",
        st.session_state.resumes_analyzed,
    )

with col2:
    st.metric(
        "Questions Generated",
        st.session_state.questions_generated,
    )

with col3:
    st.metric(
        "Answers Evaluated",
        st.session_state.answers_evaluated,
    )

st.divider()


# ==========================================
# RESUME ANALYSIS
# ==========================================

if page == "📄 Resume Analysis":

    st.header("📄 Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"],
    )

    if uploaded_file:

        if st.button(
            "Analyze Resume",
            type="primary",
        ):

            with st.spinner("Analyzing Resume..."):

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf",
                    )
                }

                try:

                    response = requests.post(
                        f"{BACKEND_URL}/upload-resume",
                        files=files,
                        timeout=60,
                    )

                    if response.status_code == 200:

                        data = response.json()

                        st.session_state.skills = data["skills"]

                        st.session_state.resumes_analyzed += 1

                        st.success(
                            "Resume Analyzed Successfully"
                        )

                        c1, c2 = st.columns(2)

                        with c1:
                            st.metric(
                                "Characters",
                                data["total_characters"],
                            )

                        with c2:
                            st.metric(
                                "Skills Found",
                                data["total_skills"],
                            )

                        st.subheader("Detected Skills")

                        badges = ""

                        for skill in data["skills"]:

                            badges += (
                                f"<span class='skill-badge'>"
                                f"{skill}"
                                f"</span>"
                            )

                        st.markdown(
                            badges,
                            unsafe_allow_html=True,
                        )

                    else:

                        st.error(
                            f"Failed to analyze resume "
                            f"(HTTP {response.status_code})"
                        )

                except requests.exceptions.RequestException as error:

                    st.error(
                        f"Unable to connect to backend: {error}"
                    )


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

        default_skills = ""

        st.info(
            "Analyze a resume first, or enter your skills manually."
        )

    skills = st.text_input(
        "Skills",
        value=default_skills,
        placeholder="Python, FastAPI, SQL, Machine Learning",
    )

    if st.button(
        "Generate Questions",
        type="primary",
    ):

        skill_list = [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

        if not skill_list:

            st.warning(
                "Please enter at least one skill."
            )

        else:

            with st.spinner(
                "Generating Questions..."
            ):

                try:

                    response = requests.post(
                        f"{BACKEND_URL}/generate-questions",
                        json={
                            "skills": skill_list
                        },
                        timeout=120,
                    )

                    if response.status_code == 200:

                        data = response.json()

                        st.session_state.questions_generated += 1

                        st.success(
                            "Questions Generated Successfully"
                        )

                        st.markdown(
                            data["questions"]
                        )

                    else:

                        st.error(
                            f"Failed to generate questions "
                            f"(HTTP {response.status_code})"
                        )

                except requests.exceptions.RequestException as error:

                    st.error(
                        f"Unable to connect to backend: {error}"
                    )


# ==========================================
# ANSWER EVALUATION
# ==========================================

elif page == "📊 Answer Evaluation":

    st.header("📊 AI Answer Evaluation")

    question = st.text_area(
        "Interview Question",
        height=120,
        placeholder="Enter the interview question...",
    )

    answer = st.text_area(
        "Your Answer",
        height=220,
        placeholder="Enter your answer...",
    )

    if st.button(
        "Evaluate Answer",
        type="primary",
    ):

        if not question.strip():

            st.warning(
                "Please enter the interview question."
            )

        elif not answer.strip():

            st.warning(
                "Please enter your answer."
            )

        else:

            with st.spinner(
                "Evaluating Answer..."
            ):

                try:

                    response = requests.post(
                        f"{BACKEND_URL}/evaluate-answer",
                        json={
                            "question": question,
                            "answer": answer,
                        },
                        timeout=120,
                    )

                    if response.status_code == 200:

                        data = response.json()

                        evaluation = data["evaluation"]

                        st.session_state.answers_evaluated += 1

                        st.success(
                            "Evaluation Completed"
                        )

                        # ----------------------------------
                        # Extract Score
                        # ----------------------------------

                        score = None

                        match = re.search(
                            r"\b(\d+)\s*/\s*10\b",
                            evaluation,
                        )

                        if match:

                            score = int(
                                match.group(1)
                            )

                            if 0 <= score <= 10:

                                st.subheader(
                                    "Interview Score"
                                )

                                st.progress(
                                    score / 10
                                )

                                st.metric(
                                    "Score",
                                    f"{score}/10",
                                )

                        # ----------------------------------
                        # Display Evaluation
                        # ----------------------------------

                        st.markdown(
                            evaluation
                        )

                        # ----------------------------------
                        # Generate PDF Report
                        # ----------------------------------

                        report_path = (
                            "PrepAI_Report.pdf"
                        )

                        generate_report(
                            report_path,
                            question,
                            answer,
                            evaluation,
                            score if score is not None else 0,
                        )

                        with open(
                            report_path,
                            "rb",
                        ) as pdf_file:

                            st.download_button(
                                label="📄 Download Interview Report",
                                data=pdf_file,
                                file_name="PrepAI_Report.pdf",
                                mime="application/pdf",
                            )

                    else:

                        st.error(
                            f"Evaluation failed "
                            f"(HTTP {response.status_code})"
                        )

                except requests.exceptions.RequestException as error:

                    st.error(
                        f"Unable to connect to backend: {error}"
                    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🚀 PrepAI | Built by Anand Mohan Jha

    FastAPI • Groq AI • Streamlit

    </div>
    """,
    unsafe_allow_html=True,
)