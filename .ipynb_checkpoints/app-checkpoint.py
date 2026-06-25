import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Major Vendor Order",
    page_icon="📦",
    layout="wide"
)
#####

st.markdown("""
<style>

/* PAGE BACKGROUND */
.stApp {
    background-color: #FEFAE0;
}

/* MAIN CONTAINER SPACING */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

/* HERO TITLE */
h1 {
    text-align: center;
    color: #283618;
    font-size: 44px;
    margin-bottom: 0.2rem;
    letter-spacing: 0.5px;
}

/* SUBHEADINGS */
h2 {
    text-align: center;
    color: #283618;
    font-weight: 600;
}

/* REMOVE markdown noise spacing */
div[data-testid="stMarkdownContainer"] {
    font-size: 16px;
    line-height: 1.6;
}

/* CARD STYLE (this is the key upgrade) */
div.stAlert {
    border-radius: 16px;
    border: 1px solid #DDA15E;
    background-color: #FFF7E3;
}

/* FILE UPLOADER "CARD" */
section[data-testid="stFileUploader"] {
    background-color: #FFFFFF;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #DDA15E;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}

/* BUTTONS */
.stButton button {
    background-color: #BC6C25;
    color: white;
    border-radius: 10px;
    padding: 0.45rem 1rem;
    border: none;
}

/* DOWNLOAD BUTTON */
.stDownloadButton button {
    background-color: #283618;
    color: white;
    border-radius: 10px;
}

/* DIVIDERS */
hr {
    border: none;
    border-top: 1px solid #DDA15E;
    margin: 2rem 0;
}

</style>
""", unsafe_allow_html=True)


####

st.markdown("<h1>Major Vendor Order Report</h1>", unsafe_allow_html=True)

st.markdown("## How to Pull Report from Lightspeed")

st.markdown("""
<div style="
    background-color:#FFF7E3;
    padding:20px;
    border-radius:16px;
    border:1px solid #DDA15E;
">
""", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("""
### 📊 Export 4-Week Item Report

Follow these steps in Lightspeed:
    """)

with col2:
    show_steps = st.button("Show Steps")

st.markdown("</div>", unsafe_allow_html=True)

if show_steps:
    cols = st.columns(6)

    steps = [
        "In Lightspeed, Select Reports",
        "Scroll to Grouped Sales Totals",
        "Select Item",
        "Choose date to be last 4 Weeks",
        "Change Vendor",
        "Press Export"
    ]

    icons = ["📁", "📊", "📦", "📅", "🏷️", "⬇️"]

    for i in range(6):
        with cols[i]:
            st.markdown(f"""
            <div style='text-align:center'>
                <div style='font-size:24px'>{icons[i]}</div>
                <div style='font-weight:600'>{steps[i]}</div>
            </div>
            """, unsafe_allow_html=True)





st.markdown("## Upload Report")

st.markdown("""
<div style="
    background-color:#FFFFFF;
    padding:16px;
    border-radius:14px;
    border:1px solid #DDA15E;
">
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drop your 4-week CSV report here",
    type=["csv"]
)

st.markdown("</div>", unsafe_allow_html=True)

st.divider()





if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["Order Qty"] = np.where(
        (df["Stock"] <= 0) & (df["Sold"] == 1),
        2,
        np.where(
            df["Stock"] <= 0,
            df["Sold"] * (3/4),
            np.where(
                df["Stock"] < 2,
                df["Sold"] / 2,
                np.where(
                    (df["Sold"] / 2) - df["Stock"] < 0,
                    0,
                    (df["Sold"] / 2) - df["Stock"]
                )
            )
        )
    )
    df["Order Qty"] = np.maximum(
        0,
        np.ceil(df["Order Qty"])
    ).astype(int)
    
    df = df[df["Order Qty"] > 0]

    df = df.sort_values("Order Qty", ascending=False)

    st.dataframe(df.head(20))

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Output CSV",
        data=csv,
        file_name="output.csv",
        mime="text/csv"
    )