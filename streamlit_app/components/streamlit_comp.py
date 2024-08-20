import streamlit as st

class Streamlit_UI:
    def __init__(self) -> None:
        pass
    
    def UI(self):
        # Set up the header text
        st.title("Image Segmentation App")

        # Get the input image
        image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        # Display a spinner till the task is done
        with st.spinner("Processing..."):
            # Simulate a process (like a model prediction)
            st.write("Task completed")

if __name__ == "__main__":
    pass