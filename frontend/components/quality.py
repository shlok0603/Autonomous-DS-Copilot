import streamlit as st


def render(profile):

    st.subheader("📊 Data Quality")

    st.write("### Column Types")

    dtypes_df = profile["dtypes"].reset_index()
    dtypes_df.columns = ["Column", "Data Type"]

    st.dataframe(dtypes_df, width="stretch")

    st.write("### Missing Values")

    missing_df = profile["missing"].reset_index()
    missing_df.columns = ["Column", "Missing Values"]

    st.dataframe(missing_df, width="stretch")

    st.write("### Summary Statistics")

    st.dataframe(profile["summary"], width="stretch")