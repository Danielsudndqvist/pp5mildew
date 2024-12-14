import pytest
from unittest.mock import MagicMock


# Mock streamlit
class StreamlitMock:
    def __init__(self):
        self.title = MagicMock()
        self.write = MagicMock()
        self.info = MagicMock()
        self.error = MagicMock()
        self.sidebar = MagicMock()
        self.columns = MagicMock(return_value=[MagicMock(), MagicMock()])
        self.image = MagicMock()
        self.success = MagicMock()
        self.metric = MagicMock()


@pytest.fixture
def mock_st(monkeypatch):
    """Create a mock for streamlit."""
    mock_streamlit = StreamlitMock()
    monkeypatch.setattr("streamlit.title", mock_streamlit.title)
    monkeypatch.setattr("streamlit.write", mock_streamlit.write)
    monkeypatch.setattr("streamlit.info", mock_streamlit.info)
    monkeypatch.setattr("streamlit.error", mock_streamlit.error)
    monkeypatch.setattr("streamlit.sidebar", mock_streamlit.sidebar)
    monkeypatch.setattr("streamlit.columns", mock_streamlit.columns)
    monkeypatch.setattr("streamlit.image", mock_streamlit.image)
    monkeypatch.setattr("streamlit.success", mock_streamlit.success)
    monkeypatch.setattr("streamlit.metric", mock_streamlit.metric)
    return mock_streamlit


def test_home_page_structure(mock_st):
    """Test home page content structure."""
    # Import here to use mocked streamlit
    from src.app_pages.home import app

    app()

    # Verify page structure
    mock_st.title.assert_called_once()
    assert mock_st.write.called
    assert mock_st.info.called


def test_visualization_page_structure(mock_st):
    """Test visualization page content structure."""
    from src.app_pages.visualization import app

    app()

    # Verify page structure
    mock_st.title.assert_called_once()
    assert mock_st.write.called


def test_prediction_page_structure(mock_st):
    """Test prediction page content structure."""
    from src.app_pages.prediction import app

    app()

    # Verify page structure
    mock_st.title.assert_called_once()
    assert mock_st.write.called
