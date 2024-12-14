from pathlib import Path
import sys
import pytest


def pytest_sessionstart(session):
    """Set up the test environment."""
    root_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(root_dir))


@pytest.fixture
def sample_image():
    """Create a sample test image."""
    from PIL import Image
    return Image.new('RGB', (224, 224), color='red')


@pytest.fixture
def mock_data():
    """Provide mock data for tests."""
    return {
        'metrics': {
            'accuracy': 0.98,
            'precision': 0.97,
            'recall': 0.96
        }
    }
