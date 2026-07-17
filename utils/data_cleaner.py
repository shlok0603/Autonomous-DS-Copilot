import pandas as pd


class DataCleaner:

    @staticmethod
    def clean(df: pd.DataFrame):

        cleaned_df = df.copy()

        steps = []

        # ---------------------------------
        # Remove Duplicate Rows
        # ---------------------------------

        duplicates = cleaned_df.duplicated().sum()

        if duplicates > 0:
            cleaned_df.drop_duplicates(inplace=True)
            steps.append(f"Removed {duplicates} duplicate rows.")

        # ---------------------------------
        # Remove Constant Columns
        # ---------------------------------

        constant_columns = [
            col
            for col in cleaned_df.columns
            if cleaned_df[col].nunique(dropna=False) <= 1
        ]

        if constant_columns:
            cleaned_df.drop(columns=constant_columns, inplace=True)
            steps.append(
                "Removed constant columns: "
                + ", ".join(constant_columns)
            )

        # ---------------------------------
        # Fill Missing Values
        # ---------------------------------

        numeric_columns = cleaned_df.select_dtypes(
            include="number"
        ).columns

        categorical_columns = cleaned_df.select_dtypes(
            include=["object", "category"]
        ).columns

        for col in numeric_columns:

            if cleaned_df[col].isnull().sum() > 0:

                cleaned_df[col].fillna(
                    cleaned_df[col].median(),
                    inplace=True
                )

                steps.append(
                    f"Filled missing values in '{col}' using median."
                )

        for col in categorical_columns:

            if cleaned_df[col].isnull().sum() > 0:

                mode = cleaned_df[col].mode()

                if not mode.empty:
                    cleaned_df[col].fillna(
                        mode.iloc[0],
                        inplace=True
                    )

                    steps.append(
                        f"Filled missing values in '{col}' using mode."
                    )

        return cleaned_df, steps