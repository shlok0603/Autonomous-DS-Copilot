import streamlit as st
import pandas as pd

from frontend.ui.hero import render as hero

from utils.problem_detector import ProblemDetector
from utils.automl import AutoML


def leaderboard_card(rank, model, score, metric):

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    medal = medals.get(rank, "🏅")

    st.markdown(
        f"""
<div style="
background:#1E293B;
border:1px solid rgba(255,255,255,.08);
border-radius:18px;
padding:22px;
margin-bottom:15px;
box-shadow:0 10px 25px rgba(0,0,0,.30);
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="font-size:30px;">
{medal}
</div>

<div style="
font-size:20px;
font-weight:700;
color:white;
margin-top:10px;
">

{model}

</div>

<div style="
color:#94A3B8;
margin-top:6px;
">

{metric}

</div>

</div>

<div style="
font-size:30px;
font-weight:800;
color:#22C55E;
">

{round(score,4)}

</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


def render(df):

    hero(
        title="Enterprise AutoML",
        subtitle="Automatically train, compare and recommend the best machine learning model.",
        icon="🤖"
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
            "Unable to detect a target column."
        )

        return

    st.divider()

    if st.button(
        "🚀 Start AutoML Training",
        use_container_width=True
    ):

        progress = st.progress(0)

        status = st.empty()

        status.info("Preparing dataset...")

        progress.progress(20)

        if problem == "Classification":

            status.info("Training classification models...")

            result = AutoML.classification(
                df,
                target
            )

            metric = "Accuracy"

        elif problem == "Regression":

            status.info("Training regression models...")

            result = AutoML.regression(
                df,
                target
            )

            metric = "R² Score"

        else:

            st.warning(
                "Only Classification and Regression are supported."
            )

            return

        progress.progress(80)

        status.success(
            "Selecting best model..."
        )

        progress.progress(100)

        st.success(
            "✅ AutoML Completed Successfully"
        )

        st.divider()

        leaderboard = pd.DataFrame(

            {

                "Model": result["leaderboard"].keys(),

                "Score": result["leaderboard"].values()

            }

        ).sort_values(

            by="Score",

            ascending=False

        )

        best_model = leaderboard.iloc[0]

        st.markdown("## 🏆 Best Model")

        st.markdown(
            f"""
<div style="
background:linear-gradient(135deg,#4338CA,#7C3AED);
padding:35px;
border-radius:24px;
margin-bottom:25px;
">

<h2 style="
margin:0;
color:white;
">

🥇 {best_model['Model']}

</h2>

<p style="
font-size:20px;
color:white;
margin-top:15px;
">

{metric}: <b>{round(best_model['Score'],4)}</b>

</p>

</div>
""",
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Models Trained",
                len(leaderboard)
            )

        with c2:
            st.metric(
                "Best Score",
                round(best_model["Score"],4)
            )

        with c3:
            st.metric(
                "Metric",
                metric
            )

        st.divider()

        st.markdown("## 📊 Leaderboard")

        rank = 1

        for _, row in leaderboard.iterrows():

            leaderboard_card(

                rank,

                row["Model"],

                row["Score"],

                metric

            )

            rank += 1

        st.divider()

        st.markdown("## 📋 Detailed Scores")

        st.dataframe(

            leaderboard,

            use_container_width=True

        )