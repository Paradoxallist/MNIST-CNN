import tkinter as tk
import numpy as np
from PIL import Image, ImageGrab, ImageOps, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from common.config import GRID_SIZE
import tensorflow as tf

class RecognitionWindow:
    def __init__(self, master, canvas, model):
        self.master = tk.Toplevel(master)
        self.master.title("Digit Recognition")

        self.canvas_widget = canvas
        self.model = model

        # ==== График вероятностей ====
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.bar_canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.bar_canvas.get_tk_widget().pack()

        # ==== Окно обработанного изображения ====
        self.processed_window = tk.Toplevel(master)
        self.processed_window.title("Processed Image")

        self.processed_label = tk.Label(self.processed_window)
        self.processed_label.pack()

        # Для остановки after
        self.after_id = None

        self.is_running = True

        # Обработчик закрытия всех окон
        self.master.protocol("WM_DELETE_WINDOW", self.close_all_windows)

        # Запуск обновления
        self.update_chart()

    def preprocess_canvas_image(self, show_processed=False):
        # Получаем координаты холста
        self.master.update()
        x = self.canvas_widget.winfo_rootx()
        y = self.canvas_widget.winfo_rooty()
        w = x + self.canvas_widget.winfo_width()
        h = y + self.canvas_widget.winfo_height()

        # Снимок холста
        img = ImageGrab.grab(bbox=(x, y, w, h)).convert('L')
        img = ImageOps.invert(img)  # Инвертируем цвета

        # Переводим в numpy
        img_array = np.array(img)

        # Находим непустые пиксели
        coords = np.column_stack(np.where(img_array > 0))
        if coords.size > 0:
            top_left = coords.min(axis=0)
            bottom_right = coords.max(axis=0)

            cropped = img_array[
                      top_left[0]:bottom_right[0] + 1,
                      top_left[1]:bottom_right[1] + 1
                      ]
        else:
            cropped = img_array

        # Масштабируем так, чтобы максимальная сторона была 20 пикселей
        cropped_img = Image.fromarray(cropped)
        max_side = max(cropped_img.size)
        scaling_factor = 20.0 / max_side
        new_size = (max(1, int(cropped_img.size[0] * scaling_factor)),
                    max(1, int(cropped_img.size[1] * scaling_factor)))
        resized_img = cropped_img.resize(new_size, Image.LANCZOS)

        # Создаем пустое 28x28 изображение
        new_img = Image.new('L', (28, 28), 0)

        # Вставляем цифру в центр
        upper_left = ((28 - new_size[0]) // 2, (28 - new_size[1]) // 2)
        new_img.paste(resized_img, upper_left)

        # Нормализуем
        img_array = np.array(new_img).astype('float32') / 255.0
        img_array = np.expand_dims(img_array, axis=(0, -1))  # (batch, height, width, channels)

        if show_processed:
            display_img = Image.fromarray(np.uint8(np.squeeze(img_array) * 255))
            display_img = display_img.resize((140, 140))  # увеличиваем для удобства просмотра
            display_img = ImageTk.PhotoImage(display_img)

            self.processed_label.configure(image=display_img)
            self.processed_label.image = display_img

        return img_array

    def update_chart(self):
        if not self.is_running:
            return  # Если закрыто — сразу выходим

        try:
            input_img = self.preprocess_canvas_image(show_processed=True)
            predictions = self.model.predict(input_img, verbose=0)[0]

            self.ax.clear()
            self.ax.bar(range(10), predictions, color='skyblue')
            self.ax.set_ylim([0, 1])
            self.ax.set_xticks(range(10))
            self.ax.set_xlabel('Digit')
            self.ax.set_ylabel('Probability')
            self.ax.set_title('Digit Recognition Prediction')
            self.bar_canvas.draw()

            self.after_id = self.master.after(500, self.update_chart)

        except Exception as e:
            print(f"Exception caught in update_chart: {e}")
            # В случае любой ошибки (уничтожено окно, уже нет ресурсов) — просто молчим
            pass

    def close_all_windows(self):
        self.is_running = False
        if self.after_id is not None:
            try:
                self.master.after_cancel(self.after_id)
            except Exception:
                pass
        try:
            self.master.destroy()
        except Exception:
            pass
        try:
            self.processed_window.destroy()
        except Exception:
            pass

