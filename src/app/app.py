import streamlit as st
from app_pages.home import page_home_body
from app_pages.visualization import page_visualization_body
from app_pages.prediction import page_prediction_body
from app_pages.about import page_about_body

def main():
    st.set_page_config(
        page_title="Cherry Leaf Mildew Detection",
        page_icon="🍒",
        layout="wide"
    )
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", 
        ["Home", "Visualization", "Prediction", "About"]
    )
    
    # Page content
    if selection == "Home":
        page_home_body()
    elif selection == "Visualization":
        page_visualization_body()
    elif selection == "Prediction":
        page_prediction_body()
    elif selection == "About":
        page_about_body()

if __name__ == "__main__":
    main()