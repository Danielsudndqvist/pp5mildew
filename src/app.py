import sys
from pathlib import Path
import streamlit as st

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# Import pages after path setup
from app_pages import home, visualization, prediction  # noqa: E402


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
