import streamlit as st
from PIL import Image
import numpy as np
from src.data_management import load_images_data
import torch
from torchvision import transforms

def load_model():
    """
    Load the trained model
    """
    model = torch.load('outputs/model.pth', map_location=torch.device('cpu'))
    model.eval()
    return model

def process_image(image):
    """
    Process uploaded image for prediction
    """
    # Define the same transforms used during training
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
    ])
    
    image = transform(image).unsqueeze(0)
    return image

def page_prediction_body():
    st.write("# Leaf Disease Prediction")
    
    st.info(
        "This page allows you to upload a cherry leaf image "
        "and get a prediction on whether it's healthy or infected with powdery mildew."
    )
    
    uploaded_file = st.file_uploader("Upload a cherry leaf image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Make Prediction"):
            # Load model
            model = load_model()
            
            # Process image
            processed_image = process_image(image)
            
            # Make prediction
            with torch.no_grad():
                output = model(processed_image)
                prediction = torch.argmax(output, dim=1).item()
                confidence = torch.nn.functional.softmax(output, dim=1)[0]
                
            # Display results
            st.write("## Results:")
            if prediction == 1:
                st.error("🔴 Powdery Mildew Detected")
            else:
                st.success("✅ Healthy Leaf")
                
            st.write(f"Confidence: {confidence[prediction].item()*100:.2f}%")
            
            # Additional information
            st.write(
                "### What to do next?\n"
                "* If mildew is detected, consider treatment options\n"
                "* Regular monitoring is recommended\n"
                "* Consider checking surrounding trees"
            )