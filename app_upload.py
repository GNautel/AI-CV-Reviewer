import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="CV Tailor AI", page_icon="📄")

st.title("📄 CV Tailor AI")
st.write("Upload your CV and paste a job description.")

client = OpenAI(
    api_key=st.secrets["OPEN_Router_Api_Key"],
    base_url="https://openrouter.ai/api/v1"
)

uploaded_file = st.file_uploader(
    "Upload your CV file",
    type=["txt"]
)

cv_text = ""

if uploaded_file is not None:
    cv_text = uploaded_file.read().decode("utf-8")
    st.success("CV uploaded successfully.")
    st.text_area("CV Preview", cv_text, height=200)

job_text = st.text_area("Paste the job description here", height=250)

tone = st.selectbox(
    "Choose tone",
    ["Professional", "Confident", "Simple", "Formal"]
)

output_type = st.selectbox(
    "Choose output",
    [
        "CV summary",
        "Skill gap analysis",
        "Improved bullet points",
        "Cover letter paragraph"
    ]
)

if st.button("Generate"):
    if not cv_text or not job_text:
        st.warning("Please upload CV and paste job description.")
    else:
        prompt = f"""
You are a professional career advisor.

Task:
Create a {output_type} based on the CV and job description.

Tone:
{tone}

Rules:
Be honest.
Do not invent experience.
Use keywords from the job description naturally.
Make the output clear and useful for a student applying for a job.

CV:
{cv_text}

Job Description:
{job_text}
"""

        with st.spinner("Generating..."):
            response = client.responses.create(
                model="openrouter/free",
                input=prompt
            )

        st.subheader("AI Output")
        st.write(response.output_text)