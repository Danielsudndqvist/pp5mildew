import pytest
import os
import sys
from pathlib import Path


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and before performing 
    collection and entering the run test loop.
    """
    # Get the repository root directory
    root_dir = Path(__file__).parent.parent
    
    # Add the root directory to Python path
    sys.path.insert(0, str(root_dir))
    
    # Add src directory to Python path
    src_dir = root_dir / 'src'
    if src_dir.exists():
        sys.path.insert(0, str(src_dir))


@pytest.fixture
def test_data_path():
    """Fixture to provide test data directory path."""
    return Path(__file__).parent / 'test_data'


@pytest.fixture
def sample_image():
    """Create a sample image for testing."""
    from PIL import Image
    return Image.new('RGB', (224, 224), color='red')


@pytest.fixture(autouse=True)
def mock_streamlit():
    """Mock streamlit for all tests."""
    import sys
    from unittest.mock import MagicMock
    
    mock_st = MagicMock()
    mock_st.sidebar = MagicMock()
    mock_st.columns = MagicMock(return_value=[MagicMock(), MagicMock()])
    
    sys.modules['streamlit'] = mock_st
    return mock_st
