import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def get_line_plot(data):
    '''
    This function displays a line plot.

    Input: data (Pandas dataframe): data to display line plot for
    Output: None
    '''
    show_line_plot = st.checkbox("Show line plot", value=False)
    if show_line_plot:
        st.subheader("Line Plot")
        x_axis_col = st.selectbox("Select X-axis column", data.columns)
        y_axis_col = st.selectbox("Select Y-axis column", data.columns)
        if x_axis_col and y_axis_col:
            x = data[x_axis_col]
            y = data[y_axis_col]
            st.line_chart(data=data, x=x_axis_col, y=y_axis_col)

def show_histogram(data):
    '''
    This function displays a histogram.

    Input: data (Pandas dataframe): data to display histogram for
    Output: None
    '''
    show_histogram = st.checkbox("Show histogram", value=False)
    if show_histogram:
        st.subheader("Histogram")
        column = st.selectbox("Select column", data.columns)
        if column:
            fig = px.histogram(data, x=column, title="Histogram", nbins=None)
            st.plotly_chart(fig)
