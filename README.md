# GenAI Data Quality Copilot

A Python-based tool that reads Excel datasets, detects data quality issues, and uses OpenAI to generate human-friendly explanations and recommended next actions.

## What this project does

This project simulates a lightweight enterprise data quality workflow:

1. Reads Excel input data using pandas
2. Detects common data quality issues such as:
   - missing values
   - duplicate IDs
   - invalid numeric values
3. Sends the detected issues to an OpenAI model
4. Generates an AI-assisted Markdown report with explanations and suggested remediation steps

## Why I built this

I wanted to build a practical GenAI project that connects data engineering, validation logic, and AI-assisted reporting.

This project reflects real-world enterprise use cases in banking, analytics, and regulatory reporting, where data quality issues need to be identified and explained clearly for business and technical stakeholders.

## Tech stack

- Python
- pandas
- openpyxl
- OpenAI API
- Markdown reporting
- Git / GitHub

## Project structure

```text
genai-data-quality-copilot/
├── src/
│   ├── dq_checks.py
│   └── llm_report.py
├── data/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore

WORKFLOW::::

Excel file
   ↓
pandas DataFrame
   ↓
Data quality checks
   ↓
OpenAI issue explanation
   ↓
Markdown report output

# Data Quality Report

## Issues Detected

- Column 'country' has 1 null values
- Column 'as_of_date' has 1 null values
- Found 1 duplicate customer_id values
- Found 1 records with negative exposure

## AI Summary

The identified issues suggest a combination of data completeness, uniqueness, and business rule validation failures. These may originate from upstream ingestion issues, incomplete source submissions, or insufficient validation rules in the pipeline.

Recommended next actions include validating source file completeness, applying uniqueness constraints on business keys, and adding pre-ingestion checks for numeric rule violations.
