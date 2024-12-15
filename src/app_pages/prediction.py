import streamlit as st
from PIL import Image
from src.model.prediction import predict_mildew
from src.utils.validation import validate_image


def app():
    """Render the prediction page."""
    st.title("Leaf Disease Prediction")

    # Add debug toggle in sidebar
    debug_mode = st.sidebar.checkbox("Show Debug Info")

    st.write("### Upload Cherry Leaf Images")

    uploaded_files = st.file_uploader(
        "Choose image files",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True,
        help="Upload one or more images of cherry leaves for analysis"
    )

    if uploaded_files:
        st.write("### Analysis Results")

        for uploaded_file in uploaded_files:
            col1, col2 = st.columns([1, 1])

            with col1:
                is_valid, error_message = validate_image(uploaded_file)
                if not is_valid:
                    st.error(f"Error with {uploaded_file.name}: {error_message}")
                    continue

                image = Image.open(uploaded_file)
                st.image(image, caption=uploaded_file.name)

            with col2:
                with st.spinner("Analyzing..."):
                    result, confidence, metrics = predict_mildew(image)

                    # Show prediction
                    if result == "Healthy":
                        st.success(
                            f"✅ Leaf is Healthy\n\n"
                            f"Confidence: {confidence:.1%}"
                        )
                    else:
                        st.error(
                            f"🔴 Mildew Detected\n\n"
                            f"Confidence: {confidence:.1%}"
                        )

                    # Debug information
                    if debug_mode:
                        st.write("### Debug Information")
                        st.write("Raw prediction details:")
                        st.json({
                            "Result": result,
                            "Confidence": f"{confidence:.3f}",
                            "Metrics": metrics,
                        })

                        # Show model performance metrics
                        st.write("### Model Metrics")
                        if 'confusion_matrix' in metrics:
                            st.write("Confusion Matrix:", metrics['confusion_matrix'])
                        st.write(f"Accuracy: {metrics.get('accuracy', 'N/A')}")
                        st.write(f"Precision: {metrics.get('precision', 'N/A')}")
                        st.write(f"Recall: {metrics.get('recall', 'N/A')}")

            st.write("---")

    else:
        st.write("Please upload an image to begin analysis.")


if __name__ == "__main__":
    app()
