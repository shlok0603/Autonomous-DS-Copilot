import pandas as pd
import plotly.express as px

from utils.smart_column_selector import SmartColumnSelector


class ChartGenerator:
    """
    Generates Plotly charts for visualization
    and PDF report generation.
    """

    # =====================================================
    # Common Layout
    # =====================================================

    @staticmethod
    def apply_theme(fig):

        fig.update_layout(

            template="plotly_dark",

            paper_bgcolor="#1E293B",

            plot_bgcolor="#1E293B",

            font=dict(
                color="white",
                size=14
            ),

            title=dict(
                x=0.5,
                xanchor="center",
                font=dict(
                    size=20
                )
            ),

            margin=dict(
                l=30,
                r=30,
                t=70,
                b=30
            ),

            height=500,

            legend=dict(
                bgcolor="rgba(0,0,0,0)"
            )
        )

        return fig

    # =====================================================
    # Column Helpers
    # =====================================================

    @staticmethod
    def get_numeric_columns(df):
        return df.select_dtypes(include="number").columns.tolist()

    @staticmethod
    def get_categorical_columns(df):
        return df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

    # =====================================================
    # Histogram
    # =====================================================

    @staticmethod
    def histogram(df, column):

        fig = px.histogram(
            df,
            x=column,
            title=f"Histogram • {column}"
        )

        fig.update_traces(
            marker_line_width=1
        )

        return ChartGenerator.apply_theme(fig)

    # =====================================================
    # Box Plot
    # =====================================================

    @staticmethod
    def boxplot(df, column):

        fig = px.box(
            df,
            y=column,
            title=f"Box Plot • {column}"
        )

        return ChartGenerator.apply_theme(fig)

    # =====================================================
    # Bar Chart
    # =====================================================

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

        return ChartGenerator.apply_theme(fig)

    # =====================================================
    # Pie Chart
    # =====================================================

    @staticmethod
    def pie_chart(df, column):

        fig = px.pie(
            df,
            names=column,
            title=f"{column} Distribution"
        )

        fig.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        return ChartGenerator.apply_theme(fig)

    # =====================================================
    # Scatter Plot
    # =====================================================

    @staticmethod
    def scatter_plot(df, x_col, y_col):

        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            title=f"{x_col} vs {y_col}"
        )

        fig.update_traces(
            marker=dict(size=9)
        )

        return ChartGenerator.apply_theme(fig)

    # =====================================================
    # Correlation Heatmap
    # =====================================================

    @staticmethod
    def correlation_heatmap(df):

        numeric_df = df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            return None

        corr = numeric_df.corr(numeric_only=True)

        fig = px.imshow(

            corr,

            text_auto=".2f",

            aspect="auto",

            title="Correlation Heatmap",

            color_continuous_scale="Viridis"

        )

        fig.update_layout(
            height=600
        )

        return ChartGenerator.apply_theme(fig)

    # =====================================================
    # Generate All Charts
    # =====================================================

    @staticmethod
    def generate_all(df):

        charts = []

        numeric_columns = SmartColumnSelector.top_numeric(df)

        categorical_columns = SmartColumnSelector.top_categorical(df)

        # ---------------- Numeric ----------------

        for column in numeric_columns:

            charts.append(
                (
                    f"Histogram - {column}",
                    ChartGenerator.histogram(df, column)
                )
            )

            charts.append(
                (
                    f"Box Plot - {column}",
                    ChartGenerator.boxplot(df, column)
                )
            )

        # ---------------- Heatmap ----------------

        heatmap = ChartGenerator.correlation_heatmap(df)

        if heatmap is not None:

            charts.append(
                (
                    "Correlation Heatmap",
                    heatmap
                )
            )

        # ---------------- Scatter ----------------

        if len(numeric_columns) >= 2:

            charts.append(
                (
                    f"{numeric_columns[0]} vs {numeric_columns[1]}",
                    ChartGenerator.scatter_plot(
                        df,
                        numeric_columns[0],
                        numeric_columns[1]
                    )
                )
            )

        # ---------------- Categorical ----------------

        for column in categorical_columns:

            charts.append(
                (
                    f"Bar Chart - {column}",
                    ChartGenerator.bar_chart(df, column)
                )
            )

            charts.append(
                (
                    f"Pie Chart - {column}",
                    ChartGenerator.pie_chart(df, column)
                )
            )

        return charts