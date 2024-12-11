import numpy as np
from PIL import Image
import os


def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """
    Load and preprocess a single image.
    
    Args:
        image_path: Path to the image
        target_size: Desired size for the image
        
    Returns:
        Preprocessed image array
    """
    img = Image.open(image_path)
    img = img.resize(target_size)
    img = np.array(img) / 255.0
    return img


def generate_average_images():
    """
    Generate and save average images for both classes.
    
    Returns:
        tuple: Paths to generated average images
    """
    healthy_path = "inputs/cherry-leaves/healthy"
    mildew_path = "inputs/cherry-leaves/powdery_mildew"
    output_path = "outputs"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Initialize arrays for averaging
    healthy_sum = np.zeros((224, 224, 3))
    mildew_sum = np.zeros((224, 224, 3))
    healthy_count = 0
    mildew_count = 0
    
    # Process healthy leaves
    for img_name in os.listdir(healthy_path):
        if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(healthy_path, img_name)
            img = load_and_preprocess_image(img_path)
            healthy_sum += img
            healthy_count += 1
    
    # Process infected leaves
    for img_name in os.listdir(mildew_path):
        if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(mildew_path, img_name)
            img = load_and_preprocess_image(img_path)
            mildew_sum += img
            mildew_count += 1
    
    # Calculate averages
    avg_healthy = (healthy_sum / healthy_count * 255).astype(np.uint8)
    avg_mildew = (mildew_sum / mildew_count * 255).astype(np.uint8)
    
    # Save images
    healthy_out = os.path.join(output_path, 'avg_healthy.png')
    mildew_out = os.path.join(output_path, 'avg_mildew.png')
    
    Image.fromarray(avg_healthy).save(healthy_out)
    Image.fromarray(avg_mildew).save(mildew_out)
    
    return healthy_out, mildew_out


def main():
    """Generate all visualizations."""
    print("Generating average images...")
    generate_average_images()
    print("Visualization generation complete!")


if __name__ == "__main__":
    main()