import streamlit as st
from PIL import Image
from src.model.prediction import predict_mildew
from src.utils.validation import validate_image


def app():
    """Render the prediction page."""
    st.title("Leaf Disease Prediction")

    st.write("Upload a cherry leaf image for mildew detection.")

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png', 'jpg', 'jpeg']
    )

    if uploaded_file:
        # Validate uploaded file
        is_valid, error_message = validate_image(uploaded_file)

        if not is_valid:
            st.error(error_message)
            return

        # Display and analyze image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Leaf"):
            with st.spinner("Analyzing..."):
                result, confidence, metrics = predict_mildew(image)

                # Display results
                display_prediction_results(result, confidence)

                # Show performance metrics
                display_metrics(metrics)


def display_prediction_results(result, confidence):
    """Display prediction results with appropriate styling."""
    if result == "Mildew Detected":
        st.error(f"🔴 {result} (Confidence: {confidence:.2%})")
        display_recommendations(infected=True)
    else:
        st.success(f"✅ {result} (Confidence: {confidence:.2%})")
        display_recommendations(infected=False)


def display_recommendations(infected):
    """Display appropriate recommendations based on prediction."""
    st.write("### Recommendations")

    if infected:
        st.write(
            "* Isolate infected plants\n"
            "* Apply appropriate fungicide\n"
            "* Improve air circulation\n"
            "* Monitor surrounding plants\n"
            "* Regular inspection recommended"
        )
    else:
        st.write(
            "* Continue regular monitoring\n"
            "* Maintain good ventilation\n"
            "* Practice preventive care\n"
            "* Keep leaves dry"
        )


def display_metrics(metrics):
    """Display model performance metrics."""
    st.write("### Model Performance")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", f"{metrics['accuracy']:.2%}")
    with col2:
        st.metric("Precision", f"{metrics['precision']:.2%}")
    with col3:
        st.metric("Recall", f"{metrics['recall']:.2%}")


if __name__ == "__main__":
    app()
