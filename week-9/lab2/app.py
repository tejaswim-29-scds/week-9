
import streamlit as st

st.title("Lab 2: Widgets Playground")

name = st.text_input("Enter your name")
age = st.slider("Select your age", 1, 100, 18)
course = st.selectbox(
    "Choose your course",
    ["Python", "Java", "Web Development"]
)

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
