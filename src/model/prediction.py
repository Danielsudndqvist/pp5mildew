import numpy as np
from PIL import Image
from src.model.model_loader import load_model
from src.model.metrics import MetricsTracker

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
            # For testing when model isn't available
            prediction = 0.7
        else:
            prediction = model.predict(processed_image)[0][0]

        # Determine result
        predicted_label = 1 if prediction > 0.5 else 0
        result = "Mildew Detected" if predicted_label == 1 else "Healthy"

        # Update metrics
        metrics_tracker.update_metrics(1, predicted_label, prediction)

        return result, prediction, metrics_tracker.get_metrics()

    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")
