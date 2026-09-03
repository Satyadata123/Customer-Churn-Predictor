# 📊 Customer Churn Prediction

An end-to-end **Customer Churn Prediction** system that uses an
**Artificial Neural Network (ANN)** to predict whether a customer is
likely to churn. The application also converts the predicted probability
into a **Low / Medium / High risk level** and provides an actionable
business recommendation.

The project demonstrates a complete machine learning workflow from
preprocessing and class balancing to model training, API development,
interactive UI, and Docker deployment.

## 🚀 Project Overview

Customer churn is an important business problem for organizations such
as banks, telecom companies, and e-commerce businesses. Losing customers
can directly affect revenue, while identifying customers at risk early
can give businesses an opportunity to take preventive action.

This project predicts customer churn from customer and account
information and provides:

-   Churn / Not Churn prediction
-   Churn probability
-   Risk level
-   Actionable retention suggestion
-   FastAPI prediction API
-   Streamlit interactive frontend
-   Dockerized application

## 🎯 Objectives

-   Build an ANN-based binary classification model for customer churn.
-   Process categorical and numerical customer features.
-   Handle class imbalance using SMOTE.
-   Create a reusable preprocessing pipeline.
-   Expose the prediction system through FastAPI.
-   Build an interactive Streamlit interface.
-   Containerize the complete application using Docker.

## 🧠 Machine Learning Workflow

``` text
Customer Dataset
       ↓
Data Preprocessing
       ↓
Drop Irrelevant Columns
       ↓
One-Hot Encoding
       ↓
Standard Scaling
       ↓
SMOTE on Training Data
       ↓
ANN Model Training
       ↓
Churn Probability
       ↓
Risk Classification
       ↓
Business Recommendation
```

## 📁 Dataset

**Dataset:** Telco / Bank Customer Churn Dataset\
**Source:** Kaggle community upload\
**Rows:** 10,000\
**Original columns:** 13 (12 input features + `Exited` target)

The exact Kaggle uploader and dataset URL are not available in the
project information.

### Target Variable

  Column     Description
  ---------- -----------------------
  `Exited`   Customer churn status
  `0`        Not Churn
  `1`        Churn

Approximate class distribution:

-   Non-churn: \~80%
-   Churn: \~20%

### Features

  Feature             Description
  ------------------- ------------------------------------------------------
  `RowNumber`         Dataset row identifier; dropped during preprocessing
  `CustomerId`        Customer identifier; dropped during preprocessing
  `Surname`           Customer surname; dropped during preprocessing
  `CreditScore`       Customer credit score
  `Geography`         Customer geography
  `Gender`            Customer gender
  `Age`               Customer age
  `Tenure`            Years of relationship with the bank
  `Balance`           Current account balance
  `NumOfProducts`     Number of products/services used
  `HasCrCard`         Whether the customer has a credit card
  `IsActiveMember`    Whether the customer is an active member
  `EstimatedSalary`   Estimated annual salary

> **Dataset license:** Not specified for the source dataset used in this
> project.

## 🧹 Data Preprocessing

The project uses a reusable Scikit-learn preprocessing pipeline.

### 1. Dropping irrelevant columns

The following identifier-related columns are removed:

``` text
RowNumber
CustomerId
Surname
```

### 2. One-Hot Encoding

Categorical features are encoded using:

``` python
OneHotEncoder(drop="first")
```

Applied to:

-   `Geography`
-   `Gender`

### 3. Feature Scaling

Numerical features are standardized using:

``` python
StandardScaler()
```

### 4. Handling Class Imbalance

The training data is balanced using **SMOTE (Synthetic Minority
Oversampling Technique)**.

``` python
SMOTE(random_state=42)
```

SMOTE is applied to the training data after preprocessing and is not
applied to the test data.

## 🧠 ANN Model Architecture

The project uses **TensorFlow / Keras** to build an Artificial Neural
Network.

``` text
Input Layer
11 features
     ↓
Dense Layer
16 neurons
ELU activation
     ↓
Dense Layer
80 neurons
ReLU activation
     ↓
Dense Layer
112 neurons
ELU activation
     ↓
Output Layer
1 neuron
Sigmoid activation
```

### Model Configuration

  Parameter              Value
  ---------------------- ---------------------------
  Framework              TensorFlow / Keras
  Model                  Artificial Neural Network
  Input features         11
  Hidden layers          3
  Hidden layer sizes     16 → 80 → 112
  Activations            ELU → ReLU → ELU
  Output neurons         1
  Output activation      Sigmoid
  Optimizer              Adam
  Loss                   Binary Crossentropy
  Training epochs        50
  Batch size             32 (Keras default)
  Prediction threshold   0.5

## 📈 Model Results

The reported test evaluation is:

**Accuracy: 77.45%**

### Confusion Matrix

``` text
[[1279, 328],
 [ 123, 270]]
```

  Actual / Predicted     Not Churn   Churn
  -------------------- ----------- -------
  **Not Churn**               1279     328
  **Churn**                    123     270

The model correctly identified **270 churned customers** and missed
**123 churned customers** in the reported evaluation.

> **Note:** Before publishing final benchmark claims, verify that the
> evaluation was performed with the intended separate test dataset. The
> current preprocessing code previously shared contains a test-data
> assignment that should use `x_test_data` rather than `x_train_data`.

## 🌐 FastAPI Backend

FastAPI provides the prediction API.

### Endpoints

#### `GET /`

Basic home endpoint.

Example response:

``` json
{
  "message": "This is the home page"
}
```

#### `POST /predict`

Accepts validated customer information and returns the churn prediction.

The API:

1.  Validates incoming data using Pydantic.
2.  Converts the request into a Pandas DataFrame.
3.  Loads the saved preprocessing pipeline.
4.  Loads the saved ANN model.
5.  Transforms the customer data.
6.  Generates churn probability.
7.  Converts probability into a binary prediction.
8.  Assigns a risk level.
9.  Returns an actionable suggestion.

### Example API Response

``` json
{
  "probability_raw": 0.78,
  "probability_percent": "78.0%",
  "prediction": 1,
  "churn_status": "Churn",
  "risk_level": "High",
  "suggestion": "Offer retention incentives or personalized support."
}
```

## ⚠️ Risk Classification

The application converts the predicted probability into three business
risk categories.

  -----------------------------------------------------------------------
  Probability             Risk Level              Recommendation
  ----------------------- ----------------------- -----------------------
  `< 40%`                 Low                     Customer is stable.
                                                  Continue normal
                                                  engagement.

  `40% – <70%`            Medium                  Monitor engagement and
                                                  consider proactive
                                                  outreach.

  `≥ 70%`                 High                    Offer retention
                                                  incentives or
                                                  personalized support.
  -----------------------------------------------------------------------

## 🖥️ Streamlit Frontend

The Streamlit application provides an interactive interface where users
can enter customer details.

### Input Fields

-   Row Number
-   Customer ID
-   Surname
-   Credit Score
-   Geography
-   Gender
-   Age
-   Tenure
-   Balance
-   Number of Products
-   Has Credit Card
-   Active Member
-   Estimated Salary

After clicking **Predict**, the application displays:

-   Churn Status
-   Risk Level
-   Churn Probability
-   Business Suggestion

### Application Architecture

``` text
                ┌─────────────────────┐
                │       User          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Streamlit Frontend  │
                │      Port 8501      │
                └──────────┬──────────┘
                           │ HTTP POST
                           ▼
                ┌─────────────────────┐
                │   FastAPI Backend   │
                │      Port 8000      │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Prediction Pipeline │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Preprocessing + ANN │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Probability / Risk  │
                └─────────────────────┘
```

## 🐳 Docker Deployment

The application is containerized using Docker.

### Docker Image

Docker Hub repository:

**`satyamsingh2005/churn-app`**

Available tags:

-   `v2`
-   `v1.0`

Pull the latest project image:

``` bash
docker pull satyamsingh2005/churn-app:v2
```

### Run the Container

``` bash
docker run -p 8000:8000 -p 8501:8501 satyamsingh2005/churn-app:v2
```

The Docker container runs both FastAPI and Streamlit.

### Access the Application

**Streamlit:**

http://localhost:8501

**FastAPI:**

http://localhost:8000

**FastAPI Swagger Documentation:**

http://localhost:8000/docs

## 💻 Local Installation

### 1. Clone the repository

``` bash
git clone https://github.com/Satyadata123/Customer-Churn-Predictor.git
cd Customer-Churn-Predictor
```

### 2. Create a virtual environment

Windows:

``` bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Start FastAPI

``` bash
uvicorn app:app --reload
```

FastAPI will be available at:

``` text
http://localhost:8000
```

Swagger API documentation:

``` text
http://localhost:8000/docs
```

### 5. Start Streamlit

Open another terminal with the virtual environment activated:

``` bash
streamlit run template.py
```

Then open:

``` text
http://localhost:8501
```

## 📦 Main Dependencies

-   Python 3.11
-   TensorFlow 2.21.0
-   Keras 3.15.1
-   Scikit-learn 1.5.1
-   Pandas
-   NumPy
-   Imbalanced-learn
-   FastAPI
-   Pydantic
-   Streamlit
-   Docker

## 📂 Project Structure

``` text
Customer-Churn-Predictor/
│
├── artifacts/
│   ├── transform.pkl
│   └── ann_model.pkl
│
├── src/
│   ├── prediction_pipline/
│   │   └── prediction.py
│   ├── until.py
│   ├── exception.py
│   └── logger.py
│
├── app.py
├── template.py
├── Data_validation.py
├── Dockerfile
├── requirements.txt
└── README.md
```

> The exact repository may contain additional training/data-ingestion
> files not listed above.

## 🔐 Input Validation

Customer requests are validated using Pydantic before reaching the
prediction pipeline.

Examples include:

-   Geography limited to `France`, `Germany`, or `Spain`
-   Gender limited to `Male` or `Female`
-   Tenure restricted to 0--10 years
-   Number of products restricted to 1--4
-   Binary fields restricted to 0/1
-   Age and financial values checked against defined constraints

This helps prevent invalid input from reaching the model.

## 🛠️ Technologies Used

  Category             Technologies
  -------------------- ---------------------
  Programming          Python
  Data Processing      Pandas, NumPy
  Machine Learning     Scikit-learn, SMOTE
  Deep Learning        TensorFlow, Keras
  API                  FastAPI
  Validation           Pydantic
  Frontend             Streamlit
  Serialization        Pickle
  Containerization     Docker
  Repository           GitHub
  Container Registry   Docker Hub

## 🔮 Future Improvements

Potential improvements include:

-   Add a dedicated validation set instead of using the test set for
    validation during ANN training.
-   Add additional evaluation metrics such as Precision, Recall,
    F1-score, and ROC-AUC.
-   Perform hyperparameter tuning and systematic model comparison.
-   Add model explainability using SHAP or similar techniques.
-   Improve the UI with visual risk indicators and charts.
-   Add authentication and API security.
-   Deploy the application to a cloud platform.
-   Add automated CI/CD.
-   Add monitoring and model-performance tracking.
-   Add automated tests for preprocessing, API validation, and
    predictions.

## 📌 Known Development Note

The current training code creates an EarlyStopping callback with a
patience of 5, but the callback is not passed to `model.fit()`.
Therefore, early stopping is not active in the current implementation.

If enabled, training would use:

``` python
model.fit(
    x_train_transform,
    y_train,
    epochs=500,
    validation_data=(x_test_transform, y_test),
    callbacks=[stop_early]
)
```

For a production-quality workflow, a separate validation set should be
used rather than the final test set for early-stopping decisions.

## 👨‍💻 Author

**Satyam Singh**

BCA Student \| Machine Learning & AI Developer

-   GitHub: [Satyadata123](https://github.com/Satyadata123)
-   LinkedIn: [Satyam
    Singh](https://www.linkedin.com/in/satyam-singh-b487ba361)
-   Email: <satyamsinghsolanki2005@gmail.com>

## 📄 License

This project's own source-code license has not been specified yet.

The dataset license is also not specified because the exact original
Kaggle dataset listing/uploader could not be verified from the available
project information.

------------------------------------------------------------------------

⭐ If you find this project useful, consider giving the repository a
star.
