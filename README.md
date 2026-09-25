# Customer Churn Prediction

A Machine Learning project that predicts whether a customer is likely to **churn (leave the service)** based on customer-related information.

The project covers the complete ML workflow — from data analysis and preprocessing to model training, evaluation, saving the trained model, and deployment using Streamlit.

## 📌 Project Overview

Customer churn is an important problem for businesses because retaining existing customers is often important for long-term growth.

This project uses customer information such as:

* Age
* Gender
* Tenure
* Support Calls
* Other customer-related attributes

to build a Machine Learning model that predicts the customer's churn status.

## 🎯 Objectives

* Analyze customer churn data
* Perform data preprocessing and cleaning
* Explore relationships between customer features and churn
* Train Machine Learning classification models
* Evaluate model performance
* Save the trained model
* Build a user-friendly Streamlit application
* Deploy the ML model for real-time predictions

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-learn** – Machine Learning
* **Joblib** – Model serialization
* **Jupyter Notebook** – Data analysis and experimentation
* **Streamlit** – Web application and deployment
* **Git & GitHub** – Version control

## 📂 Project Structure

```text
Customer_Churn_Prediction/
│
├── data/
│   └── customer_churn.csv
│
├── model/
│   └── trained model files
│
├── notebooks/
│   └── Customer_Churn_Analysis.ipynb
│
├── train_model.py
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Customer Churn Prediction
```

## 📊 Dataset

The project uses a customer churn dataset containing customer-related information and a churn target variable.

Example features include:

* Age
* Gender
* Tenure
* Support Calls
* Churn

The dataset is stored inside the `data` folder.

## 🤖 Machine Learning

This project uses supervised Machine Learning classification techniques to predict customer churn.

The general process is:

1. Load the dataset
2. Check missing values and duplicate records
3. Perform exploratory data analysis
4. Encode categorical variables
5. Prepare input features and target variable
6. Split the data into training and testing sets
7. Train the classification model
8. Evaluate the model
9. Save the trained model
10. Use the model for prediction through Streamlit

## 📈 Model Evaluation

The trained model can be evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help understand how well the model identifies customers who may churn.

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Customer_Churn_Prediction.git
```

### 2. Open the project

```bash
cd Customer_Churn_Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Train the Model

Run:

```bash
python train_model.py
```

The trained model will be saved in the `model` folder.

## 🌐 Run the Streamlit Application

Start the application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually it runs at:

```text
http://localhost:8501
```

## 🔮 Prediction

The Streamlit application allows the user to enter customer information and receive a prediction indicating whether the customer is likely to churn.

Example:

```text
Customer Information
        ↓
Machine Learning Model
        ↓
Prediction
        ↓
Churn / No Churn
```

## 📚 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python Programming
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Feature Engineering
* Machine Learning
* Classification
* Model Evaluation
* Model Saving
* Streamlit
* Git & GitHub
* Project Deployment

## 🚀 Future Improvements

* Compare multiple classification algorithms
* Improve model performance through hyperparameter tuning
* Add advanced feature engineering
* Add probability-based churn prediction
* Improve Streamlit UI
* Deploy the application online
* Add model explainability using SHAP
* Add customer retention recommendations

## 👨‍💻 Author

**Alok Gupta**

B.Tech – Computer Science and Engineering

Interested in **Machine Learning, AI, Data Science and Software Development**.

## ⭐ Project Status

🚧 **Currently under development**

The project is being continuously improved with better model evaluation, UI, and deployment.

---

## 📜 License

This project is created for educational and portfolio purposes.
