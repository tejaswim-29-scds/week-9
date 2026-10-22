
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lab 6 - File Upload")

st.title("Lab 6: File Upload and Pandas")

st.write("Upload a CSV file to view and analyze its data.")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Dataset Information")
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Basic Statistics")
    st.write(df.describe())

    st.subheader("Clean Data")
    option = st.radio(
        "Choose how to handle missing values",
        ["Keep", "Drop missing rows", "Fill with 0"]
    )

    if option == "Drop missing rows":
        df = df.dropna()
    elif option == "Fill with 0":
        df = df.fillna(0)

    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Processed CSV",
        data=csv,
        file_name="processed.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a CSV file to begin.")
