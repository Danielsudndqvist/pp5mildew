from PIL import Image
import numpy as np
from src.model.metrics import MetricsTracker
import tensorflow as tf

metrics_tracker = MetricsTracker()
model = tf.keras.models.load_model('models/mildew_model.h5')

def process_image(image, target_size=(224, 224)):
    if isinstance(image, str):
        image = Image.open(image)
    img = image.resize(target_size)
    img_array = np.array(img)
    processed = img_array.astype('float32') / 255.0
    return np.expand_dims(processed, axis=0)

def predict_mildew(image):
    processed_image = process_image(image)
    prediction = model.predict(processed_image)[0][0]
    predicted_label = 1 if prediction > 0.5 else 0
    
    # For demo purposes, assuming true label is 1 (infected)
    # In production, you'd get this from user input or ground truth
    true_label = 1
    
    metrics_tracker.update_metrics(true_label, predicted_label, prediction)
    metrics = metrics_tracker.get_metrics()
    
    result = "Mildew Detected" if predicted_label == 1 else "Healthy"
    return result, prediction, metrics