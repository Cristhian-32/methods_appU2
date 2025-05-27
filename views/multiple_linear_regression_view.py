import tkinter as tk
from tkinter import messagebox
import numpy as np

class MultipleLinearRegressionView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Regresión Lineal Múltiple", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        tk.Label(self, text="Matriz X (variables independientes):", bg="#121212", fg="white").pack()
        self.entry_X = tk.Text(self, width=50, height=10)
        self.entry_X.insert("1.0", "0,0\n0,2\n1,2\n2,4\n0,4\n1,6\n2,6\n2,2\n1,1")
        self.entry_X.pack(pady=5)

        tk.Label(self, text="Vector y (variable dependiente):", bg="#121212", fg="white").pack()
        self.entry_y = tk.Text(self, width=50, height=10)
        self.entry_y.insert("1.0", "14\n21\n11\n12\n23\n23\n14\n6\n11")
        self.entry_y.pack(pady=5)

        tk.Button(self, text="Calcular", command=self.calculate,
                  font=("Helvetica", 12), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=15, pady=5).pack(pady=10)

        tk.Button(self, text="Atrás", command=self.controller.show_methods,
                  font=("Helvetica", 12, "bold"), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=20, pady=10).pack(pady=10)

    def calculate(self):
        try:
            X_input = self.entry_X.get("1.0", tk.END).strip().split("\n")
            y_input = self.entry_y.get("1.0", tk.END).strip().split("\n")

            X = [list(map(float, row.split(','))) for row in X_input]
            y = [float(val) for val in y_input]

            B, std_err, r = self.controller.solve_multiple_linear_regression(X, y)

            result = "\n".join([f"Coef. β{i}: {coef:.6f}" for i, coef in enumerate(B)])
            result += f"\n\nError estándar: {std_err:.6f}\nCoef. de correlación (r): {r:.6f}"
            self.controller.show_popup("Resultados - Regresión Lineal Múltiple", result)

        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
