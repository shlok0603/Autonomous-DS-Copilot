import shap
import matplotlib.pyplot as plt
import pandas as pd


class Explainability:

    @staticmethod
    def feature_importance(model, feature_names):

        if hasattr(model, "feature_importances_"):

            importance = pd.DataFrame({

                "Feature": feature_names,

                "Importance": model.feature_importances_

            })

            importance = importance.sort_values(
                "Importance",
                ascending=False
            )

            return importance

        return None

    @staticmethod
    def shap_summary(model, X_test):

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(X_test)

        fig = plt.figure()

        shap.summary_plot(
            shap_values,
            X_test,
            show=False
        )

        return fig