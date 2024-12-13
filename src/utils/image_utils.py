from typing import Optional, Tuple
import cv2
import numpy as np
from PIL import Image
from src.utils.logger_config import logger


def enhance_image(
    image: Image.Image,
    contrast_limit: float = 2.0,
    tile_grid_size: Tuple[int, int] = (8, 8)
) -> Image.Image:
    """
    Enhance image quality for better prediction.
    
    Args:
        image: Input PIL Image
        contrast_limit: CLAHE contrast limit
        tile_grid_size: CLAHE tile grid size
    
    Returns:
        PIL Image: Enhanced image
        
    Raises:
        ValueError: If image processing fails
    """
    try:
        # Convert PIL image to cv2 format
        img_array = np.array(image)
        img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Apply CLAHE enhancement
        clahe = cv2.createCLAHE(
            clipLimit=contrast_limit,
            tileGridSize=tile_grid_size
        )
        
        # Convert to LAB color space
        img_lab = cv2.cvtColor(img_cv, cv2.COLOR_BGR2LAB)
        l_channel = img_lab[:,:,0]
        
        # Apply CLAHE to L channel
        enhanced_l = clahe.apply(l_channel)
        img_lab[:,:,0] = enhanced_l
        
        # Convert back to BGR and RGB
        img_enhanced = cv2.cvtColor(img_lab, cv2.COLOR_LAB2BGR)
        img_enhanced_rgb = cv2.cvtColor(img_enhanced, cv2.COLOR_BGR2RGB)
        
        return Image.fromarray(img_enhanced_rgb)

    except Exception as e:
        logger.error(f"Image enhancement error: {str(e)}")
        return image  # Return original image if enhancement fails


def normalize_image(
    image: np.ndarray,
    target_mean: float = 0.5,
    target_std: float = 0.5
) -> np.ndarray:
    """
    Normalize image to target mean and standard deviation.
    
    Args:
        image: Input image array
        target_mean: Desired mean value
        target_std: Desired standard deviation
    
    Returns:
        numpy.ndarray: Normalized image array
    """
    img_mean = np.mean(image)
    img_std = np.std(image)
    
    if img_std == 0:
        img_std = 1e-10  # Prevent division by zero
        
    normalized = (image - img_mean) / img_std
    scaled = (normalized * target_std) + target_mean
    
    return np.clip(scaled, 0, 1)  # Ensure values are in [0,1]