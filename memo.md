# Assignment 5 Memo

**To:** Technical Manager  
**From:** Marcela Lozano  
**Date:** May 2026  
**RE:** RAG-Based Job Fit Analysis System Evaluation and Recommendations  

## Summary

The purpose of this project was to develop a Retrieval-Augmented Generation(RAG) system that can be used to evaluate how well a candidate’s resume aligns with different job descriptions. The goal of the system was to support the job application process by generating structured AI analyses that identify skill gaps, keyword alignment, and overall job fit. The system uses retrieved resume and job description context to produce more actionable and specific recommendations for each job description rather than relying only on a general language model response.

The project focuses on three main analysis types: Skill Gap Analysis, Keyword Alignment, and Fit Summary. These outputs were tested across the top three target job descriptions, resulting in nine total evaluations. The system was evaluated based on retrieval relevance, skill identification accuracy, actionability, and faithfulness.

## Project Approach

The system begins by loading the candidate resume and multiple job descriptions. Next the text was split into chunks so the model could retrieve smaller and relevant sections instead of processing the full documents all at once. I used two chunking strategies for testing: fixed-size chunking and sentence-aware chunking.

The first approach was fixed-size chunking which splits text into sections of similar length. The second approach uses sentence-aware chunking which attempts to preserve sentence boundaries and maintain more natural context. I selected sentence-aware chunking as the stronger option because the retrieved text was easier to interpret and more useful for job fit analysis. It was key to preserve sentence meaning since resume bullet points and job requirement statements can lose meaning if they are split in the middle.

After chunking, the system uses embeddings to convert text into numerical representations. These embeddings are stored in a vector database, which allows the system to retrieve the most relevant resume and job description sections based on the user’s question or selected analysis type. The retrieved context is then passed into an OpenAI model to generate the final response.

## Prompting Strategy

The project tested both zero-shot and few-shot prompting. Zero-shot prompting asked the model to complete the analysis without examples. Few-shot prompting included examples of the expected output style and structure.

Few-shot prompting produced stronger results because it gave the model a clearer expectation for how to organize the analysis to ensure user readability. This was especially helpful for the Skill Gap Analysis and Keyword Alignment outputs, where the response needed to distinguish between matched qualifications, missing skills, and transferable experience.

At least three prompt iterations were completed during development. The prompts were revised to make the outputs more specific, reduce vague recommendations, and improve the connection between the resume evidence and the job description requirements.

## Key Results

The strongest analysis type was the Skill Gap Analysis. This output was the most actionable because it identified specific missing or underdeveloped skills and translated them into practical recommendations. For example, it could point out when a candidate had transferable analytics experience but lacked direct job-specific terminology such as pricing analytics, supply chain systems, product roadmap experience, or experimentation platforms.

Keyword Alignment also performed well. It was useful for identifying which job description terms were already reflected in the resume and which terms were missing. This analysis is especially helpful for improving applicant tracking system alignment because it shows where the resume could be revised to better match the language of the job posting.

Fit Summary was useful for providing a high-level assessment of job match, but it was slightly less actionable than the other two analysis types. The fit summaries were generally relevant but they sometimes overstated experience and gave broader recommendations instead of specific resume revision steps.

Overall, the system successfully produced the required nine evaluations across the top three job descriptions and three analysis types.

## Evaluation Method

The outputs were evaluated using four criteria:

### Retrieval Relevance

Retrieval relevance measured whether the analysis used the correct resume and job description information. A strong output referenced the right role-specific skills, qualifications, and experience. A weaker output included information that was too general or not clearly connected to the selected job description.

### Skill Identification Accuracy

Skill identification accuracy measured whether the system correctly identified the candidate’s existing skills, missing skills, and transferable experience. This was important because the system should not claim that the candidate has direct experience when the resume only shows related or conceptual knowledge.

### Actionability

Actionability measured how useful the output was for improving the resume or job application strategy.

The actionability score used a 1 to 5 scale:

| Score | Meaning |
|---|---|
| 1 | Not actionable. The response is vague, generic, or unrelated to the resume and job description. |
| 2 | Slightly actionable. The response identifies some relevant points but gives limited guidance. |
| 3 | Moderately actionable. The response gives useful suggestions, but they may be broad or missing clear next steps. |
| 4 | Actionable. The response gives relevant and practical recommendations that could be applied to the resume or application strategy. |
| 5 | Highly actionable. The response gives specific, realistic, and directly applicable recommendations tied to the resume and job description. |

### Faithfulness

Faithfulness measured whether the output stayed grounded in the provided resume and job description. A faithful response avoided inventing experience or exaggerating the candidate’s qualifications. This was especially important because job fit analysis can become misleading if the model overstates the candidate’s background.

## Model Recommendation

The recommended system design is the RAG pipeline using sentence-aware chunking, embedding-based retrieval, and few-shot prompts. This combination produced the most useful and grounded results.

The best final analysis type for job seekers is the Skill Gap Analysis since it provides the clearest next steps. It not only identifies missing qualifications but also explains how the candidate can improve their resume, application strategy, or interview preparation. Keyword Alignment is also valuable because it helps improve resume language and alignment with job descriptions. Fit Summary should be used as a supporting overview rather than the primary decision-making output.

## Key Limitations

One limitation is that the quality of the output depends heavily on the quality of the resume and job description text. If the resume lacks detail or the job description is vague, the system may produce broader recommendations.

A second limitation is that some skills may be inferred from transferable experience. For example, consulting, client management, analytics coursework, and project work may suggest product or business strategy potential even though they do not always prove direct professional experience in those areas. This lead to the the system struggling to clearly distinguish between direct experience, transferable experience, and missing experience.

Another limitation is that the final outputs still require human review. The system can support resume revision and job targeting but still requires the user to verify that the recommendations are accurate before making changes to an application.

## Business Implications

A RAG-based job fit analysis system can help students and job seekers better understand how their resumes align with specific roles they are looking to apply to. This type of tool is useful because many candidates apply to jobs without knowing which skills are missing or how well their resume matches the job description.

The system is meant to support career advising by giving students a structured starting point for resume revisions and tailoring resumes to reflect specific keywords in the job description. It can also help users prioritize which jobs are stronger matches and which roles require more preparation. Instead of treating the job search as a generic process, this tool provides role-specific feedback based on the candidate’s actual resume and job descriptions.

For future improvements, the system could provide resume bullet suggestions, ATS keyword recommendations, and a final job fit score. These improvements would make the system more interactive and useful for real job search workflows.

## Final Recommendation

The final recommendation is to use the RAG-based job fit analysis system as a resume and job application support tool. The system is not meant to replace human judgement but it provides meaningful value by identifying skill gaps, improving keyword alignment, and summarizing job fit in a structured way. The strongest use case is helping candidates revise their resumes and prepare more targeted applications for specific roles.
