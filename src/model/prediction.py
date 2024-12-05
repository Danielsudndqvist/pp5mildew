import numpy as np
from PIL import Image
from src.utils.logger_config import logger

def predict_mildew(image):
    try:
        logger.info("Starting prediction for new image")
        processed_image = process_image(image)
        prediction = model.predict(processed_image)
        probability = float(prediction[0])
        
        result = "Mildew Detected" if probability > 0.5 else "Healthy"
        logger.info(f"Prediction: {result} (confidence: {probability:.2f})")
        
        return result, probability
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise

def process_image(image, target_size=(224, 224)):
    """
    Process image for model prediction
    Args:
        image: PIL Image object
        target_size: tuple of (height, width)
    Returns:
        processed_image: numpy array ready for model prediction
    """
    # Resize image
    if image.size != target_size:
        image = image.resize(target_size)
    
    # Convert to numpy array and normalize
    image_array = np.array(image)
    processed_image = image_array.astype('float32') / 255.0
    
    return processed_image