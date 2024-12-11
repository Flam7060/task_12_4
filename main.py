import numpy as np
import tkinter as tk
from tkinter import messagebox


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.check_validity()

    def check_validity(self):
        """Проверка корректности сторон треугольника."""
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError(
                "Стороны треугольника не могут быть меньше или равны нулю."
            )
        if (
            self.a + self.b <= self.c
            or self.a + self.c <= self.b
            or self.b + self.c <= self.a
        ):
            raise ValueError("Сумма двух сторон должна быть больше третьей.")

    def type_by_sides(self):
        """Определение типа треугольника по сторонам."""
        if self.a == self.b == self.c:
            return "Равносторонний"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Равнобедренный"
        return "Разносторонний"

    def area(self):
        """Вычисление площади треугольника по формуле Герона."""
        s = (self.a + self.b + self.c) / 2  # Полупериметр
        return np.sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )  # Площадь по формуле Герона

    def angles(self):
        """Вычисление углов треугольника с использованием теоремы косинусов."""
        cos_A = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        cos_B = (self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)
        cos_C = (self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)

        angle_A = np.arccos(np.clip(cos_A, -1, 1))
        angle_B = np.arccos(np.clip(cos_B, -1, 1))
        angle_C = np.arccos(np.clip(cos_C, -1, 1))

        return np.degrees(angle_A), np.degrees(angle_B), np.degrees(angle_C)

    def type_by_angles(self):
        """Определение типа углов треугольника."""
        angles = self.angles()
        if any(angle > 90 for angle in angles):
            return "Тупоугольный"
        elif any(angle == 90 for angle in angles):
            return "Прямоугольный"
        return "Остроугольный"


class TriangleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор треугольников")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.config(bg="#f4f4f4")

        self.create_widgets()

    def create_widgets(self):
        """Создание интерфейса пользователя."""
        input_frame = tk.Frame(self.root, bg="#f4f4f4")
        input_frame.pack(pady=20)

        self.create_input_field(input_frame, "Длина первой стороны:", 0)
        self.create_input_field(input_frame, "Длина второй стороны:", 1)
        self.create_input_field(input_frame, "Длина третьей стороны:", 2)

        calc_button = tk.Button(
            self.root,
            text="Вычислить",
            command=self.calculate,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
        )
        calc_button.pack(pady=20)

        result_frame = tk.Frame(self.root, bg="#f4f4f4")
        result_frame.pack(pady=10)

        self.result_label = self.create_result_label(result_frame)
        self.area_label = self.create_result_label(result_frame)
        self.angle_label = self.create_result_label(result_frame)
        self.angles_label = self.create_result_label(result_frame)

    def create_input_field(self, parent, text, row):
        """Создание поля ввода."""
        tk.Label(parent, text=text, bg="#f4f4f4").grid(
            row=row, column=0, padx=10, pady=5, sticky="w"
        )
        entry = tk.Entry(parent)
        entry.grid(row=row, column=1, padx=10, pady=5)
        setattr(self, f"entry_{row}", entry)

    def create_result_label(self, parent):
        """Создание метки для отображения результатов."""
        label = tk.Label(parent, text="", bg="#f4f4f4", font=("Arial", 10))
        label.grid(row=parent.grid_size()[1], column=0, padx=10, pady=5, sticky="w")
        return label

    def calculate(self):
        """Обработчик вычислений."""
        try:
            a = float(self.entry_0.get())
            b = float(self.entry_1.get())
            c = float(self.entry_2.get())

            triangle = Triangle(a, b, c)

            self.result_label.config(
                text=f"Тип треугольника по сторонам: {triangle.type_by_sides()}"
            )
            self.area_label.config(text=f"Площадь треугольника: {triangle.area():.2f}")
            self.angle_label.config(
                text=f"Тип треугольника по углам: {triangle.type_by_angles()}"
            )
            self.angles_label.config(
                text=f"Углы треугольника: {', '.join(f'{angle:.2f}' for angle in triangle.angles())}"
            )

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleCalculatorApp(root)
    root.mainloop()
