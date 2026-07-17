import pandas as pd


class ProblemDetector:

    CLASSIFICATION_KEYWORDS = [
        "survived",
        "target",
        "label",
        "class",
        "diagnosis",
        "status",
        "churn",
        "default",
        "approved",
        "attrition",
        "species",
        "type",
        "outcome",
        "result",
        "y"
    ]

    REGRESSION_KEYWORDS = [
        "price",
        "salary",
        "sales",
        "revenue",
        "income",
        "profit",
        "amount",
        "score",
        "cost"
    ]

    @staticmethod
    def detect(df):

        columns = list(df.columns)

        # ------------------------
        # Keyword detection
        # ------------------------

        for col in columns:

            lower = col.lower()

            for key in ProblemDetector.CLASSIFICATION_KEYWORDS:

                if key == lower or key in lower:

                    return "Classification", col

            for key in ProblemDetector.REGRESSION_KEYWORDS:

                if key == lower or key in lower:

                    return "Regression", col

        # ------------------------
        # Last column heuristic
        # ------------------------

        target = columns[-1]

        series = df[target]

        unique = series.nunique(dropna=True)

        if pd.api.types.is_numeric_dtype(series):

            if unique <= 20:
                return "Classification", target

            return "Regression", target

        return "Classification", target