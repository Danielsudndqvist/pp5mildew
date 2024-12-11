import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def plot_confusion_matrix(conf_matrix):
    """Create confusion matrix visualization."""
    fig = px.imshow(
        conf_matrix,
        labels=dict(x="Predicted", y="Actual"),
        x=['Healthy', 'Mildew'],
        y=['Healthy', 'Mildew'],
        text=conf_matrix,
        aspect="auto",
        title="Confusion Matrix"
    )
    return fig


def plot_metrics_history(metrics_history):
    """Create metrics history visualization."""
    df = pd.DataFrame(metrics_history)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['accuracy'], name='Accuracy'))
    fig.add_trace(go.Scatter(x=df.index, y=df['precision'], name='Precision'))
    fig.add_trace(go.Scatter(x=df.index, y=df['recall'], name='Recall'))
    
    fig.update_layout(
        title="Model Performance Metrics Over Time",
        xaxis_title="Prediction Count",
        yaxis_title="Score",
        yaxis_range=[0, 1]
    )
    return fig