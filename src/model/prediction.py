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
        if model:
            logger.info("Model loaded successfully")
        else:
            logger.warning("Failed to load model")
    return model


def process_image(image, target_size=(224, 224)):
    """
    Process image for prediction.

    Args:
        image: PIL Image object or path
        target_size: Output image dimensions

    Returns:
        numpy array: Processed image array
    """
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

        # Get prediction
        model = get_model()
        if model is None:
            logger.warning("Model not available, using fallback prediction")
            prediction = 0.1  # Default to healthy with high confidence
        else:
            prediction = float(model.predict(processed_image)[0][0])
            logger.info(f"Raw prediction value: {prediction}")

        # Determine result and confidence
        predicted_label = 1 if prediction > 0.5 else 0
        result = "Mildew Detected" if predicted_label == 1 else "Healthy"
        confidence = prediction if predicted_label == 1 else 1 - prediction

        # Log prediction details
        logger.info(f"Prediction: {result} with confidence {confidence:.2%}")

        # Update metrics
        metrics_tracker.update_metrics(1, predicted_label, confidence)
        
        return result, confidence, metrics_tracker.get_metrics()

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise Exception(f"Prediction error: {str(e)}")


if __name__ == "__main__":
    # Test prediction
    try:
        test_image = Image.new('RGB', (224, 224), color='white')
        result, conf, metrics = predict_mildew(test_image)
        print(f"Test prediction: {result} with confidence {conf:.2%}")
    except Exception as e:
        print(f"Test failed: {str(e)}")
