
import streamlit as st
import requests

st.set_page_config(page_title="Weather API Demo", page_icon="🌦️")

st.title("Lab 10: API Integration + JSON + Secrets")

# Read API key from Streamlit secrets
API_KEY = st.secrets.get("API_KEY", "demo_key")

city = st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):
    # Simulated JSON response for practice
    resp = {
        "city": city,
        "temperature": 30,
        "condition": "Sunny",
        "humidity": 65
    }

    # Display JSON data
    st.subheader("Weather JSON Response")
    st.json(resp)

    # Display weather details
    c1, c2, c3 = st.columns(3)
    c1.metric("Temperature", f"{resp['temperature']} °C")
    c2.metric("Condition", resp["condition"])
    c3.metric("Humidity", f"{resp['humidity']}%")

st.divider()
st.subheader("HTTP Methods")
st.markdown("""
- **GET** — Retrieve data
- **POST** — Send data
- **PUT** — Update data
- **DELETE** — Delete data
""")
