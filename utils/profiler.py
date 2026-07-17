import pandas as pd


class DataProfiler:

    @staticmethod
    def profile(df: pd.DataFrame):

        memory = df.memory_usage(deep=True).sum()

        if memory < 1024 * 1024:
            memory = f"{round(memory / 1024, 2)} KB"
        else:
            memory = f"{round(memory / (1024 * 1024), 2)} MB"

        numeric_columns = df.select_dtypes(include="number").columns.tolist()

        categorical_columns = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        missing_percentage = (
            (df.isnull().sum() / len(df)) * 100
        ).round(2)

        # -----------------------------
        # Dataset Health Score
        # -----------------------------

        missing_percentage_total = (
                                           df.isnull().sum().sum()
                                           / df.size
                                   ) * 100

        duplicate_percentage = (
                                       df.duplicated().sum()
                                       / len(df)
                               ) * 100

        health_score = (
                100
                - (missing_percentage_total * 0.7)
                - (duplicate_percentage * 0.3)
        )

        health_score = max(
            0,
            min(
                round(health_score),
                100
            )
        )

        return {

            # Dataset Information
            "rows": len(df),
            "columns": len(df.columns),
            "memory": memory,

            # Data Quality
            "duplicates": int(df.duplicated().sum()),
            "missing": df.isnull().sum().astype(int),
            "missing_percentage": missing_percentage,

            # Column Information
            "numeric_columns": numeric_columns,
            "categorical_columns": categorical_columns,
            "numeric_count": len(numeric_columns),
            "categorical_count": len(categorical_columns),

            # Data Types
            "dtypes": df.dtypes.astype(str),

            "health_score": health_score,

            # Statistical Summary
            "summary": df.describe(include="all")
        }