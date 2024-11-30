import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

def load_model():
    try:
        model = tf.keras.models.load_model('models/mildew_detector.h5')
        return model
    except:
        st.error("Model not found. Please ensure the model is trained and saved.")
        return None

def preprocess_image(img):
    img = img.resize((224, 224))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def page_prediction_body():
    st.write("# Leaf Analysis")
    
    st.write("""
    Upload a cherry leaf image to detect if it's healthy or infected with powdery mildew.
    """)
    
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        model = load_model()
        if model:
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            
            st.write("## Results:")
            if prediction[0] > 0.5:
                st.error("🔴 Powdery Mildew Detected")
                confidence = prediction[0][0] * 100
            else:
                st.success("🟢 Healthy Leaf")
                confidence = (1 - prediction[0][0]) * 100
            
            st.write(f"Confidence: {confidence:.2f}%")