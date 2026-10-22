
import streamlit as st
import psycopg2
from passlib.hash import bcrypt

st.set_page_config(page_title="Lab 13 - Login", page_icon="🔐")
st.title("Lab 13: Login / Signup")

# Database connection settings
def get_connection():
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        port=st.secrets.get("DB_PORT", "5432")
    )

# Create the users table
def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)

try:
    create_table()

    choice = st.radio("Choose an option", ["Signup", "Login"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if choice == "Signup":
        if st.button("Create Account"):
            if username.strip() and password:
                with get_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                            (username.strip(), bcrypt.hash(password))
                        )
                st.success("Account created successfully!")
            else:
                st.warning("Enter both username and password.")

    else:
        if st.button("Login"):
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT password_hash FROM users WHERE username = %s",
                        (username.strip(),)
                    )
                    row = cur.fetchone()

            if row and bcrypt.verify(password, row[0]):
                st.success(f"Welcome, {username}!")
            else:
                st.error("Invalid username or password.")

except Exception as e:
    st.error("Could not connect to PostgreSQL.")
    st.info("Check that PostgreSQL is running and your database secrets are correct.")
