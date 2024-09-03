import streamlit as st

# Import your pages
import home
import data
import dashboard
import history
import Churn_prediction

# Hard-coded credentials 
USERNAME = 'user1'
PASSWORD = 'password1'

# Login function
def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    return False

# Main function to run the app
def main():
    st.title("Telco Customer Churn Prediction App")

    # Create login form
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.session_state['logged_in'] = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")
    else:
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Go to", ["Home", "Data", "Dashboard", "History", "Churn Prediction"])

        if page == "Home":
            home.run()  
        elif page == "Data":
            data.run()
        elif page == "Dashboard":
            dashboard.run()
        elif page == "History":
            history.run()
        elif page == "Churn Prediction":
            Churn_prediction.run()

        # Logout button
        if st.sidebar.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state.clear()  
            st.success("Logged out successfully")

if __name__ == "__main__":
    main()
