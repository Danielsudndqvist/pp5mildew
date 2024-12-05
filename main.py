import streamlit as st
from app_pages import prediction_page, metrics_page

st.set_page_config(page_title="Mildew Detection", layout="wide")

pages = {
    "Prediction": prediction_page,
    "Model Metrics": metrics_page,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

pages[selection].app()