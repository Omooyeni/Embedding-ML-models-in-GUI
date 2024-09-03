# **Telco Customer Churn Prediction App**

This is a Streamlit application that predicts customer churn for a Telco company. The app leverages machine learning models to forecast whether a customer is likely to churn, providing valuable insights for customer retention strategies.

**Table of Contents**

Introduction
Features
Usage
Acknowledgements

**Introduction**

Customer churn refers to the rate at which customers stop doing business with a company. This app predicts whether a customer will churn based on historical data. By identifying potential churners, Telco company can take proactive measures to retain them.

**Features**

**Prediction:** Predicts whether a customer will churn using trained machine learning models.
**Interactive Dashboard:** Provides an EDA (Exploratory Data Analysis) dashboard with various visualizations such as bar charts and line graphs.
**History:** View the history of predited Churn.
**Key Performance Indicators (KPIs):** Displays KPIs relevant to churn prediction.
**Dataset:** View and Download the dataset used to Train the model.
**User Authentication:** Simple authentication system to secure access to the app.

# **Usage**

**Login:** Start by logging in using your credentials.
# **Navigate through the app:**
Use the Dashboard page to explore customer data and key insights.
Use the Churn Prediction page to predict whether a specific customer will churn.
Use the History page to view historical data of the predited Churn..
Use the Data page to view, Dowaload and explore the raw data used to train the model used for Prediction.
Adjust Parameters: Use sliders and dropdowns on the Churn prediction pade to change parameters use to predict churn.

# **Model Information**

The app uses pre-trained machine learning models to predict customer churn. The models are loaded from external URLs:

Gradient Boosting model: 'https://raw.githubusercontent.com/richmond-yeboah/Telecom-Customer-Churn-Prediction/main/model/GradientBoosting.joblib' 
   
Support Vector model: 'https://raw.githubusercontent.com/richmond-yeboah/Telecom-Customer-Churn-Prediction/main/model/SupportVector.joblib'

Label encoder: 'https://raw.githubusercontent.com/richmond-yeboah/Telecom-Customer-Churn-Prediction/main/model/label_encoder.joblib'

# **Acknowledgements**

I will like to thank the open-source community for providing the tools and resources used in this project and all the free available resource made available online.