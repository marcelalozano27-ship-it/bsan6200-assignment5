# Test Results

## Overview

This file documents the testing and evaluation results for the Assignment 5 RAG-based Job Fit Analysis system. The system was evaluated based on chunking strategy, retrieval quality, prompt performance, and final analysis output quality.

## Chunking Strategy Comparison

Two chunking strategies were tested:

| Chunking Strategy | Description | Result |
|---|---|---|
| Fixed-size chunking | Splits text into chunks of similar character length | Worked, but sometimes separated related job requirements or resume details |
| Sentence-aware chunking | Splits text while preserving sentence boundaries | Performed better because the retrieved context was easier to interpret and more complete |

Sentence-aware chunking was selected for the final pipeline because it better preserved meaning in resume bullet points and job description requirements.

## Retrieval Testing

Retrieval was tested by running similarity searches against the resume and job description content stored in the vector database. The goal was to confirm that the system retrieved relevant sections before generating the final AI response.

The retrieval results were evaluated based on whether the returned context matched the selected job description and analysis type.

| Test Area | Result |
|---|---|
| Resume retrieval | Relevant resume sections were retrieved for job fit questions |
| Job description retrieval | Relevant job requirements and qualifications were retrieved |
| Role-specific context | Retrieval was strongest when the query clearly referenced the target role or analysis type |
| Overall retrieval quality | Good, but dependent on clear prompts and well-structured source text |

## Prompt Testing

The project tested both zero-shot and few-shot prompting.

| Prompt Type | Result |
|---|---|
| Zero-shot prompting | Produced usable responses but sometimes gave broad or generic recommendations |
| Few-shot prompting | Produced stronger structure, clearer recommendations, and more consistent formatting |

Few-shot prompting was selected as the stronger approach because it helped the model better distinguish between matched skills, missing skills, and transferable experience.

## Prompt Iterations

At least three prompt iterations were completed.

| Iteration | Modification | Result |
|---|---|---|
| Iteration 1 | Basic prompt asking for a general job fit response | Output was relevant but too broad |
| Iteration 2 | Added specific sections for matched skills, missing skills, and recommendations | Output became more organized and useful |
| Iteration 3 | Added clearer instructions to avoid exaggerating experience and to ground the response in the resume and job description | Output became more faithful and actionable |

## Final Analysis Evaluation

The final evaluation tested three analysis types across the top three job descriptions, resulting in nine total outputs.

The three analysis types were:

1. Fit Summary
2. Keyword Alignment
3. Skill Gap Analysis

The outputs were evaluated using four criteria:

| Criterion | Meaning |
|---|---|
| Retrieval Relevance | Whether the output used relevant resume and job description information |
| Skill Identification Accuracy | Whether the system correctly identified matched, missing, and transferable skills |
| Actionability | Whether the output gave practical recommendations |
| Faithfulness | Whether the output stayed grounded in the resume and job description without inventing experience |

## Actionability Rating Scale

| Score | Meaning |
|---|---|
| 1 | Not actionable. The response is vague, generic, or unrelated to the resume and job description. |
| 2 | Slightly actionable. The response identifies some relevant points but gives limited guidance. |
| 3 | Moderately actionable. The response gives useful suggestions, but they may be broad or missing clear next steps. |
| 4 | Actionable. The response gives relevant and practical recommendations that could be applied to the resume or application strategy. |
| 5 | Highly actionable. The response gives specific, realistic, and directly applicable recommendations tied to the resume and job description. |

## Evaluation Table

| Position | Analysis Type | Retrieval Relevance | Skill Identification Accuracy | Actionability | Faithfulness | Notes |
|---|---|---|---|---|---|---|
| Data Analyst Lead | Fit Summary | Yes | Correct: analytics background, SQL, Python, Tableau, Power BI and communication. Partial: demand forecasting and pricing optimization slightly overstated. Incorrect: A/B Testing is listed as hands on experience but resume specifies only a conceptual understanding. | 3 | Partial | Strong overall fit assessment, but slightly overstated experience level. This analysis was overall less useful and less actionable without concrete steps. |
| Data Analyst Lead | Keyword Alignment | Yes | Correct: Tableau, Power BI, forecasting, customer segmentation, SQL, ML, communication. Partial: pricing strategy and business partnering were inferred from transferable experience. Incorrect: No major errors. | 4 | Faithful | Strong keyword extraction and alignment quality. Actionable summary is provided indicating a lack of specific experience like ticketing strategy. |
| Data Analyst Lead | Skill Gap Analysis | Yes | Correct: pricing elasticity gap, ticketing analytics gap, experimentation platforms, advanced SQL/BI skills. Partial: business partnering and ML specialization partially inferred from experience. Incorrect:  No major errors. | 5 | Faithful | Most actionable and detailed output. Correctly identified that A/B testing is only known conceptually. Links transferrable skills correctly and provides specific recommendations|
| Production & Supply Planning Intern | Fit Summary | Partial | Correct: analytical skills, data management, organization, project management. Partial: supply chain process improvement potential inferred from analytics background. Incorrect: No major errors. | 4 | Partial | Transferable skills identified correctly, but domain alignment was weaker. The model assumes that the individual would not be a good fit for this role because they are overqualified. |
| Production & Supply Planning Intern | Keyword Alignment | Yes | Correct: communication, organization, attention to detail, data management. Partial: vendor communication partially inferred from client management. Incorrect: No major errors. | 4 | Faithful | Accurate identification of missing supply chain terminology. Correctly identified that the role may not be the best fit without supply chain and fashion business experience. |
| Production & Supply Planning Intern | Skill Gap Analysis | Yes | Correct: ERP systems, vendor communication, fashion business knowledge, supply chain gaps. Partial: Excel gap somewhat overstated because Excel already exists in resume. Incorrect:  No major errors. | 5 | Faithful | Recommendations were realistic and actionable. Recommendations identify the gaps and provide straightforward and easy to follow interpretation. |
| Associate Product Manager | Fit Summary | Yes | Correct: cross-functional collaboration, analytics, communication, project management. Partial: product strategy and customer research partially inferred from consulting experience. Incorrect: No major errors. | 3 | Faithful | Strong transferable skills identified for PM role. No real actions are recommended which makes this analysis weaker. |
| Associate Product Manager | Keyword Alignment | Yes | Correct: research, collaboration, communication, data analysis, multiple projects. Partial: product knowledge partially inferred from strategy work. Incorrect: No major errors. | 4 | Faithful | Good distinction between matched and missing PM terminology. |
| Associate Product Manager | Skill Gap Analysis | Yes | Correct: product roadmap, Jira/Trello, product marketing, customer feedback gaps. Partial: PM methodology gaps inferred indirectly. Incorrect: No major errors. | 5 | Faithful | Clear recommendations for transitioning into PM roles. |

## Overall Findings

The Skill Gap Analysis proved to be the strongest analysis type since it gave the most specific and actionable recommendations. It clearly identified missing skills and explained how the candidate could improve the resume to match keywords for the job description as well as how to prepare for the role.

Keyword Alignment was also useful because it identified matched and missing job description terms. This is helpful for improving resume wording and applicant tracking system alignment.

Fit Summary was useful as a high-level overview, but it was less actionable since it gave broader recommendations and occasionally overstated experience.

## Final Recommendation

The final recommended pipeline uses sentence-aware chunking, embedding-based retrieval, and few-shot prompting. This combination produced the most structured, grounded, and useful job fit analysis results.
