import numpy as np
from PIL import Image


def preprocess_image(image: Image.Image, target_size=(224, 224)) -> np.ndarray:
    """Preprocess image for model input."""
    # Resize image
    img = image.resize(target_size)
    # Convert to array and normalize
    img_array = np.array(img)
    processed = img_array.astype('float32') / 255.0
    return processed
