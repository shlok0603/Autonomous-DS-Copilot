import streamlit as st

from utils.loader import DatasetLoader
from utils.profiler import DataProfiler

st.set_page_config(
    page_title="Autonomous Data Science Co-Pilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Data Science Co-Pilot")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx", "json"]
)

if uploaded_file:

    df = DatasetLoader.load(uploaded_file)

    profile = DataProfiler.profile(df)

    st.success("Dataset Loaded Successfully")

    st.subheader("Preview")

    st.dataframe(df.head(), width="stretch")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", profile["rows"])

    col2.metric("Columns", profile["columns"])

    col3.metric("Missing Values", int(profile["missing"].sum()))

    col4.metric("Duplicate Rows", profile["duplicates"])

    st.subheader("Column Types")

    dtypes_df = profile["dtypes"].reset_index()
    dtypes_df.columns = ["Column", "Data Type"]

    st.dataframe(dtypes_df, width="stretch")

    st.subheader("Missing Values")

    missing_df = profile["missing"].reset_index()
    missing_df.columns = ["Column", "Missing Values"]

    st.dataframe(missing_df, width="stretch")

    st.subheader("Summary Statistics")

    st.dataframe(profile["summary"], width="stretch")

    st.metric("Memory Usage", profile["memory"])