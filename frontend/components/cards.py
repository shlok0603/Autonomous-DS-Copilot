import streamlit as st


def metric_card(title, value, icon, color, subtitle=""):

    html = f"""
<style>
.dashboard-card {{
    position: relative;
    background: linear-gradient(145deg,#1E293B,#111827);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 22px;
    padding: 24px;
    min-height: 220px;
    padding-bottom: 45px;
    position: relative;
    overflow: hidden;
    transition: all .35s ease;
    box-shadow: 0 18px 35px rgba(0,0,0,.35);
}}

.dashboard-card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 25px 45px rgba(99,102,241,.35);
    border: 1px solid {color};
}}

.dashboard-glow {{
    position: absolute;
    width: 160px;
    height: 160px;
    background: {color};
    filter: blur(80px);
    opacity: .15;
    right: -70px;
    top: -70px;
}}

.dashboard-icon {{
    width:60px;
    height:60px;
    border-radius:18px;
    background:linear-gradient(135deg,{color},#8B5CF6);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:30px;
    margin-bottom:18px;
}}

.dashboard-title {{
    color:#CBD5E1;
    font-size:15px;
}}

.dashboard-value {{
    color:white;
    font-size:34px;
    font-weight:800;
    margin-top:6px;
}}

.dashboard-subtitle {{
    color:#22C55E;
    font-size:14px;
    margin-top:18px;
    position:absolute;
    bottom:22px;
    left:24px;
}}
</style>

<div class="dashboard-card">
<div class="dashboard-glow"></div>

<div class="dashboard-icon">{icon}</div>

<div class="dashboard-title">{title}</div>

<div class="dashboard-value">{value}</div>

<div class="dashboard-subtitle">{subtitle}</div>

</div>
"""

    st.markdown(html, unsafe_allow_html=True)