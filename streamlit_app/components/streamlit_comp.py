import streamlit as st

class Streamlit_UI:
    def __init__(self) -> None:
        self.image = None
    
    def UI(self):
        # Set up the header text
        st.title("Image Segmentation App")

        # Get the input image
        self.image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        # Display a spinner till the task is done
        # with st.spinner("Processing..."): 
        #     if self.image is not None:
        #         # Display a completion message
        #         st.write("Task completed")
        #         self.display_image(image)
        #     else:
        #         st.write("No image uploaded.")
        
        return self.image
    
    def display_image(self, image):
        st.image(image)
    
if __name__ == "__main__":
    pass