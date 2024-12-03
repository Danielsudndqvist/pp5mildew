import os
from PIL import Image
import logging
from src.utils.logger import logger

def validate_image(image_file):
    """
    Validate uploaded image files
    Returns: tuple (is_valid, error_message)
    """
    try:
        # Check if file is provided
        if image_file is None:
            return False, "No file uploaded"

        # Check file extension
        valid_extensions = {'.jpg', '.jpeg', '.png'}
        file_ext = os.path.splitext(image_file.name.lower())[1]
        if file_ext not in valid_extensions:
            return False, f"Invalid file type. Please upload {', '.join(valid_extensions)} files only"

        # Check file size (e.g., max 5MB)
        if image_file.size > 5 * 1024 * 1024:
            return False, "File size too large. Maximum size is 5MB"

        # Try opening the image to verify it's not corrupted
        img = Image.open(image_file)
        img.verify()
        
        return True, ""

    except Exception as e:
        logger.error(f"Image validation error: {str(e)}")
        return False, "Invalid or corrupted image file"