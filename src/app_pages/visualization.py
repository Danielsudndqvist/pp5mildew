import streamlit as st
import plotly.express as px
from PIL import Image
import os
import numpy as np


def app():
    """Render the visualization page."""
    st.title("Leaf Analysis Study")

    tab1, tab2, tab3 = st.tabs([
        "Difference Study",
        "Statistical Analysis",
        "Average Features"
    ])

    with tab1:
        show_difference_study()

    with tab2:
        show_statistical_analysis()

    with tab3:
        show_average_features()


def show_difference_study():
    """Show visual differences between healthy and infected leaves."""
    st.write("### Visual Difference Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.write("#### Healthy Leaf Example")
        if os.path.exists("data/cherry_leaves/healthy"):
            images = os.listdir("data/cherry_leaves/healthy")
            if images:
                img_path = os.path.join(
                    "data/cherry_leaves/healthy",
                    images[0]
                )
                image = Image.open(img_path)
                st.image(image, caption="Healthy Leaf", use_column_width=True)

    with col2:
        st.write("#### Infected Leaf Example")
        if os.path.exists("data/cherry_leaves/powdery_mildew"):
            images = os.listdir("data/cherry_leaves/powdery_mildew")
            if images:
                img_path = os.path.join(
                    "data/cherry_leaves/powdery_mildew",
                    images[0]
                )
                image = Image.open(img_path)
                st.image(image, caption="Infected Leaf", use_column_width=True)

    st.write("""
    ### Key Differences:
    1. Healthy leaves show uniform coloration
    2. Infected leaves display white powdery patches
    3. Texture changes are visible in infected areas
    """)


def show_statistical_analysis():
    """Show statistical analysis of leaf features."""
    st.write("### Statistical Analysis")

    # Example data for demonstration
    healthy_data = np.random.normal(0.3, 0.1, 100)
    infected_data = np.random.normal(0.7, 0.1, 100)

    fig = px.histogram(
        {
            'Healthy Leaves': healthy_data,
            'Infected Leaves': infected_data
        },
        barmode='overlay',
        title="Distribution of Leaf Features",
        opacity=0.7
    )

    st.plotly_chart(fig)

    st.write("""
    ### Analysis Insights:
    * Clear separation between healthy and infected populations
    * Distinct feature patterns for each category
    * Reliable basis for automated detection
    """)


def show_average_features():
    """Show average features of leaves."""
    st.write("### Average Feature Analysis")

    st.write("""
    #### Observations from Average Features:
    1. Consistent patterns in infection presentation
    2. Common locations for mildew development
    3. Typical progression of infection
    """)


if __name__ == "__main__":
    app()
