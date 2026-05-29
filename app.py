# ==========================================
# IMPORT LIBRARIES
# ==========================================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Seller Dashboard",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================
st.title("📊 Seller Sales Dashboard")

st.markdown("Analyze seller performance by region and vendor.")

# ==========================================
# LOAD EXCEL FILE
# ==========================================
df = pd.read_excel("sellers.xlsx")

# ==========================================
# SIDEBAR FILTER
# ==========================================
st.sidebar.header("Filters")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["REGION"].unique())
)

# ==========================================
# FILTER DATA
# ==========================================
if region != "All":
    filtered_df = df[df["REGION"] == region]
else:
    filtered_df = df

# ==========================================
# DISPLAY TABLE
# ==========================================
st.subheader("Seller Table")

st.dataframe(filtered_df)

# ==========================================
# METRICS
# ==========================================
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Units Sold",
    int(filtered_df["SOLD UNITS"].sum())
)

col2.metric(
    "Total Sales",
    int(filtered_df["TOTAL SALES"].sum())
)

col3.metric(
    "Average Sales",
    round(filtered_df["SALES AVERAGE"].mean(), 2)
)

# ==========================================
# CHARTS
# ==========================================
st.subheader("Sales Charts")

# Units Sold Chart
fig1, ax1 = plt.subplots(figsize=(8,4))
ax1.bar(filtered_df["NAME"], filtered_df["SOLD UNITS"])
ax1.set_title("Units Sold by Seller")
plt.xticks(rotation=90)

st.pyplot(fig1)

# Total Sales Chart
fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.bar(filtered_df["NAME"], filtered_df["TOTAL SALES"])
ax2.set_title("Total Sales by Seller")
plt.xticks(rotation=90)

st.pyplot(fig2)

# Average Sales Chart
fig3, ax3 = plt.subplots(figsize=(8,4))
ax3.bar(filtered_df["NAME"], filtered_df["SALES AVERAGE"])
ax3.set_title("Average Sales by Seller")
plt.xticks(rotation=90)

st.pyplot(fig3)

# ==========================================
# SELLER SEARCH
# ==========================================
st.subheader("Search Specific Seller")

seller_name = st.selectbox(
    "Choose a Seller",
    filtered_df["NAME"]
)

seller_data = filtered_df[
    filtered_df["NAME"] == seller_name
]

st.write(seller_data)

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.write("Dashboard created with Streamlit")