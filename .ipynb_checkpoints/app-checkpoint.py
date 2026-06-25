import streamlit as st
import pandas as pd
import numpy as np
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

st.set_page_config(
    page_title="Major Vendor Order",
    page_icon="images/logo.png",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu, header, footer {
    visibility: hidden;
}

[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    display: none;
}

.stApp {
    background-color: #F6F1E5;
    color: #2F372D;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1050px;
}

.hero {
    background-color: #1D5A3E;
    padding: 40px 30px;
    border-radius: 26px;
    margin-bottom: 34px;
    box-shadow: 0px 8px 22px rgba(29,90,62,.18);
}

.hero h1 {
    text-align: center;
    color: #FFF9EF;
    font-size: 44px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    text-align: center;
    color: rgba(255,249,239,0.88);
    font-size: 17px;
    margin-top: 12px;
    margin-bottom: 0;
}

.section-label {
    color: #C97822;
    font-weight: 800;
    font-size: 13px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.section-title {
    color: #1D5A3E;
    font-size: 31px;
    font-weight: 800;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #5C7A58;
    font-size: 16px;
    margin-bottom: 20px;
}


.mini-step {
    background-color: #FDF7EA;
    border: 1px solid #D7C8A4;
    border-radius: 18px;
    padding: 14px 10px;
    min-height: 125px;
    text-align: center;
    box-shadow: 0px 3px 10px rgba(47,55,45,0.04);
}

.mini-number {
    background-color: #C97822;
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 999px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 6px;
}

.mini-step h4 {
    color: #1D5A3E;
    font-size: 16px;
    margin: 5px 0 3px 0;
}

.mini-step p {
    color: #5C7A58;
    font-size: 12px;
    margin: 0;
    line-height: 1.35;
}

.stButton button {
    background-color: #C97822;
    color: white;
    border-radius: 12px;
    padding: 0.55rem 1rem;
    border: none;
    font-weight: 700;
}

.stButton button:hover {
    background-color: #B4671C;
    color: white;
}

.stDownloadButton button {
    background-color: #1D5A3E;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 700;
}

.stDownloadButton button:hover {
    background-color: #15442F;
    color: white;
}

section[data-testid="stFileUploader"] {
    background-color: #FFF9EF;
    padding: 22px;
    border-radius: 22px;
    border: 1px solid #D7C8A4;
    box-shadow: 0px 4px 14px rgba(47,55,45,0.07);
}

div[data-testid="stMetric"] {
    background-color: #FFF9EF;
    border: 1px solid #D7C8A4;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 4px 14px rgba(47,55,45,0.06);
}

hr {
    border: none;
    border-top: 1px solid #D7C8A4;
    margin: 2rem 0;
}

h2, h3 {
    color: #1D5A3E;
}
</style>
""", unsafe_allow_html=True)

logo_base64 = image_to_base64("images/logo.png")

st.markdown("""
<div class="hero">
    <h1> Major Vendor Order Report</h1>
    <p>Generate a vendor order from a Lightspeed 4-week item sales report.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-label">Step 1</div>
<div class="section-title">Export Report from Lightspeed</div>
<div class="section-subtitle">Follow these steps to export the correct CSV report.</div>
""", unsafe_allow_html=True)


steps = [
    ("images/reports.png", "Reports", "Open Reports from the sidebar."),
    ("images/grouped_sales.png", "Grouped Sales", "Scroll to Grouped Sales Totals."),
    ("images/item_report.png", "Item Report", "Select Item as the report type."),
    ("images/calendar.png", "Date Filter", "Set date range to last 4 weeks."),
    ("images/vendor.png", "Vendor Filter", "Choose the desired vendor."),
    ("images/export.png", "Export CSV", "Press Export and save the CSV.")
]

def render_mini_step(number, image_path, title, desc):
    image_base64 = image_to_base64(image_path)

    st.markdown(f"""
    <div class="mini-step">
        <div class="mini-number">{number}</div>
        <br>
        <img src="data:image/png;base64,{image_base64}" width="42" style="margin:0 auto 5px auto;">
        <h4>{title}</h4>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)


row1 = st.columns(3)
for i, step in enumerate(steps[:3]):
    with row1[i]:
        render_mini_step(i + 1, *step)

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

row2 = st.columns(3)
for i, step in enumerate(steps[3:]):
    with row2[i]:
        render_mini_step(i + 4, *step)



st.divider()

st.markdown("""
<div class="section-label">Step 2</div>
<div class="section-title">Upload Item Sale Report</div>
<div class="section-subtitle">Upload the 4-week CSV report exported from Lightspeed.</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
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

        st.markdown("""
        <div class="section-label">Step 3</div>
        <div class="section-title">Order Results</div>
        <div class="section-subtitle">Review the recommended order quantities and download your CSV.</div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Items to Order", len(output_df))

        with col2:
            st.metric("Total Units", int(output_df["Order Qty"].sum()))

        with col3:
            st.metric(
                "Top Order Qty",
                int(output_df["Order Qty"].max()) if len(output_df) > 0 else 0
            )

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