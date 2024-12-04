import numpy as np
from PIL import Image

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