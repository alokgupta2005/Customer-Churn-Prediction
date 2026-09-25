from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load trained ML model
model = joblib.load("models/churn_model.pkl")


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is working"}


@app.post("/predict")
def predict(data: dict):

    input_data = pd.DataFrame(
        [
            {
                "gender": data["gender"],
                "SeniorCitizen": data["SeniorCitizen"],
                "Partner": data["Partner"],
                "Dependents": data["Dependents"],
                "tenure": data["tenure"],
                "PhoneService": data["PhoneService"],
                "MultipleLines": data["MultipleLines"],
                "InternetService": data["InternetService"],
                "OnlineSecurity": data["OnlineSecurity"],
                "OnlineBackup": data["OnlineBackup"],
                "DeviceProtection": data["DeviceProtection"],
                "TechSupport": data["TechSupport"],
                "StreamingTV": data["StreamingTV"],
                "StreamingMovies": data["StreamingMovies"],
                "Contract": data["Contract"],
                "PaperlessBilling": data["PaperlessBilling"],
                "PaymentMethod": data["PaymentMethod"],
                "MonthlyCharges": data["MonthlyCharges"],
                "TotalCharges": data["TotalCharges"],
            }
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "Churn"
    else:
        result = "Not Churn"

    return {"prediction": result}
