import os
import sys
from PIL import Image
from io import BytesIO

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streamlit_app.components.streamlit_comp import Streamlit_UI
from models.segmentation_model import Segmenting_objects

def main_page():
    # Create an instance of the Streamlit_UI class
    app = Streamlit_UI()

    # Display the streamlit page by calling the UI method
    uploaded_image = app.UI()
    
    # call the segmentation_model if the image is uploaded
    if uploaded_image is not None:
        # Convert the UploadedFile object to PIL Image
        image = Image.open(BytesIO(uploaded_image.read()))
        
        # Create an instance of Segmenting_objects
        segmenter = Segmenting_objects(image)
        
        # Call the segmentation function
        boxed_image = segmenter.segmentation()
    
        # Display the segmented image
        if boxed_image is not None:
            app.display_image(boxed_image)     

if __name__ == "__main__":
    main_page()
