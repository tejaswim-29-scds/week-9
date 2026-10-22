
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Hello App",
    page_icon="👋",
    layout="centered"
)

# Headings
st.title("Hello Streamlit")
st.header("My First App")
st.subheader("Learning Basics")

# Text formatting
st.write("Streamlit converts Python scripts into web apps.")
st.markdown("**Bold text**, *Italic text*, and `code`.")

# Messages
st.success("App loaded successfully!")
st.info("This is an information message.")
st.warning("This is a warning message.")
st.error("This is an error message.")

# User inputs
name = st.text_input("Enter your name")
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)

if name:
    st.write(f"Hello, {name}!")

st.write("Your age:", age)

# Sample table
st.subheader("Sample Data")
st.table({
    "Name": ["A", "B"],
    "Marks": [85, 90]
})
