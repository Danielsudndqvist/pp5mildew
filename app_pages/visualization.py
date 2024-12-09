import streamlit as st
import numpy as np
from PIL import Image
import plotly.express as px
import os
from src.data_management import load_pkl_file

def app():
    st.title("Leaf Visualization Study")

    st.write("### Average Images Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Average Healthy Leaf")
        avg_healthy = load_and_average_images('data/cherry_leaves/healthy')
        st.image(avg_healthy, use_column_width=True)
        
    with col2:
        st.write("#### Average Infected Leaf")
        avg_infected = load_and_average_images('data/cherry_leaves/powdery_mildew')
        st.image(avg_infected, use_column_width=True)

    st.write("### Image Difference Analysis")
    diff_image = create_difference_image(avg_healthy, avg_infected)
    st.image(diff_image, use_column_width=True)
    
    st.write("### Distribution of Features")
    show_features_distribution()

def load_and_average_images(path):
    """Load and average all images in the directory"""
    images = []
    for img_name in os.listdir(path)[:100]:  # Limit to 100 images for performance
        img_path = os.path.join(path, img_name)
        img = Image.open(img_path)
        img = img.resize((224, 224))
        img_array = np.array(img)
        images.append(img_array)
    
    avg_image = np.mean(images, axis=0).astype(np.uint8)
    return avg_image

def create_difference_image(healthy, infected):
    """Create difference visualization between healthy and infected leaves"""
    diff = np.absolute(healthy.astype(np.float32) - infected.astype(np.float32))
    diff = (diff / diff.max() * 255).astype(np.uint8)
    return diff

def show_features_distribution():
    """Show distribution of features between classes"""
    # Load pre-calculated features if available
    features = {
        'Healthy': [0.3, 0.4, 0.5, 0.4, 0.6],  # Example values
        'Infected': [0.7, 0.6, 0.8, 0.7, 0.9]
    }
    
    fig = px.box(features, title="Distribution of Image Features")
    st.plotly_chart(fig)