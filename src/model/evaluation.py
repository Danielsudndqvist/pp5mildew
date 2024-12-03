import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import json
import os

def evaluate_model_performance(y_true, y_pred, y_prob):
    """
    Evaluate model performance and save metrics
    """
    # Calculate metrics
    conf_matrix = confusion_matrix(y_true, y_pred)
    class_report = classification_report(y_true, y_pred, output_dict=True)
    
    # Save metrics to JSON
    metrics = {
        'accuracy': class_report['accuracy'],
        'healthy_precision': class_report['0']['precision'],
        'healthy_recall': class_report['0']['recall'],
        'mildew_precision': class_report['1']['precision'],
        'mildew_recall': class_report['1']['recall']
    }
    
    # Create outputs directory if it doesn't exist
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    
    # Save metrics
    with open('outputs/model_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    
    # Generate confusion matrix plot
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Healthy', 'Mildew'],
                yticklabels=['Healthy', 'Mildew'])
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig('outputs/confusion_matrix.png')
    plt.close()
    
    return metrics