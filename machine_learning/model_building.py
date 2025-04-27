from tensorflow.keras import layers, models
from common.config import INPUT_SHAPE, NUM_CLASSES

def build_cnn_model(input_shape=INPUT_SHAPE, num_classes=NUM_CLASSES):
    model = models.Sequential()

    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))

    model.add(layers.Dense(num_classes, activation='softmax'))

    return model
