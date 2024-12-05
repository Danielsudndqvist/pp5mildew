import streamlit as st
from app_pages.prediction import app as prediction_app
from app_pages.metrics import page_metrics

st.set_page_config(page_title="Cherry Leaf Mildew Detection", layout="wide")

# Create dictionary of pages
pages = {
    "Home": lambda: st.write("Welcome to Cherry Leaf Mildew Detection App"),
    "Make Prediction": prediction_app,
    "Model Performance": page_metrics,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

pages[selection]()