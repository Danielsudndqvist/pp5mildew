import os
from tensorflow import keras
from src.utils.logger_config import logger


def load_model(model_path='models/mildew_model.h5'):
    """
    Load the trained model with comprehensive logging.

    Args:
        model_path (str): Path to the model file

    Returns:
        Loaded Keras model or None
    """
    try:
        # Resolve absolute path
        resolved_path = os.path.abspath(model_path)

        # Detailed path logging
        logger.info(f"Attempting to load model from: {resolved_path}")
        logger.info(f"Current working directory: {os.getcwd()}")

        # Check file existence
        if not os.path.exists(resolved_path):
            logger.error(f"Model file not found at {resolved_path}")
            logger.info("Listing contents of current directory:")
            logger.info(str(os.listdir('.')))
            logger.info("Listing contents of 'models' directory:")
            logger.info(
                str(os.listdir('models') if os.path.exists('models')
                    else "models directory not found")
            )
            return None

        # File details
        file_stat = os.stat(resolved_path)
        logger.info(f"Model file size: {file_stat.st_size} bytes")

        # Load model
        model = keras.models.load_model(resolved_path)

        # Verify model
        logger.info("Model architecture summary:")
        model.summary()

        logger.info("Model loaded successfully")
        return model

    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return None
