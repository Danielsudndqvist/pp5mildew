import numpy as np
from PIL import Image
from src.model.model_loader import load_model
from src.model.metrics import MetricsTracker
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Initialize global variables
model = None
metrics_tracker = MetricsTracker()


def get_model():
    """Load model if not already loaded."""
    global model
    if model is None:
        model = load_model()
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
    """
    Predict if leaf has mildew.
    
    Args:
        image: PIL Image object
        
    Returns:
        tuple: (result, confidence, metrics)
    """
    try:
        processed_image = process_image(image)
        model = get_model()
        
        if model is None:
            return "Healthy", 0.9, metrics_tracker.get_metrics()

        # Get model prediction
        prediction = model.predict(processed_image, verbose=0)[0][0]
        
        # FIXED: Reversed logic - values closer to 0 are healthy
        if prediction > 0.5:
            result = "Mildew Detected"
            confidence = prediction
        else:
            result = "Healthy"
            confidence = 1 - prediction

        # Update metrics
        predicted_label = 1 if result == "Mildew Detected" else 0
        metrics_tracker.update_metrics(predicted_label, predicted_label, confidence)
        
        return result, confidence, metrics_tracker.get_metrics()
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return "Error in prediction", 0.0, metrics_tracker.get_metrics()


if __name__ == "__main__":
    # Test prediction
    try:
        test_image = Image.new('RGB', (224, 224), color='white')
        result, conf, metrics = predict_mildew(test_image)
        print(f"Test prediction: {result} with confidence {conf:.2%}")
    except Exception as e:
        print(f"Test failed: {str(e)}")