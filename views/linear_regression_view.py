import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class LinearRegressionView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Regresión Lineal - Mínimos Cuadrados", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        tk.Label(self, text="Datos X (separados por comas):", bg="#121212", fg="white").pack()
        self.entry_x = tk.Entry(self, width=50)
        self.entry_x.insert(0, "1, 2, 3, 4, 5, 6, 7, 8, 9")
        self.entry_x.pack(pady=5)

        tk.Label(self, text="Datos Y (separados por comas):", bg="#121212", fg="white").pack()
        self.entry_y = tk.Entry(self, width=50)
        self.entry_y.insert(0, "1, 1.5, 2, 3, 4, 5, 8, 10, 13")
        self.entry_y.pack(pady=5)

        tk.Button(self, text="Calcular", command=self.calculate,
                  font=("Helvetica", 12), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=15, pady=5).pack(pady=10)

        tk.Button(self, text="Atrás", command=self.controller.show_methods,
                  font=("Helvetica", 12, "bold"), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=20, pady=10).pack(pady=10)

    def calculate(self):
        try:
            x_str = self.entry_x.get()
            y_str = self.entry_y.get()

            m, b, s, r, log = self.controller.solve_linear_regression(x_str, y_str)

            self.controller.show_popup("Resultado - Regresión Lineal", log)
            self.show_graph_popup(m, b, x_str, y_str)

        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")


    def show_graph_popup(self, m, b, x_str, y_str):
        popup = tk.Toplevel(self)
        popup.title("Gráfica - Regresión Lineal")
        popup.geometry("700x500")
        popup.configure(bg="#121212")

        fig, ax = plt.subplots(figsize=(7,5), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.get_tk_widget().pack(fill="both", expand=True)

        x_vals = np.array([float(x.strip()) for x in x_str.split(',')])
        y_vals = np.array([float(y.strip()) for y in y_str.split(',')])

        ax.scatter(x_vals, y_vals, color='red', label='Datos')

        x_line = np.linspace(min(x_vals), max(x_vals), 400)
        y_line = m * x_line + b
        ax.plot(x_line, y_line, color='cyan', label='Recta de regresión')

        ax.set_title("Regresión Lineal - Mínimos Cuadrados", color='white')
        ax.legend()
        ax.grid(True)
        ax.set_facecolor("#121212")
        fig.patch.set_facecolor("#121212")
        ax.tick_params(colors='white')
        ax.yaxis.label.set_color('white')
        ax.xaxis.label.set_color('white')

        canvas.draw()
