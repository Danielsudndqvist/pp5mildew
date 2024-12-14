import pytest
from PIL import Image
import numpy as np


@pytest.fixture
def test_image():
    """Create a test image."""
    return Image.new('RGB', (224, 224), color='white')


def test_process_image_shape(test_image):
    """Test if processed image has correct shape."""
    from src.model.prediction import process_image
    
    processed = process_image(test_image)
    assert processed.shape == (1, 224, 224, 3)


def test_process_image_values(test_image):
    """Test if processed image values are normalized."""
    from src.model.prediction import process_image
    
    processed = process_image(test_image)
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0
