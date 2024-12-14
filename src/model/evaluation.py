import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def evaluate_model(model, test_images, test_labels):
    """Evaluate model performance."""
    predictions = model.predict(test_images)
    pred_labels = (predictions > 0.5).astype(int)

    # Calculate confusion matrix
    cm = confusion_matrix(test_labels, pred_labels)

    # Calculate metrics
    accuracy = np.sum(pred_labels == test_labels) / len(test_labels)
    precision = cm[1, 1] / (cm[1, 1] + cm[0, 1])
    recall = cm[1, 1] / (cm[1, 1] + cm[1, 0])

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'confusion_matrix': cm
    }


def plot_training_history(history):
    """Plot training history metrics."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Accuracy plot
    ax1.plot(history.history['accuracy'], label='Training')
    ax1.plot(history.history['val_accuracy'], label='Validation')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()

    # Loss plot
    ax2.plot(history.history['loss'], label='Training')
    ax2.plot(history.history['val_loss'], label='Validation')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()

    return fig
