import pandas as pd
import numpy as np

from src.prediction_pipline.prediction import pipline
from Data_validation import Churn_validation

from fastapi import FastAPI





app = FastAPI()


@app.get('/')
def home():
    return {"message" : "This is the home page"}


@app.post('/predict')
def predict_data(user_data : Churn_validation):
    df = pd.DataFrame([user_data.dict()])
    model = pipline(df)
    
    y_prob, y_pred = model.predict()
    prob = y_prob.squeeze().item()
    pred = int(y_pred.squeeze())
    
    # Convert to percentage
    prob_percent = round(prob * 100, 2)
    
    # Map prediction to churn label
    churn_status = "Churn" if pred == 1 else "Not Churn"
    
    # Risk level + suggestion
    if prob >= 0.7:
        risk_level = "High"
        suggestion = "Offer retention incentives or personalized support."
    elif prob >= 0.4:
        risk_level = "Medium"
        suggestion = "Monitor engagement and consider proactive outreach."
    else:
        risk_level = "Low"
        suggestion = "Customer is stable. Continue normal engagement."
    
    return {
        "probability_raw": prob,
        "probability_percent": f"{prob_percent}%",
        "prediction": pred,
        "churn_status": churn_status,
        "risk_level": risk_level,
        "suggestion": suggestion
    }


