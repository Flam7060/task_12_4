import tkinter as tk
from tkinter import messagebox
from simpleeval import simple_eval
import numpy as np


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Calculator")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(
            self.root,
            font=("Arial", 24),
            bd=10,
            relief=tk.RIDGE,
            justify="right",
            bg="#ffffff",
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 3),
            ("C", 5, 0),
            ("sqrt", 5, 1),
            ("^", 5, 2),
            ("log", 5, 3),
        ]

        for text, row, col in buttons:
            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18),
                bd=4,
                relief=tk.RAISED,
                bg="#e6e6e6",
                activebackground="#cccccc",
                command=lambda t=text: self.on_button_click(t),
            )
            button.grid(
                row=row, column=col, padx=10, pady=10, sticky="nsew", ipadx=20, ipady=20
            )

        equal_button = tk.Button(
            self.root,
            text="=",
            font=("Arial", 18),
            bd=4,
            relief=tk.RAISED,
            bg="#ffcccb",
            activebackground="#ff9999",
            command=self.calculate,
        )
        equal_button.grid(
            row=4, column=2, padx=10, pady=10, sticky="nsew", ipadx=20, ipady=20
        )

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)

    def on_button_click(self, button_text):
        match button_text:
            case "C":
                self.entry.delete(0, tk.END)
            case "sqrt":
                self.insert_function("sqrt(")
            case "log":
                self.insert_function("log10(")
            case "^":
                self.entry.insert(tk.END, "**")
            case _:
                self.entry.insert(tk.END, button_text)

    def insert_function(self, func):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{func}{current_text})")

    def calculate(self):
        expression = self.entry.get()
        try:
            result = simple_eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
