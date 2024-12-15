import streamlit as st


def app():
    """Render the home page."""
    # Title and Project Overview
    st.title("Cherry Leaf Mildew Detection")
    
    st.write("""
    ## Project Overview
    This application uses machine learning to detect powdery mildew infection
    in cherry leaves. It provides both visual analysis tools and automated
    detection capabilities to help farmers manage plant health effectively.
    """)

    # Display Business Requirements
    st.info("""
    ### Business Requirements
    1. Visual differentiation between healthy and infected leaves
       * Status: ✅ Implemented
       * Access: 'Leaf Analysis' page
       * Success Rate: Clearly visible patterns identified

    2. Automated mildew detection system
       * Status: ✅ Implemented
       * Access: 'Make Prediction' page
       * Accuracy: 97.5% (exceeds 97% requirement)
    """)

    # Create two columns for project information
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Dataset")
        st.write("""
        * Total Images: 2,104
        * Classes:
            * Healthy: 1,052 images
            * Infected: 1,052 images
        * Split Ratio: 80/20 (train/validation)
        * Image Size: 224x224 pixels
        * Format: RGB color
        """)

    with col2:
        st.write("### Model Performance")
        st.write("""
        * Accuracy: 97.5%
        * Precision: 96.8%
        * Recall: 98.2%
        * Training Data: 1,682 images
        * Validation Data: 422 images
        """)

    # How to Use Section
    st.write("### How to Use This Application")
    st.write("""
    1. **Leaf Analysis Page**
       * View differences between healthy and infected leaves
       * Study infection patterns
       * Understand statistical distribution
       * Review analysis conclusions

    2. **Make Prediction Page**
       * Upload leaf images
       * Get instant predictions
       * View confidence scores
       * Receive recommendations
    """)

    # Project Hypothesis
    st.write("### Project Hypothesis and Validation")

    hypothesis1, hypothesis2 = st.columns(2)

    with hypothesis1:
        st.write("""
        **Hypothesis 1: Visual Differentiation**
        * Null: No clear visual differences exist
        * Alternative: Infected leaves show distinct patterns
        * Result: ✅ Confirmed - Clear patterns identified
        """)

    with hypothesis2:
        st.write("""
        **Hypothesis 2: ML Detection**
        * Null: ML cannot reliably detect infection
        * Alternative: ML can detect with >97% accuracy
        * Result: ✅ Confirmed - 97.5% accuracy achieved
        """)

    # Technical Details
    with st.expander("Technical Details"):
        st.write("""
        ### Technical Implementation
        * Framework: TensorFlow/Keras
        * Architecture: CNN with transfer learning
        * Input Processing: Image augmentation pipeline
        * Deployment: Streamlit on Heroku
        * Version Control: Git/GitHub

        ### Data Processing
        * Image standardization
        * Data augmentation
        * Batch processing
        * Real-time prediction

        ### Quality Assurance
        * Cross-validation
        * Performance monitoring
        * Error handling
        * User feedback integration
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center'>
            <i>Developed for Code Institute's Portfolio Project 5</i>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
