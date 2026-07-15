import pandas as pd


class DataQualityAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):

        report = {}

        # Dataset information
        report["rows"] = len(df)
        report["columns"] = len(df.columns)

        # Missing values
        missing = (
            df.isnull().sum() / len(df) * 100
        ).round(2)

        report["missing_percentage"] = missing

        # Duplicate rows
        report["duplicates"] = int(df.duplicated().sum())

        # Numeric & categorical columns
        numeric = df.select_dtypes(include="number").columns.tolist()
        categorical = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        report["numeric_columns"] = numeric
        report["categorical_columns"] = categorical

        # Constant columns
        report["constant_columns"] = [
            col for col in df.columns
            if df[col].nunique(dropna=False) <= 1
        ]

        return report

    @staticmethod
    def detect_outliers(df):

        outliers = {}

        numeric = df.select_dtypes(include="number")

        for column in numeric.columns:

            q1 = numeric[column].quantile(0.25)
            q3 = numeric[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            count = (
                (numeric[column] < lower)
                |
                (numeric[column] > upper)
            ).sum()

            outliers[column] = int(count)

        return outliers

    @staticmethod
    def quality_score(df):

        score = 100

        # Missing values penalty
        missing_percent = (
            df.isnull().sum().sum()
            /
            (df.shape[0] * df.shape[1])
        ) * 100

        score -= missing_percent

        # Duplicate penalty
        duplicate_percent = (
            df.duplicated().sum()
            /
            len(df)
        ) * 100

        score -= duplicate_percent

        return max(0, round(score, 2))