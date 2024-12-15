import os
from PIL import Image


def validate_image(image_file):
    """
    Validate uploaded image files.

    Args:
        image_file: File object from streamlit uploader

    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        if image_file is None:
            return False, "No file uploaded"

        # Check file extension
        valid_extensions = {'.jpg', '.jpeg', '.png'}
        file_ext = os.path.splitext(image_file.name.lower())[1]

        if file_ext not in valid_extensions:
            return False, (
                f"Invalid file type. Please upload "
                f"{', '.join(valid_extensions)} files only"
            )

        # Check file size (5MB limit)
        if image_file.size > 5 * 1024 * 1024:
            return False, "File size too large. Maximum size is 5MB"

        # Verify image can be opened and is valid
        img = Image.open(image_file)
        img.verify()

        # Check dimensions
        img = Image.open(image_file)  # Reopen after verify
        width, height = img.size
        if width < 224 or height < 224:
            return False, (
                "Image dimensions too small. "
                "Minimum size is 224x224 pixels"
            )

        return True, ""

    except Exception as e:
        return False, f"Invalid or corrupted image file: {str(e)}"
