import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Major Vendor Order",
    page_icon="📦",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #FEFAE0;
    color: #283618;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1050px;
}

h1 {
    text-align: center;
    color: #283618;
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 0.2rem;
}

h2, h3 {
    color: #283618;
}

.subtitle {
    text-align: center;
    color: rgba(40,54,24,0.75);
    font-size: 18px;
    margin-bottom: 2rem;
}

.card {
    background-color: #FFF7E3;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #DDA15E;
    box-shadow: 0px 4px 14px rgba(40,54,24,0.08);
    margin-bottom: 24px;
}

.step-card {
    background-color: #FFFFFF;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(221,161,94,0.7);
    text-align: center;
    min-height: 145px;
}

.step-number {
    background-color: #BC6C25;
    color: white;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    margin-bottom: 10px;
}

.muted {
    color: rgba(40,54,24,0.75);
}

.stButton button {
    background-color: #BC6C25;
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    border: none;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #A85F20;
    color: white;
}

.stDownloadButton button {
    background-color: #283618;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

section[data-testid="stFileUploader"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #DDA15E;
}

div[data-testid="stMetric"] {
    background-color: #FFF7E3;
    border: 1px solid #DDA15E;
    padding: 16px;
    border-radius: 14px;
}

hr {
    border: none;
    border-top: 1px solid #DDA15E;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>Major Vendor Order Report</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Upload a 4-week Lightspeed item report and generate a recommended vendor order.</div>",
    unsafe_allow_html=True
)


st.markdown("""
<div class="card">
    <h2 style="text-align:center; margin-top:0;">1. Export Report from Lightspeed</h2>
    <p class="muted" style="text-align:center;">
        Pull the 4-week item sales report before uploading your CSV.
    </p>
</div>
""", unsafe_allow_html=True)

with st.expander("📊 Show Lightspeed Export Steps", expanded=True):
    steps = [
        ("📁", "Reports", "In Lightspeed, select Reports."),
        ("📊", "Grouped Sales Totals", "Scroll to Grouped Sales Totals."),
        ("📦", "Item Report", "Select Item as the report type."),
        ("📅", "Last 4 Weeks", "Set the date range to the last 4 weeks."),
        ("🏷️", "Vendor Filter", "Change the vendor filter if needed."),
        ("⬇️", "Export CSV", "Press Export and save the CSV file.")
    ]

    row1 = st.columns(3)
    row2 = st.columns(3)

    for i, step in enumerate(steps[:3]):
        icon, title, desc = step
        with row1[i]:
            st.markdown(f"""
            <div class="step-card">
                <div class="step-number">{i + 1}</div>
                <div style="font-size:26px;">{icon}</div>
                <h4 style="margin:6px 0;">{title}</h4>
                <p class="muted" style="font-size:14px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    for i, step in enumerate(steps[3:]):
        icon, title, desc = step
        with row2[i]:
            st.markdown(f"""
            <div class="step-card">
                <div class="step-number">{i + 4}</div>
                <div style="font-size:26px;">{icon}</div>
                <h4 style="margin:6px 0;">{title}</h4>
                <p class="muted" style="font-size:14px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)


st.divider()

st.markdown("## 2. Upload Report")

uploaded_file = st.file_uploader(
    "Drop your 4-week CSV report here",
    type=["csv"]
)

st.divider()


if uploaded_file:
    df = pd.read_csv(uploaded_file)

    required_columns = ["Stock", "Sold"]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        st.error(
            f"Your CSV is missing these required columns: {', '.join(missing_columns)}"
        )
    else:
        df["Order Qty"] = np.where(
            (df["Stock"] <= 0) & (df["Sold"] == 1),
            2,
            np.where(
                df["Stock"] <= 0,
                df["Sold"] * (3 / 4),
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

        output_df = df[df["Order Qty"] > 0].copy()
        output_df = output_df.sort_values("Order Qty", ascending=False)

        st.markdown("## 3. Order Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Items to Order", len(output_df))

        with col2:
            st.metric("Total Units", int(output_df["Order Qty"].sum()))

        with col3:
            st.metric("Top Order Qty", int(output_df["Order Qty"].max()) if len(output_df) > 0 else 0)

        st.markdown("### Recommended Order Preview")
        st.dataframe(output_df.head(50), use_container_width=True)

        csv = output_df.to_csv(index=False)

        st.download_button(
            label="Download Output CSV",
            data=csv,
            file_name="major_vendor_order_output.csv",
            mime="text/csv"
        )

else:
    st.info("Upload a CSV report to generate your order recommendation.")