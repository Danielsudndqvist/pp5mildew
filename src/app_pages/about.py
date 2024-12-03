import streamlit as st

def page_about_body():
    st.write("# About Cherry Leaf Mildew Detector")

    st.info(
        "This project was developed to help farmers and agricultural specialists "
        "identify powdery mildew infection in cherry leaves using machine learning."
    )

    st.write(
        """
        ### Project Overview
        
        This application uses machine learning to detect powdery mildew in cherry leaves 
        with high accuracy. The model was trained on a dataset of over 2,000 images of 
        healthy and infected cherry leaves.
        
        ### Model Performance
        
        The current model achieves:
        * Accuracy: 97%+
        * Precision: 96%+
        * Recall: 96%+
        
        ### How to Use
        
        1. Navigate to the Prediction page
        2. Upload an image of a cherry leaf
        3. Click 'Make Prediction' to get results
        4. View the Visualization page to understand infection patterns
        
        ### Dataset Information
        
        The dataset contains balanced classes of:
        * Healthy cherry leaves
        * Cherry leaves infected with powdery mildew
        
        ### Technologies Used
        
        * Python
        * Streamlit
        * TensorFlow/Keras
        * OpenCV
        * Scikit-learn
        """
    )