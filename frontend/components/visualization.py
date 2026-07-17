import streamlit as st

from utils.charts import ChartGenerator


def chart_card(title, fig):

    st.markdown(
        f"""
<div class="glass-card">

<div class="glass-title">

{title}

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displaylogo": False,
            "displayModeBar": False
        },
    )


def render(df):

    st.markdown(
        """
<div style="
background:linear-gradient(135deg,#4338CA,#7C3AED);
padding:35px;
border-radius:25px;
margin-bottom:30px;
">

<h1 style="color:white;margin:0;">
📊 Interactive Analytics Dashboard
</h1>

<p style="color:#E5E7EB;font-size:18px;margin-top:10px;">

Automatically generated visual insights from your dataset.

</p>

</div>
""",
        unsafe_allow_html=True,
    )

    numeric = ChartGenerator.get_numeric_columns(df)

    categorical = ChartGenerator.get_categorical_columns(df)

    # =====================================================
    # NUMERIC VISUALIZATIONS
    # =====================================================

    st.markdown("## 📈 Numerical Analysis")

    for column in numeric:

        c1, c2 = st.columns(2)

        with c1:

            chart_card(
                f"Histogram • {column}",
                ChartGenerator.histogram(df, column),
            )

        with c2:

            chart_card(
                f"Box Plot • {column}",
                ChartGenerator.boxplot(df, column),
            )

    # =====================================================
    # HEATMAP
    # =====================================================

    heatmap = ChartGenerator.correlation_heatmap(df)

    if heatmap is not None:

        st.markdown("## 🔥 Correlation Analysis")

        chart_card(
            "Correlation Heatmap",
            heatmap,
        )

    # =====================================================
    # CATEGORICAL
    # =====================================================

    st.markdown("## 📊 Categorical Analysis")

    for column in categorical:

        c1, c2 = st.columns(2)

        with c1:

            chart_card(
                f"Bar Chart • {column}",
                ChartGenerator.bar_chart(df, column),
            )

        with c2:

            chart_card(
                f"Pie Chart • {column}",
                ChartGenerator.pie_chart(df, column),
            )