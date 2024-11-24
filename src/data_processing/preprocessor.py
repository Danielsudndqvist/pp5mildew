import numpy as np

def preprocess_data(images, labels):
    images = images.astype('float32') / 255.0
    train_size = int(0.8 * len(images))
    
    train_images = images[:train_size]
    train_labels = labels[:train_size]
    val_images = images[train_size:]
    val_labels = labels[train_size:]
    
    return (train_images, train_labels), (val_images, val_labels)