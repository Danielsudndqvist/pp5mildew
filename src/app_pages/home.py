import streamlit as st

def page_home_body():
    st.write("# Cherry Leaf Mildew Detection")
    
    st.write("""
    ## Business Requirements
    1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew
    2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew
    
    ## Dataset
    * The dataset contains 4208 images taken from the client's crop fields
    * Balanced dataset with 2104 healthy leaf images and 2104 powdery mildew images
    * High quality images of cherry leaves
    
    ## Project Summary
    This project provides:
    * Data visualization and analysis of cherry leaf images
    * Machine learning model for detecting powdery mildew
    * User-friendly interface for instant predictions
    """)