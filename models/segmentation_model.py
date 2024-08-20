from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image, ImageDraw
from io import BytesIO

class Segmenting_objects:
    def __init__(self,input_image):
        # Loading the pretrained model from huggingface
        self.model_url = "facebook/detr-resnet-50"
        self.processor = DetrImageProcessor.from_pretrained(self.model_url, revision="no_timm")
        self.model = DetrForObjectDetection.from_pretrained(self.model_url, revision="no_timm")
        self.input_img = input_image
        
    def segmentation(self):
        # Passing the input image through the processor to get the input_img in the required form 
        inputs = self.processor(images=self.input_img, return_tensors="pt")
        
        # Generating the segmented objects
        outputs = self.model(**inputs)
        
        # Getting the results from the output generated, since that particular
        target_sizes = torch.tensor([self.input_img.size[::-1]])
        results = self.processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
        
        bounding_boxes = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            bounding_boxes.append([round(i, 2) for i in box.tolist()])
            
        image = self.input_img
        
        # Create an ImageDraw object using which we will draw the bounding boxes
        draw = ImageDraw.Draw(image)
        
        # Draw each bounding box
        for bbox in bounding_boxes:
            x_min, y_min, x_max, y_max = bbox
            draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=3)
        
        return image
        
if __name__ == "__main__":
    pass