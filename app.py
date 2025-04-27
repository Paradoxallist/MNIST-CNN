import tensorflow as tf
import os
import sys
import tkinter as tk
from application.drawing_app import DrawingApp
from application.recognition_window import RecognitionWindow
from common.config import MODEL_SAVE_PATH

class FullApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digit Drawing Application")

        # Проверяем наличие модели перед загрузкой
        if not os.path.exists(MODEL_SAVE_PATH):
            print(f"Error: Model file '{MODEL_SAVE_PATH}' not found. Please train the model first.")
            sys.exit(1)

        # Загружаем модель
        self.model = tf.keras.models.load_model(MODEL_SAVE_PATH)

        # Запускаем окно рисования
        self.drawing_app = DrawingApp(self.root)  # Передаем root

        # Запускаем окно распознавания
        self.recognition_window = RecognitionWindow(
            master=self.root,
            canvas=self.drawing_app.canvas,
            model=self.model
        )
        self.drawing_app.recognition_window = self.recognition_window  # Связали их

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FullApp()
    app.run()
