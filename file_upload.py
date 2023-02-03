import pandas as pd
import streamlit as st

def upload_file():
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "tsv", "json", "xlsx", "xml"], key='file')
    data = None
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "csv":
            data = pd.read_csv(uploaded_file)
        elif file_extension == "tsv":
            data = pd.read_csv(uploaded_file, sep="\t")
        elif file_extension == "json":
            data = pd.read_json(uploaded_file)
        elif file_extension == "xlsx":
            data = pd.read_excel(uploaded_file)
        elif file_extension == "xml":
            # You will need to install the 'xmltodict' library to read XML files
            import xmltodict
            with uploaded_file as file:
                data = pd.DataFrame.from_dict(xmltodict.parse(file.read()))

    return data
