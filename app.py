import streamlit as st
import pandas as pd
import numpy as np

st.title("Major Vendor Order Report") # Sets the title for the page
# st.info("""
#         HOW TO USE:
#             1. In LightSpeed, click on "Reports" in the sidebar
#             2. Scroll down to "Grouped Sales Totals"
#             3. Select "Item"
#             4. For Major Vendor Orders, change the date to account for the last four weeks 
#             5. Select the Vendor you choose to order from under "Default Vendor"
#             6. Press "Export"
#         """)
st.divider()
with st.expander("Where do I find this report?"):
    st.write("""
            1. In LightSpeed, click on "Reports" in the sidebar
            2. Scroll down to "Grouped Sales Totals"
            3. Select "Item"
            4. For Major Vendor Orders, change the date to account for the last four weeks 
            5. Select the Vendor you choose to order from under "Default Vendor"
            6. Press "Export"
            """)
st.divider()

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