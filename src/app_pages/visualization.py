# app_pages/visualization.py

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import pandas as pd
import numpy as np
from src.data_management import load_images_data
import os

def create_probability_distribution(predictions):
    """Create probability distribution plot"""
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(
        x=predictions,
        nbinsx=30,
        name='Predictions',
        opacity=0.75
    ))
    
    fig.update_layout(
        title="Distribution of Prediction Probabilities",
        xaxis_title="Probability of Mildew",
        yaxis_title="Count",
        bargap=0.1
    )
    
    return fig

def create_class_distribution():
    """Create pie chart of class distribution"""
    healthy_path = "inputs/cherry-leaves/healthy"
    mildew_path = "inputs/cherry-leaves/powdery_mildew"
    
    healthy_count = len(os.listdir(healthy_path))
    mildew_count = len(os.listdir(mildew_path))
    
    fig = go.Figure(data=[go.Pie(
        labels=['Healthy', 'Infected'],
        values=[healthy_count, mildew_count],
        hole=.3
    )])
    
    fig.update_layout(title="Dataset Distribution")
    return fig

def page_visualization_body():
    st.write("# Data Visualization")
    
    st.info("""
        Explore the visual patterns that distinguish healthy cherry leaves from those
        infected with powdery mildew. These visualizations help understand the
        characteristics used by the model for classification.
    """)
    
    # Create tabs for different visualizations
    tab_dist, tab_analysis, tab_features = st.tabs([
        "Data Distribution", 
        "Image Analysis",
        "Feature Importance"
    ])
    
    with tab_dist:
        st.write("### Dataset Distribution")
        dist_fig = create_class_distribution()
        st.plotly_chart(dist_fig, use_container_width=True)
        
        st.write("""
        This chart shows the distribution of images in our dataset.
        A balanced distribution helps ensure reliable model training.
        """)
    
    with tab_analysis:
        st.write("### Leaf Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Healthy Leaf Example")
            healthy_img = Image.open("inputs/cherry-leaves/healthy/healthy_1.jpg")
            st.image(healthy_img, use_column_width=True)
        
        with col2:
            st.write("#### Infected Leaf Example")
            infected_img = Image.open("inputs/cherry-leaves/powdery_mildew/powdery_mildew_1.jpg")
            st.image(infected_img, use_column_width=True)
            
        st.write("""
        ### Key Visual Differences:
        1. Color patterns
        2. Texture variations
        3. Visible signs of infection
        """)
    
    with tab_features:
        st.write("### Model Performance Analysis")
        
        # Add confusion matrix visualization
        conf_matrix = np.array([[97, 3], [2, 98]])  # Example values
        fig = px.imshow(
            conf_matrix,
            labels=dict(x="Predicted", y="Actual"),
            x=['Healthy', 'Infected'],
            y=['Healthy', 'Infected'],
            text=conf_matrix,
            aspect="auto",
            title="Confusion Matrix"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("""
        The confusion matrix shows the model's prediction accuracy:
        * True Positives: Correctly identified infected leaves
        * True Negatives: Correctly identified healthy leaves
        * False Positives: Healthy leaves incorrectly classified as infected
        * False Negatives: Infected leaves incorrectly classified as healthy
        """)

if __name__ == "__main__":
    page_visualization_body()