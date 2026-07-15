import pandas as pd
import plotly.express as px


class ChartGenerator:

    @staticmethod
    def get_numeric_columns(df):

        return df.select_dtypes(include="number").columns.tolist()

    @staticmethod
    def get_categorical_columns(df):

        return df.select_dtypes(include=["object", "category"]).columns.tolist()

    @staticmethod
    def histogram(df, column):

        fig = px.histogram(
            df,
            x=column,
            title=f"Histogram of {column}"
        )

        return fig

    @staticmethod
    def boxplot(df, column):

        fig = px.box(
            df,
            y=column,
            title=f"Box Plot of {column}"
        )

        return fig

    @staticmethod
    def bar_chart(df, column):

        counts = (
            df[column]
            .value_counts()
            .reset_index()
        )

        counts.columns = [column, "Count"]

        fig = px.bar(
            counts,
            x=column,
            y="Count",
            title=f"{column} Distribution"
        )

        return fig

    @staticmethod
    def pie_chart(df, column):

        fig = px.pie(
            df,
            names=column,
            title=f"{column} Distribution"
        )

        return fig

    @staticmethod
    def correlation_heatmap(df):

        numeric_df = df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            return None

        corr = numeric_df.corr(numeric_only=True)

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Correlation Heatmap"
        )

        return fig