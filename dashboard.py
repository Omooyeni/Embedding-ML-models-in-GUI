import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title("Dashboard Page")
    st.write("Welcome to the Dashboard page!")

    # Load dataset
    file_path = r'C:/Users/USER/Desktop/Web App Streanlit/Embedding-ML-models-in-GUI/Data/dataset.csv'
    df = pd.read_csv(file_path)

    # Create a sidebar for navigation
    st.sidebar.title("Navigate the pades")
    page = st.sidebar.radio("Go to", ["EDA Dashboard", "KPIs"])

    if page == "EDA Dashboard":
        st.title("Exploratory Data Analysis Dashboard")

        # Displaying the dataset
        st.subheader("Dataset Overview")
        st.write(df.head())

        # Bar chart (Distribution of Churn)
        st.subheader("Distribution of Churn")
        churn_counts = df['Churn'].value_counts()
        st.bar_chart(churn_counts)

        # Stacked Column Chart (Gender vs Churn)
        st.subheader("Gender vs Churn")
        gender_churn = pd.crosstab(df['gender'], df['Churn'])
        gender_churn.plot(kind='bar', stacked=True)
        st.pyplot(plt)

        # Line Chart (Monthly Charges over Tenure)
        st.subheader("Monthly Charges vs. Tenure")
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x='tenure', y='MonthlyCharges', hue='Churn', ax=ax)
        ax.set_title("Monthly Charges vs. Tenure")
        st.pyplot(fig)

        # Pie Chart (Churn Distribution)
        st.subheader("Churn Distribution")
        churn_distribution = df['Churn'].value_counts()
        plt.figure()
        plt.pie(churn_distribution, labels=churn_distribution.index, autopct='%1.1f%%', startangle=140)
        plt.title("Churn Distribution")
        st.pyplot(plt)

        # Bar Chart (Churn Count by Internet Service)
        st.subheader("Churn Count by Internet Service")
        internet_churn = df.groupby('InternetService')['Churn'].value_counts().unstack().fillna(0)
        st.bar_chart(internet_churn)

        # Bar Chart (Churn Count by Contract Type)
        st.subheader("Churn Count by Contract Type")
        churn_contract = df.groupby('Contract')['Churn'].value_counts().unstack().fillna(0)
        st.bar_chart(churn_contract)

    elif page == "KPIs":
        st.title("Key Performance Indicators (KPIs)")

        # Convert Churn to numeric
        df['Churn'] = pd.to_numeric(df['Churn'], errors='coerce')

        # Calculate KPIs
        total_customers = df.shape[0]
        churn_rate = df['Churn'].mean() * 100

        total_male = df[df['gender'] == 'Male'].shape[0]
        st.metric(label="Total Male", value=total_male)

        total_female = df[df['gender'] == 'Female'].shape[0]
        st.metric(label="Total Female", value=total_female)
        
        senior_citizen = df[df['SeniorCitizen'] == 1].shape[0]
        st.metric(label="Senior Citizen", value=senior_citizen)

        junior_citizen = df[df['SeniorCitizen'] == 0].shape[0]
        st.metric(label="Junior Citizen", value=junior_citizen)

# Call the run function when the script is executed
if __name__ == "__main__":
    run()
