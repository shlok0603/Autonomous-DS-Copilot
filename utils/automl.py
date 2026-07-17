import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from sklearn.tree import DecisionTreeClassifier

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression
)

from utils.model_evaluator import ModelEvaluator


class AutoML:

    @staticmethod
    def prepare(df, target):

        df = df.copy()

        encoders = {}

        for col in df.select_dtypes(include=["object", "category"]):

            encoder = LabelEncoder()

            df[col] = encoder.fit_transform(
                df[col].astype(str)
            )

            encoders[col] = encoder

        X = df.drop(columns=[target])

        y = df[target]

        return train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

    @staticmethod
    def classification(df, target):

        X_train, X_test, y_train, y_test = AutoML.prepare(
            df,
            target
        )

        models = {

            "Random Forest":
                RandomForestClassifier(random_state=42),

            "Decision Tree":
                DecisionTreeClassifier(random_state=42),

            "Logistic Regression":
                LogisticRegression(max_iter=1000)

        }

        leaderboard = {}

        trained_models = {}

        evaluations = {}

        for name, model in models.items():

            model.fit(X_train, y_train)

            trained_models[name] = model

            result = ModelEvaluator.evaluate_classification(
                model,
                X_test,
                y_test
            )

            evaluations[name] = result

            leaderboard[name] = result["accuracy"]

        best_name = max(
            leaderboard,
            key=leaderboard.get
        )

        return {

            "leaderboard": leaderboard,

            "best_model_name": best_name,

            "best_model": trained_models[best_name],

            "evaluation": evaluations[best_name],

            "X_test": X_test,

            "y_test": y_test,

            "feature_names": list(X_train.columns)

        }

    @staticmethod
    def regression(df, target):

        X_train, X_test, y_train, y_test = AutoML.prepare(
            df,
            target
        )

        models = {

            "Random Forest":
                RandomForestRegressor(random_state=42),

            "Linear Regression":
                LinearRegression()

        }

        leaderboard = {}

        trained_models = {}

        evaluations = {}

        for name, model in models.items():

            model.fit(X_train, y_train)

            trained_models[name] = model

            result = ModelEvaluator.evaluate_regression(
                model,
                X_test,
                y_test
            )

            evaluations[name] = result

            leaderboard[name] = result["r2"]

        best_name = max(
            leaderboard,
            key=leaderboard.get
        )

        return {

            "leaderboard": leaderboard,

            "best_model_name": best_name,

            "best_model": trained_models[best_name],

            "evaluation": evaluations[best_name],

            "X_test": X_test,

            "y_test": y_test,

            "feature_names": list(X_train.columns)

        }