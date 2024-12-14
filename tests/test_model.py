import pytest
import numpy as np
from PIL import Image
from unittest.mock import MagicMock


@pytest.fixture
def sample_image():
    """Create a sample image for testing."""
    return Image.new('RGB', (224, 224), color='red')


@pytest.fixture
def mock_model():
    """Create a mock model for testing."""
    model = MagicMock()
    model.predict.return_value = np.array([[0.8]])
    return model


def test_process_image(sample_image):
    """Test image processing function."""
    from src.model.prediction import process_image
    
    processed = process_image(sample_image)
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (1, 224, 224, 3)
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0


def test_predict_mildew(sample_image, mock_model, monkeypatch):
    """Test mildew prediction function."""
    from src.model.prediction import predict_mildew
    import src.model.prediction as prediction_module
    
    # Mock the model
    monkeypatch.setattr(prediction_module, "model", mock_model)
    
    # Test prediction
    result, confidence, metrics = predict_mildew(sample_image)
    
    # Assertions
    assert isinstance(result, str)
    assert isinstance(confidence, float)
    assert isinstance(metrics, dict)
    assert result in ["Healthy", "Mildew Detected"]
    assert 0 <= confidence <= 1


def test_predict_mildew_no_model(sample_image, monkeypatch):
    """Test prediction behavior when model is None."""
    from src.model.prediction import predict_mildew
    import src.model.prediction as prediction_module
    
    # Set model to None
    monkeypatch.setattr(prediction_module, "model", None)
    
    # Test prediction
    result, confidence, metrics = predict_mildew(sample_image)
    
    # Assertions
    assert isinstance(result, str)
    assert isinstance(confidence, float)
    assert isinstance(metrics, dict)
