import streamlit as st
from PIL import Image
import numpy as np
from src.model.prediction import process_image, predict_mildew


def app():
    """Render the prediction page."""
    st.title("Leaf Disease Detection")

    st.info(
        "Upload a clear image of a cherry leaf for instant analysis "
        "of potential mildew infection."
    )

    # Image upload
    uploaded_file = st.file_uploader(
        "Upload Leaf Image",
        type=['png', 'jpg', 'jpeg'],
        help="Upload a clear image of a single cherry leaf"
    )

    if uploaded_file:
        try:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Leaf", use_column_width=True)

            # Make prediction
            if st.button("Analyze Leaf"):
                with st.spinner("Analyzing..."):
                    # Get prediction
                    result, confidence, metrics = predict_mildew(image)
                    
                    # Display results
                    display_results(result, confidence)
                    
                    # Display model performance
                    display_metrics(metrics)
                    
                    # Show recommendations
                    show_recommendations(result)

        except Exception as e:
            st.error(f"Error processing image: {str(e)}")


def display_results(result, confidence):
    """Display prediction results."""
    st.write("### Analysis Results")

    # Create columns for results
    col1, col2 = st.columns([1, 1])

    with col1:
        if result == "Mildew Detected":
            st.error("🔴 Mildew Detected")
        else:
            st.success("✅ Healthy Leaf")

    with col2:
        st.metric("Confidence Score", f"{confidence:.1%}")


def display_metrics(metrics):
    """Display model performance metrics."""
    st.write("### Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", f"{metrics['accuracy']:.1%}")
    with col2:
        st.metric("Precision", f"{metrics['precision']:.1%}")
    with col3:
        st.metric("Recall", f"{metrics['recall']:.1%}")


def show_recommendations(result):
    """Show recommendations based on prediction."""
    st.write("### Recommendations")

    if result == "Mildew Detected":
        st.warning("""
        #### Immediate Actions Required:
        1. **Isolate** affected plants
        2. **Remove** heavily infected leaves
        3. **Improve** air circulation
        4. **Apply** appropriate fungicide
        5. **Monitor** nearby plants daily
        """)
    else:
        st.success("""
        #### Preventive Measures:
        1. **Maintain** good air circulation
        2. **Monitor** regularly
        3. **Keep** leaves dry
        4. **Space** plants appropriately
        5. **Practice** good garden hygiene
        """)


if __name__ == "__main__":
    app()