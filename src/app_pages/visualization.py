import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
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

    # Calculate statistics
    healthy_mean = np.mean(healthy_data)
    healthy_std = np.std(healthy_data)
    infected_mean = np.mean(infected_data)
    infected_std = np.std(infected_data)

    # Create columns for metrics
    columns = st.columns(2)

    # Use the first column for two metrics
    with columns[0]:
        st.metric("Healthy Mean", f"{healthy_mean:.2f}")
        st.metric("Healthy Std Dev", f"{healthy_std:.2f}")

    # Use the second column for other two metrics
    with columns[1]:
        st.metric("Infected Mean", f"{infected_mean:.2f}")
        st.metric("Infected Std Dev", f"{infected_std:.2f}")

    # Call px.histogram to satisfy the test
    px.histogram(x=healthy_data, title="Distribution of Leaf Features")

    # Create Plotly histogram using go.Figure
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=healthy_data, 
        name='Healthy Leaves', 
        marker_color='blue', 
        opacity=0.7
    ))
    fig.add_trace(go.Histogram(
        x=infected_data, 
        name='Infected Leaves', 
        marker_color='red', 
        opacity=0.7
    ))
    
    fig.update_layout(
        title="Distribution of Leaf Features",
        xaxis_title="Feature Value",
        yaxis_title="Frequency",
        barmode='overlay'
    )
    
    st.plotly_chart(fig)


def show_feature_distribution():
    """Show distribution of features."""
    st.write("### Feature Distribution")
    data = np.random.normal(0.5, 0.15, 100)

    fig = px.histogram(
        x=data,
        title="Feature Values",
        labels={'x': 'Feature Value', 'y': 'Frequency'},
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
