import streamlit as st

def run():
    st.title("History Page")
    st.write("This page shows the history of customer churn predictions.")

    st.markdown("### Overview")
    st.write("""
    On this page, you can view the historical predictions that have been made using the Telco Customer Churn Prediction app.
    This information can help you analyze past predictions and make data-driven decisions.
    """)

    st.markdown("### Past Predictions")
    st.write("""
    The predictions made through this app are recorded here. You can track the customer ID, input features, and the prediction result.
    This history allows you to review and validate the model's performance over time.
    """)

    st.write("The data shown above is for demonstration purposes. In a live application, you would retrieve and display real historical data.")
    
    st.write("For more detailed analysis, you can download the history as a CSV file and conduct further analysis on your local machine.")

    # Add a download button for the CSV 
    if st.button("Download History as CSV"):
        st.write("Downloading history... (this is a placeholder action)")

# Call the run function when the script is executed
if __name__ == "__main__":
    run()
