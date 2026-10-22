
import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_iris

st.set_page_config(page_title="Iris Prediction", page_icon="🌸")

st.title("Lab 8: Iris Flower Prediction")
st.write("Enter flower measurements to predict its species.")

# Load the trained model
model = joblib.load("iris_model.pkl")
iris = load_iris()

with st.form("prediction_form"):
    sepal_length = st.number_input(
        "Sepal length (cm)", 0.1, 10.0, 5.1
    )
    sepal_width = st.number_input(
        "Sepal width (cm)", 0.1, 10.0, 3.5
    )
    petal_length = st.number_input(
        "Petal length (cm)", 0.1, 10.0, 1.4
    )
    petal_width = st.number_input(
        "Petal width (cm)", 0.1, 10.0, 0.2
    )

    submitted = st.form_submit_button("Predict Species")

if submitted:
    features = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediction = model.predict(features)[0]
    species = iris.target_names[prediction]

    st.success(f"Predicted species: {species.title()}")
