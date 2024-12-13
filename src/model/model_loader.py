# src/model/model_loader.py
import tensorflow as tf
import os
from src.utils.logger_config import logger


def load_model(model_path='models/mildew_model.h5', custom_objects=None):
    """
    Load the trained model with additional error handling and customization.
    
    Args:
        model_path (str): Path to the model file
        custom_objects (dict): Custom objects needed for loading the model
    
    Returns:
        tf.keras.Model or None: The loaded model or None if loading fails
    """
    try:
        # Ensure models directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)

        if not os.path.exists(model_path):
            logger.error(f"Model file not found at {model_path}")
            return None

        # Verify file size before loading
        file_size = os.path.getsize(model_path)
        if file_size < 1000:
            logger.error(f"Model file appears to be corrupt or empty: {model_path}")
            return None

        # Load model with custom objects if provided
        model = tf.keras.models.load_model(model_path, custom_objects=custom_objects)

        # Verify model structure
        if not isinstance(model, tf.keras.Model):
            logger.error("Loaded object is not a valid Keras model")
            return None

        logger.info(f"Model loaded successfully from {model_path}")
        logger.info(f"Model input shape: {model.input_shape}")
        logger.info(f"Model output shape: {model.output_shape}")

        return model

    except tf.errors.OpError as e:
        logger.error(f"TensorFlow error loading model: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error loading model: {str(e)}")
        return None
