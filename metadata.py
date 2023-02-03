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

    # Show number of rows
    st.write("Number of rows:", data.shape[0])

    # Show number of columns
    st.write("Number of columns:", data.shape[1])

    # Show summary statistics
    st.write("Summary statistics:")
    st.write(data.describe())

    # Show missing values count
    st.write("Missing values count:")
    st.write(data.isna().sum())

    # Show unique values count
    st.write("Unique values count:")
    unique_values_count = {col: len(data[col].unique()) for col in data.columns}
    st.dataframe(pd.DataFrame(list(unique_values_count.items()), columns=["Column", "Unique Count"]))

    # Show most frequent values
    st.write("Most frequent values:")
    most_frequent_values = {col: data[col].value_counts().head(1).reset_index().rename(columns={'index':'value', col:'count'}) for col in data.columns}
    most_frequent_values_df = pd.concat(most_frequent_values.values(), keys=most_frequent_values.keys(), axis=1)
    st.dataframe(most_frequent_values_df.T)
