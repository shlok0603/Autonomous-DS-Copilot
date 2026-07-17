class DomainDetector:

    DOMAINS = {

        "Human Resources": [
            "employee",
            "salary",
            "department",
            "experience",
            "performance",
            "designation",
            "age",
            "joining"
        ],

        "Sales": [
            "sales",
            "revenue",
            "profit",
            "customer",
            "product",
            "quantity",
            "discount",
            "region"
        ],

        "Healthcare": [
            "patient",
            "diagnosis",
            "disease",
            "hospital",
            "medicine",
            "blood",
            "heart",
            "glucose"
        ],

        "Finance": [
            "loan",
            "credit",
            "bank",
            "account",
            "income",
            "expense",
            "balance"
        ],

        "Education": [
            "student",
            "marks",
            "grade",
            "attendance",
            "subject",
            "semester"
        ]
    }

    @staticmethod
    def detect(df):

        columns = [
            c.lower()
            for c in df.columns
        ]

        scores = {}

        for domain, keywords in DomainDetector.DOMAINS.items():

            score = 0

            for keyword in keywords:

                score += sum(
                    keyword in col
                    for col in columns
                )

            scores[domain] = score

        best = max(
            scores,
            key=scores.get
        )

        if scores[best] == 0:
            return "General Dataset"

        return best