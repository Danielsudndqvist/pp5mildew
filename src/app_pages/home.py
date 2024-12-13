import streamlit as st


def app():
    """Render the home page."""
    st.title("Cherry Leaf Mildew Detection")

    # Project Overview
    st.write("### Project Overview")
    st.info(
        "This app helps detect powdery mildew infection in cherry leaves using "
        "machine learning techniques."
    )

    # Project Details
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Dataset")
        st.write("""
        * 2104 cherry leaf images
        * Balanced dataset:
            * Healthy leaves
            * Infected leaves
        * Training/Validation split: 80/20
        """)

    with col2:
        st.write("### Predictions")
        st.write("""
        * Real-time analysis
        * 97%+ accuracy
        * Instant visual feedback
        * Treatment recommendations
        """)

    # How to Use
    st.write("### How to Use")
    st.write("""
    1. Navigate to 'Leaf Analysis' to study visual differences
    2. Use 'Make Prediction' to analyze new leaf images
    3. Upload clear images of cherry leaves
    4. Get instant analysis results
    """)


if __name__ == "__main__":
    app()