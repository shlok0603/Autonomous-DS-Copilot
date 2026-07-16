import pandas as pd
import plotly.express as px


class ChartGenerator:
    """
    Generates Plotly charts for visualization
    and PDF report generation.
    """

    @staticmethod
    def get_numeric_columns(df):
        """Return all numeric columns."""
        return df.select_dtypes(include="number").columns.tolist()

    @staticmethod
    def get_categorical_columns(df):
        """Return all categorical columns."""
        return df.select_dtypes(include=["object", "category"]).columns.tolist()

    @staticmethod
    def histogram(df, column):
        """Generate histogram."""
        fig = px.histogram(
            df,
            x=column,
            title=f"Histogram of {column}"
        )
        return fig

    @staticmethod
    def boxplot(df, column):
        """Generate box plot."""
        fig = px.box(
            df,
            y=column,
            title=f"Box Plot of {column}"
        )
        return fig

    @staticmethod
    def bar_chart(df, column):
        """Generate bar chart."""

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
        """Generate pie chart."""

        fig = px.pie(
            df,
            names=column,
            title=f"{column} Distribution"
        )

        return fig

    @staticmethod
    def correlation_heatmap(df):
        """Generate correlation heatmap."""

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

    @staticmethod
    def generate_all(df):
        """
        Generate all important charts for the PDF report.

        Returns:
            list of tuples
            [
                ("Histogram - Age", figure),
                ("Box Plot - Age", figure),
                ("Correlation Heatmap", figure),
                ("Bar Chart - Department", figure),
                ("Pie Chart - Department", figure)
            ]
        """

        charts = []

        numeric = ChartGenerator.get_numeric_columns(df)
        categorical = ChartGenerator.get_categorical_columns(df)

        # -------------------------------
        # Numeric Charts
        # -------------------------------
        if numeric:

            first_numeric = numeric[0]

            charts.append(
                (
                    f"Histogram - {first_numeric}",
                    ChartGenerator.histogram(df, first_numeric)
                )
            )

            charts.append(
                (
                    f"Box Plot - {first_numeric}",
                    ChartGenerator.boxplot(df, first_numeric)
                )
            )

        # -------------------------------
        # Correlation Heatmap
        # -------------------------------
        heatmap = ChartGenerator.correlation_heatmap(df)

        if heatmap is not None:
            charts.append(
                (
                    "Correlation Heatmap",
                    heatmap
                )
            )

        # -------------------------------
        # Categorical Charts
        # -------------------------------
        if categorical:

            first_category = categorical[0]

            charts.append(
                (
                    f"Bar Chart - {first_category}",
                    ChartGenerator.bar_chart(df, first_category)
                )
            )

            charts.append(
                (
                    f"Pie Chart - {first_category}",
                    ChartGenerator.pie_chart(df, first_category)
                )
            )

        return charts