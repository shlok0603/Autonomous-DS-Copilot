import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
)

from sklearn.tree import DecisionTreeClassifier

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression,
)

from utils.model_evaluator import ModelEvaluator


class AutoML:

    @staticmethod
    def prepare(df, target, classification=True):

        df = df.copy()

        # -----------------------------
        # Separate X and y
        # -----------------------------
        X = df.drop(columns=[target])
        y = df[target]

        # -----------------------------
        # Numeric columns
        # -----------------------------
        numeric_cols = X.select_dtypes(include=["number"]).columns

        if len(numeric_cols) > 0:
            num_imputer = SimpleImputer(strategy="median")
            X[numeric_cols] = num_imputer.fit_transform(
                X[numeric_cols]
            )

        # -----------------------------
        # Categorical columns
        # -----------------------------
        categorical_cols = X.select_dtypes(
            include=["object", "category", "bool"]
        ).columns

        if len(categorical_cols) > 0:

            cat_imputer = SimpleImputer(
                strategy="most_frequent"
            )

            X[categorical_cols] = cat_imputer.fit_transform(
                X[categorical_cols]
            )

            X = pd.get_dummies(
                X,
                columns=categorical_cols,
                drop_first=True,
            )

        # -----------------------------
        # Target preprocessing
        # -----------------------------
        if classification:

            if y.dtype == "object" or str(y.dtype) == "category":

                target_encoder = LabelEncoder()

                y = target_encoder.fit_transform(
                    y.astype(str)
                )

            elif y.isnull().sum() > 0:

                y = y.fillna(
                    y.mode()[0]
                )

        else:

            if y.isnull().sum() > 0:

                y = y.fillna(
                    y.median()
                )

        # -----------------------------
        # Train Test Split
        # -----------------------------
        return train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
        )

    @staticmethod
    def classification(df, target):

        X_train, X_test, y_train, y_test = AutoML.prepare(
            df,
            target,
            classification=True,
        )

        models = {

            "Random Forest":
                RandomForestClassifier(random_state=42),

            "Decision Tree":
                DecisionTreeClassifier(random_state=42),

            "Logistic Regression":
                LogisticRegression(
                    max_iter=1000
                ),

        }

        leaderboard = {}

        trained_models = {}

        evaluations = {}

        for name, model in models.items():
            for name, model in models.items():
                print("=" * 50)
                print("Training:", name)
                print(X_train.isna().sum())
                print("=" * 50)
                print("TOTAL NaN =", X_train.isna().sum().sum())
                print("=" * 50)

                model.fit(
                    X_train,
                    y_train,
                )

                trained_models[name] = model

            model.fit(
                X_train,
                y_train,
            )

            trained_models[name] = model

            result = ModelEvaluator.evaluate_classification(
                model,
                X_test,
                y_test,
            )

            evaluations[name] = result

            leaderboard[name] = result["accuracy"]

        best_name = max(
            leaderboard,
            key=leaderboard.get,
        )

        return {

            "leaderboard": leaderboard,

            "best_model_name": best_name,

            "best_model": trained_models[best_name],

            "evaluation": evaluations[best_name],

            "X_test": X_test,

            "y_test": y_test,

            "feature_names": list(
                X_train.columns
            ),

        }

    @staticmethod
    def regression(df, target):

        X_train, X_test, y_train, y_test = AutoML.prepare(
            df,
            target,
            classification=False,
        )

        models = {

            "Random Forest":
                RandomForestRegressor(
                    random_state=42
                ),

            "Linear Regression":
                LinearRegression(),

        }

        leaderboard = {}

        trained_models = {}

        evaluations = {}

        for name, model in models.items():

            model.fit(
                X_train,
                y_train,
            )

            trained_models[name] = model

            result = ModelEvaluator.evaluate_regression(
                model,
                X_test,
                y_test,
            )

            evaluations[name] = result

            leaderboard[name] = result["r2"]

        best_name = max(
            leaderboard,
            key=leaderboard.get,
        )

        return {

            "leaderboard": leaderboard,

            "best_model_name": best_name,

            "best_model": trained_models[best_name],

            "evaluation": evaluations[best_name],

            "X_test": X_test,

            "y_test": y_test,

            "feature_names": list(
                X_train.columns
            ),

        }