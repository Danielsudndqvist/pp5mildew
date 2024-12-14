from unittest.mock import MagicMock, patch
import pytest
import numpy as np


@pytest.fixture(autouse=True)
def mock_streamlit():
    """Mock all streamlit functions."""
    with patch('streamlit.title') as mock_title, \
         patch('streamlit.write') as mock_write, \
         patch('streamlit.plotly_chart') as mock_chart, \
         patch('streamlit.columns') as mock_cols, \
         patch('streamlit.tabs') as mock_tabs, \
         patch('streamlit.metric') as mock_metric:

        mock_tabs.return_value = [MagicMock(), MagicMock(), MagicMock()]
        mock_cols.return_value = [MagicMock(), MagicMock()]

        yield {
            'title': mock_title,
            'write': mock_write,
            'plotly_chart': mock_chart,
            'columns': mock_cols,
            'tabs': mock_tabs,
            'metric': mock_metric
        }


def test_home_page_structure(mock_streamlit):
    """Test home page content structure."""
    from src.app_pages.home import app
    app()
    assert mock_streamlit['title'].called
    assert mock_streamlit['write'].called


def test_visualization_page_structure(mock_streamlit):
    """Test visualization page content structure."""
    from src.app_pages.visualization import app
    app()
    mock_streamlit['title'].assert_called_once_with("Leaf Analysis Study")
    assert mock_streamlit['tabs'].called


def test_prediction_page_structure(mock_streamlit):
    """Test prediction page content structure."""
    from src.app_pages.prediction import app
    app()
    assert mock_streamlit['title'].called
    assert mock_streamlit['write'].called


@patch('numpy.random.normal', return_value=np.array([0.5] * 100))
def test_statistical_analysis(mock_normal, mock_streamlit):
    """Test statistical analysis visualization."""
    from src.app_pages.visualization import show_statistical_analysis
    show_statistical_analysis()

    assert mock_streamlit['write'].called
    assert mock_streamlit['plotly_chart'].called
    assert mock_streamlit['metric'].called


def test_plotly_chart_creation():
    """Test Plotly chart creation."""
    with patch('numpy.random.normal', return_value=np.array([0.5] * 100)) as mock_normal, \
         patch('plotly.express.histogram', return_value=MagicMock()) as mock_hist, \
         patch('streamlit.write'), \
         patch('streamlit.plotly_chart'), \
         patch('streamlit.columns', return_value=[MagicMock(), MagicMock()]), \
         patch('streamlit.metric'):

        from src.app_pages.visualization import show_statistical_analysis
        show_statistical_analysis()
        
        assert mock_hist.called
        mock_hist.assert_called_once()
