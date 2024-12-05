import streamlit as st
import numpy as np
from PIL import Image
from src.model.prediction import predict_mildew
import plotly.express as px

def load_model():
    # Add your model loading code here
    return model

def app():
    st.title("Mildew Detection")
    
    uploaded_file = st.file_uploader("Upload leaf image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Predict"):
            model = load_model()
            result, confidence, metrics = predict_mildew(image, model)
            
            # Display prediction
            if result == "Mildew Detected":
                st.error(f"Result: {result}")
            else:
                st.success(f"Result: {result}")
            st.write(f"Confidence: {confidence:.2%}")
            
            # Display metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Accuracy", f"{metrics['accuracy']:.2%}")
            col2.metric("Precision", f"{metrics['precision']:.2%}")
            col3.metric("Recall", f"{metrics['recall']:.2%}")
            
            # Display confusion matrix
            fig = px.imshow(
                metrics['confusion_matrix'],
                labels=dict(x="Predicted", y="Actual"),
                x=['Healthy', 'Mildew'],
                y=['Healthy', 'Mildew']
            )
            st.plotly_chart(fig)