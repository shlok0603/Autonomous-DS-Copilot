import pandas as pd


class DatasetLoader:

    @staticmethod
    def load(file):

        filename = file.name.lower()

        if filename.endswith(".csv"):
            return pd.read_csv(file)

        elif filename.endswith(".xlsx"):
            return pd.read_excel(file)

        elif filename.endswith(".json"):
            return pd.read_json(file)

        else:
            raise ValueError("Unsupported file type.")