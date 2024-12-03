# app_pages/prediction.py

import streamlit as st
from PIL import Image
import numpy as np
from src.utils.validation import validate_image
from src.utils.logger import logger

def handle_prediction(image):
    """Handle the prediction process with error handling"""
    try:
        # Load model (with error handling)
        try:
            model = load_model()
        except Exception as e:
            logger.error(f"Model loading error: {str(e)}")
            st.error("Error loading the model. Please try again later.")
            return

        # Process image
        try:
            processed_image = process_image(image)
        except Exception as e:
            logger.error(f"Image processing error: {str(e)}")
            st.error("Error processing the image. Please try a different image.")
            return

        # Make prediction
        try:
            with st.spinner("Analyzing image..."):
                prediction, confidence = make_prediction(model, processed_image)
            
            # Display results
            display_prediction_results(prediction, confidence)
            
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            st.error("Error making prediction. Please try again.")
            
    except Exception as e:
        logger.error(f"Unexpected error in prediction handler: {str(e)}")
        st.error("An unexpected error occurred. Please try again later.")

def page_prediction_body():
    st.write("# Leaf Disease Prediction")
    
    st.info(
        "Upload a cherry leaf image to detect if it's healthy or infected with powdery mildew."
    )
    
    uploaded_file = st.file_uploader(
        "Upload a cherry leaf image",
        type=['png', 'jpg', 'jpeg']
    )
    
    if uploaded_file is not None:
        # Validate image
        is_valid, error_message = validate_image(uploaded_file)
        
        if not is_valid:
            st.error(error_message)
            return
            
        # Display image
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
        except Exception as e:
            logger.error(f"Error displaying image: {str(e)}")
            st.error("Error displaying the image. Please try a different image.")
            return
            
        # Prediction button
        if st.button("Make Prediction"):
            handle_prediction(image)
            
def display_prediction_results(prediction, confidence):
    """Display prediction results with formatting"""
    st.write("## Results:")
    
    if prediction == 1:
        st.error("🔴 Powdery Mildew Detected")
        severity = "High" if confidence > 0.9 else "Moderate"
        st.write(f"Severity: {severity}")
    else:
        st.success("✅ Healthy Leaf")
        
    st.write(f"Confidence: {confidence*100:.2f}%")
    
    # Additional information
    with st.expander("What does this mean?"):
        if prediction == 1:
            st.write("""
            ### Recommendations:
            1. Isolate infected plants to prevent spread
            2. Consider fungicide treatment
            3. Monitor surrounding plants
            4. Improve air circulation
            """)
        else:
            st.write("""
            ### Maintenance Tips:
            1. Continue regular monitoring
            2. Maintain good air circulation
            3. Avoid overhead watering
            """)