import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay

from frontend.ui.hero import render as hero

from utils.problem_detector import ProblemDetector
from utils.automl import AutoML


def metric_card(title, value):

    st.markdown(
        f"""
<div style="
background:#1E293B;
padding:20px;
border-radius:18px;
text-align:center;
border:1px solid rgba(255,255,255,.08);
">

<div style="
font-size:15px;
color:#94A3B8;
">

{title}

</div>

<div style="
font-size:28px;
font-weight:800;
color:white;
margin-top:10px;
">

{value}

</div>

</div>
""",
        unsafe_allow_html=True
    )


def render(df):

    hero(
        title="Model Evaluation",
        subtitle="Train models and evaluate their performance using enterprise metrics.",
        icon="📈"
    )

    problem, target = ProblemDetector.detect(df)

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Problem Type",
            problem
        )

    with c2:
        st.metric(
            "Target",
            target if target else "Not Detected"
        )

    if target is None:

        st.warning(
            "Unable to detect target column."
        )

        return

    st.divider()

    if st.button(
        "🚀 Train & Evaluate",
        use_container_width=True
    ):

        progress = st.progress(0)

        status = st.empty()

        progress.progress(15)

        status.info("Preparing dataset...")

        if problem == "Classification":

            progress.progress(55)

            status.info("Training classification models...")

            result = AutoML.classification(
                df,
                target
            )

        elif problem == "Regression":

            progress.progress(55)

            status.info("Training regression models...")

            result = AutoML.regression(
                df,
                target
            )

        else:

            st.warning(
                "Unsupported problem type."
            )

            return

        progress.progress(100)

        status.success("Evaluation Completed")

        leaderboard = pd.DataFrame(
            {
                "Model": result["leaderboard"].keys(),
                "Score": result["leaderboard"].values()
            }
        ).sort_values(
            by="Score",
            ascending=False
        )

        st.markdown("## 🏆 Model Leaderboard")

        st.dataframe(
            leaderboard,
            use_container_width=True
        )

        st.success(
            f"🥇 Best Model : {result['best_model_name']}"
        )

        evaluation = result["evaluation"]

        st.divider()

        if problem == "Classification":

            st.markdown("## 📊 Performance Metrics")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                metric_card(
                    "Accuracy",
                    round(
                        evaluation["accuracy"],
                        4
                    )
                )

            with c2:
                metric_card(
                    "Precision",
                    round(
                        evaluation["precision"],
                        4
                    )
                )

            with c3:
                metric_card(
                    "Recall",
                    round(
                        evaluation["recall"],
                        4
                    )
                )

            with c4:
                metric_card(
                    "F1 Score",
                    round(
                        evaluation["f1"],
                        4
                    )
                )

            st.divider()

            st.markdown("## 🎯 Confusion Matrix")

            fig, ax = plt.subplots(
                figsize=(6,6)
            )

            ConfusionMatrixDisplay(
                evaluation["confusion_matrix"]
            ).plot(
                ax=ax,
                colorbar=False
            )

            st.pyplot(
                fig,
                use_container_width=True
            )

            st.divider()

            st.markdown("## 📄 Classification Report")

            st.code(
                evaluation[
                    "classification_report"
                ],
                language="text"
            )

        else:

            st.markdown("## 📊 Regression Metrics")

            c1, c2, c3 = st.columns(3)

            with c1:
                metric_card(
                    "R² Score",
                    round(
                        evaluation["r2"],
                        4
                    )
                )

            with c2:
                metric_card(
                    "MAE",
                    round(
                        evaluation["mae"],
                        4
                    )
                )

            with c3:
                metric_card(
                    "RMSE",
                    round(
                        evaluation["rmse"],
                        4
                    )
                )

        st.divider()

        st.caption(
            "📈 Enterprise Evaluation Dashboard • Autonomous Data Science Co-Pilot"
        )