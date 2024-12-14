import os
import shutil

def organize_images():
    # Source directories
    source_healthy = 'data/cherry_leaves/cherry-leaves/healthy'
    source_mildew = 'data/cherry_leaves/cherry-leaves/powdery_mildew'

    # Target directories
    target_healthy = 'data/cherry_leaves/healthy'
    target_mildew = 'data/cherry_leaves/powdery_mildew'

    # Create target directories
    os.makedirs(target_healthy, exist_ok=True)
    os.makedirs(target_mildew, exist_ok=True)

    # Move healthy images
    if os.path.exists(source_healthy):
        for filename in os.listdir(source_healthy):
            src = os.path.join(source_healthy, filename)
            dst = os.path.join(target_healthy, filename)
            shutil.copy2(src, dst)

    # Move mildew images
    if os.path.exists(source_mildew):
        for filename in os.listdir(source_mildew):
            src = os.path.join(source_mildew, filename)
            dst = os.path.join(target_mildew, filename)
            shutil.copy2(src, dst)

    print("Images organized!")
    print(f"Healthy images: {len(os.listdir(target_healthy))}")
    print(f"Mildew images: {len(os.listdir(target_mildew))}")

if __name__ == "__main__":
    organize_images()
