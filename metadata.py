import streamlit as st
import pandas as pd

def show_metadata(data):
    '''
    This function displays the metadata of the data.

    Input: data (Pandas dataframe): data to display metadata for
    Output: None
    '''
    st.title("Metadata")
    if data is None:
        st.write("No data loaded.")
        return

    # Place number of rows metric and number of columns metric side by side
    col1, col2 = st.columns(2)
    
    # Show number of rows in col1 and number of columns in col2
    with col1:
        # Show number of rows
        st.metric("Number of rows", data.shape[0])

    with col2:
        # Show number of columns
        st.metric("Number of columns", data.shape[1])

    

    # Show summary statistics
    st.subheader("Summary statistics:")
    st.table(data.describe())

    col1, col2, col3 = st.columns(3)
    with col1:
        # Show missing values count
        st.subheader("Missing values count:")
        st.table(data.isna().sum())

    with col2:
        # Show unique values count
        st.subheader("Unique values count:")
        unique_values_count = {col: len(data[col].unique()) for col in data.columns}
        st.table(pd.DataFrame(list(unique_values_count.items()), columns=["Column", "Unique Count"]))

    with col3:
        # Show most frequent values
        st.subheader("Most frequent values:")
        most_frequent_values = {col: data[col].value_counts().head(1).reset_index().rename(columns={'index':'value', col:'count'}) for col in data.columns}
        most_frequent_values_df = pd.concat(most_frequent_values.values(), keys=most_frequent_values.keys(), axis=1)
        st.table(most_frequent_values_df.T)
