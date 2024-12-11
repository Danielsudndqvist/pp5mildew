import os
from PIL import Image
import numpy as np


class DataLoader:
    """Class for loading and preprocessing image data."""
    
    def __init__(self, data_dir):
        """Initialize with data directory path."""
        self.data_dir = data_dir
        self.classes = ['healthy', 'powdery_mildew']

    def load_data(self, target_size=(224, 224)):
        """
        Load and preprocess all images.
        
        Args:
            target_size: Desired image dimensions
            
        Returns:
            tuple: (images, labels)
        """
        images = []
        labels = []
        
        for class_idx, class_name in enumerate(self.classes):
            class_path = os.path.join(self.data_dir, class_name)
            
            for image_name in os.listdir(class_path):
                if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(class_path, image_name)
                    image = Image.open(image_path)
                    image = image.resize(target_size)
                    image = np.array(image) / 255.0
                    
                    images.append(image)
                    labels.append(class_idx)
        
        return np.array(images), np.array(labels)