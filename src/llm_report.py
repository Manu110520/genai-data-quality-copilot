from openai import OpenAI
import os


def generate_llm_summary(issues):
    """
    Takes a list of DQ issues and returns a human-friendly explanation.
    """
    if not issues:
        return "No data quality issues were detected."

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
You are a data quality analyst working on enterprise reporting data.

Here are the detected data quality issues:
{chr(10).join("- " + issue for issue in issues)}

Please provide:
1. A short summary of what these issues mean
2. Possible root causes
3. Recommended next actions

Keep it clear, professional, and concise.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
