from utils.prompt_loader import PromptLoader
from utils.quality_analyzer import DataQualityAnalyzer


class InsightGenerator:

    @staticmethod
    def build_prompt(df):

        report = DataQualityAnalyzer.analyze(df)

        outliers = DataQualityAnalyzer.detect_outliers(df)

        template = PromptLoader.load(
            "dataset_analysis.txt"
        )

        prompt = template.format(

            rows=report["rows"],

            columns=report["columns"],

            duplicates=report["duplicates"],

            missing=report["missing_percentage"].to_string(),

            numeric=", ".join(report["numeric_columns"]),

            categorical=", ".join(report["categorical_columns"]),

            outliers=outliers
        )

        return prompt