import numpy as np
from PIL import Image
from src.model.prediction import process_image


def test_process_image():
    """Test basic image processing."""
    # Create a test image
    test_image = Image.new('RGB', (100, 100), color='white')
    
    # Process the image
    processed = process_image(test_image)
    
    # Basic checks
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (1, 224, 224, 3)
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0