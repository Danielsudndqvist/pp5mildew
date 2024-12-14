from app_pages import home, visualization, prediction
import streamlit as st
import pytest


def test_home_app():
    """Test home page renders without errors."""
    try:
        home.app()
        assert True
    except Exception as e:
        pytest.fail(f"Home page failed to render: {str(e)}")


def test_visualization_page():
    """Test visualization page renders without errors."""
    try:
        visualization.app()
        assert True
    except Exception as e:
        pytest.fail(f"Visualization page failed to render: {str(e)}")
