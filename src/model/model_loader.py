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
        if file_size < 1000:  # Check if file is too small (likely corrupt)
            logger.error(f"Model file appears to be corrupt or empty: {model_path}")
            return None
            
        # Load the model with custom objects if provided
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


# src/utils/logger_config.py
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler


def setup_logger(name='mildew_detector', 
                log_dir='logs',
                max_size_mb=10,
                backup_count=5):
    """
    Configure and set up logging system with enhanced features.
    
    Args:
        name (str): Logger name
        log_dir (str): Directory for log files
        max_size_mb (int): Maximum size of log file in MB
        backup_count (int): Number of backup files to keep
    
    Returns:
        logging.Logger: Configured logger instance
    """
    try:
        # Create logs directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)
        
        # Generate log filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f'{name}_{timestamp}.log'
        log_filepath = os.path.join(log_dir, log_filename)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # Clear any existing handlers
        if logger.hasHandlers():
            logger.handlers.clear()
        
        # Create formatters
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # File handler with rotation
        file_handler = RotatingFileHandler(
            log_filepath,
            maxBytes=max_size_mb * 1024 * 1024,  # Convert MB to bytes
            backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        logger.info(f"Logger initialized: {name}")
        logger.info(f"Log file: {log_filepath}")
        
        return logger
        
    except Exception as e:
        # Fallback to basic logging if setup fails
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logger = logging.getLogger(name)
        logger.error(f"Error setting up logger: {str(e)}")
        return logger


# Initialize logger
logger = setup_logger()