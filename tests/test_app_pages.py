# tests/test_app_pages.py
import streamlit as st
from app_pages.home import app as home_app
from app_pages.prediction import app as prediction_app

def test_home_page():
    home_app()
    assert st.title == "Cherry Leaf Mildew Detection"

def test_prediction_page():
    prediction_app()
    assert any(element.type == "file_uploader" for element in st._elements)