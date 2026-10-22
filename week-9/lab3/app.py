
import streamlit as st

st.set_page_config(
    page_title="Lab 3 Layouts",
    page_icon="📐",
    layout="wide"
)

st.title("Lab 3: Streamlit Layouts")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Welcome to my application!")
page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "About", "Contact"]
)

# Columns
st.header("Columns Example")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column 1")
    st.write("This is the first column.")

with col2:
    st.subheader("Column 2")
    st.write("This is the second column.")

with col3:
    st.subheader("Column 3")
    st.write("This is the third column.")

# Tabs
st.header("Tabs Example")

tab1, tab2, tab3 = st.tabs(
    ["Home", "Courses", "Contact"]
)

with tab1:
    st.write("Welcome to the Home tab.")

with tab2:
    st.write("Available courses: Python, Java, Web Development.")

with tab3:
    st.write("Contact us for more information.")

# Selected sidebar page
st.header("Selected Page")
st.write("You selected:", page)
