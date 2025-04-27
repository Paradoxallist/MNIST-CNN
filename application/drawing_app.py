import tkinter as tk
from tkinter import messagebox
from common.config import CANVAS_SIZE, BRUSH_SIZE, BACKGROUND_COLOR, BRUSH_COLOR, ERASER_COLOR, MIN_BRUSH_SIZE, MAX_BRUSH_SIZE
import sys

class DrawingApp:
    def __init__(self, root):
        self.root = root  # Получаем уже существующий root
        self.setup()

    def setup(self):
        # ==== ХОЛСТ ====
        self.brush_size = BRUSH_SIZE
        self.brush_color = BRUSH_COLOR
        self.eraser_mode = False
        self.last_x = None
        self.last_y = None

        self.canvas = tk.Canvas(
            self.root,
            width=CANVAS_SIZE,
            height=CANVAS_SIZE,
            bg=BACKGROUND_COLOR
        )
        self.canvas.grid(row=0, column=0, rowspan=7)

        # ==== Панель кнопок ====

        # Кнопка переключения режима
        self.mode_switch_button = tk.Button(self.root, text="Switch Mode (E)", command=self.toggle_eraser)
        self.mode_switch_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Кнопка очистки холста
        self.clear_button = tk.Button(self.root, text="Clear (C)", command=self.clear_canvas)
        self.clear_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Кнопка увеличения кисти
        self.increase_button = tk.Button(self.root, text="Brush + (+)", command=self.increase_brush_size)
        self.increase_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Кнопка уменьшения кисти
        self.decrease_button = tk.Button(self.root, text="Brush - (-)", command=self.decrease_brush_size)
        self.decrease_button.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Индикатор текущего режима
        self.mode_label = tk.Label(self.root, text="Current Mode: Brush")
        self.mode_label.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Индикатор размера кисти
        self.size_label = tk.Label(self.root, text=f"Brush Size: {self.brush_size}")
        self.size_label.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        # Кнопка подсказки
        self.help_button = tk.Button(self.root, text="?", command=self.show_help)
        self.help_button.grid(row=6, column=1, padx=10, pady=5, sticky="sew")

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=7, column=1, padx=10, pady=5, sticky="sew")

        # ==== Привязка событий ====

        self.canvas.bind("<B1-Motion>", self.paint)  # Рисование ЛКМ
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_position)  # Отпустил мышь - сброс координат
        self.root.bind("<KeyPress-e>", self.toggle_eraser)
        self.root.bind("<KeyPress-c>", self.clear_canvas)
        self.root.bind("<KeyPress-plus>", self.increase_brush_size)
        self.root.bind("<KeyPress-equal>", self.increase_brush_size)  # для ноутбуков
        self.root.bind("<KeyPress-minus>", self.decrease_brush_size)

    def paint(self, event):
        color = ERASER_COLOR if self.eraser_mode else self.brush_color
        if self.last_x and self.last_y:
            # Рисуем линию между предыдущей и текущей точкой
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                width=self.brush_size * 2,  # умножаем на 2 для естественной толщины
                fill=color,
                capstyle=tk.ROUND,
                smooth=True
            )
        else:
            # Если нет предыдущей точки — ставим круг
            self.canvas.create_oval(
                event.x - self.brush_size,
                event.y - self.brush_size,
                event.x + self.brush_size,
                event.y + self.brush_size,
                fill=color,
                outline=color
            )
        self.last_x = event.x
        self.last_y = event.y

    def reset_last_position(self, event=None):
        self.last_x = None
        self.last_y = None

    def toggle_eraser(self, event=None):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.mode_label.config(text="Current Mode: Eraser")
        else:
            self.mode_label.config(text="Current Mode: Brush")

    def clear_canvas(self, event=None):
        self.canvas.delete("all")
        self.canvas.configure(bg=BACKGROUND_COLOR)

    def increase_brush_size(self, event=None):
        if self.brush_size < MAX_BRUSH_SIZE:
            self.brush_size += 1
            self.update_size_label()

    def decrease_brush_size(self, event=None):
        if self.brush_size > MIN_BRUSH_SIZE:
            self.brush_size -= 1
            self.update_size_label()

    def update_size_label(self):
        self.size_label.config(text=f"Brush Size: {self.brush_size}")

    def show_help(self, event=None):
        help_text = (
            "Controls:\n"
            "- Left Mouse Button: Draw\n"
            "- E: Toggle between Brush and Eraser\n"
            "- C: Clear the canvas\n"
            "- + : Increase brush size\n"
            "- - : Decrease brush size\n"
        )
        messagebox.showinfo("Help", help_text)

    def run(self):
        self.root.mainloop()

    def exit_app(self):
        self.root.destroy()
        sys.exit(0)


if __name__ == "__main__":
    app = DrawingApp()
    app.run()
