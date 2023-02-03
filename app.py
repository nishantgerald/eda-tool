import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto")

st.markdown("""
<style>
footer {
display: none;
}
</style>
""", unsafe_allow_html=True)

menu = ["Upload", "Metadata"]
choice = st.sidebar.selectbox("Select an option", menu)

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"], key='file')
data = None
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

def main():
    if choice == "Upload":
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
        st.title("Metadata")
        if data is None:
            st.write("No data loaded.")
            return
        st.write("Number of rows:", data.shape[0])
        st.write("Number of columns:", data.shape[1])
        st.write("Summary statistics:")
        st.write(data.describe())
        st.write("Missing values count:")
        st.write(data.isna().sum())
        st.write("Unique values count:")
        unique_values_count = [len(data[col].unique()) for col in data.columns]
        st.write(unique_values_count)
        st.write("Most frequent values:")
        most_frequent_values = [data[col].value_counts().head(5) for col in data.columns]
        st.write(most_frequent_values)


if __name__ == "__main__":
    main()
