import pandas as pd
from llm_report import generate_llm_summary


def run_checks(df):
    results = []

    # Null check
    nulls = df.isnull().sum().to_dict()
    for col, count in nulls.items():
        if count > 0:
            results.append(f"Column '{col}' has {count} null values")

    # Duplicate customer_id
    if "customer_id" in df.columns and df["customer_id"].duplicated().any():
        dup_count = df["customer_id"].duplicated().sum()
        results.append(f"Found {dup_count} duplicate customer_id values")

    # Negative exposure
    if "exposure" in df.columns and (df["exposure"] < 0).any():
        neg_count = (df["exposure"] < 0).sum()
        results.append(f"Found {neg_count} records with negative exposure")

    return results


if __name__ == "__main__":
    print("Reading Excel: data/sample.xlsx")

    df = pd.read_excel("data/sample.xlsx")
    issues = run_checks(df)

    llm_summary = generate_llm_summary(issues)

    report_lines = []
    report_lines.append("# Data Quality Report\n\n")

    if not issues:
        report_lines.append("No issues found ✅\n")
    else:
        report_lines.append("## Issues Detected\n\n")
        for issue in issues:
            report_lines.append(f"- {issue}\n")

        report_lines.append("\n## AI Summary\n\n")
        report_lines.append(llm_summary)

    with open("outputs/report.md", "w", encoding="utf-8") as f:
        f.writelines(report_lines)

    print("Report generated at outputs/report.md")
