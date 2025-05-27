import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math
from sympy import sympify, Symbol
from sympy.utilities.lambdify import lambdify

class GoldenSectionView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Método de Sección Dorada", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        # Entrada para la función
        tk.Label(self, text="Función f(x):", bg="#121212", fg="white").pack()
        self.entry_function = tk.Entry(self, width=40)
        self.entry_function.insert(0, "-x**4-2*x**3-8*x**2-5*x")
        self.entry_function.pack(pady=5)

        tk.Label(self, text="Límite inferior (a):", bg="#121212", fg="white").pack()
        self.entry_a = tk.Entry(self, width=30)
        self.entry_a.insert(0, "-2")
        self.entry_a.pack(pady=5)

        tk.Label(self, text="Límite superior (b):", bg="#121212", fg="white").pack()
        self.entry_b = tk.Entry(self, width=30)
        self.entry_b.insert(0, "1")
        self.entry_b.pack(pady=5)

        tk.Label(self, text="Tolerancia:", bg="#121212", fg="white").pack()
        self.entry_tol = tk.Entry(self, width=30)
        self.entry_tol.insert(0, "0.01")
        self.entry_tol.pack(pady=5)

        tk.Button(self, text="Calcular", command=self.calculate,
                  font=("Helvetica", 12), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=15, pady=5).pack(pady=10)

        tk.Button(self, text="Atrás", command=self.controller.show_methods,
                  font=("Helvetica", 12, "bold"), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=20, pady=10).pack(pady=10)

    def calculate(self):
        try:
            func_str = self.entry_function.get()
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            tol = float(self.entry_tol.get())

            x_max, fx_max, log, history = self.controller.solve_golden_section(func_str, a, b, tol)
            self.controller.show_popup("Iteraciones - Sección Dorada", log)

            # Mostrar gráfica automáticamente después de mostrar el popup de texto
            self.show_graph_popup(func_str, a, b, history)

        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def show_graph_popup(self, func_str, a, b, history):
        popup = tk.Toplevel(self)
        popup.title("Gráfica - Método Sección Dorada")
        popup.geometry("700x500")
        popup.configure(bg="#121212")

        fig, ax = plt.subplots(figsize=(7,5), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.get_tk_widget().pack(fill="both", expand=True)


        x = Symbol('x')
        expr = sympify(func_str)
        f = lambdify(x, expr, modules=["math"])

        x_vals = np.linspace(a - (b - a)*0.1, b + (b - a)*0.1, 400)
        y_vals = np.array([f(xi) for xi in x_vals])

        ax.plot(x_vals, y_vals, label='f(x)', color='cyan', linewidth=2)

        for (a_i, b_i, c_i, d_i, f_c, f_d) in history:
            ax.axvline(a_i, color='gray', linestyle='--', alpha=0.3, label='Límite inferior' if 'Límite inferior' not in ax.get_legend_handles_labels()[1] else "")
            ax.axvline(b_i, color='gray', linestyle='--', alpha=0.3, label='Límite superior' if 'Límite superior' not in ax.get_legend_handles_labels()[1] else "")
            ax.plot(c_i, f_c, 'ro', label='c (evaluado)' if 'c (evaluado)' not in ax.get_legend_handles_labels()[1] else "")
            ax.plot(d_i, f_d, 'bo', label='d (evaluado)' if 'd (evaluado)' not in ax.get_legend_handles_labels()[1] else "")

        ax.set_title("Método de Sección Dorada", color='white', fontsize=14)
        ax.legend(loc='upper right')
        ax.grid(True, linestyle='--', alpha=0.4)
        ax.set_facecolor("#121212")
        fig.patch.set_facecolor("#121212")

        ax.tick_params(colors='white', which='both')
        ax.yaxis.label.set_color('white')
        ax.xaxis.label.set_color('white')

        canvas.draw()



