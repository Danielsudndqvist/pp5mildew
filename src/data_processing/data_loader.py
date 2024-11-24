import os
import cv2
import numpy as np

def load_data(data_dir):
    images = []
    labels = []
    
    # Load healthy images
    healthy_dir = os.path.join(data_dir, 'healthy')
    if os.path.exists(healthy_dir):
        for img_name in os.listdir(healthy_dir):
            if img_name.endswith('.JPG'):
                img_path = os.path.join(healthy_dir, img_name)
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, (224, 224))
                    images.append(img)
                    labels.append(0)  # 0 for healthy

    # Load mildew images
    mildew_dir = os.path.join(data_dir, 'powdery_mildew')
    if os.path.exists(mildew_dir):
        for img_name in os.listdir(mildew_dir):
            if img_name.endswith('.JPG'):
                img_path = os.path.join(mildew_dir, img_name)
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, (224, 224))
                    images.append(img)
                    labels.append(1)  # 1 for mildew

    print(f"Total images loaded: {len(images)}")
    return np.array(images), np.array(labels)