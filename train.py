import tensorflow as tf
from src.data_processing.data_loader import load_data
from src.data_processing.preprocessor import preprocess_data
from src.model.model import create_model

def main():
    # Load and check data
    images, labels = load_data('data/cherry_leaves')
    print("Images shape:", images.shape)
    print("Labels shape:", labels.shape)

    # Preprocess and check data
    (train_images, train_labels), (val_images, val_labels) = preprocess_data(images, labels)
    print("Training images shape:", train_images.shape)
    print("Training labels shape:", train_labels.shape)

    # Create and train model
    model = create_model()
    model.summary()

    history = model.fit(
        train_images, train_labels,
        validation_data=(val_images, val_labels),
        epochs=10,
        batch_size=32
    )

if __name__ == "__main__":
    main()
