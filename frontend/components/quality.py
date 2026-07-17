import streamlit as st

from frontend.ui.hero import render as hero
from utils.quality_analyzer import DataQualityAnalyzer


def render(df, profile):

    hero(
        title="Data Quality Dashboard",
        subtitle="Analyze missing values, outliers and overall dataset quality.",
        icon="📊"
    )

    report = DataQualityAnalyzer.analyze(df)

    outliers = DataQualityAnalyzer.detect_outliers(df)

    score = DataQualityAnalyzer.quality_score(df)

    st.markdown("## 📈 Quality Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Quality Score",
            f"{score}/100"
        )

    with c2:

        st.metric(
            "Rows",
            profile["rows"]
        )

    with c3:

        st.metric(
            "Columns",
            profile["columns"]
        )

    with c4:

        st.metric(
            "Duplicates",
            report["duplicates"]
        )

    st.divider()

    st.markdown("## 🚨 Missing Values")

    missing_df = (

        report["missing_percentage"]

        .reset_index()

    )

    missing_df.columns = [

        "Column",

        "Missing (%)"

    ]

    st.dataframe(

        missing_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    st.markdown("## 📌 Outlier Analysis")

    outlier_df = outliers.items()

    st.dataframe(

        outlier_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("### 🧾 Constant Columns")

        st.write(report["constant_columns"])

    with c2:

        st.markdown("### 🔢 Numeric Columns")

        st.write(report["numeric_columns"])

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("### 🏷 Categorical Columns")

        st.write(report["categorical_columns"])

    with c2:

        st.markdown("### 🔁 Duplicate Rows")

        st.write(report["duplicates"])

    st.divider()

    st.progress(score / 100)

    st.success(
        f"Dataset Quality Score : {score}/100"
    )