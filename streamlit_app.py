import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path
from openai import OpenAI

# ---------------------------------------------------
# Load API key
# ---------------------------------------------------

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

if not api_key:
    st.error("OpenAI API key not found. Add it to Streamlit Secrets or a local .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# ---------------------------------------------------
# Page config
# ---------------------------------------------------

st.set_page_config(
    page_title="Job Fit Analyzer",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("Job Fit Analyzer")

st.sidebar.markdown("""
### About this app

This tool compares a resume against a job description and generates three types of analysis:

1. **Skill Gap Analysis**  
Identifies missing skills, transferable skills, and recommendations.

2. **Keyword Alignment**  
Compares resume keywords against job description keywords.

3. **Fit Summary**  
Provides a short overall assessment of candidate fit.

### How to use

1. Select a job description from the dropdown or paste your own job description  
2. Paste your resume or use the default resume  
3. Choose an analysis type  
4. Click **Run Analysis**

### Recommended resume format

Use a simple text-based resume with sections like:

- Education  
- Technical Skills  
- Experience  
- Projects  
- Leadership or Activities
""")

with st.sidebar.expander("Preview example resume format"):
    st.code("""
JORDAN MILLER
Los Angeles, CA
jordanmiller@email.com

EDUCATION
University of California, Los Angeles
B.S. Business Economics

TECHNICAL SKILLS
SQL
Python
Excel
Tableau
Power BI

EXPERIENCE
Data Analytics Intern
BrightWave Media

- Built Tableau dashboards to track campaign performance
- Analyzed customer data using SQL and Python
- Presented insights to stakeholders

PROJECTS
Customer Segmentation Analysis
- Used Python clustering techniques to segment customers
""")

# ---------------------------------------------------
# Load metadata
# ---------------------------------------------------

@st.cache_data
def load_metadata():
    return pd.read_csv("data/jd_metadata.csv")

metadata = load_metadata()

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("AI Job Fit Analyzer")
st.write("Compare a resume against a job description using structured LLM analysis.")

# ---------------------------------------------------
# JD selection / paste option
# ---------------------------------------------------

col_select, col_analysis = st.columns([1, 1])

with col_select:

    st.subheader("1. Job Description")

    jd_input = st.text_area(
        "Optional: Paste your own job description here:",
        height=220,
        placeholder="Paste a job description here, or leave blank to select one from the dropdown."
    )

    if jd_input.strip():
        jd_text = jd_input
        selected_label = "Custom pasted job description"
        st.info("Using pasted job description.")
    else:
        jd_labels = [
            f"{row.get('Company', row.get('company', 'Unknown Company'))} -- {row.get('title', row.get('Title', 'Unknown Title'))}"
            for _, row in metadata.iterrows()
        ]

        selected_label = st.selectbox(
            "Or choose a job description from the corpus:",
            jd_labels
        )

        selected_row = metadata.iloc[jd_labels.index(selected_label)]

        jd_path = f"data/job_descriptions/{selected_row['filename']}"

        with open(jd_path, "r", encoding="utf-8") as f:
            jd_text = f.read()

    with st.expander("Preview Job Description"):
        st.text(jd_text[:2000] + ("..." if len(jd_text) > 2000 else ""))

with col_analysis:

    st.subheader("2. Choose Analysis Type")

    analysis_type = st.radio(
        "Select analysis:",
        [
            "Skill Gap Analysis",
            "Keyword Alignment",
            "Fit Summary"
        ]
    )

# ---------------------------------------------------
# Resume paste option
# ---------------------------------------------------

st.subheader("3. Resume")

resume_input = st.text_area(
    "Optional: Paste your resume here:",
    height=260,
    placeholder="Paste a resume here, or leave blank to use the default resume."
)

if resume_input.strip():
    resume_text = resume_input
    st.info("Using pasted resume.")
else:
    resume_path = "data/resume/resume.txt"

    with open(resume_path, "r", encoding="utf-8") as f:
        resume_text = f.read()

    st.info("Using default resume from project files.")

with st.expander("Preview Resume"):
    st.text(resume_text[:2000] + ("..." if len(resume_text) > 2000 else ""))

# ---------------------------------------------------
# Prompt templates
# ---------------------------------------------------

def build_prompt(analysis_type):

    if analysis_type == "Skill Gap Analysis":

        return f"""
        Compare this resume against the job description.

        Use only the provided resume and job description.
        Do not assume years of experience unless explicitly stated.

        Resume:
        {resume_text}

        Job Description:
        {jd_text}

        Provide:
        1. Missing Skills
        2. Transferable Skills
        3. Recommendations
        """

    elif analysis_type == "Keyword Alignment":

        return f"""
        Compare the resume and job description.

        Use only the provided resume and job description.

        Resume:
        {resume_text}

        Job Description:
        {jd_text}

        Provide:
        1. Matching Keywords
        2. Missing Keywords
        3. Alignment Summary
        """

    else:

        return f"""
        Evaluate the candidate's fit for the role.

        Use only the provided resume and job description.
        Do not exaggerate the candidate's experience.

        Resume:
        {resume_text}

        Job Description:
        {jd_text}

        Provide:
        1. Overall Fit
        2. Strengths
        3. Weaknesses
        """

# ---------------------------------------------------
# Run analysis
# ---------------------------------------------------

st.divider()

if st.button("Run Analysis", type="primary"):

    try:

        prompt = build_prompt(analysis_type)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        output = response.choices[0].message.content

        st.subheader(f"Results: {analysis_type}")

        st.markdown(output)

    except Exception as e:

        st.error(f"Error: {e}")
