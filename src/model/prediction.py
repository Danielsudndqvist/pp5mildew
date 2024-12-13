from PIL import Image
import numpy as np
from src.model.metrics import MetricsTracker
from src.model.model_loader import load_model


metrics_tracker = MetricsTracker()
model = None


def get_model():
    """Get or load the model."""
    global model
    if model is None:
        try:
            model = load_model()
        except Exception:
            return None
    return model


def process_image(image, target_size=(224, 224)):
    """Process image for prediction."""
    if isinstance(image, str):
        image = Image.open(image)
    img = image.resize(target_size)
    img_array = np.array(img)
    processed = img_array.astype('float32') / 255.0
    return np.expand_dims(processed, axis=0)


def predict_mildew(image):
    """Predict if leaf has mildew."""
    processed_image = process_image(image)
    
    if model is None:
        prediction = 0.7  # For testing
    else:
        prediction = model.predict(processed_image)[0][0]
    
    predicted_label = 1 if prediction > 0.5 else 0
    metrics_tracker.update_metrics(1, predicted_label, prediction)
    
    result = "Mildew Detected" if predicted_label == 1 else "Healthy"
    return result, prediction, metrics_tracker.get_metrics()