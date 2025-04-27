import tensorflow as tf
from common.config import LEARNING_RATE

def compile_and_train_model(
    model,
    x_train,
    y_train,
    x_val,
    y_val,
    epochs=10,
    batch_size=32,
    learning_rate=LEARNING_RATE,
):
    """
    Компиляция и обучение модели.

    Параметры:
        model: собранная модель Keras
        x_train, y_train: тренировочные данные и метки
        x_val, y_val: валидационные данные и метки
        epochs: количество эпох обучения
        batch_size: размер батча
        learning_rate: скорость обучения оптимизатора

    Возвращает:
        Обученная модель, история обучения
    """
    # Компиляция модели
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    # Обучение модели
    history = model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )

    return model, history
