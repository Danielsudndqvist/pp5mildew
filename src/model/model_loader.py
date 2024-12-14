from tensorflow import keras
import os
from src.utils.logger_config import logger


def load_model(model_path='models/mildew_model.h5'):
    """
    Load the trained model.
    
    Args:
        model_path: Path to model file
    
    Returns:
        Loaded model or None if loading fails
    """
    try:
        if not os.path.exists(model_path):
            logger.error(f"Model file not found at {model_path}")
            return None

        # Load and verify model
        model = keras.models.load_model(model_path)
        logger.info("Model loaded successfully")
        return model

    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return None


# tests/test_app_pages.py
import pytest
import streamlit as st
from app_pages import home, visualization, prediction


def test_home_page():
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


def test_prediction_page():
    """Test prediction page renders without errors."""
    try:
        prediction.app()
        assert True
    except Exception as e:
        pytest.fail(f"Prediction page failed to render: {str(e)}")
