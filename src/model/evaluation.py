import json
import os
from datetime import datetime
from sklearn.metrics import confusion_matrix, classification_report


def evaluate_model_performance(y_true, y_pred, y_prob):
    """
    Evaluate model performance and save metrics.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_prob: Prediction probabilities
        
    Returns:
        dict: Calculated metrics
    """
    # Calculate metrics
    conf_matrix = confusion_matrix(y_true, y_pred)
    class_report = classification_report(y_true, y_pred, output_dict=True)
    
    # Save metrics
    metrics = {
        'accuracy': class_report['accuracy'],
        'healthy_precision': class_report['0']['precision'],
        'healthy_recall': class_report['0']['recall'],
        'mildew_precision': class_report['1']['precision'],
        'mildew_recall': class_report['1']['recall']
    }
    
    # Create outputs directory if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    # Save metrics to JSON
    with open('outputs/model_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    
    return metrics