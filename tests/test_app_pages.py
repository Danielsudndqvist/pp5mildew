from unittest.mock import MagicMock, patch
from contextlib import ExitStack
import pytest
import numpy as np


@pytest.fixture(autouse=True)
def mock_streamlit():
    """Mock all streamlit functions."""
    with (patch('streamlit.title') as mock_title,
          patch('streamlit.write') as mock_write,
          patch('streamlit.plotly_chart') as mock_chart,
          patch('streamlit.columns') as mock_cols,
          patch('streamlit.tabs') as mock_tabs,
          patch('streamlit.metric') as mock_metric):

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


def test_visualization_page_structure(mock_streamlit):
    """Test visualization page content structure."""
    from src.app_pages.visualization import app
    app()
    mock_streamlit['title'].assert_called_once_with("Leaf Analysis Study")
    assert mock_streamlit['tabs'].called


@patch('numpy.random.normal')
def test_statistical_analysis(mock_normal, mock_streamlit):
    """Test statistical analysis visualization."""
    mock_normal.return_value = np.array([0.5] * 100)
    from src.app_pages.visualization import show_statistical_analysis
    show_statistical_analysis()
    assert mock_streamlit['write'].called
    assert mock_streamlit['plotly_chart'].called
    assert mock_streamlit['metric'].called


def test_plotly_chart_creation():
    """Test Plotly chart creation."""
    patches = [
        patch('numpy.random.normal',
              return_value=np.array([0.5] * 100)),
        patch('plotly.express.histogram',
              return_value=MagicMock()),
        patch('streamlit.write'),
        patch('streamlit.plotly_chart'),
        patch('streamlit.columns',
              return_value=[MagicMock(), MagicMock()]),
        patch('streamlit.metric')
    ]

    with ExitStack() as stack:
        mocks = [stack.enter_context(p) for p in patches]
        mock_hist = mocks[1]

        from src.app_pages.visualization import show_statistical_analysis
        show_statistical_analysis()
        assert mock_hist.called
        mock_hist.assert_called_once()
