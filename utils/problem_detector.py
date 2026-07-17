import pandas as pd


class ProblemDetector:

    REGRESSION_KEYWORDS = [
        "salary",
        "price",
        "revenue",
        "sales",
        "income",
        "profit",
        "score",
        "amount",
        "cost"
    ]

    CLASSIFICATION_KEYWORDS = [
        "target",
        "label",
        "class",
        "diagnosis",
        "disease",
        "status",
        "approved",
        "survived",
        "churn",
        "default",
        "performance",
        "attrition"
    ]

    @staticmethod
    def detect(df: pd.DataFrame):

        columns = list(df.columns)
        lower_columns = [c.lower() for c in columns]

        # ---------------------------------
        # STEP 1 : Keyword Detection
        # ---------------------------------

        for keyword in ProblemDetector.CLASSIFICATION_KEYWORDS:

            for original, lower in zip(columns, lower_columns):

                if keyword in lower:

                    return "Classification", original

        for keyword in ProblemDetector.REGRESSION_KEYWORDS:

            for original, lower in zip(columns, lower_columns):

                if keyword in lower:

                    return "Regression", original

        # ---------------------------------
        # STEP 2 : Intelligent Detection
        # ---------------------------------

        for column in reversed(columns):

            series = df[column]

            unique = series.nunique(dropna=True)

            if pd.api.types.is_numeric_dtype(series):

                # Small number of unique values
                # e.g. 0/1/2 or 1-5 ratings
                if unique <= 10:

                    return "Classification", column

                # Continuous numeric values
                return "Regression", column

            else:

                # Categorical target
                if unique <= 20:

                    return "Classification", column

        # ---------------------------------
        # STEP 3 : No obvious target
        # ---------------------------------

        return "Clustering", None