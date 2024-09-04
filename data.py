import streamlit as st
import pandas as pd

def run():
    st.title("Data Page")
    st.write("This is the Data Page where you can explore, view, and download the data used to train the models.")

    # Load the dataset from the csv file
    @st.cache_data
    def load_data():
        df = pd.read_csv("https://raw.githubusercontent.com/Omooyeni/Embedding-ML-models-in-GUI/main/Data/dataset.csv")
        return df

    df = load_data()

    # Display the raw data
    st.subheader("Raw Data")
    st.write(df)

    # Show basic statistics
    st.subheader("Data Statistics")
    st.write(df.describe())

    # Filter data by a specific column (e.g., customer ID, tenure, etc.)
    st.subheader("Filter Data")
    selected_column = st.selectbox("Select a column to filter by:", df.columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value:", unique_values)
    
    filtered_data = df[df[selected_column] == selected_value]
    st.write(filtered_data)

# Call the run function when the script is executed
if __name__ == "__main__":
    run()
