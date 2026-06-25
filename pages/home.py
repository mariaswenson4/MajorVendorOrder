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
    max-width: 980px;
    padding-top: 1.25rem;
    padding-bottom: 3rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFF9EF;
    border-right: 1px solid #D7C8A4;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #1D5A3E, #15442F);
    border-radius: 26px;
    padding: 34px 28px;
    margin-bottom: 34px;
    box-shadow: 0px 12px 30px rgba(29,90,62,.22);
}

.hero-logo {
    display: block;
    margin: 0 auto 14px auto;
}

.hero h1 {
    color: #FFF9EF;
    text-align: center;
    font-size: 42px;
    font-weight: 850;
    margin: 0;
}

.hero p {
    color: rgba(255,249,239,.88);
    text-align: center;
    font-size: 17px;
    margin: 10px 0 0 0;
}

/* Section heading */
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
    font-size: 31px;
    font-weight: 850;
    margin-bottom: 3px;
}

.section-subtitle {
    color: #5C7A58;
    font-size: 16px;
    margin-bottom: 22px;
}

/* Cards */
.app-card {
    background-color: #FFFDF8;
    border: 1px solid #D7C8A4;
    border-radius: 24px 24px 0 0;
    min-height: 250px;
    box-shadow: 0px 7px 22px rgba(47,55,45,.08);
    transition: all .18s ease;
}

.app-card:hover {
    transform: translateY(-3px);
    border-color: #C97822;
    box-shadow: 0px 12px 28px rgba(47,55,45,.13);
}

.app-card-body {
    padding: 32px 30px 26px 30px;
    text-align: center;
}

.app-icon-wrap {
    background-color: #F6F1E5;
    width: 92px;
    height: 92px;
    border-radius: 24px;
    margin: 0 auto 22px auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.app-card h3 {
    color: #1D5A3E;
    font-size: 25px;
    font-weight: 850;
    margin: 0 0 12px 0;
}

.app-card p {
    color: #4F5F4A;
    font-size: 15.5px;
    line-height: 1.5;
    margin: 0;
}

/* Button footer */
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
    font-weight: 800;
}

.stButton button:hover {
    background-color: #C97822;
    color: white;
    border-color: #C97822;
}

/* Disabled footer */
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
    font-weight: 800;
}

/* Info banner */
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
    font-weight: 800;
}

.info-title {
    color: #1D5A3E;
    font-size: 17px;
    font-weight: 800;
}

.info-text {
    color: #5C7A58;
    font-size: 14.5px;
}
</style>
""", unsafe_allow_html=True)

logo = image_to_base64("images/logo.png")

st.markdown(f"""
<div class="hero">
    <img class="hero-logo" src="data:image/png;base64,{logo}" width="125">
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
                <div style="font-size:50px;">📦</div>
            </div>
            <h3>Major Vendor Order</h3>
            <p>Upload a 4-week Lightspeed report and generate vendor ordering quantities.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Application  →", use_container_width=True, key="open_mvo"):
        st.switch_page("pages/MVO.py")

with col2:
    st.markdown("""
    <div class="app-card">
        <div class="app-card-body">
            <div class="app-icon-wrap">
                <div style="font-size:50px;">📦</div>
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