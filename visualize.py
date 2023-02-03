import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def get_line_plot(data):
    st.subheader("Line Plot")
    x_axis_col = st.selectbox("Select X-axis column", data.columns)
    y_axis_col = st.selectbox("Select Y-axis column", data.columns)
    if x_axis_col and y_axis_col:
        x = data[x_axis_col]
        y = data[y_axis_col]
        st.line_chart(data=data, x=x_axis_col, y=y_axis_col)

def show_histogram(data):
    st.subheader("Histogram")
    column = st.selectbox("Select column", data.columns)
    # Set bin spacing
    nbins = st.slider("Number of bins", min_value=1, max_value=100, value=10)
    if column:
        fig = px.histogram(data, x=column, title="Histogram", nbins=None)
        st.plotly_chart(fig)
