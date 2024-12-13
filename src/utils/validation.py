from typing import Tuple, Union, BinaryIO
from PIL import Image
import os
from src.utils.logger_config import logger


def validate_image(
    image_file: Union[str, BinaryIO]
) -> Tuple[bool, str]:
    """
    Validate uploaded image files.
    
    Args:
        image_file: File object or path to validate
        
    Returns:
        tuple: (is_valid, error_message)
            - is_valid (bool): Whether the image is valid
            - error_message (str): Description of any validation errors
    
    Raises:
        None: Exceptions are caught and returned as error messages
    """
    try:
        if image_file is None:
            return False, "No file uploaded"

        # Validate file extension
        valid_extensions = {'.jpg', '.jpeg', '.png'}
        if isinstance(image_file, str):
            file_ext = os.path.splitext(image_file.lower())[1]
        else:
            file_ext = os.path.splitext(image_file.name.lower())[1]

        if file_ext not in valid_extensions:
            return False, (
                f"Invalid file type. Please upload "
                f"{', '.join(valid_extensions)} files only"
            )

        # Check file size (5MB limit)
        if hasattr(image_file, 'size'):
            if image_file.size > 5 * 1024 * 1024:
                return False, "File size too large. Maximum size is 5MB"

        # Verify image can be opened and is valid
        img = Image.open(image_file)
        img.verify()

        # Check minimum dimensions
        img = Image.open(image_file)  # Reopen after verify
        width, height = img.size
        if width < 224 or height < 224:
            return False, (
                "Image dimensions too small. "
                "Minimum size is 224x224 pixels"
            )

        return True, ""

    except Exception as e:
        logger.error(f"Image validation error: {str(e)}")
        return False, f"Invalid or corrupted image file: {str(e)}"
