import os
import traceback
import numpy as np
from PIL import Image
import logging
import json

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
METRICS_TRACKER = MetricsTracker()


def get_model():
    """Load model if not already loaded."""
    global MODEL
    if MODEL is None:
        MODEL = load_model()
    return MODEL


def process_image(image, target_size=(224, 224)):
    """
    Process image for prediction with detailed logging.

    Args:
        image (PIL.Image or str): Input image
        target_size (tuple): Target image size

    Returns:
        numpy.ndarray: Processed image array
    """
    if isinstance(image, str):
        image = Image.open(image)

    # Log original image details
    logger.info(f"Original Image - Mode: {image.mode}, Size: {image.size}")

    # Resize and convert to array
    img = image.resize(target_size)
    img_array = np.array(img)

    # Detailed array logging
    logger.info(
        f"Processed Array - Shape: {img_array.shape}, "
        f"Dtype: {img_array.dtype}"
    )
    logger.info(
        f"Pixel Value Range: Min={img_array.min()}, Max={img_array.max()}"
    )

    # Normalize
    processed = img_array.astype('float32') / 255.0

    # Additional logging
    logger.info(
        f"Normalized Array - Shape: {processed.shape}, "
        f"Range: {processed.min()}-{processed.max()}"
    )

    return np.expand_dims(processed, axis=0)


def predict_mildew(image):
    """
    Comprehensive mildew prediction with extensive diagnostics.

    Args:
        image (PIL.Image): Image to predict

    Returns:
        tuple: (result, confidence, metrics)
    """
    try:
        # Process image with detailed logging
        processed_image = process_image(image)

        # Get model
        model = get_model()
        if model is None:
            logger.error("Model failed to load")
            return "Model not loaded", 0.0, {
                'accuracy': 0.0,
                'precision': 0.0,
                'recall': 0.0,
                'confusion_matrix': [[0, 0], [0, 0]]
            }

        # Comprehensive prediction logging
        logger.info("Prediction Input Details:")
        logger.info(f"Input Shape: {processed_image.shape}")
        logger.info(f"Input Data Type: {processed_image.dtype}")
        logger.info(
            f"Input Value Range: {processed_image.min()}-{processed_image.max()}"
        )

        # Prediction with verbose output
        prediction = model.predict(processed_image, verbose=1)
        logger.info(f"Raw Prediction Output: {prediction}")
        logger.info(f"Prediction Shape: {prediction.shape}")

        # Extract scalar prediction value
        raw_prediction = float(prediction[0][0])
        logger.info(f"Scalar Prediction Value: {raw_prediction}")

        # Detailed classification logic
        if raw_prediction < 0.5:
            result = "Healthy"
            confidence = 1 - raw_prediction
        else:
            result = "Mildew Detected"
            confidence = raw_prediction

        logger.info(f"Final Classification: {result}")
        logger.info(f"Confidence: {confidence}")

        # Default metrics
        default_metrics = {
            'accuracy': 0.8,
            'precision': 0.75,
            'recall': 0.85,
            'confusion_matrix': [[80, 20], [15, 85]]
        }

        return result, float(confidence), default_metrics

    except Exception as e:
        logger.error(f"Prediction Error: {str(e)}")
        logger.error(traceback.format_exc())
        return "Prediction Error", 0.0, {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'confusion_matrix': [[0, 0], [0, 0]]
        }


def analyze_model_prediction(image):
    """
    Comprehensive model prediction analysis.

    Args:
        image (PIL.Image): Input image

    Returns:
        dict: Detailed prediction diagnostic information
    """
    try:
        # Process image with different preprocessing variations
        preprocessed_variants = [
            # Standard preprocessing
            process_image(image),

            # Alternative normalization
            np.expand_dims(
                np.array(image.resize((224, 224))) / 255.0,
                axis=0
            ),

            # Pixel scaling
            np.expand_dims(
                (np.array(image.resize((224, 224))).astype('float32')
                 - 127.5) / 127.5,
                axis=0
            )
        ]

        model = get_model()
        if not model:
            return {"error": "Model not loaded"}

        # Predict with different preprocessing
        predictions = [
            model.predict(variant, verbose=0)[0][0]
            for variant in preprocessed_variants
        ]

        return {
            "preprocessing_variants": [
                {
                    "min_value": float(variant.min()),
                    "max_value": float(variant.max()),
                    "mean_value": float(variant.mean()),
                    "prediction": float(pred)
                }
                for variant, pred in zip(preprocessed_variants, predictions)
            ],
            "input_image_details": {
                "original_size": image.size,
                "mode": image.mode,
                "pixel_stats": {
                    "min": float(np.array(image).min()),
                    "max": float(np.array(image).max()),
                    "mean": float(np.array(image).mean())
                }
            }
        }

    except Exception as e:
        logger.error(f"Diagnostic analysis error: {str(e)}")
        return {"error": str(e)}
