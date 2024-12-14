from PIL import Image
import numpy as np
from src.model.prediction import process_image, predict_mildew


def test_process_image():
    """Test image processing function."""
    # Create test image
    test_image = Image.new('RGB', (100, 100))
    processed = process_image(test_image)

    # Verify shape and properties
    assert processed.shape == (1, 224, 224, 3)
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0


def test_predict_mildew():
    """Test mildew prediction function."""
    # Create test image
    test_image = Image.new('RGB', (100, 100))
    result, confidence, metrics = predict_mildew(test_image)

    # Verify outputs
    assert result in ["Healthy", "Mildew Detected"]
    assert isinstance(confidence, float)
    assert 0 <= confidence <= 1