import pytest
import numpy as np
from PIL import Image
from src.model.prediction import process_image
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model.prediction import process_image

def test_process_image():
    """Test basic image processing"""
    # Create a test image
    test_image = Image.new('RGB', (100, 100), color='white')
    
    # Process the image
    processed = process_image(test_image)
    
    # Basic checks
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (224, 224, 3)  # Check if resized correctly
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0  # Check normalization
    assert np.min(processed) >= 0.0