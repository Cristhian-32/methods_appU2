import tkinter as tk
from tkinter import messagebox

class NewtonInterpolationView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Interpolación de Newton", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        tk.Label(self, text="Valores x separados por comas:", bg="#121212", fg="white").pack()
        self.entry_x = tk.Entry(self, width=50)
        self.entry_x.insert(0, "1,2,3,5,7,8")
        self.entry_x.pack(pady=5)

        tk.Label(self, text="Valores f(x) separados por comas:", bg="#121212", fg="white").pack()
        self.entry_y = tk.Entry(self, width=50)
        self.entry_y.insert(0, "3,6,19,99,291,444")
        self.entry_y.pack(pady=5)

        tk.Label(self, text="Valor a evaluar (x):", bg="#121212", fg="white").pack()
        self.entry_eval = tk.Entry(self, width=20)
        self.entry_eval.insert(0, "4")
        self.entry_eval.pack(pady=5)

        tk.Label(self, text="Orden máximo del polinomio (1-4):", bg="#121212", fg="white").pack()
        self.entry_order = tk.Entry(self, width=20)
        self.entry_order.insert(0, "4")
        self.entry_order.pack(pady=5)

        tk.Button(self, text="Calcular", command=self.calculate,
                  font=("Helvetica", 12), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=15, pady=5).pack(pady=10)

        tk.Button(self, text="Atrás", command=self.controller.show_methods,
                  font=("Helvetica", 12, "bold"), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=20, pady=10).pack(pady=10)

    def calculate(self):
        try:
            x_values = list(map(float, self.entry_x.get().split(',')))
            y_values = list(map(float, self.entry_y.get().split(',')))
            x_eval = float(self.entry_eval.get())
            max_order = int(self.entry_order.get())

            if not (1 <= max_order <= 4):
                raise ValueError("El orden máximo debe estar entre 1 y 4")

            results = self.controller.interpolate_newton(x_values, y_values, x_eval, max_order)

            result_text = f"Interpolación en x = {x_eval}:\n\n"
            for order, val in results.items():
                result_text += f"Orden {order}: f({x_eval}) ≈ {val:.6f}\n"

            self.controller.show_popup("Resultados - Interpolación de Newton", result_text)

        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
