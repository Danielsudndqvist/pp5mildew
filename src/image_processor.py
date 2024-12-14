import cv2
import numpy as np
from PIL import Image


class ImageProcessor:
    """Process images for model prediction."""

    def __init__(self, target_size=(224, 224)):
        """Initialize with target image size."""
        self.target_size = target_size

    def preprocess(self, image):
        """
        Preprocess image for model input.
        
        Args:
            image: PIL Image or path to image
            
        Returns:
            numpy array: Processed image
        """
        if isinstance(image, str):
            image = Image.open(image)
        img = self._resize_image(image)
        img_array = np.array(img)
        return self._normalize_image(img_array)

    def _resize_image(self, image):
        """Resize image to target size."""
        return image.resize(self.target_size)

    def _normalize_image(self, img_array):
        """Normalize image array to [0,1] range."""
        return img_array.astype('float32') / 255.0

    def apply_augmentation(self, image):
        """
        Apply data augmentation to image.
        
        Args:
            image: PIL Image
            
        Returns:
            PIL Image: Augmented image
        """
        img_array = np.array(image)
        augmented = self._random_augmentation(img_array)
        return Image.fromarray(augmented)

    def _random_augmentation(self, img_array):
        """Apply random augmentation to image array."""
        angle = np.random.randint(-30, 30)
        matrix = cv2.getRotationMatrix2D(
            (img_array.shape[1] / 2, img_array.shape[0] / 2),
            angle, 1.0
        )
        rotated = cv2.warpAffine(
            img_array, matrix,
            (img_array.shape[1], img_array.shape[0])
        )
        return rotated
