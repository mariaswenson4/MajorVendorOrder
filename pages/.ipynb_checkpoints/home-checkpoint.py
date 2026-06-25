import streamlit as st
import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


st.markdown("""
<style>
.stApp {
    background-color: #F6F1E5;
    color: #2F372D;
}

.block-container {
    max-width: 1120px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background-color: #FFF9EF;
    border-right: 1px solid #D7C8A4;
}

.hero {
    background: linear-gradient(rgba(29,90,62,.95), rgba(21,68,47,.98));
    border-radius: 28px;
    padding: 48px 36px;
    margin-bottom: 34px;
    box-shadow: 0px 10px 28px rgba(29,90,62,.22);
}

.hero-logo {
    display: block;
    margin: 0 auto 20px auto;
}

.hero h1 {
    color: #FFF9EF;
    text-align: center;
    font-size: 52px;
    font-weight: 850;
    margin: 0;
}

.hero p {
    color: rgba(255,249,239,.88);
    text-align: center;
    font-size: 20px;
    margin-top: 14px;
}

.section-kicker {
    color: #C97822;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-weight: 800;
    margin-bottom: 4px;
}

.section-title {
    color: #1D5A3E;
    font-size: 34px;
    font-weight: 850;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #5C7A58;
    font-size: 17px;
    margin-bottom: 24px;
}

.app-card {
    background-color: #FFFDF8;
    border: 1px solid #D7C8A4;
    border-radius: 24px;
    min-height: 300px;
    overflow: hidden;
    box-shadow: 0px 7px 22px rgba(47,55,45,.08);
    transition: all .18s ease;
}

.app-card:hover {
    transform: translateY(-3px);
    border-color: #C97822;
    box-shadow: 0px 12px 28px rgba(47,55,45,.13);
}

.app-card-body {
    padding: 36px 34px 28px 34px;
    text-align: center;
    min-height: 220px;
}

.app-icon-wrap {
    background-color: #F6F1E5;
    width: 108px;
    height: 108px;
    border-radius: 28px;
    margin: 0 auto 24px auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.app-card h3 {
    color: #1D5A3E;
    font-size: 29px;
    font-weight: 850;
    margin: 0 0 14px 0;
}

.app-card p {
    color: #4F5F4A;
    font-size: 17px;
    line-height: 1.55;
    margin: 0;
}

button[kind="primary"] {
    background-color: #FFF7EA !important;
    color: #C97822 !important;
    border: 1px solid #D7C8A4 !important;
    border-radius: 0 0 24px 24px !important;
    height: 64px !important;
    font-size: 17px !important;
    font-weight: 800 !important;
    box-shadow: none !important;
}

button[kind="primary"]:hover {
    background-color: #C97822 !important;
    color: white !important;
    border-color: #C97822 !important;
}

div[data-testid="stButton"] {
    margin-top: -1px;
}

.disabled-footer {
    background-color: #F4EFE3;
    border: 1px solid #D7C8A4;
    border-top: none;
    border-radius: 0 0 24px 24px;
    height: 64px;
    color: #7B776E;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
}

.info-banner {
    background-color: #FFF9EF;
    border: 1px solid #D7C8A4;
    border-radius: 18px;
    padding: 22px 26px;
    margin-top: 30px;
    display: flex;
    align-items: center;
    gap: 18px;
    box-shadow: 0px 4px 14px rgba(47,55,45,.06);
}

.info-icon {
    background-color: #1D5A3E;
    color: white;
    min-width: 42px;
    height: 42px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
}

.info-title {
    color: #1D5A3E;
    font-size: 18px;
    font-weight: 800;
}

.info-text {
    color: #5C7A58;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)


logo = image_to_base64("images/logo.png")

st.markdown(f"""
<div class="hero">
    <img class="hero-logo" src="data:image/png;base64,{logo}" width="150">
    <h1>Tabby & Jack's Analytics</h1>
    <p>Internal reporting and automation tools</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-kicker">Reports</div>
<div class="section-title">Reports</div>
<div class="section-subtitle">Select an application below to get started.</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="app-card">
        <div class="app-card-body">
            <div class="app-icon-wrap">
                <div style="font-size:58px;">📦</div>
            </div>
            <h3>Major Vendor Order</h3>
            <p>Upload a 4-week Lightspeed report and generate vendor ordering quantities.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Application  →", type="primary", use_container_width=True, key="open_mvo"):
        st.switch_page("pages/MVO.py")


with col2:
    st.markdown("""
    <div class="app-card">
        <div class="app-card-body">
            <div class="app-icon-wrap">
                <div style="font-size:58px;">📦</div>
            </div>
            <h3>Small Vendor Order</h3>
            <p>Upload sales data and generate smaller vendor ordering quantities.</p>
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