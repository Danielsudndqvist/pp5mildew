import streamlit as st
import plotly.express as px
import numpy as np


def app():
    """Render the visualization page."""
    st.title("Leaf Analysis Study")
    st.write("Analysis of differences between healthy and infected leaves.")

    tabs = st.tabs([
        "Statistical Analysis",
        "Feature Distribution",
        "Pattern Analysis"
    ])

    with tabs[0]:
        show_statistical_analysis()
    with tabs[1]:
        show_feature_distribution()
    with tabs[2]:
        show_pattern_analysis()


def show_statistical_analysis():
    """Show statistical analysis of leaf features."""
    st.write("### Statistical Analysis")

    # Generate example data
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


def show_feature_distribution():
    """Show distribution of features."""
    st.write("### Feature Distribution")
    data = np.random.normal(0.5, 0.15, 100)

    fig = px.histogram(
        data,
        title="Feature Values",
        labels={'value': 'Feature Value', 'count': 'Frequency'},
        opacity=0.7
    )
    st.plotly_chart(fig)


def show_pattern_analysis():
    """Show analysis of patterns."""
    st.write("### Pattern Analysis")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pattern Size", "2.3 mm", delta="0.2 mm")
    with col2:
        st.metric("Density", "60%", delta="5%")
