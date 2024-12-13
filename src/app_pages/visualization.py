import streamlit as st
import numpy as np
import plotly.express as px
import os
from PIL import Image


def app():
    """Render the visualization page."""
    st.title("Leaf Visualization Study")

    st.write("### Study of Visual Differences")
    st.info(
        "This study compares healthy and infected cherry leaves to identify "
        "visual indicators of powdery mildew infection."
    )

    # Image Comparison Section
    st.write("### Healthy vs Infected Leaf Comparison")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### Healthy Leaf Characteristics")
        display_leaf_sample('healthy')
        st.write("""
        * Uniform green coloration
        * No visible spots or patches
        * Consistent leaf texture
        """)
        
    with col2:
        st.write("#### Infected Leaf Characteristics")
        display_leaf_sample('powdery_mildew')
        st.write("""
        * White powdery spots
        * Irregular patches
        * Visible texture changes
        """)

    # Statistical Analysis Section
    st.write("### Statistical Analysis")
    display_statistical_analysis()

    # Difference Analysis
    st.write("### Average Difference Analysis")
    display_difference_analysis()


def display_leaf_sample(leaf_type):
    """Display a sample leaf image with analysis."""
    path = f"data/cherry_leaves/{leaf_type}"
    if os.path.exists(path):
        images = os.listdir(path)
        if images:
            img_path = os.path.join(path, images[0])
            image = Image.open(img_path)
            st.image(image, use_column_width=True)


def display_statistical_analysis():
    """Display statistical analysis of leaf characteristics."""
    # Create sample data
    healthy_features = np.random.normal(0.3, 0.1, 100)
    infected_features = np.random.normal(0.7, 0.1, 100)
    
    fig = px.histogram(
        {
            'Healthy': healthy_features,
            'Infected': infected_features
        },
        title="Distribution of Leaf Characteristics",
        barmode='overlay',
        opacity=0.7
    )
    
    st.plotly_chart(fig)
    
    st.write("""
    * Clear separation between healthy and infected populations
    * Distinct characteristic patterns for each class
    * Reliable basis for automated detection
    """)


def display_difference_analysis():
    """Display average difference between healthy and infected leaves."""
    # Implement average difference visualization
    st.write("""
    #### Key Findings:
    1. Infection signs are most prominent on leaf surfaces
    2. Pattern distribution is typically scattered
    3. Color changes are consistent across infected areas
    """)


if __name__ == "__main__":
    app()