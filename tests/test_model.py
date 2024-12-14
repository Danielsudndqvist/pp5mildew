import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from PIL import Image


@pytest.fixture
def mock_model():
    """Create mock model."""
    model = MagicMock()
    model.predict.return_value = np.array([[0.8]])
    return model


@pytest.fixture
def test_image():
    """Create test image."""
    return Image.new('RGB', (224, 224), color='white')


def test_process_image(test_image):
    """Test image processing function."""
    from src.model.prediction import process_image
    processed = process_image(test_image)
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (1, 224, 224, 3)
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0


def test_predict_mildew(test_image, mock_model):
    """Test mildew prediction function."""
    from src.model.prediction import predict_mildew
    with patch('src.model.prediction.model', mock_model):
        result, confidence, metrics = predict_mildew(test_image)
        assert isinstance(result, str)
        assert isinstance(confidence, float)
        assert isinstance(metrics, dict)
        assert result in ["Healthy", "Mildew Detected"]
        assert 0 <= confidence <= 1


def test_predict_mildew_no_model(test_image):
    """Test prediction with no model."""
    from src.model.prediction import predict_mildew
    with patch('src.model.prediction.model', None):
        result, confidence, metrics = predict_mildew(test_image)
        assert isinstance(result, str)
        assert isinstance(confidence, float)
        assert isinstance(metrics, dict)
