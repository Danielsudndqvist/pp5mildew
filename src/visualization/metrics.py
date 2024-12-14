import plotly.express as px
import pandas as pd


def plot_metrics_history(metrics_history):
    """Plot metrics history using plotly."""
    df = pd.DataFrame(metrics_history)
    fig = px.line(
        df,
        x='timestamp',
        y=['accuracy', 'precision', 'recall'],
        title='Model Metrics Over Time'
    )
    return fig


def plot_confusion_matrix(confusion_matrix):
    """Plot confusion matrix using plotly."""
    labels = ['Healthy', 'Infected']
    fig = px.imshow(
        confusion_matrix,
        x=labels,
        y=labels,
        color_continuous_scale='Blues',
        title='Confusion Matrix'
    )
    return fig
