import streamlit as st
from src.model.metrics import MetricsTracker


def app():
    """Render the metrics page."""
    st.title("Model Performance Analysis")

    metrics_tracker = MetricsTracker()
    metrics = metrics_tracker.get_metrics()

    # Display overall metrics
    st.write("### Model Performance Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Accuracy",
            value=f"{metrics['accuracy']:.2%}"
        )
    with col2:
        st.metric(
            label="Precision",
            value=f"{metrics['precision']:.2%}"
        )
    with col3:
        st.metric(
            label="Recall",
            value=f"{metrics['recall']:.2%}"
        )


if __name__ == "__main__":
    app()
