import numpy as np
from PIL import Image
import logging
from src.model.model_loader import load_model
from src.model.metrics import MetricsTracker

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler if no handlers exist
if not logger.handlers:
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

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
    
    # Resize and convert to array
    img = image.resize(target_size)
    img_array = np.array(img)
    
    # Normalize
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
        # Process image
        processed_image = process_image(image)
        
        # Get model prediction
        model = get_model()
        if model is None:
            return "Model not loaded", 0.0, metrics_tracker.get_metrics()

        # Get raw prediction and convert to Python float
        raw_prediction = float(model.predict(processed_image, verbose=0)[0][0])
        logger.info(f"Raw prediction value: {raw_prediction}")

        # Prediction logic
        if raw_prediction < 0.5:
            result = "Healthy"
            confidence = float(1 - raw_prediction)
        else:
            result = "Mildew Detected"
            confidence = float(raw_prediction)

        logger.info(f"Final prediction: {result} with confidence: {confidence}")
        
        # Convert metrics
        metrics = metrics_tracker.get_metrics()
        metrics = {
            'accuracy': float(metrics['accuracy']),
            'precision': float(metrics['precision']),
            'recall': float(metrics['recall']),
            'confusion_matrix': [
                [int(x) for x in row] 
                for row in metrics['confusion_matrix']
            ]
        }
        
        # Update metrics
        predicted_label = 0 if result == "Healthy" else 1
        metrics_tracker.update_metrics(predicted_label, predicted_label, confidence)
        
        return result, confidence, metrics

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return "Error in prediction", 0.0, {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'confusion_matrix': [[0, 0], [0, 0]]
        }


def debug_prediction(image):
    """Debug function to show prediction details."""
    try:
        processed_image = process_image(image)
        model = get_model()
        if model:
            raw_pred = float(model.predict(processed_image, verbose=0)[0][0])
            return {
                'raw_prediction': raw_pred,
                'threshold': 0.5,
                'would_classify_as': 'Healthy' if raw_pred < 0.5 else 'Mildew',
                'confidence': float(1 - raw_pred if raw_pred < 0.5 else raw_pred)
            }
    except Exception as e:
        logger.error(f"Debug error: {str(e)}")
        return {'error': str(e)}
