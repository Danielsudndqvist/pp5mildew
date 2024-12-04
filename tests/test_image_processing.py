import pytest
from PIL import Image
import numpy as np
import os
from src.data_management import load_images_data  # adjust import based on your structure

def test_image_directories_exist():
    """Test if the image directories exist"""
    assert os.path.exists('data/cherry-leaves/healthy')
    assert os.path.exists('data/cherry-leaves/powdery_mildew')

def test_image_loading():
    """Test if we can load and process images"""
    # Get path to a test image
    healthy_dir = 'data/cherry-leaves/healthy'
    test_images = os.listdir(healthy_dir)
    
    if test_images:
        test_image_path = os.path.join(healthy_dir, test_images[0])
        image = Image.open(test_image_path)
        
        # Basic image checks
        assert isinstance(image, Image.Image)
        assert image.mode in ['RGB', 'RGBA']
        assert image.size[0] > 0
        assert image.size[1] > 0

def test_image_dimensions():
    """Test if images have consistent dimensions"""
    healthy_dir = 'data/cherry-leaves/healthy'
    test_images = os.listdir(healthy_dir)[:5]  # Test first 5 images
    
    if test_images:
        first_image = Image.open(os.path.join(healthy_dir, test_images[0]))
        target_size = first_image.size
        
        for img_name in test_images[1:]:
            img = Image.open(os.path.join(healthy_dir, img_name))
            assert img.size == target_size, f"Image {img_name} has inconsistent dimensions"