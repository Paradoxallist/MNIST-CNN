import tensorflow as tf
import numpy as np


def load_and_preprocess_data():
    # Загружаем датасет MNIST
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Нормализация значений пикселей: приводим к диапазону [0, 1]
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # Добавляем ось каналов (для CNN нужно 4D: (batch_size, height, width, channels))
    x_train = np.expand_dims(x_train, axis=-1)  # (60000, 28, 28, 1)
    x_test = np.expand_dims(x_test, axis=-1)  # (10000, 28, 28, 1)

    return x_train, y_train, x_test, y_test
