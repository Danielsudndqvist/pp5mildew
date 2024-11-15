import streamlit as st

def main():
    st.title("Cherry Leaf Mildew Detection")
    uploaded_file = st.file_uploader("Upload leaf image", type=['jpg', 'png'])
    
    if uploaded_file:
        # Add processing logic later
        st.image(uploaded_file, caption='Uploaded Image')

if __name__ == "__main__":
    main()