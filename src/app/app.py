import streamlit as st
from app_pages import (
    home,
    prediction,
    visualization,
    metrics
)


class MildewDetectionApp:
    """Main application class for Mildew Detection."""
    
    def __init__(self):
        """Initialize application configuration."""
        st.set_page_config(
            page_title="Cherry Leaf Mildew Detection",
            layout="wide"
        )
        
        self.pages = {
            "Home": home.app,
            "Make Prediction": prediction.app,
            "Data Visualization": visualization.app,
            "Model Performance": metrics.app
        }

    def run(self):
        """Run the application."""
        st.sidebar.title("Navigation")
        
        # Add project summary to sidebar
        st.sidebar.info(
            "This application uses machine learning to detect "
            "powdery mildew in cherry leaves."
        )
        
        # Page selection
        page = st.sidebar.radio(
            "Go to",
            list(self.pages.keys())
        )
        
        # Run selected page
        self.pages[page]()


if __name__ == "__main__":
    app = MildewDetectionApp()
    app.run()