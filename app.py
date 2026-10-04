import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="CV Tailor AI", page_icon="📄")

st.title("📄 CV Tailor AI")
st.write("Paste your CV and a job description. The app will generate a tailored CV summary, skill match, and improved bullet points.")

client = OpenAI(
    api_key=st.secrets["OPEN_Router_Api_Key"],
    base_url="https://openrouter.ai/api/v1"
)

cv_text = st.text_area("Paste your CV here", height=250)

job_text = st.text_area("Paste the job description here", height=250)

tone = st.selectbox(
    "Choose tone",
    ["Professional", "Confident", "Simple", "Formal"]
)

output_type = st.selectbox(
    "Choose output",
    ["CV summary", "Skill gap analysis", "Improved bullet points", "Cover letter paragraph"]
)

if st.button("Generate"):
    if not cv_text or not job_text:
        st.warning("Please paste both CV and job description.")
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
            response = client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=300
            )

        st.subheader("AI Output")
        st.write(response.choices[0].message.content)