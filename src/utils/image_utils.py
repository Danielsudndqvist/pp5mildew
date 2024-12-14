from typing import Tuple
import cv2
import numpy as np
from PIL import Image


def enhance_image(
    image: Image.Image,
    contrast_limit: float = 2.0,
    tile_grid_size: Tuple[int, int] = (8, 8)
) -> Image.Image:
    """Enhance image quality for better prediction."""
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
        l_channel = img_lab[:, :, 0]

        # Apply CLAHE to L channel
        enhanced_l = clahe.apply(l_channel)
        img_lab[:, :, 0] = enhanced_l

        # Convert back to BGR and RGB
        img_enhanced = cv2.cvtColor(img_lab, cv2.COLOR_LAB2BGR)
        img_enhanced_rgb = cv2.cvtColor(img_enhanced, cv2.COLOR_BGR2RGB)

        return Image.fromarray(img_enhanced_rgb)

    except Exception:
        return image  # Return original if enhancement fails
