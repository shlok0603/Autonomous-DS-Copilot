class MLRecommender:

    @staticmethod
    def recommend(problem):

        if problem == "Regression":

            return {

                "models": [

                    "XGBoost Regressor",

                    "CatBoost Regressor",

                    "LightGBM",

                    "Random Forest Regressor",

                    "Linear Regression"

                ],

                "metrics": [

                    "MAE",

                    "MSE",

                    "RMSE",

                    "R² Score"

                ]

            }

        elif problem == "Classification":

            return {

                "models": [

                    "XGBoost Classifier",

                    "CatBoost",

                    "LightGBM",

                    "Random Forest",

                    "Logistic Regression",

                    "SVM"

                ],

                "metrics": [

                    "Accuracy",

                    "Precision",

                    "Recall",

                    "F1 Score",

                    "ROC-AUC"

                ]

            }

        elif problem == "Clustering":

            return {

                "models": [

                    "K-Means",

                    "DBSCAN",

                    "Hierarchical Clustering"

                ],

                "metrics": [

                    "Silhouette Score",

                    "Davies-Bouldin Index"

                ]

            }

        return {

            "models": ["Unknown"],

            "metrics": []

        }