from utils.prompt_loader import PromptLoader
from utils.quality_analyzer import DataQualityAnalyzer
from utils.domain_detector import DomainDetector
from utils.problem_detector import ProblemDetector


class InsightGenerator:

    @staticmethod
    def build_prompt(df):

        # -----------------------------
        # Dataset Statistics
        # -----------------------------
        report = DataQualityAnalyzer.analyze(df)

        outlier_report = DataQualityAnalyzer.detect_outliers(df)

        domain = DomainDetector.detect(df)
        problem_type, target = ProblemDetector.detect(df)

        outliers = "\n".join(
            [
                f"{col}: {count}"
                for col, count in outlier_report.items()
            ]
        )

        missing = "\n".join(
            [
                f"{col}: {round(val, 2)}%"
                for col, val in report["missing_percentage"].items()
            ]
        )

        # -----------------------------
        # Dataset Preview
        # -----------------------------
        preview = df.head(5).to_markdown(index=False)

        # -----------------------------
        # Column Information
        # -----------------------------
        dtypes = "\n".join(
            [
                f"{col}: {dtype}"
                for col, dtype in df.dtypes.items()
            ]
        )

        # -----------------------------
        # Statistical Summary
        # -----------------------------
        summary = df.describe(include="all").to_markdown()

        # -----------------------------
        # Base Prompt
        # -----------------------------
        template = PromptLoader.load(
            "dataset_analysis.txt"
        )

        prompt = template.format(

            rows=report["rows"],

            columns=report["columns"],

            duplicates=report["duplicates"],

            missing=missing,

            numeric=", ".join(report["numeric_columns"]),

            categorical=", ".join(report["categorical_columns"]),

            outliers=outliers

        )

        # -----------------------------
        # Enterprise Prompt
        # -----------------------------
        prompt += f"""

======================================================
ADDITIONAL DATASET CONTEXT
======================================================

Dataset Domain:
{domain}

Problem Type:
{problem_type}

Predicted Target Column:
{target}

======================================================
COLUMN DATA TYPES
======================================================

{dtypes}

======================================================
FIRST 5 ROWS
======================================================

{preview}

======================================================
STATISTICAL SUMMARY
======================================================

{summary}

======================================================
YOUR TASK
======================================================

Act as a Principal Data Scientist.

Generate a complete enterprise analysis.

Your report MUST include:

1. Executive Summary

2. Dataset Overview

3. Data Quality Assessment

4. Statistical Findings

5. Business Insights

6. Dataset Risks

7. Target Column Analysis

8. Problem Type Explanation

9. Recommended Machine Learning Models

10. Feature Engineering Suggestions

11. Recommended Evaluation Metrics

12. Data Cleaning Strategy

13. Deployment Recommendation

14. Business Recommendations

15. Final Conclusion

Whenever recommending models,
explain WHY they are suitable.

If the problem is Regression,
recommend regression algorithms.

If Classification,
recommend classification algorithms.

If clustering is more appropriate,
explain why."""

        return prompt