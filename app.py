import streamlit as st
import pandas as pd
import numpy as np

st.title("Major Vendor Order Report")

uploaded_file = st.file_uploader(
    "Upload reports_sales_listings CSV",
    type=["csv"]
)
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