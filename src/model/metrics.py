import json
import os
from datetime import datetime


class MetricsTracker:
    """Track and store model performance metrics."""

    def __init__(self, metrics_file='metrics/model_metrics.json'):
        """Initialize metrics tracker."""
        self.metrics_file = metrics_file
        self.metrics = self._load_metrics()
        os.makedirs('metrics', exist_ok=True)

    def _load_metrics(self):
        """Load metrics from file or initialize new metrics."""
        if os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        return {
            'confusion_matrix': [[0, 0], [0, 0]],
            'accuracy': 0,
            'precision': 0,
            'recall': 0,
            'history': []
        }

    def update_metrics(self, true_label, predicted_label, confidence):
        """Update metrics with new prediction."""
        self.metrics['confusion_matrix'][true_label][predicted_label] += 1
        self._calculate_metrics()
        self.metrics['history'].append({
            'timestamp': datetime.now().isoformat(),
            'accuracy': self.metrics['accuracy'],
            'precision': self.metrics['precision'],
            'recall': self.metrics['recall'],
            'confidence': confidence
        })
        self._save_metrics()

    def _calculate_metrics(self):
        """Calculate performance metrics from confusion matrix."""
        cm = self.metrics['confusion_matrix']
        total = sum(sum(row) for row in cm)
        correct = cm[0][0] + cm[1][1]
        self.metrics['accuracy'] = correct / total if total > 0 else 0
        self.metrics['precision'] = (
            cm[1][1] / (cm[1][1] + cm[0][1])
            if (cm[1][1] + cm[0][1]) > 0 else 0
        )
        self.metrics['recall'] = (
            cm[1][1] / (cm[1][1] + cm[1][0])
            if (cm[1][1] + cm[1][0]) > 0 else 0
        )

    def _save_metrics(self):
        """Save metrics to file."""
        with open(self.metrics_file, 'w') as f:
            json.dump(self.metrics, f, indent=4)

    def get_metrics(self):
        """Return current metrics."""
        return self.metrics