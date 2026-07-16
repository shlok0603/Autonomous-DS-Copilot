import streamlit as st

from utils.charts import ChartGenerator


def render(df):

    st.subheader("Automatic Visualizations")

    numeric = ChartGenerator.get_numeric_columns(df)

    categorical = ChartGenerator.get_categorical_columns(df)

    ########################################

    st.header("Numerical Columns")

    ########################################

    for column in numeric:

        st.plotly_chart(
            ChartGenerator.histogram(df, column),
            width="stretch"
        )

        st.plotly_chart(
            ChartGenerator.boxplot(df, column),
            width="stretch"
        )

    ########################################

    heatmap = ChartGenerator.correlation_heatmap(df)

    if heatmap:

        st.plotly_chart(
            heatmap,
            width="stretch"
        )

    ########################################

    st.header("Categorical Columns")

    ########################################

    for column in categorical:

        st.plotly_chart(
            ChartGenerator.bar_chart(df, column),
            width="stretch"
        )

        st.plotly_chart(
            ChartGenerator.pie_chart(df, column),
            width="stretch"
        )