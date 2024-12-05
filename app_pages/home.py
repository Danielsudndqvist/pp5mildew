import streamlit as st

def app():
    st.title("Cherry Leaf Mildew Detection")
    
    st.info("""
        Detect powdery mildew infection in cherry leaves using machine learning.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Quick Project Summary")
        st.write("""
            - Upload cherry leaf images
            - Get instant predictions
            - View model performance metrics
        """)
    
    with col2:
        st.write("### Business Value")
        st.write("""
            - Early detection of infections
            - Reduce crop losses
            - Optimize treatment timing
        """)

    st.write("### How to Use")
    st.write("""
        1. Navigate to 'Make Prediction'
        2. Upload a leaf image
        3. Get instant analysis result
    """)