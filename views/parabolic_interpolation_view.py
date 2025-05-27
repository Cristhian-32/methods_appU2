import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math
from sympy import sympify, Symbol
from sympy.utilities.lambdify import lambdify

class ParabolicInterpolationView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Método de Interpolación Parabólica", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        # Entrada para la función
        tk.Label(self, text="Función f(x):", bg="#121212", fg="white").pack()
        self.entry_function = tk.Entry(self, width=40)
        self.entry_function.insert(0, "-x**4-2*x**3-8*x**2-5*x")
        self.entry_function.pack(pady=5)

        # Entradas para x0, x1, x2
        tk.Label(self, text="x0:", bg="#121212", fg="white").pack()
        self.entry_x0 = tk.Entry(self, width=30)
        self.entry_x0.insert(0, "-2")
        self.entry_x0.pack(pady=5)

        tk.Label(self, text="x1:", bg="#121212", fg="white").pack()
        self.entry_x1 = tk.Entry(self, width=30)
        self.entry_x1.insert(0, "-1")
        self.entry_x1.pack(pady=5)

        tk.Label(self, text="x2:", bg="#121212", fg="white").pack()
        self.entry_x2 = tk.Entry(self, width=30)
        self.entry_x2.insert(0, "1")
        self.entry_x2.pack(pady=5)

        # Entrada para tolerancia
        tk.Label(self, text="Tolerancia:", bg="#121212", fg="white").pack()
        self.entry_tol = tk.Entry(self, width=30)
        self.entry_tol.insert(0, "0.01")
        self.entry_tol.pack(pady=5)

        # NUEVA Entrada para cantidad de iteraciones
        tk.Label(self, text="Cantidad de iteraciones:", bg="#121212", fg="white").pack()
        self.entry_iterations = tk.Entry(self, width=30)
        self.entry_iterations.insert(0, "10")
        self.entry_iterations.pack(pady=5)

        tk.Button(self, text="Calcular", command=self.calculate,
                  font=("Helvetica", 12), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=15, pady=5).pack(pady=10)

        tk.Button(self, text="Atrás", command=self.controller.show_methods,
                  font=("Helvetica", 12, "bold"), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=20, pady=10).pack(pady=10)

    def calculate(self):
        try:
            func_str = self.entry_function.get()
            x0 = float(self.entry_x0.get())
            x1 = float(self.entry_x1.get())
            x2 = float(self.entry_x2.get())
            tol = float(self.entry_tol.get())
            iterations = int(self.entry_iterations.get())  # NUEVO

            x_max, fx_max, log, history = self.controller.solve_parabolic_interpolation(func_str, x0, x1, x2, tol, iterations)

            self.controller.show_popup("Iteraciones - Interpolación Parabólica", log)
            self.show_graph_popup(func_str, history)

        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def show_graph_popup(self, func_str, history):

        popup = tk.Toplevel(self)
        popup.title("Gráfica - Método Interpolación Parabólica")
        popup.geometry("700x500")
        popup.configure(bg="#121212")

        fig, ax = plt.subplots(figsize=(7,5), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.get_tk_widget().pack(fill="both", expand=True)

        xs = [row['x0'] for row in history] + [row['x1'] for row in history] + [row['x2'] for row in history] + [row['x3'] for row in history]
        x_min, x_max = min(xs), max(xs)
        padding = (x_max - x_min) * 0.2 if x_max != x_min else 1
        x_vals = np.linspace(x_min - padding, x_max + padding, 400)

        # Interpretar la función usando sympy y lambdify
        x = Symbol('x')
        expr = sympify(func_str)
        f = lambdify(x, expr, modules=["math"])

        y_vals = np.array([f(xi) for xi in x_vals])
        ax.plot(x_vals, y_vals, label='f(x)', color='cyan')

        for row in history:
            ax.plot(row['x0'], row['f0'], 'ro', label='x0' if row['i'] == 1 else "")
            ax.plot(row['x1'], row['f1'], 'go', label='x1' if row['i'] == 1 else "")
            ax.plot(row['x2'], row['f2'], 'bo', label='x2' if row['i'] == 1 else "")
            ax.plot(row['x3'], row['f3'], 'mo', label='x3 (nuevo)' if row['i'] == 1 else "")

        ax.set_title("Método Interpolación Parabólica", color='white')
        ax.legend()
        ax.grid(True)
        ax.set_facecolor("#121212")
        fig.patch.set_facecolor("#121212")
        ax.tick_params(colors='white')
        ax.yaxis.label.set_color('white')
        ax.xaxis.label.set_color('white')

        canvas.draw()

