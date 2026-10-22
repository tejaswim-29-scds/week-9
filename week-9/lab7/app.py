
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("Lab 7: Interactive Sales Dashboard")

# Generate sample sales data
df = pd.DataFrame({
    "Year": np.random.choice([2022, 2023, 2024], 200),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], 200
    ),
    "Product": np.random.choice(["A", "B", "C"], 200),
    "Sales": np.random.randint(1000, 10000, 200)
})

# Sidebar filters
st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

region = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

product = st.sidebar.multiselect(
    "Product",
    sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

# Filter data
filtered = df[
    df["Year"].isin(year)
    & df["Region"].isin(region)
    & df["Product"].isin(product)
]

# Key performance indicators
c1, c2, c3 = st.columns(3)

total_sales = filtered["Sales"].sum()
average_sales = filtered["Sales"].mean()

c1.metric("Total Sales", f"{total_sales:,}")
c2.metric(
    "Average Sales",
    f"{average_sales:,.0f}" if not filtered.empty else "0"
)
c3.metric("Records", len(filtered))

# Charts
st.subheader("Sales by Region")
st.bar_chart(filtered.groupby("Region")["Sales"].sum())

st.subheader("Sales by Year")
st.line_chart(filtered.groupby("Year")["Sales"].sum())

# Display filtered data
st.subheader("Filtered Sales Data")
st.dataframe(filtered)

# Download filtered data
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Filtered CSV",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv"
)

