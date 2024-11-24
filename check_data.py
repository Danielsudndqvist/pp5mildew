import os

def check_data():
    base_dir = 'data/cherry_leaves'
    
    print("Checking directory structure:")
    for root, dirs, files in os.walk(base_dir):
        print(f"\nDirectory: {root}")
        print(f"Number of files: {len(files)}")
        if files:
            print(f"Sample files: {files[:3]}")
            
    # Check specific directories
    healthy_dir = os.path.join(base_dir, 'healthy')
    mildew_dir = os.path.join(base_dir, 'powdery_mildew')
    
    print("\nCounting images in each category:")
    if os.path.exists(healthy_dir):
        healthy_images = [f for f in os.listdir(healthy_dir) if f.endswith('.JPG')]
        print(f"Healthy images: {len(healthy_images)}")
    else:
        print("Healthy directory not found")
        
    if os.path.exists(mildew_dir):
        mildew_images = [f for f in os.listdir(mildew_dir) if f.endswith('.JPG')]
        print(f"Mildew images: {len(mildew_images)}")
    else:
        print("Mildew directory not found")

if __name__ == "__main__":
    check_data()