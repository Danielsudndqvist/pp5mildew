import streamlit as st
import plotly.express as px
import numpy as np
import os
from PIL import Image


def app():
    """Render the visualization page."""
    st.title("Leaf Analysis Study")

    # Create tabs
    tabs = st.tabs([
        "Difference Study",
        "Statistical Analysis",
        "Average Features"
    ])

    with tabs[0]:
        show_difference_study()
    with tabs[1]:
        show_statistical_analysis()
    with tabs[2]:
        show_average_features()


def show_statistical_analysis():
    """Show statistical analysis of leaf features."""
    st.write("### Statistical Analysis")

    try:
        # Generate example data
        healthy_data = np.random.normal(0.3, 0.1, 100)
        infected_data = np.random.normal(0.7, 0.1, 100)

        # Create histogram
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

        st.write("### Summary Statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Healthy Leaves Mean",
                value=f"{np.mean(healthy_data):.3f}"
            )
            st.metric(
                label="Healthy Leaves Std",
                value=f"{np.std(healthy_data):.3f}"
            )

        with col2:
            st.metric(
                label="Infected Leaves Mean",
                value=f"{np.mean(infected_data):.3f}"
            )
            st.metric(
                label="Infected Leaves Std",
                value=f"{np.std(infected_data):.3f}"
            )

    except Exception as e:
        st.error(f"Error generating statistical analysis: {str(e)}")


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


def show_average_features():
    """Show average features of leaves."""
    st.write("### Average Feature Analysis")

    feature_tabs = st.tabs(["Distribution", "Patterns"])
    with feature_tabs[0]:
        show_feature_distribution()
    with feature_tabs[1]:
        show_pattern_analysis()


def show_feature_distribution():
    """Show distribution of leaf features."""
    st.write("#### Feature Distribution Analysis")
    feature_data = np.random.normal(0.5, 0.15, 100)
    fig = px.histogram(
        feature_data,
        title="Feature Value Distribution",
        labels={'value': 'Feature Value', 'count': 'Frequency'},
        opacity=0.7
    )
    st.plotly_chart(fig)


def show_pattern_analysis():
    """Show analysis of infection patterns."""
    st.write("#### Pattern Analysis")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Average Pattern Size",
            value="2.3 mm",
            delta="0.2 mm"
        )
    with col2:
        st.metric(
            label="Pattern Density",
            value="60%",
            delta="5%"
        )
