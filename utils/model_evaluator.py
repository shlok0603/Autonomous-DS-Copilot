import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


class ModelEvaluator:

    @staticmethod
    def evaluate_classification(model, X_test, y_test):

        prediction = model.predict(X_test)

        return {

            "accuracy": accuracy_score(
                y_test,
                prediction
            ),

            "precision": precision_score(
                y_test,
                prediction,
                average="weighted",
                zero_division=0
            ),

            "recall": recall_score(
                y_test,
                prediction,
                average="weighted",
                zero_division=0
            ),

            "f1": f1_score(
                y_test,
                prediction,
                average="weighted",
                zero_division=0
            ),

            "confusion_matrix": confusion_matrix(
                y_test,
                prediction
            ),

            "classification_report":
                classification_report(
                    y_test,
                    prediction,
                    zero_division=0
                ),

            "prediction": prediction
        }

    @staticmethod
    def evaluate_regression(model, X_test, y_test):

        prediction = model.predict(X_test)

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                prediction
            )
        )

        return {

            "r2": r2_score(
                y_test,
                prediction
            ),

            "mae": mean_absolute_error(
                y_test,
                prediction
            ),

            "rmse": rmse,

            "prediction": prediction
        }