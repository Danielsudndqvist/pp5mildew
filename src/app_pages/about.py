import streamlit as st

def page_home_body():
    # Title and Project Overview
    st.write("# Cherry Leaf Mildew Detection")
    st.image("inputs/cherry-leaves/healthy/healthy_1.jpg", caption="Sample Cherry Leaf", use_column_width=True)

    # Project Summary
    st.info("""
        This application helps farmers and agricultural specialists detect 
        powdery mildew infection in cherry leaves using machine learning technology.
    """)

    # Business Requirements
    st.write("""
    ### Business Requirements
    
    The project addresses two main business requirements:
    
    1. **Visual Differentiation Study**: The client wants to visually differentiate 
       between healthy and powdery mildew infected cherry leaves.
       
    2. **Predictive Analysis**: The client requires a tool that can predict 
       whether a cherry leaf is healthy or infected with powdery mildew.
    """)

    # Quick Links Section
    st.write("""
    ### Quick Links
    
    Navigate through the app using the sidebar menu to:
    * **Predict**: Upload and analyze leaf images
    * **Visualize**: Explore data visualizations and patterns
    * **About**: Learn more about the project and model performance
    """)

    # Project Dataset
    with st.expander("Project Dataset Details"):
        st.write("""
        * The dataset contains over 2,000 images of cherry leaves
        * Images are categorized into:
          - Healthy leaves
          - Leaves infected with powdery mildew
        * The dataset is balanced between both classes
        * All images are high quality and suitable for analysis
        """)

    # Technical Details
    with st.expander("Technical Details"):
        st.write("""
        * The model is built using state-of-the-art deep learning techniques
        * Achieves over 97% accuracy in detection
        * Uses image preprocessing for optimal results
        * Provides real-time predictions
        """)

    # Usage Instructions
    with st.expander("How to Use"):
        st.write("""
        1. Select 'Prediction' from the sidebar
        2. Upload an image of a cherry leaf
        3. Click 'Make Prediction'
        4. View the results and confidence score
        5. Use 'Visualization' to understand patterns
        """)

def app():
    page_home_body()

if __name__ == "__main__":
    app()