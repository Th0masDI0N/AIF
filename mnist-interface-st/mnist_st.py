import streamlit as st
import requests
from PIL import Image
import io

st.title("Image Classifier")

uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    
    # Convert image to bytes
    img_binary = io.BytesIO()
    image.save(img_binary, format="PNG")
    img_bytes = img_binary.getvalue()
    
    # Send request to API
    if st.button("Predict"):
        #response = requests.post("http://127.0.0.1:5000/predict", data=img_bytes)
        response = requests.post("http://mnist-flask-app:5000/predict", data=img_bytes)
        if response.status_code == 200:
            predicted_label = response.json().get("prediction", "No prediction available")
            st.write(f"**Predicted Label:** {predicted_label}")
        else:
            st.write("Error in prediction request V2")