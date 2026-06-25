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

/* Background */
.stApp {
    background-color: #FEFAE0;
}

/* Main header */
h1 {
    text-align: center;
    color: #283618;
    font-size: 42px;
    margin-bottom: 0px;
}

/* Subheaders */
h2, h3 {
    text-align: center;
    color: #283618;
}

/* Card style */
div[data-testid="stMarkdownContainer"] {
    font-size: 16px;
}

/* File uploader box */
section[data-testid="stFileUploader"] {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DDA15E;
}

/* Divider spacing */
hr {
    border-color: #DDA15E;
}

/* Buttons */
.stDownloadButton button {
    background-color: #BC6C25;
    color: white;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


####

st.markdown("<h1>Major Vendor Order Report</h1>", unsafe_allow_html=True)

with st.container()
    st.markdown("## How to Pull Report from Lightspeed?"):
    st.info("""
            Go to: 
            ** Reports → Grouped Sales Totals →  Item ** 

            Then: 
                1. Set the date range to the last FOUR weeks
                2. Select Major Vendor under "Default Vendor"
                3. Select **EXPORT** 🗎
            """)
st.divider()

st.markdown("""
### Please drag and drop your CSV file below
""")

uploaded_file = st.file_uploader(
    "↓ Upload 4 Week Item Report Here ↓",
    type=["csv"]
)

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