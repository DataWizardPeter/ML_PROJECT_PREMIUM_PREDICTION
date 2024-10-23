from joblib import load
import pandas as pd

# Load models and scalers with raw string paths to prevent escape character issues
model_rest = load(r"C:\Project Regression\app\artifacts\model_rest.joblib")
model_young = load(r"C:\Project Regression\app\artifacts\model_young.joblib")
scaler_rest = load(r"C:\Project Regression\app\artifacts\scaler_rest.joblib")
scaler_young = load(r"C:\Project Regression\app\artifacts\scaler_young.joblib")


def predict(input_dict):
    # Convert input_dict to DataFrame for model input
    input_df = pd.DataFrame([input_dict])

    # Use your model logic to make predictions
    # Example: 
    # if input_df['age'][0] < 30:  # Customize your logic
    #     model = model_young
    # else:
    #     model = model_rest

    # Perform necessary scaling if applicable
    # input_scaled = scaler.transform(input_df)  # Use the appropriate scaler

    # Get the prediction
    # prediction = model.predict(input_scaled)  # Call the prediction method on the model

    # For demonstration, returning a placeholder value
    return [10000]  # Replace with actual prediction logic