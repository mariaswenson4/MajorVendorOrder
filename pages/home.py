import streamlit as st
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

st.set_page_config(layout="wide")

st.markdown("""
<style>

.stApp {
    background-color: #F6F1E5;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.hero {
    background:#1D5A3E;
    border-radius:24px;
    padding:40px;
    margin-bottom:35px;
}

.hero h1{
    color:white;
    text-align:center;
    margin-bottom:10px;
}

.hero p{
    color:#E9E8E1;
    text-align:center;
    font-size:18px;
}

.tool-card{
    background:white;
    border-radius:18px;
    border:1px solid #D7C8A4;
    padding:28px;
    text-align:center;
    transition:.2s;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
    margin-bottom:20px;
}

.tool-card:hover{
    border:1px solid #C97822;
    box-shadow:0 8px 20px rgba(0,0,0,.12);
}

.tool-title{
    color:#1D5A3E;
    font-size:24px;
    font-weight:700;
    margin-top:10px;
}

.tool-desc{
    color:#5C7A58;
    margin-top:10px;
    margin-bottom:18px;
}

.stButton button{
    width:100%;
    background:#C97822;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:700;
    padding:.65rem;
}

.stButton button:hover{
    background:#B4671C;
    color:white;
}

</style>
""", unsafe_allow_html=True)

logo = image_to_base64("images/logo.png")

st.markdown(f"""
<div class="hero">

<img src="data:image/png;base64,{logo}"
width="170"
style="display:block;margin:auto;">

<h1>Tabby & Jack's Analytics</h1>

<p>
Internal reporting and automation tools
</p>

</div>
""", unsafe_allow_html=True)

st.subheader("Reports")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="tool-card">

    <div style="font-size:55px;">📦</div>

    <div class="tool-title">
    Major Vendor Order
    </div>

    <div class="tool-desc">
    Upload a 4-week Lightspeed report and generate vendor ordering quantities.
    </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Major Vendor Order"):
        st.switch_page("pages/mvo.py")

with col2:

    st.markdown("""
    <div class="tool-card">

    <div style="font-size:55px;">🏷️</div>

    <div class="tool-title">
    MAP Price Update
    </div>

    <div class="tool-desc">
    Match UPCs and automatically update MAP pricing.
    </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("Coming Soon", disabled=True):
        pass