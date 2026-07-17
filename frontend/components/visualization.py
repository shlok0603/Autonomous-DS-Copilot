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
background:linear-gradient(135deg,#4338CA,#6D28D9,#7C3AED);
padding:38px;
border-radius:24px;
margin-bottom:30px;
box-shadow:0 20px 45px rgba(99,102,241,.30);
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
display:inline-block;
padding:8px 16px;
background:rgba(255,255,255,.12);
border-radius:999px;
color:white;
font-size:13px;
margin-bottom:16px;
">

📊 Enterprise Analytics

</div>

<h1 style="margin:0;color:white;font-size:40px;">

Interactive Analytics Dashboard

</h1>

<p style="
margin-top:14px;
font-size:18px;
color:#E9D5FF;
">

Automatically generated visual insights from your dataset.

</p>

</div>

<div style="
font-size:70px;
opacity:.18;
">

📊

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    numeric = ChartGenerator.get_numeric_columns(df)
    categorical = ChartGenerator.get_categorical_columns(df)

    # =====================================================
    # DATASET SUMMARY
    # =====================================================

    st.markdown("## 📌 Dataset Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Numeric Columns", len(numeric))
    c2.metric("Categorical Columns", len(categorical))
    c3.metric("Total Features", len(df.columns))

    st.divider()

    # =====================================================
    # NUMERICAL
    # =====================================================

    st.markdown("## 📈 Numerical Analysis")

    for column in numeric:

        st.markdown(f"### 🔹 {column}")

        left, right = st.columns(2)

        with left:
            chart_card(
                "Histogram",
                ChartGenerator.histogram(df, column),
            )

        with right:
            chart_card(
                "Box Plot",
                ChartGenerator.boxplot(df, column),
            )

        st.divider()

    # =====================================================
    # CORRELATION
    # =====================================================

    heatmap = ChartGenerator.correlation_heatmap(df)

    if heatmap is not None:

        st.markdown("## 🔥 Correlation Heatmap")

        chart_card(
            "Feature Correlation",
            heatmap,
        )

        st.divider()

    # =====================================================
    # CATEGORICAL
    # =====================================================

    st.markdown("## 📊 Categorical Analysis")

    for column in categorical:

        st.markdown(f"### 🔹 {column}")

        left, right = st.columns(2)

        with left:

            chart_card(
                "Bar Chart",
                ChartGenerator.bar_chart(df, column),
            )

        with right:

            chart_card(
                "Pie Chart",
                ChartGenerator.pie_chart(df, column),
            )

        st.divider()