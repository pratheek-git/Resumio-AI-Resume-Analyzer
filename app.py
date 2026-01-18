import streamlit as st
from dotenv import load_dotenv

from utils.pdf_utils import extract_pdf_text
from services.ats_service import calculate_similarity_bert
from services.groq_service import generate_report
from utils.score_utils import extract_scores

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("AI Resume Analyzer")

# Session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "resume" not in st.session_state:
    st.session_state.resume = ""
if "job_desc" not in st.session_state:
    st.session_state.job_desc = ""

# Form
if not st.session_state.submitted:
    with st.form("resume_form"):
        resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
        job_desc = st.text_area("Job Description")

        submitted = st.form_submit_button("Analyze")
        if submitted:
            if resume_file and job_desc.strip():
                st.session_state.resume = extract_pdf_text(resume_file)
                st.session_state.job_desc = job_desc
                st.session_state.submitted = True
                st.rerun()
            else:
                st.warning("Please upload resume and job description.")

# Results
if st.session_state.submitted:
    st.info("Generating analysis...")

    ats_score = calculate_similarity_bert(
        st.session_state.resume,
        st.session_state.job_desc
    )

    report = generate_report(
        st.session_state.resume,
        st.session_state.job_desc
    )

    scores = extract_scores(report)
    avg_score = round(sum(scores) / len(scores), 2) if scores else 0

    col1, col2 = st.columns(2)
    col1.metric("ATS Similarity Score", round(ats_score, 2))
    col2.metric("AI Evaluation Score", round(avg_score, 2))

    st.subheader("AI Analysis Report")
    st.markdown(report)


    st.download_button(
        "Download Report",
        report,
        file_name="resume_analysis.txt"
    )
