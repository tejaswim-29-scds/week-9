
import streamlit as st

st.set_page_config(page_title="Lab 4 Forms")

st.title("Lab 4: Forms and Session State")

if "count" not in st.session_state:
    st.session_state.count = 0

with st.form("student_form"):
    name = st.text_input("Student Name")
    marks = st.number_input(
        "Enter Marks",
        min_value=0,
        max_value=100,
        value=50
    )
    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state.count += 1
    st.success(f"Name: {name}")
    st.write("Marks:", marks)

st.write("Forms submitted:", st.session_state.count)

if st.button("Reset Counter"):
    st.session_state.count = 0
    st.rerun()
