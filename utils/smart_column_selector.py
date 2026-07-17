import re


class SmartColumnSelector:

    # Words that indicate identifier columns
    ID_KEYWORDS = [
        "id",
        "uuid",
        "index",
        "serial",
        "roll",
        "emp_id",
        "employee_id",
        "customer_id",
        "order_id",
        "invoice_id",
        "transaction_id"
    ]

    # Words that indicate name columns
    NAME_KEYWORDS = [
        "name",
        "firstname",
        "lastname",
        "full_name",
        "employee_name",
        "customer_name"
    ]

    NUMERIC_PRIORITY = [
        "salary",
        "income",
        "price",
        "amount",
        "sales",
        "revenue",
        "profit",
        "cost",
        "age",
        "experience",
        "score",
        "rating",
        "marks",
        "height",
        "weight",
        "bmi",
        "glucose",
        "balance"
    ]

    CATEGORICAL_PRIORITY = [
        "department",
        "gender",
        "city",
        "country",
        "state",
        "region",
        "category",
        "segment",
        "product",
        "education",
        "occupation",
        "designation"
    ]

    @staticmethod
    def normalize(name):

        return (
            str(name)
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

    @classmethod
    def is_identifier(cls, column):

        col = cls.normalize(column)

        for keyword in cls.ID_KEYWORDS:

            if keyword == col:
                return True

            if col.endswith("_id"):
                return True

            if col.startswith("id_"):
                return True

        return False

    @classmethod
    def is_name(cls, column):

        col = cls.normalize(column)

        for keyword in cls.NAME_KEYWORDS:

            if keyword in col:
                return True

        return False

    @classmethod
    def top_numeric(cls, df, limit=3):

        numeric = list(df.select_dtypes(include="number").columns)

        # Remove ID columns
        numeric = [
            col for col in numeric
            if not cls.is_identifier(col)
        ]

        selected = []

        # Priority columns first
        for keyword in cls.NUMERIC_PRIORITY:

            for col in numeric:

                if keyword in cls.normalize(col):

                    if col not in selected:
                        selected.append(col)

        # Remaining numeric columns
        for col in numeric:

            if col not in selected:
                selected.append(col)

        return selected[:limit]

    @classmethod
    def top_categorical(cls, df, limit=2):

        categorical = list(
            df.select_dtypes(include=["object", "category"]).columns
        )

        # Remove names
        categorical = [
            col for col in categorical
            if not cls.is_name(col)
        ]

        selected = []

        # Priority first
        for keyword in cls.CATEGORICAL_PRIORITY:

            for col in categorical:

                if keyword in cls.normalize(col):

                    if col not in selected:
                        selected.append(col)

        # Remaining
        for col in categorical:

            if col not in selected:

                # Skip high-cardinality columns
                if df[col].nunique() > len(df) * 0.7:
                    continue

                selected.append(col)

        return selected[:limit]