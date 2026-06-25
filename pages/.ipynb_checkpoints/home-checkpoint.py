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

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #FFF9EF;
    border-right: 1px solid #D7C8A4;
}

section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {
    color: #1D5A3E;
}

.hero {
    background:
        linear-gradient(rgba(29,90,62,.94), rgba(21,68,47,.98));
    border-radius: 26px;
    padding: 48px 32px;
    margin-bottom: 34px;
    box-shadow: 0px 10px 28px rgba(29,90,62,.22);
    border: 1px solid rgba(255,249,239,.18);
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
    letter-spacing: -.5px;
}

.hero p {
    color: rgba(255,249,239,.88);
    text-align: center;
    font-size: 20px;
    margin: 14px 0 0 0;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 46px;
    margin-top: 34px;
}

.hero-stat {
    text-align: center;
    color: #FFF9EF;
    min-width: 120px;
}

.hero-stat-number {
    font-size: 34px;
    font-weight: 800;
}

.hero-stat-label {
    font-size: 14px;
    opacity: .85;
    margin-top: 2px;
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
    min-height: 340px;
    overflow: hidden;
    box-shadow: 0px 7px 22px rgba(47,55,45,.08);
    transition: all .18s ease;
    margin-bottom: 12px;
}

.app-card:hover {
    transform: translateY(-3px);
    border-color: #C97822;
    box-shadow: 0px 12px 28px rgba(47,55,45,.13);
}

.app-card-body {
    padding: 36px 34px 28px 34px;
    text-align: center;
    min-height: 235px;
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

.app-card-footer {
    border-top: 1px solid #E6D9BC;
    background-color: #FFF7EA;
    padding: 20px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.footer-text {
    color: #C97822;
    font-size: 17px;
    font-weight: 700;
}

.arrow-circle {
    background-color: #E97800;
    color: white;
    width: 52px;
    height: 52px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
}

.arrow-circle-disabled {
    background-color: #DDD6C8;
    color: #6F6A5F;
}

.click-card {
    text-decoration: none;
}

.info-banner {
    background-color: #FFF9EF;
    border: 1px solid #D7C8A4;
    border-radius: 18px;
    padding: 22px 26px;
    margin-top: 26px;
    display: flex;
    align-items: center;
    gap: 18px;
    box-shadow: 0px 4px 14px rgba(47,55,45,.06);
}

.info-icon {
    background-color: #1D5A3E;
    color: white;
    width: 42px;
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
box_icon = image_to_base64("images/logo.png")

st.markdown(f"""
<div class="hero">
    <img class="hero-logo" src="data:image/png;base64,{logo}" width="150">
    <h1>Tabby & Jack's Analytics</h1>
    <p>Internal reporting and automation tools</p>

    <div class="hero-stats">
        <div class="hero-stat">
            <div class="hero-stat-number">2</div>
            <div class="hero-stat-label">Report Tools</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-number">1</div>
            <div class="hero-stat-label">Automation</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-number">1</div>
            <div class="hero-stat-label">Utility</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-kicker">Reports</div>
<div class="section-title">Reports</div>
<div class="section-subtitle">Select a tool below to get started.</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <a class="click-card" href="/MVO" target="_self">
        <div class="app-card">
            <div class="app-card-body">
                <div class="app-icon-wrap">
                    <div style="font-size:58px;">📦</div>
                </div>
                <h3>Major Vendor Order</h3>
                <p>Upload a 4-week Lightspeed report and generate vendor ordering quantities.</p>
            </div>
            <div class="app-card-footer">
                <div class="footer-text">Open Application</div>
                <div class="arrow-circle">→</div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="app-card">
        <div class="app-card-body">
            <div class="app-icon-wrap">
                <div style="font-size:58px;">🏷️</div>
            </div>
            <h3>Small Vendor Order</h3>
            <p>Upload sales data and generate smaller vendor ordering quantities.</p>
        </div>
        <div class="app-card-footer">
            <div class="footer-text" style="color:#7B776E;">Coming Soon</div>
            <div class="arrow-circle arrow-circle-disabled">→</div>
        </div>
    </div>
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