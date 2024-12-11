import streamlit as st
from PIL import Image
import numpy as np
from src.model.prediction import predict_mildew
from src.utils.logger_config import logger

def app():
    st.title("Leaf Disease Prediction")
    
    try:
        uploaded_file = st.file_uploader("Upload a cherry leaf image", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file:
            # Display image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Add prediction button with loading state
            if st.button("Analyze Image"):
                with st.spinner("Analyzing..."):
                    try:
                        result, confidence, metrics = predict_mildew(image)
                        
                        # Display results
                        if result == "Mildew Detected":
                            st.error(f"🔴 {result}")
                        else:
                            st.success(f"✅ {result}")
                            
                        st.write(f"Confidence: {confidence:.2%}")
                        
                        # Display recommendations
                        st.write("### Recommendations")
                        if result == "Mildew Detected":
                            st.write("""
                                - Isolate infected plants
                                - Consider fungicide treatment
                                - Improve air circulation
                                - Monitor surrounding plants
                            """)
                        else:
                            st.write("""
                                - Continue regular monitoring
                                - Maintain good ventilation
                                - Practice preventive care
                            """)
                            
                    except Exception as e:
                        logger.error(f"Prediction error: {str(e)}")
                        st.error("Error analyzing image. Please try again.")
                        
    except Exception as e:
        logger.error(f"App error: {str(e)}")
        st.error("An error occurred. Please refresh the page and try again.")