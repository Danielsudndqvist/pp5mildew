import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import os

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

    print("Setting up data generators...")
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

    print("Loading training data...")
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        classes=['healthy', 'powdery_mildew'],  # Explicitly specify classes
        subset='training'
    )

    print("Loading validation data...")
    validation_generator = train_datagen.flow_from_directory(
        TRAIN_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        classes=['healthy', 'powdery_mildew'],  # Explicitly specify classes
        subset='validation'
    )

    print("Creating model...")
    model = create_model()
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    print("Training model...")
    history = model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=15,  # Increased epochs
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

    # Save the model
    print("Saving model...")
    os.makedirs('models', exist_ok=True)
    model.save('models/mildew_model.h5')

    # Plot training history
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'])

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'])

    os.makedirs('outputs/plots', exist_ok=True)
    plt.savefig('outputs/plots/training_history.png')

    # Print class indices to verify labels
    print("\nClass indices:", train_generator.class_indices)
    
    # Evaluate model
    print("\nEvaluating model...")
    test_loss, test_accuracy = model.evaluate(validation_generator)
    print(f"Test Accuracy: {test_accuracy:.4f}")
    print(f"Test Loss: {test_loss:.4f}")

if __name__ == "__main__":
    train_model()
