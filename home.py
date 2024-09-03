import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    layout="wide"
)

# Main app content after login
def run():
    st.title("Home Page")
    st.write("Welcome to the Home page!")

    st.title("Telco Customer Churn Prediction")
    st.write("""
    Welcome to the Telco Customer Churn Prediction App! This tool allows you to analyze customer data and predict the likelihood of churn. 
    The Telco Customer Churn Prediction App is designed to help Telco identify customers who are likely to leave their service.
    By predicting churn, Telco can take proactive measures to retain customers and improve overall satisfaction.
    """)

    st.image("download.jpeg", caption="Predicting Customer Churn", width=700)

    st.markdown("### Instructions for Users")
    st.write("### How to Use the App")
    st.write("""
    1. Navigate to the 'Prediction' tab.
    2. Input customer data such as tenure, monthly charges, etc.
    3. Click 'Predict' to see if the customer is likely to churn.
    4. Review the results and take action accordingly.
    """)

    st.subheader("Overview")
    st.markdown("""
    - **Data Exploration:** Check the customer data and gain insights into it from the Data page.
    - **Churn Prediction:** Use the trained model to predict customer churn.
    - **Visualization:** See the important metrics and trends on the Dashboard on the Dashboard page.
    """)

    st.write("### Need Help?")
    st.write("If you have any questions or need support, please reach out to me at [oyewalecharles6@gmail.com]")

    if st.button("Learn More"):
        st.write("Visit my GitHub Repository for more in-depth articles and Full Analysis on Telco customer churn.")
        st.markdown("[Go to Blog](https://github.com/Omooyeni/Telco-Customer-churn-prediction-/blob/main/notebook/main.ipynb)")

# Call the run function when the script is executed
if __name__ == "__main__":
    run()
