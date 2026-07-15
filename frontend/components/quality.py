import streamlit as st

from utils.quality_analyzer import DataQualityAnalyzer


def render(df, profile):

    report = DataQualityAnalyzer.analyze(df)

    outliers = DataQualityAnalyzer.detect_outliers(df)

    score = DataQualityAnalyzer.quality_score(df)

    st.subheader("📊 Data Quality Report")

    st.metric("Quality Score", f"{score}/100")

    st.divider()

    st.write("### Missing Values (%)")

    missing_df = (
        report["missing_percentage"]
        .reset_index()
    )

    missing_df.columns = [
        "Column",
        "Missing (%)"
    ]

    st.dataframe(missing_df, width="stretch")

    st.write("### Outliers")

    st.dataframe(
        outliers.items(),
        width="stretch"
    )

    st.write("### Constant Columns")

    st.write(report["constant_columns"])

    st.write("### Numeric Columns")

    st.write(report["numeric_columns"])

    st.write("### Categorical Columns")

    st.write(report["categorical_columns"])

    st.write("### Duplicate Rows")

    st.write(report["duplicates"])