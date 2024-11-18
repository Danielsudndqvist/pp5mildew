import tensorflow as tf

def preprocess_data(images, labels):
    # Normalize images
    images = images / 255.0
    
    # Split data
    train_images, val_images = images[:int(0.8*len(images))], images[int(0.8*len(images)):]
    train_labels, val_labels = labels[:int(0.8*len(labels))], labels[int(0.8*len(labels)):]
    
    return (train_images, train_labels), (val_images, val_labels)

# src/model/model.py
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(224, 224, 3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam',
                 loss='binary_crossentropy',
                 metrics=['accuracy'])
    return model

# Training script
def train_model():
    images, labels = load_data('data/cherry_leaves')
    (train_images, train_labels), (val_images, val_labels) = preprocess_data(images, labels)
    
    model = create_model()
    history = model.fit(train_images, train_labels,
                       epochs=10,
                       validation_data=(val_images, val_labels))
    
    model.save('models/mildew_detector.h5')
    return history