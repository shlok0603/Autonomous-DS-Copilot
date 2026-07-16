from utils.prompt_loader import PromptLoader
from utils.quality_analyzer import DataQualityAnalyzer


class InsightGenerator:

    @staticmethod
    def build_prompt(df):

        report = DataQualityAnalyzer.analyze(df)

        outlier_report = DataQualityAnalyzer.detect_outliers(df)

        outliers = "\n".join(
            [
                f"{col}: {count}"
                for col, count in outlier_report.items()
            ]
        )

        template = PromptLoader.load(
            "dataset_analysis.txt"
        )

        prompt = template.format(

            rows=report["rows"],

            columns=report["columns"],

            duplicates=report["duplicates"],

            missing="\n".join(
                [
                    f"{col}: {round(val, 2)}%"
                    for col, val in report["missing_percentage"].items()
                ]
            ),

            numeric=", ".join(report["numeric_columns"]),

            categorical=", ".join(report["categorical_columns"]),

            outliers=outliers
        )

        return prompt