import streamlit as st
from PyPDF2 import PdfReader
from resume_parser import extract_text_from_pdf
from matching import match_resume_to_job

st.title("📄 AI-Powered Resume Analyzer")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_desc = st.text_area("Paste the Job Description")

if uploaded_file and job_desc:
    # Extract resume text
    pdf_reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    # Compute match score
    match_score = match_resume_to_job(resume_text, job_desc)

    # Display score
    st.success(f"✅ Resume Match Score: {match_score}%")

    # Suggest improvements
    if match_score < 50:
        st.warning("🔸 Try adding more relevant skills and experience!")
    elif match_score < 80:
        st.info("🔹 Your resume is decent but could be improved!")
    else:
        st.success("🎯 Your resume is a great match for this job!")
