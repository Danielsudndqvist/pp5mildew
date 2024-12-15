import streamlit as st
from PIL import Image
from src.model.prediction import predict_mildew


def app():
    """Render the prediction page."""
    st.title("Leaf Disease Prediction")
    st.write("Upload a cherry leaf image for mildew detection.")

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png', 'jpg', 'jpeg']
    )

    if uploaded_file:
        # Display image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Make prediction
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                result, confidence, metrics = predict_mildew(image)
                show_prediction_results(result, confidence)
                show_metrics(metrics)


def show_prediction_results(result, confidence):
    """Display prediction results."""
    if result == "Healthy":
        st.success(f"✅ Leaf is Healthy\nConfidence: {confidence:.1%}")
        show_healthy_recommendations()
    else:
        st.error(f"🔴 Mildew Detected\nConfidence: {confidence:.1%}")
        show_mildew_recommendations()


def show_healthy_recommendations():
    """Show recommendations for healthy leaves."""
    st.write("""
    ### Recommendations:
    * Continue regular monitoring
    * Maintain good ventilation
    * Practice preventive care
    * Keep leaves dry
    """)


def show_mildew_recommendations():
    """Show recommendations for infected leaves."""
    st.write("""
    ### Recommendations:
    * Isolate infected plants
    * Apply appropriate fungicide
    * Improve air circulation
    * Monitor surrounding plants
    * Schedule follow-up inspection
    """)


def show_metrics(metrics):
    """Display model metrics."""
    st.write("### Model Performance")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", f"{metrics['accuracy']:.2%}")
    with col2:
        st.metric("Precision", f"{metrics['precision']:.2%}")
    with col3:
        st.metric("Recall", f"{metrics['recall']:.2%}")
