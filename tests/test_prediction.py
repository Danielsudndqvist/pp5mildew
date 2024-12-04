import pytest
import numpy as np
from PIL import Image
import os
from src.model.prediction import process_image  # adjust import based on your structure

def test_prediction_processing():
    """Test the image processing for prediction"""
    # Create a dummy test image
    test_image = Image.new('RGB', (224, 224), color='white')
    
    # Process the image
    processed = process_image(test_image)
    
    # Check the processed image properties
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (224, 224, 3)
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0

def test_model_input_shape():
    """Test if the model input shape is correct"""
    test_image = Image.new('RGB', (224, 224), color='white')
    processed = process_image(test_image)
    assert processed.shape == (224, 224, 3)