import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
import io

def load_model():
    try:
        return tf.keras.models.load_model('models/mildew_detector.h5')
    except:
        st.error("Model not found. Please train the model first.")
        return None

def preprocess_image(img):
    # Convert to numpy array
    img = np.array(img)
    # Resize
    img = cv2.resize(img, (224, 224))
    # Normalize
    img = img / 255.0
    # Add batch dimension
    img = np.expand_dims(img, axis=0)
    return img

def main():
    st.title("Cherry Leaf Mildew Detection")
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Upload", "About"])
    
    if page == "Home":
        st.write("""
        ## Welcome to Cherry Leaf Mildew Detection
        
        This application helps detect powdery mildew in cherry leaves using machine learning.
        
        ### How to use:
        1. Navigate to the Upload page
        2. Upload a cherry leaf image
        3. Get instant prediction
        """)
        
    elif page == "Upload":
        st.write("## Upload Cherry Leaf Image")
        
        # File uploader
        uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file is not None:
            # Display image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            
            # Load model and make prediction
            model = load_model()
            if model:
                # Make prediction
                processed_image = preprocess_image(image)
                prediction = model.predict(processed_image)
                
                # Display result
                st.write("### Prediction:")
                if prediction[0] > 0.5:
                    st.error("Powdery Mildew Detected!")
                    confidence = prediction[0][0] * 100
                    st.write(f"Confidence: {confidence:.2f}%")
                else:
                    st.success("Healthy Leaf!")
                    confidence = (1 - prediction[0][0]) * 100
                    st.write(f"Confidence: {confidence:.2f}%")
    
    elif page == "About":
        st.write("""
        ## About This Project
        
        This project uses machine learning to detect powdery mildew in cherry leaves.
        
        ### Dataset
        - Total Images: 4208
        - Healthy Leaves: 2104
        - Infected Leaves: 2104
        
        ### Model
        - Architecture: CNN
        - Input Size: 224x224x3
        - Training Accuracy: XX%
        """)

if __name__ == '__main__':
    main()