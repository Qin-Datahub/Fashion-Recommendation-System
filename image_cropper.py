from ultralytics import YOLO
from PIL import Image

class ImageCropper:
    def __init__(self):
        "Load weights of the yolov8."
        self.model = YOLO('yolov8n-seg.pt') 
    
    def crop(self, image_path):
        """Crop the image, keep only the area of interest."""
        results = self.model(image_path, stream=False)

        # Get coordinates for the area of interest
        x_min, y_min, x_max, y_max = results[0].boxes.xyxy[0].numpy().flatten()
        
        # Crop image and save it (reuse the same path)
        img = Image.open(image_path)
        cropped_img = img.crop((x_min, y_min, x_max, y_max))
        cropped_img.save(image_path)
