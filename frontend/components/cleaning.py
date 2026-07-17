import streamlit as st

from frontend.ui.hero import render as hero
from utils.data_cleaner import DataCleaner


def render(df):

    hero(
        title="One-Click Data Cleaning",
        subtitle="Automatically clean your dataset using enterprise data preparation.",
        icon="🧹"
    )

    st.markdown("## ✨ Cleaning Operations")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("✅ Remove Duplicate Rows")

    with c2:
        st.success("✅ Fill Missing Values")

    with c3:
        st.success("✅ Remove Constant Columns")

    st.divider()

    if st.button(
        "🚀 Clean Dataset",
        use_container_width=True
    ):

        progress = st.progress(0)

        status = st.empty()

        progress.progress(20)
        status.info("Removing duplicates...")

        cleaned_df, steps = DataCleaner.clean(df)

        progress.progress(70)
        status.info("Optimizing dataset...")

        st.session_state.cleaned_df = cleaned_df

        progress.progress(100)

        status.success("Dataset Cleaned Successfully")

        st.divider()

        st.markdown("## 📋 Cleaning Summary")

        for step in steps:

            st.success(step)

        st.divider()

        st.markdown("## 👀 Preview")

        st.dataframe(
            cleaned_df.head(10),
            use_container_width=True,
            height=350
        )

        csv = cleaned_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇ Download Cleaned Dataset",
            csv,
            "cleaned_dataset.csv",
            "text/csv",
            use_container_width=True
        )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Original Rows",
                len(df)
            )

        with c2:
            st.metric(
                "Cleaned Rows",
                len(cleaned_df)
            )