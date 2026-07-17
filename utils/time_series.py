import pandas as pd
import plotly.express as px


class TimeSeriesAnalyzer:

    @staticmethod
    def detect_datetime_columns(df):

        datetime_columns = []

        for column in df.columns:

            try:

                converted = pd.to_datetime(
                    df[column],
                    errors="raise"
                )

                if converted.notna().sum() > 0:

                    datetime_columns.append(column)

            except Exception:

                continue

        return datetime_columns

    @staticmethod
    def trend(df, date_column, value_column):

        data = df.copy()

        data[date_column] = pd.to_datetime(
            data[date_column]
        )

        data = data.sort_values(date_column)

        fig = px.line(
            data,
            x=date_column,
            y=value_column,
            title=f"{value_column} Over Time"
        )

        fig.update_layout(
            template="plotly_white",
            title_x=0.5
        )

        return fig

    @staticmethod
    def rolling_average(df, date_column, value_column):

        data = df.copy()

        data[date_column] = pd.to_datetime(
            data[date_column]
        )

        data = data.sort_values(date_column)

        data["Rolling Mean"] = (
            data[value_column]
            .rolling(7)
            .mean()
        )

        fig = px.line(
            data,
            x=date_column,
            y="Rolling Mean",
            title="7-Day Rolling Average"
        )

        fig.update_layout(
            template="plotly_white",
            title_x=0.5
        )

        return fig