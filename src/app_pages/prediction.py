import streamlit as st
from PIL import Image
from src.model.prediction import predict_mildew


def app():
    """Render the prediction page."""
    st.title("Leaf Disease Prediction")

    uploaded_file = st.file_uploader(
        "Upload a cherry leaf image",
        type=['png', 'jpg', 'jpeg']
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                try:
                    result, confidence, metrics = predict_mildew(image)

                    if result == "Mildew Detected":
                        st.error(f"🔴 {result}")
                    else:
                        st.success(f"✅ {result}")

                    st.write(f"Confidence: {confidence:.2%}")

                    # Display recommendations
                    st.write("### Recommendations")
                    if result == "Mildew Detected":
                        st.write(
                            "* Isolate infected plants\n"
                            "* Consider fungicide treatment\n"
                            "* Improve air circulation\n"
                            "* Monitor surrounding plants"
                        )
                    else:
                        st.write(
                            "* Continue regular monitoring\n"
                            "* Maintain good ventilation\n"
                            "* Practice preventive care"
                        )
                except Exception as e:
                    st.error(f"Error analyzing image: {str(e)}")


if __name__ == "__main__":
    app()