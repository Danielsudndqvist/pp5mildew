import traceback
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
MODEL = None
model = None  # For test compatibility
METRICS_TRACKER = MetricsTracker()  # Use uppercase for global


def get_model():
    """Load model if not already loaded."""
    global MODEL, model
    if MODEL is None:
        MODEL = load_model()
        model = MODEL  # Sync with test-compatible variable
    return MODEL


def process_image(image, target_size=(224, 224)):
    """Process image for prediction with detailed logging."""
    try:
        if isinstance(image, str):
            image = Image.open(image)

        logger.info(f"Original Image - Mode: {image.mode}, Size: {image.size}")

        # Resize and convert to array
        img = image.resize(target_size)
        img_array = np.array(img)

        logger.info(
            f"Processed Array - Shape: {img_array.shape}, "
            f"Dtype: {img_array.dtype}"
        )

        # Normalize
        processed = img_array.astype('float32') / 255.0
        logger.info(
            f"Normalized Array - Shape: {processed.shape}, "
            f"Range: {processed.min()}-{processed.max()}"
        )

        return np.expand_dims(processed, axis=0)

    except Exception as e:
        logger.error(f"Image processing error: {str(e)}")
        raise


def predict_mildew(image):
    """Predict mildew presence in image with detailed error handling."""
    try:
        # Process image
        processed_image = process_image(image)

        # Get model
        current_model = get_model()
        if current_model is None:
            logger.error("Model failed to load")
            return "Error: Model not loaded", 0.0, get_default_metrics()

        # Make prediction
        prediction = current_model.predict(processed_image, verbose=0)
        logger.info(f"Raw prediction: {prediction}")

        # Process prediction value
        raw_prediction = float(prediction[0][0])
        raw_prediction = float(np.clip(raw_prediction, 0, 1))
        logger.info(f"Processed prediction: {raw_prediction}")

        # Determine result
        if raw_prediction < 0.5:
            result = "Healthy"
            confidence = float(1 - raw_prediction)
        else:
            result = "Mildew Detected"
            confidence = float(raw_prediction)

        logger.info(f"Classification: {result}, Confidence: {confidence}")

        # Get metrics
        return result, confidence, get_formatted_metrics()

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return "Error: Prediction failed", 0.0, get_default_metrics()


def get_default_metrics():
    """Return default metrics structure."""
    return {
        'accuracy': 0.0,
        'precision': 0.0,
        'recall': 0.0,
        'confusion_matrix': [[0, 0], [0, 0]]
    }


def get_formatted_metrics():
    """Get and format current metrics."""
    metrics = METRICS_TRACKER.get_metrics()
    return {
        'accuracy': float(metrics['accuracy']),
        'precision': float(metrics['precision']),
        'recall': float(metrics['recall']),
        'confusion_matrix': [
            [int(x) for x in row]
            for row in metrics['confusion_matrix']
        ]
    }
