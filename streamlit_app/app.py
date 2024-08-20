import streamlit as st
from PIL import Image
import os

# Set the title of the app
st.title("Image Upload and Processing App")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Specify the directory where the images will be saved
output_dir = "data/input_images"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the original image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save the grayscale image to the output directory
    image_filename = os.path.splitext(uploaded_file.name)[0] + "_grayscale.png"
    save_path = os.path.join(output_dir, image_filename)
    image.save(save_path)

    # Notify the user that the image has been saved
    st.write(f"Image saved to: {save_path}")
