import streamlit as st
import plotly.express as px
import pandas as pd
from src.model.metrics import MetricsTracker

def app():
    st.title("Model Performance Analysis")
    
    metrics_tracker = MetricsTracker()
    metrics = metrics_tracker.get_metrics()
    
    # Display overall metrics
    st.write("### Model Performance Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Accuracy", 
                 value=f"{metrics['accuracy']:.2%}")
    with col2:
        st.metric(label="Precision", 
                 value=f"{metrics['precision']:.2%}")
    with col3:
        st.metric(label="Recall", 
                 value=f"{metrics['recall']:.2%}")
    
    # Display confusion matrix
    st.write("### Confusion Matrix")
    conf_matrix = metrics['confusion_matrix']
    fig_cm = px.imshow(conf_matrix,
                      labels=dict(x="Predicted", y="Actual"),
                      x=['Healthy', 'Infected'],
                      y=['Healthy', 'Infected'],
                      text=conf_matrix,
                      color_continuous_scale='RdBu_r')
    st.plotly_chart(fig_cm)
    
    # Display metrics history
    if metrics['history']:
        st.write("### Performance Over Time")
        history_df = pd.DataFrame(metrics['history'])
        fig_history = px.line(history_df, 
                            x='timestamp', 
                            y=['accuracy', 'precision', 'recall'],
                            labels={'value': 'Score', 'variable': 'Metric'})
        st.plotly_chart(fig_history)
        
    # Display technical details
    with st.expander("Technical Details"):
        st.write("""
        - Model Type: Convolutional Neural Network
        - Input Shape: (224, 224, 3)
        - Training Data Split: 80/20
        - Data Augmentation: Horizontal flip, rotation
        """)