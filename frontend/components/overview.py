import streamlit as st


def render(df, profile):

    st.subheader("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Missing", int(profile["missing"].sum()))
    col4.metric("Duplicates", profile["duplicates"])

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df.head(10), width="stretch")

    st.divider()

    st.metric("Memory Usage", profile["memory"])