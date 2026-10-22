
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lab 5 Visualization")

st.title("Lab 5: Data Visualization")
st.write("Visualizing student marks using charts.")

# Sample dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [85, 72, 90, 65, 78]
}

df = pd.DataFrame(data)

st.subheader("Student Marks Dataset")
st.dataframe(df)

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(df.set_index("Student")["Marks"])

# Line chart
st.subheader("Line Chart")
st.line_chart(df.set_index("Student")["Marks"])

# Matplotlib chart
st.subheader("Matplotlib Visualization")

fig, ax = plt.subplots()
ax.bar(df["Student"], df["Marks"])
ax.set_xlabel("Student")
ax.set_ylabel("Marks")
ax.set_title("Student Marks")

st.pyplot(fig)
