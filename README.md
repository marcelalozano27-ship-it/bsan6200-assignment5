# BSAN 6200 Assignment 5: Job Fit Analyzer

## Project Overview

This project was completed for **BSAN 6200: Text Mining & Social Media Analytics** as **Assignment 5, Option B: Job Fit Analyzer**.

The primary goal of this project is to build a job fit analysis system that compares a candidate resume against multiple job descriptions. The system uses text loading, chunking, embeddings, vector search, and prompt-based analysis to generate role-specific feedback. The final project includes both a Colab notebook and a deployed Streamlit app.

## Live Streamlit App

The deployed Streamlit app is available here:

https://jobfitanalysis.streamlit.app/

## Repository Contents

```text
bsan6200-assignment5/
│
├── notebooks/
│   └── rag_pipeline.ipynb
│
├── data/
│   ├── job_descriptions/
│   ├── resume/
│   └── jd_metadata.csv
│
├── evaluation/
│   ├── test_results.md
│
├── AI_Log
├── streamlit_app.py
├── .gitignore
├── requirements.txt
├── memo.md
└── README.md
```

---

## 1. Setup and Imports

The first section installs and imports the necessary packages for the job fit analysis pipeline. The project uses Python libraries for data handling, document processing, embeddings, vector storage, and application deployment.

Key tools used include:

- `pandas`
- `numpy`
- `requests`
- `sentence-transformers`
- `chromadb`
- `python-dotenv`
- `streamlit`

This section also loads environment variables so that API keys are not hardcoded directly into the notebook.

---

## 2. Load Job Descriptions and Resume

The second section loads the resume and job description documents. The project uses:

- 13 job descriptions
- 1 candidate resume
- A metadata file containing job title, company, source URL, and collection date

The job descriptions are stored in the `data/job_descriptions/` folder, while the resume is stored in the `data/resume/` folder. The notebook also loads `jd_metadata.csv` to connect each job description file with its company, title, and source information.

The job descriptions include roles such as:

- Data Analyst Lead
- Production & Supply Planning Intern
- Associate Product Manager
- Financial Strategy Intern
- Analytics Intern
- Data Analyst Merchandising
- Content Analytics and Insights Intern
- Strategic Partnerships Intern
- Research Analytics Summer Intern
- Strategic Partner Manager Intern
- Corporate Rotational Analyst
- Brand Label Operations
- Business Supply Chain Intern

This section confirms that the documents loaded correctly by printing the number of job descriptions, the resume document, and preview text from selected files.

---

## 3. Text Chunking

The third section splits the resume and job description documents into smaller text chunks so they can be used in retrieval and analysis.

Two chunking strategies were tested:

1. **Fixed-size chunking**
   - Splits documents into chunks based on a set character length.
   - This approach is simple but can split sentences or requirements in awkward places.

2. **Sentence-aware chunking**
   - Splits documents while trying to preserve complete sentences and natural meaning.
   - This approach keeps job responsibilities, qualifications, and resume evidence more readable.

Sentence-aware chunking was selected as the better strategy because job descriptions often contain important sections such as responsibilities, qualifications, and preferred skills. By preserving complete ideas, the quality of retrieval improves and makes the analysis outputs more interpretable.

---

## 4. Embedding and Vector Store

The fourth section converts the document chunks into embeddings. Embeddings are numerical representations of text that allow the system to compare the resume and job descriptions based on meaning rather than exact keyword matches.

This project uses a sentence transformer embedding model to create vector representations of each chunk. These vectors are stored in a ChromaDB vector store.

The vector store allows the system to retrieve the most relevant resume and job description chunks for a specific query, such as:

- Skill gap analysis for a job
- Keyword alignment for a job
- Fit summary for a job

This retrieval step is important because it provides the model with focused context instead of sending the entire resume and job description at once.

---

## 5. Analysis Prompts and Chain

The fifth section defines the main analysis prompts used in the job fit analyzer. Three types of analysis are created:

### Skill Gap Analysis

This analysis identifies the skills required by the job description and compares them against the resume. It highlights matched skills, missing skills, and recommendations for improving alignment.

### Keyword Alignment

This analysis compares job description keywords with resume keywords. It identifies which keywords are already represented in the resume and which important terms could be added or emphasized.

### Fit Summary

This analysis provides a short narrative summary of how well the candidate fits the role. It uses evidence from both the resume and job description to describe strengths, transferable skills, and potential weaknesses.

The prompts were revised through multiple iterations to improve accuracy, reduce unsupported assumptions, and make the recommendations more specific to the candidate.

---

## 6. Zero-shot vs. Few-shot Comparison

The sixth section compares zero-shot and few-shot prompting.

### Zero-shot Prompting

Zero-shot prompting asks the model to complete the analysis without providing an example output. This approach is faster and more flexible, but the results can sometimes be more general or less structured.

### Few-shot Prompting

Few-shot prompting provides the model with an example of the desired output format before asking it to complete the task. This approach generally produced more consistent and detailed results because the model had a clearer structure to follow.

The comparison helped determine which prompt style produced stronger job fit outputs. The few-shot approach was more useful for structured analysis because it improved specificity, organization, and alignment with the expected response format.

---

## 7. Evaluation

The seventh section evaluates the job fit analyzer outputs across multiple job descriptions and analysis types.

The evaluation focuses on four categories:

| Evaluation Category | Description |
|---|---|
| Retrieval Relevance | Whether the system retrieved the correct job description sections |
| Skill Identification Accuracy | Whether the matched skills and skill gaps were correct |
| Actionability | Whether the recommendations were specific and useful |
| Faithfulness | Whether the output stayed grounded in the resume and job description content |

The evaluation found that the **Skill Gap Analysis** was the strongest analysis type overall because it produced the most specific and actionable recommendations. It helped identify realistic improvements for resume targeting, such as adding missing job-specific keywords and emphasizing transferable experience.

The main weakness was that some outputs occasionally inferred experience from related skills rather than direct resume evidence. For example, some outputs slightly overstated experience in areas such as pricing optimization, A/B testing, demand forecasting, supply chain process improvement, or product strategy. This showed the importance of checking faithfulness and making sure the model does not infer beyond the provided documents.

---

## 8. Streamlit App

An interactive Streamlit app was developed to make the RAG-based job fit analyzer easier to use. The app allows users to either use a pre-saved resume and job description or upload their own resume and paste a custom job description for analysis.

The app supports three analysis types:

1. **Fit Summary**: Provides an overall assessment of how well the resume aligns with the selected job description.
2. **Keyword Alignment**: Identifies matched and missing keywords between the resume and job description.
3. **Skill Gap Analysis**: Highlights missing or underdeveloped skills and provides recommendations for improving the application.

The app also includes sidebar instructions that explain how the uploaded resume should be formatted. These instructions help users structure their resume text clearly so the system can better identify experience, skills, education, and projects during the analysis.

The app is implemented in `streamlit_app.py` and deployed using Streamlit Cloud.

Live app:

https://jobfitanalysis.streamlit.app/

---

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/marcelalozano27-ship-it/bsan6200-assignment5.git
cd bsan6200-assignment5
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run streamlit_app.py
```

### 4. Open the notebook

The main notebook is located at:

```text
notebooks/rag_pipeline.ipynb
```

It can be opened in Google Colab or Jupyter Notebook.

---

## Author

Marcela Lozano  
M.S. Business Analytics  
Loyola Marymount University
