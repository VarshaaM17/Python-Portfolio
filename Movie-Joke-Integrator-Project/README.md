# Movie-Joke-Integrator
Developed a Python-based data orchestration engine to analyze movie metadata and automatically generate context-aware humorous content by mapping plot elements across multiple REST APIs.

## Objective
The goal of this project was to synchronize data between disparate platforms—the **OMDb metadata registry** and a **secondary humor database** —to create a seamless, themed content report.

# Technical Implementation
- **API Orchestration:** Engineered a multi-stage pipeline to manage requests and responses between RESTful APIs using the requests library.
- **Data Transformation:** Built logic to clean and tokenize raw plot synopses, removing punctuation and normalizing strings for search compatibility.
- **Contextual Mapping:** Implemented a keyword extraction algorithm to identify high-impact tokens within movie descriptions to drive secondary queries.
- **Dynamic Logic:** Utilized conditional formatting to tailor user messaging and output styles based on movie ratings and metadata scores.

## Skills Used
Python, REST API Integration, JSON Parsing, Data Normalization, String Manipulation.

