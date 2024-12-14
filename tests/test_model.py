import pytest
import numpy as np
from PIL import Image


@pytest.fixture
def sample_image():
    """Create a sample image for testing."""
    return Image.new('RGB', (224, 224), color='red')


def test_process_image(sample_image):
    """Test image processing function."""
    from src.model.prediction import process_image
    
    processed = process_image(sample_image)
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (1, 224, 224, 3)
    assert processed.dtype == np.float32
    assert np.max(processed) <= 1.0
    assert np.min(processed) >= 0.0


def test_predict_mildew(sample_image, mocker):
    """Test mildew prediction function."""
    from src.model.prediction import predict_mildew
    
    # Mock the model prediction
    mock_prediction = np.array([[0.8]])
    mocker.patch(
        'src.model.model_loader.load_model',
        return_value=mocker.MagicMock()
    )
    
    result, confidence, metrics = predict_mildew(sample_image)
    
    assert isinstance(result, str)
    assert isinstance(confidence, float)
    assert isinstance(metrics, dict)
    assert result in ["Healthy", "Mildew Detected"]
    assert 0 <= confidence <= 1
