import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Sample training data
data = {"study_hours": [2, 3, 5, 7, 10], "previous_scores": [55, 60, 75, 80, 95], "final_score": [58, 65, 78, 85, 98]}
df = pd.DataFrame(data)

# Train model
X = df[["study_hours", "previous_scores"]]
y = df["final_score"]
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "prediction/model.pkl")
print("Model trained and saved!")
