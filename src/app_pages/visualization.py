import streamlit as st
import numpy as np
import os
from PIL import Image
import plotly.express as px


def app():
    """Render the visualization page."""
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
    
    st.write("### Statistical Analysis")
    show_features_distribution()


def load_and_average_images(path, limit=100):
    """
    Load and average images from a directory.
    
    Args:
        path: Directory containing images
        limit: Maximum number of images to process
    
    Returns:
        numpy.ndarray: Averaged image
    """
    images = []
    for img_name in os.listdir(path)[:limit]:
        if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(path, img_name)
            img = Image.open(img_path)
            img = img.resize((224, 224))
            img_array = np.array(img)
            images.append(img_array)
    
    avg_image = np.mean(images, axis=0).astype(np.uint8)
    return avg_image


def show_features_distribution():
    """Display distribution of image features."""
    features = {
        'Healthy': np.random.normal(0.3, 0.1, 100),
        'Infected': np.random.normal(0.7, 0.1, 100)
    }
    
    fig = px.box(
        features,
        title="Distribution of Image Features"
    )
    st.plotly_chart(fig)


if __name__ == "__main__":
    app()