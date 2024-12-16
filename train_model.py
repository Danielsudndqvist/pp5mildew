import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

def create_model():
    """Create the CNN model architecture."""
    model = models.Sequential([
        # First Convolutional Block
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.BatchNormalization(),
        
        # Second Convolutional Block
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.BatchNormalization(),
        
        # Third Convolutional Block
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.BatchNormalization(),
        
        # Dense Layers
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

def train_model():
    """Train the mildew detection model."""
    # Set directory paths
    TRAIN_DATA_DIR = "data/cherry_leaves"
    IMAGE_SIZE = (224, 224)
    BATCH_SIZE = 32

    # Ensure data directory exists
    os.makedirs(TRAIN_DATA_DIR, exist_ok=True)

    # Data Augmentation and Preprocessing
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    # Data Generators
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        classes=['healthy', 'powdery_mildew'],
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        TRAIN_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        classes=['healthy', 'powdery_mildew'],
        subset='validation'
    )

    # Create and Compile Model
    model = create_model()
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    # Train Model
    history = model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=15,
        validation_data=validation_generator,
        validation_steps=len(validation_generator),
        callbacks=[
            tf.keras.callbacks.EarlyStopping(
                monitor='val_accuracy',
                patience=3,
                restore_best_weights=True
            )
        ]
    )

    # Save Model
    os.makedirs('models', exist_ok=True)
    model.save('models/mildew_model.h5')

    # Print Training Results
    print("\nTraining Complete!")
    print(f"Final Training Accuracy: {history.history['accuracy'][-1]:.4f}")
    print(f"Final Validation Accuracy: {history.history['val_accuracy'][-1]:.4f}")

if __name__ == "__main__":
    train_model()
