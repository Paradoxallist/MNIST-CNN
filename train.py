import os
from machine_learning.data_preprocessing import load_and_preprocess_data
from machine_learning.model_building import build_cnn_model
from machine_learning.model_training import compile_and_train_model
from machine_learning.visualization import plot_accuracy, plot_loss
from machine_learning.model_info_saver import save_model_info
from common.config import EPOCHS, BATCH_SIZE, LEARNING_RATE, MODEL_SAVE_PATH, MODEL_INFO_PATH

def train():
    # 1. Подготовка данных
    x_train, y_train, x_test, y_test = load_and_preprocess_data()

    # 2. Создание модели
    model = build_cnn_model()

    # 3. Обучение модели
    model, history = compile_and_train_model(
        model,
        x_train,
        y_train,
        x_test,
        y_test,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        learning_rate=LEARNING_RATE
    )

    # 4. Визуализация обучения
    plot_accuracy(history)
    plot_loss(history)

    # 5. Сохранение модели
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    model.save(MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}")

    # 6. Сохранение информации о модели
    save_model_info(model, history, MODEL_INFO_PATH)

if __name__ == "__main__":
    train()
