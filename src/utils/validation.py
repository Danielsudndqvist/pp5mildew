import os
from PIL import Image
from src.utils.logger_config import logger


def validate_image(image_file):
    """
    Validate uploaded image files.
    
    Args:
        image_file: The uploaded file to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        if image_file is None:
            return False, "No file uploaded"

        valid_extensions = {'.jpg', '.jpeg', '.png'}
        file_ext = os.path.splitext(image_file.name.lower())[1]
        
        if file_ext not in valid_extensions:
            return False, (
                f"Invalid file type. Please upload "
                f"{', '.join(valid_extensions)} files only"
            )

        if image_file.size > 5 * 1024 * 1024:
            return False, "File size too large. Maximum size is 5MB"

        img = Image.open(image_file)
        img.verify()
        
        return True, ""

    except Exception as e:
        logger.error(f"Image validation error: {str(e)}")
        return False, "Invalid or corrupted image file"