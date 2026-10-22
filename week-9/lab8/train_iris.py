
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train the machine learning model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the trained model
joblib.dump(model, "iris_model.pkl")

print("Iris model trained and saved successfully!")
