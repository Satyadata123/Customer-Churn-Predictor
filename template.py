import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"  # adjust if deployed elsewhere

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details below to predict churn risk.")

# Input fields
row_number = st.number_input("Row Number", min_value=0, step=1)
customer_id = st.number_input("Customer ID", min_value=1, step=1)
surname = st.text_input("Surname")
credit_score = st.number_input("Credit Score", min_value=0, step=1)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, step=1)
tenure = st.selectbox("Tenure (years)", list(range(0, 11)))
balance = st.number_input("Balance", min_value=0.0, step=100.0)
num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_crcard = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", min_value=0.0, step=1000.0)

# Submit button
if st.button("Predict"):
    payload = {
        "RowNumber": row_number,
        "CustomerId": customer_id,
        "Surname": surname,
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_crcard,
        "IsActiveMember": is_active,
        "EstimatedSalary": salary
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success("✅ Prediction Complete")
            st.metric("Churn Status", result["churn_status"])
            st.metric("Risk Level", result["risk_level"])
            st.metric("Probability", result["probability_percent"])
            st.write("💡 Suggestion:", result["suggestion"])
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")







