import streamlit as st

from frontend.ui.hero import render as hero
from utils.time_series import TimeSeriesAnalyzer


def render(df):

    hero(
        title="Time Series Forecasting",
        subtitle="Analyze trends and forecast future values from time-series data.",
        icon="📅"
    )

    date_columns = TimeSeriesAnalyzer.detect_datetime_columns(df)

    if len(date_columns) == 0:

        st.warning("No datetime columns detected.")

        return

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_columns) == 0:

        st.warning("No numeric columns available.")

        return

    st.markdown("## ⚙ Forecast Configuration")

    c1, c2 = st.columns(2)

    with c1:

        date_column = st.selectbox(
            "📅 Date Column",
            date_columns
        )

    with c2:

        value_column = st.selectbox(
            "📈 Value Column",
            numeric_columns
        )

    st.divider()

    st.markdown("## 📈 Trend Analysis")

    st.plotly_chart(

        TimeSeriesAnalyzer.trend(
            df,
            date_column,
            value_column
        ),

        use_container_width=True

    )

    st.divider()

    st.markdown("## 📊 Rolling Average")

    st.plotly_chart(

        TimeSeriesAnalyzer.rolling_average(
            df,
            date_column,
            value_column
        ),

        use_container_width=True

    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Records", len(df))

    with c2:
        st.metric("Date Column", date_column)

    with c3:
        st.metric("Forecast Variable", value_column)

    st.info(
        """
### 💡 Forecast Insights

• Trend chart shows historical movement.

• Rolling average smooths short-term fluctuations.

• Useful for identifying long-term patterns.

• Ideal for sales, stock, weather and business forecasting.
"""
    )