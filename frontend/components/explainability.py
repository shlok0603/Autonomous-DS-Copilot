import streamlit as st

from frontend.ui.hero import render as hero

from utils.problem_detector import ProblemDetector
from utils.automl import AutoML
from utils.explainability import Explainability


def feature_card(title, value):

    st.markdown(
        f"""
<div style="
background:#1E293B;
padding:18px;
border-radius:18px;
border:1px solid rgba(255,255,255,.08);
text-align:center;
">

<div style="
font-size:15px;
color:#94A3B8;
">

{title}

</div>

<div style="
font-size:26px;
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
        title="Explainable AI",
        subtitle="Understand how your machine learning model makes predictions.",
        icon="🧠"
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
            "Target Column",
            target if target else "Not Detected"
        )

    if target is None:

        st.warning(
            "Unable to detect target column."
        )

        return

    st.divider()

    if st.button(
        "🚀 Generate Explainability",
        use_container_width=True
    ):

        progress = st.progress(0)

        status = st.empty()

        progress.progress(20)

        status.info(
            "Training best model..."
        )

        if problem == "Classification":

            result = AutoML.classification(
                df,
                target
            )

        else:

            result = AutoML.regression(
                df,
                target
            )

        progress.progress(60)

        model = result["best_model"]

        X_test = result["X_test"]

        feature_names = result["feature_names"]

        progress.progress(100)

        status.success(
            "Explainability Generated"
        )

        st.divider()

        st.markdown("## 🏆 Best Model")

        st.success(
            result["best_model_name"]
        )

        st.divider()

        importance = Explainability.feature_importance(
            model,
            feature_names
        )

        if importance is not None:

            st.markdown("## 📊 Feature Importance")

            c1, c2, c3 = st.columns(3)

            with c1:

                feature_card(
                    "Total Features",
                    len(importance)
                )

            with c2:

                feature_card(
                    "Top Feature",
                    importance.iloc[0]["Feature"]
                )

            with c3:

                feature_card(
                    "Importance",
                    round(
                        importance.iloc[0]["Importance"],
                        4
                    )
                )

            st.divider()

            st.dataframe(

                importance,

                use_container_width=True,

                hide_index=True

            )

        if hasattr(
            model,
            "feature_importances_"
        ):

            st.divider()

            st.markdown(
                "## 🔥 SHAP Summary"
            )

            with st.spinner(
                "Generating SHAP visualization..."
            ):

                fig = Explainability.shap_summary(
                    model,
                    X_test
                )

            st.pyplot(
                fig,
                use_container_width=True
            )

        st.divider()

        st.info(
            """
### 💡 Business Interpretation

- Features at the top contribute the most to predictions.

- SHAP values explain individual feature impact.

- Use this analysis to improve trust and transparency.

- Helps identify important business drivers.
"""
        )

        st.caption(
            "🧠 Explainable AI • Autonomous Data Science Co-Pilot"
        )