import streamlit as st

def app():
    """Home page with project overview"""
    st.title("Cherry Leaf Mildew Detection")
    
    st.write("### Project Overview")
    st.info("""
        This application uses machine learning to detect powdery mildew infection in cherry leaves.
    """)
    
    st.write("### How to Use")
    st.write("""
        1. Navigate to 'Prediction' to analyze a leaf image
        2. Check 'Visualization' to see data insights
        3. View 'Model Info' for performance metrics
    """)

if __name__ == "__main__":
    app()