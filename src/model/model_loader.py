import tensorflow as tf
import os
from src.utils.logger_config import logger


def load_model():
    """
    Load the trained model.
    
    Returns:
        The loaded model or None if loading fails
    """
    try:
        model_path = 'models/mildew_model.h5'
        if os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            logger.info("Model loaded successfully")
            return model
        else:
            logger.error(f"Model file not found at {model_path}")
            return None
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return None