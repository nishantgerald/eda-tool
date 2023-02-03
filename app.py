import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64

# Set page configuration
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto")

# Set footer to not display
st.markdown("""
<style>
footer {
display: none;
}
</style>
""", unsafe_allow_html=True)

# Select option from the menu in the sidebar
menu = ["Upload", "Metadata"]
choice = st.sidebar.selectbox("Select an option", menu)

# Upload file and read it into a Pandas dataframe
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"], key='file')
data = None
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

def main():
    if choice == "Upload":
        # Show data upload & view page
        st.title("Upload & View Data")
        if data is None:
            st.write("No data loaded.")
            return
        show_dataframe = st.checkbox("Show dataframe", value=True)
        if show_dataframe:
            search_term = st.text_input("Search Term")
            filtered_data = data[data.apply(lambda row: any([search_term.lower() in str(cell).lower() for cell in row]), axis=1)]
            st.dataframe(filtered_data, width=1600, height=800)

    if choice == "Metadata":
        # Show metadata page
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
        unique_values_count = [len(data[col].unique()) for col in data.columns]
        st.write(unique_values_count)
        # Show most frequent values
        st.write("Most frequent values:")
        most_frequent_values = [data[col].value_counts().head(5) for col in data.columns]
        st.write(most_frequent_values)


if __name__ == "__main__":
    main()
