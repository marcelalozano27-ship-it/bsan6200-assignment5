import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

from openai import OpenAI

# ---------------------------------------------------
# Load API key
# ---------------------------------------------------
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")
print("API key loaded:", api_key is not None)

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
This application compares a resume against real job descriptions using LLM prompting.

Analyses included:
- Skill Gap Analysis
- Keyword Alignment
- Fit Summary

Created for BSAN 6200 Assignment 5
""")

# ---------------------------------------------------
# Load metadata
# ---------------------------------------------------

@st.cache_data
def load_metadata():
    return pd.read_csv("data/jd_metadata.csv")

metadata = load_metadata()

# ---------------------------------------------------
# JD selector
# ---------------------------------------------------

st.title("AI Job Fit Analyzer")

selected_jd = st.selectbox(
    "Select a Job Description",
    metadata["title"]
)

analysis_type = st.radio(
    "Choose Analysis Type",
    [
        "Skill Gap Analysis",
        "Keyword Alignment",
        "Fit Summary"
    ]
)

# ---------------------------------------------------
# Load selected JD
# ---------------------------------------------------

selected_row = metadata[metadata["title"] == selected_jd].iloc[0]

jd_path = f"data/job_descriptions/{selected_row['filename']}"

with open(jd_path, "r", encoding="utf-8") as f:
    jd_text = f.read()

# ---------------------------------------------------
# Load resume
# ---------------------------------------------------

resume_path = "data/resume/resume.txt"

with open(resume_path, "r", encoding="utf-8") as f:
    resume_text = f.read()

# ---------------------------------------------------
# Prompt templates
# ---------------------------------------------------

def build_prompt(analysis_type):

    if analysis_type == "Skill Gap Analysis":

        return f"""
        Compare this resume against the job description.

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

if st.button("Run Analysis"):

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

        st.subheader("Results")

        st.markdown(output)

    except Exception as e:

        st.error(f"Error: {e}")