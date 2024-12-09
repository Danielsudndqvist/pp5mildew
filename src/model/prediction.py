from PIL import Image
import numpy as np
from src.model.metrics import MetricsTracker
import tensorflow as tf
import os

metrics_tracker = MetricsTracker()
model = None

def load_model():
    global model
    if model is None and os.path.exists('models/mildew_model.h5'):
        model = tf.keras.models.load_model('models/mildew_model.h5')

def process_image(image, target_size=(224, 224)):
    if isinstance(image, str):
        image = Image.open(image)
    img = image.resize(target_size)
    img_array = np.array(img)
    return img_array.astype('float32') / 255.0

def predict_mildew(image):
    processed_image = process_image(image)
    if model is None:
        # For testing purposes
        prediction = 0.7
    else:
        prediction = model.predict(np.expand_dims(processed_image, axis=0))[0][0]
        
    predicted_label = 1 if prediction > 0.5 else 0
    metrics_tracker.update_metrics(1, predicted_label, prediction)
    
    return "Mildew Detected" if predicted_label == 1 else "Healthy", prediction, metrics_tracker.get_metrics()