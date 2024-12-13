import streamlit as st


def app():
    """Render the home page."""
    st.title("Cherry Leaf Mildew Detection")

    # Project Overview
    st.write("### Project Overview")
    st.info(
        "This app helps detect powdery mildew infection in cherry leaves "
        "using machine learning techniques."
    )

    # Business Requirements
    st.write("### Business Requirements")
    st.write(
        """
        1. Visual Differentiation Study
        * Create clear visual indicators between healthy and infected leaves
        * Provide statistical analysis of leaf characteristics
        
        2. Automated Detection System
        * Predict leaf condition with 97%+ accuracy
        * Provide confidence scores for predictions
        """
    )

    # Usage Guide
    st.write("### How to Use")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### Prediction")
        st.write("""
        * Navigate to 'Prediction' page
        * Upload a cherry leaf image
        * Get instant analysis results
        """)
    
    with col2:
        st.write("#### Analysis")
        st.write("""
        * Check 'Visualization' page
        * Compare healthy vs infected leaves
        * View statistical analysis
        """)


if __name__ == "__main__":
    app()