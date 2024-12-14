import os
from pathlib import Path
from PIL import Image
import numpy as np


class DataLoader:
    """Handle loading and organizing image data."""

    def __init__(self, data_dir: str = 'data/cherry_leaves'):
        """Initialize with data directory."""
        self.data_dir = Path(data_dir)
        self.classes = ['healthy', 'powdery_mildew']

    def load_images(self, class_name: str, limit: int = None) -> list:
        """Load images for a specific class."""
        images = []
        class_path = self.data_dir / class_name

        if not class_path.exists():
            return images

        for img_path in list(class_path.glob('*.jpg'))[:limit]:
            with Image.open(img_path) as img:
                images.append(img.copy())

        return images

    def get_class_distribution(self) -> dict:
        """Get distribution of images across classes."""
        distribution = {}

        for class_name in self.classes:
            class_path = self.data_dir / class_name
            if class_path.exists():
                distribution[class_name] = len(list(class_path.glob('*.jpg')))

        return distribution
