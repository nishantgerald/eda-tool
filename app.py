import streamlit as st
from file_upload import upload_file
import metadata as mdata


# Set page configuration
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto")

# CSS
def local_css(file_name):
    '''
    Load local CSS file into Streamlit.
    '''
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("resources/style.css")

# Select option from the menu in the sidebar
menu = ["Upload", "Metadata"]
choice = st.sidebar.selectbox("Select an option", menu)

# Upload file and read it into a Pandas dataframe
data = upload_file()

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
        if data is None:
            st.write("No data loaded.")
            return
        mdata.show_metadata(data)

if __name__ == "__main__":
    main()
