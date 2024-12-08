# tests/test_model.py
import pytest
from PIL import Image
import numpy as np
from src.model.prediction import process_image, predict_mildew

def test_process_image():
    # Create test image
    test_image = Image.new('RGB', (100, 100))
    processed = process_image(test_image)
    
    assert processed.shape == (224, 224, 3)
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0

def test_predict_mildew():
    test_image = Image.new('RGB', (100, 100))
    result, confidence, metrics = predict_mildew(test_image)
    
    assert result in ["Healthy", "Mildew Detected"]
    assert 0 <= confidence <= 1
    assert all(key in metrics for key in ['accuracy', 'precision', 'recall'])