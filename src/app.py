import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
from src.app_pages import home, visualization, prediction

def main():
    """Main function to run the Streamlit application."""
    st.set_page_config(
        page_title="Cherry Leaf Mildew Detection",
        page_icon="🍃",
        layout="wide"
    )

    # Create sidebar navigation
    st.sidebar.title("Navigation")

    # Navigation options
    pages = {
        "Home": home.app,
        "Leaf Analysis": visualization.app,
        "Make Prediction": prediction.app
    }

    # Add project summary to sidebar
    st.sidebar.info(
        "This application helps detect powdery mildew in cherry leaves "
        "using machine learning."
    )

    # Navigation selection
    page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display selected page
    pages[page]()

if __name__ == "__main__":
    main()
