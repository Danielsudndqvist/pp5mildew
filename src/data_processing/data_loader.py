import os
import cv2
import numpy as np

def load_data(data_dir):
    images = []
    labels = []
    for label in ['healthy', 'powdery_mildew']:
        path = os.path.join(data_dir, label)
        for img_name in os.listdir(path):
            img = cv2.imread(os.path.join(path, img_name))
            img = cv2.resize(img, (224, 224))
            images.append(img)
            labels.append(1 if label == 'powdery_mildew' else 0)
    return np.array(images), np.array(labels)