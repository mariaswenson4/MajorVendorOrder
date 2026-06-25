import streamlit as st
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

logo = image_to_base64("images/logo.png")
ordering = image_to_base64("images/ordering.png")

st.markdown("""
<style>
.stApp {
    background-color: #F6F1E5;
    color: #2F372D;
}

.block-container {
    max-width: 1160px;
    padding-top: 1.25rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background-color: #FFF9EF;
    border-right: 1px solid #D7C8A4;
}

.app-banner {
    background: linear-gradient(135deg, #1D5A3E, #0F3324);
    border-radius: 22px;
    padding: 30px 38px;
    margin-bottom: 34px;
    min-height: 210px;
    display: flex;
    align-items: center;
    gap: 30px;
    box-shadow: 0px 12px 30px rgba(29,90,62,.22);
}

.banner-logo {
    background: rgba(255,249,239,.10);
    border: 1px solid rgba(255,249,239,.18);
    border-radius: 22px;
    padding: 18px;
}

.banner-title h1 {
    color: #FFF9EF;
    font-size: 44px;
    font-weight: 850;
    margin: 0;
}

.banner-title p {
    color: rgba(255,249,239,.88);
    font-size: 18px;
    margin: 10px 0 0 0;
}

.section-kicker {
    color: #C97822;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-weight: 850;
    margin-bottom: 4px;
}

.section-title {
    color: #1D5A3E;
    font-size: 34px;
    font-weight: 850;
    margin-bottom: 3px;
}

.section-subtitle {
    color: #5C7A58;
    font-size: 16px;
    margin-bottom: 24px;
}

.app-card {
    background-color: #FFFDF8;
    border: 1px solid #D7C8A4;
    border-radius: 24px 24px 0 0;
    min-height: 230px;
    box-shadow: 0px 7px 22px rgba(47,55,45,.08);
}

.app-card-body {
    padding: 30px;
    text-align: left;
}

.app-card-top {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 22px;
}

.app-icon-wrap {
    background-color: #F6F1E5;
    width: 76px;
    height: 76px;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.app-card h3 {
    color: #1D5A3E;
    font-size: 25px;
    font-weight: 850;
    margin: 0;
}

.status-pill {
    display: inline-block;
    margin-top: 8px;
    background: #E9F1E7;
    color: #1D5A3E;
    border-radius: 999px;
    padding: 5px 10px;
    font-size: 12px;
    font-weight: 800;
}

.status-pill-muted {
    background: #EFE8D7;
    color: #7B776E;
}

.app-card p {
    color: #4F5F4A;
    font-size: 15.5px;
    line-height: 1.5;
    margin: 0;
}

div[data-testid="stButton"] {
    margin-top: -1px;
}

.stButton button {
    width: 100%;
    height: 58px;
    border-radius: 0 0 24px 24px;
    border: 1px solid #D7C8A4;
    border-top: none;
    background-color: #FFF7EA;
    color: #C97822;
    font-size: 16px;
    font-weight: 850;
}

.stButton button:hover {
    background-color: #C97822;
    color: white;
    border-color: #C97822;
}

.disabled-footer {
    background-color: #F4EFE3;
    border: 1px solid #D7C8A4;
    border-top: none;
    border-radius: 0 0 24px 24px;
    height: 58px;
    color: #7B776E;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 850;
}

.info-banner {
    background-color: #FFF9EF;
    border: 1px solid #D7C8A4;
    border-radius: 20px;
    padding: 20px 24px;
    margin-top: 30px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0px 4px 14px rgba(47,55,45,.06);
}

.info-icon {
    background-color: #1D5A3E;
    color: white;
    min-width: 40px;
    height: 40px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 850;
}

.info-title {
    color: #1D5A3E;
    font-size: 17px;
    font-weight: 850;
}

.info-text {
    color: #5C7A58;
    font-size: 14.5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="app-banner">
<div class="banner-logo">
<img src="data:image/png;base64,{logo}" width="105">
</div>
<div class="banner-title">
<h1>Tabby & Jack's Analytics</h1>
<p>Frequently used reporting tools for Tabby & Jack's</p>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-kicker">Reports</div>
<div class="section-title">Application Launcher</div>
<div class="section-subtitle">Open a report tool below to get started.</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(f"""
<div class="app-card">
<div class="app-card-body">
<div class="app-card-top">
<div class="app-icon-wrap">
<img src="data:image/png;base64,{ordering}" width="55">
</div>
<div>
<h3>Major Vendor Order</h3>
<div class="status-pill">Available</div>
</div>
</div>
<p>Upload a 4-week Lightspeed report and generate a major vendor report.</p>
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Open Major Vendor Order  →", use_container_width=True, key="open_mvo"):
        st.switch_page("pages/MVO.py")

with col2:
    st.markdown(f"""
<div class="app-card">
<div class="app-card-body">
<div class="app-card-top">
<div class="app-icon-wrap">
<img src="data:image/png;base64,{ordering}" width="55">
</div>
<div>
<h3>Small Vendor Order</h3>
<div class="status-pill status-pill-muted">Coming Soon</div>
</div>
</div>
<p>Upload a 90-day Lightspeed report and generate a small vendor report.</p>
</div>
</div>
<div class="disabled-footer">Coming Soon  →</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-banner">
<div class="info-icon">i</div>
<div>
<div class="info-title">More tools and reports are on the way.</div>
<div class="info-text">This dashboard will grow as more internal reporting tools are added.</div>
</div>
</div>
""", unsafe_allow_html=True)