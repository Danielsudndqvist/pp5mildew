import tensorflow as tf
import os
from src.utils.logger_config import logger

MODEL_PATH = 'models/mildew_model.h5'

def load_model():
    """Load the trained model"""
    try:
        if os.path.exists(MODEL_PATH):
            model = tf.keras.models.load_model(MODEL_PATH)
            logger.info("Model loaded successfully")
            return model
        else:
            logger.error(f"Model file not found at {MODEL_PATH}")
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise