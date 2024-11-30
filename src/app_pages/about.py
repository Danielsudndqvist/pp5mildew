import streamlit as st

def page_about_body():
    st.write("# About")
    
    st.write("""
    ## Project Overview
    This project uses machine learning to help farmers detect powdery mildew
    on cherry leaves, enabling early intervention and crop protection.
    
    ## Model Performance
    * Accuracy: XX%
    * Precision: XX%
    * Recall: XX%
    
    ## Technologies Used
    * Python
    * TensorFlow
    * Streamlit
    * OpenCV
    
    ## Dataset Information
    The dataset consists of 4208 images:
    * 2104 healthy cherry leaf images
    * 2104 powdery mildew infected cherry leaf images
    
    ## Project Impact
    This tool helps farmers:
    * Detect disease early
    * Reduce crop losses
    * Optimize treatment timing
    * Save resources
    """)