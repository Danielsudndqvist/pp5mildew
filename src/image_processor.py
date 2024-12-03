import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """Load and preprocess a single image"""
    img = Image.open(image_path)
    img = img.resize(target_size)
    img = np.array(img) / 255.0  # Normalize to [0,1]
    return img

def generate_average_images():
    """Generate and save average images for both classes"""
    # Paths
    healthy_path = "inputs/cherry-leaves/healthy"
    mildew_path = "inputs/cherry-leaves/powdery_mildew"
    output_path = "outputs"
    
    # Create outputs directory if it doesn't exist
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
    
    # Calculate difference
    difference = np.abs(avg_healthy - avg_mildew)
    difference = ((difference - difference.min()) / (difference.max() - difference.min()) * 255).astype(np.uint8)
    
    # Save images
    Image.fromarray(avg_healthy).save(os.path.join(output_path, 'avg_healthy.png'))
    Image.fromarray(avg_mildew).save(os.path.join(output_path, 'avg_mildew.png'))
    Image.fromarray(difference).save(os.path.join(output_path, 'avg_difference.png'))

def generate_summary_plots():
    """Generate and save summary plots"""
    healthy_path = "inputs/cherry-leaves/healthy"
    mildew_path = "inputs/cherry-leaves/powdery_mildew"
    output_path = "outputs"
    
    # Count images
    healthy_count = len([f for f in os.listdir(healthy_path) 
                        if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    mildew_count = len([f for f in os.listdir(mildew_path) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    
    # Create distribution plot
    plt.figure(figsize=(10, 6))
    plt.bar(['Healthy', 'Infected'], [healthy_count, mildew_count])
    plt.title('Distribution of Leaf Images')
    plt.ylabel('Number of Images')
    plt.savefig(os.path.join(output_path, 'distribution.png'))
    plt.close()

def main():
    """Main function to generate all visualizations"""
    print("Generating average images...")
    generate_average_images()
    print("Generating summary plots...")
    generate_summary_plots()
    print("Visualization generation complete!")

if __name__ == "__main__":
    main()