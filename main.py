import streamlit as st
from app_pages.home import app as home_app
from app_pages.prediction import app as prediction_app
from app_pages.visualization import app as visualization_app
from app_pages.metrics import app as metrics_app

def main():
    st.set_page_config(page_title="Cherry Leaf Disease Detector", layout="wide")

    pages = {
        "Home": home_app,
        "Leaf Analysis": visualization_app,
        "Make Prediction": prediction_app,
        "Model Performance": metrics_app
    }

    with st.sidebar:
        st.image("assets/leaves_logo.png", width=200)
        st.title("Navigation")
        selection = st.radio("Go to", list(pages.keys()))

        st.info("""
        This application helps detect powdery mildew infection in cherry leaves using machine learning.
        """)

    pages[selection]()

if __name__ == "__main__":
    main()
