# config.py

# ==== Параметры обучения ====
EPOCHS = 10
BATCH_SIZE = 32
LEARNING_RATE = 0.001

# ==== Параметры модели ====
INPUT_SHAPE = (28, 28, 1)
NUM_CLASSES = 10

# ==== Пути для сохранения моделей ====
MODEL_SAVE_PATH = "models/cnn_model.keras"
MODEL_INFO_PATH = "models/model_info.txt"

# ==== Параметры окна для рисования ====
CANVAS_SIZE = 280  # Размер самого окна (в пикселях)
GRID_SIZE = 28     # Сетка для приведения к 28x28 перед подачей в модель
BRUSH_SIZE = 8     # Толщина кисти (пиксели)

# ==== Цвета для окна ====
BACKGROUND_COLOR = "white"    # Цвет фона
BRUSH_COLOR = "black"         # Цвет кисти
ERASER_COLOR = "white"         # Цвет стирания (тот же, что фон)

MIN_BRUSH_SIZE = 1
MAX_BRUSH_SIZE = 30
