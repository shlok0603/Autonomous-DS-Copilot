import pandas as pd


class DataProfiler:

    @staticmethod
    def profile(df: pd.DataFrame):

        rows, cols = df.shape

        missing = df.isnull().sum()

        duplicates = df.duplicated().sum()

        memory = df.memory_usage(deep=True).sum()

        if memory < 1024 * 1024:
            memory = f"{round(memory / 1024, 2)} KB"
        else:
            memory = f"{round(memory / (1024 * 1024), 2)} MB"

        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "duplicates": int(df.duplicated().sum()),
            "missing": df.isnull().sum().astype(int),
            "dtypes": df.dtypes.astype(str),
            "memory": memory,
            "summary": df.describe(include="all")
        }

