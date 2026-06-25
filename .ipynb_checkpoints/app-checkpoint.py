import streamlit as st
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

st.set_page_config(
    page_title="Tabby & Jack's Analytics",
    page_icon="images/logo.png",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #F6F1E5;
    color: #2F372D;
}

.block-container {
    padding-top: 2rem;
    max-width: 1050px;
}

.hero {
    background-color: #1D5A3E;
    padding: 34px 28px;
    border-radius: 26px;
    margin-bottom: 28px;
    box-shadow: 0px 8px 22px rgba(29,90,62,.18);
}

.hero h1 {
    text-align: center;
    color: #FFF9EF;
    font-size: 42px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    text-align: center;
    color: rgba(255,249,239,0.88);
    font-size: 17px;
    margin-top: 12px;
}

.report-card {
    background-color: #FFF9EF;
    border: 1px solid #D7C8A4;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0px 4px 14px rgba(47,55,45,0.07);
}

.report-card h3 {
    color: #1D5A3E;
    margin-top: 0;
}

.report-card p {
    color: #5C7A58;
}
</style>
""", unsafe_allow_html=True)

logo_base64 = image_to_base64("images/logo.png")

st.markdown(f"""
<div class="hero">
    <img src="data:image/png;base64,{logo_base64}"
         width="150"
         style="display:block; margin:0 auto 18px auto;">
    <h1>Tabby & Jack's Report Tools</h1>
    <p>Select a report tool from the sidebar to get started.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="report-card">
        <h3>📦 Major Vendor Order</h3>
        <p>Generate recommended purchase quantities from a 4-week Lightspeed sales report.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Major Vendor Order"):
        st.switch_page("pages/MVO.py")

with col2:
    st.markdown("""
    <div class="report-card">
        <h3>🏷️ MAP Price Update</h3>
        <p>Match UPCs between sheets and apply vendor pricing updates.</p>
    </div>
    """, unsafe_allow_html=True)