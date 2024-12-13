from PIL import Image


def preprocess_image(image, target_size=(224, 224)):
    """
    Preprocess a single image for model input.
    
    Args:
        image: PIL Image or path to image
        target_size: Desired dimensions (height, width)
    
    Returns:
        Preprocessed image as numpy array
    """
    if isinstance(image, str):
        image = Image.open(image)
    
    # Resize image
    image = image.resize(target_size)
    return image