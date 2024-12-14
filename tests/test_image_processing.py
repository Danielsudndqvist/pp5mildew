import os
from PIL import Image


def test_image_directories_exist():
    """Test if required image directories exist."""
    assert os.path.exists('data/cherry_leaves/healthy')
    assert os.path.exists('data/cherry_leaves/powdery_mildew')


def test_image_loading():
    """Test if images can be loaded and processed."""
    # Get path to a test image
    healthy_dir = 'data/cherry_leaves/healthy'
    test_images = os.listdir(healthy_dir)

    if test_images:
        test_image_path = os.path.join(healthy_dir, test_images[0])
        image = Image.open(test_image_path)

        # Basic image checks
        assert isinstance(image, Image.Image)
        assert image.mode in ['RGB', 'RGBA']


def test_image_dimensions():
    """Test if images have consistent dimensions."""
    # Get path to test images
    healthy_dir = 'data/cherry_leaves/healthy'
    test_images = os.listdir(healthy_dir)[:5]

    if test_images:
        first_image = Image.open(os.path.join(healthy_dir, test_images[0]))
        target_size = first_image.size

        # Check dimensions of subsequent images
        for img_name in test_images[1:]:
            img = Image.open(os.path.join(healthy_dir, img_name))
            assert img.size == target_size
