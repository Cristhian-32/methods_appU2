import tkinter as tk
from tkinter import messagebox

class GaussSeidelView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Método Iterativo de Gauss-Seidel", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        tk.Label(self, text="Ingrese la matriz (filas separadas por ; y valores por ,):",
                 bg="#121212", fg="white").pack()
        self.matrix_entry = tk.Entry(self, width=60)
        self.matrix_entry.pack(pady=5)
        self.matrix_entry.insert(0, "6,-1,0,-2,0,0,0,0,0; -1,6,-1,0,-2,0,0,0,0; 0,1,6,0,0,-2,0,0,0; -2,0,0,6,-1,0,-2,0,0; 0,-2,0,-1,6,-1,0,-2,0; 0,0,-2,0,-1,6,0,0,-2; 0,0,0,-2,0,0,6,-1,0; 0,0,0,0,-2,0,1,6,-1; 0,0,0,0,0,-2,0,-1,6")

        tk.Label(self, text="Ingrese el vector independiente (valores separados por ,):",
                 bg="#121212", fg="white").pack()
        self.vector_entry = tk.Entry(self, width=60)
        self.vector_entry.pack(pady=5)
        self.vector_entry.insert(0, "3,2,3,1,0,1,3,2,3")

        tk.Label(self, text="Ingrese la tolerancia (ejemplo: 0.0001):",
                 bg="#121212", fg="white").pack()
        self.tol_entry = tk.Entry(self, width=20)
        self.tol_entry.pack(pady=5)
        self.tol_entry.insert(0, "0.0001")

        tk.Label(self, text="Ingrese el máximo de iteraciones:",
                 bg="#121212", fg="white").pack()
        self.max_iter_entry = tk.Entry(self, width=20)
        self.max_iter_entry.pack(pady=5)
        self.max_iter_entry.insert(0, "100")

        tk.Button(self, text="Calcular", command=self.calculate,
                  font=("Helvetica", 12), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=15, pady=5).pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#121212", fg="white", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        tk.Button(self, text="Atrás", command=self.controller.show_methods,
                  font=("Helvetica", 12, "bold"), bg="#1F1F1F", fg="white",
                  activebackground="#333333", activeforeground="white", bd=0, padx=20, pady=10).pack(pady=10)

    def calculate(self):
        try:
            matrix_input = self.matrix_entry.get()
            vector_input = self.vector_entry.get()
            tol = float(self.tol_entry.get())
            max_iter = int(self.max_iter_entry.get())

            matrix = [list(map(float, row.split(','))) for row in matrix_input.split(';')]
            vector = list(map(float, vector_input.split(',')))

            self.controller.close_all_popups()  # cerrar popups previos

            solution, iterations = self.controller.solve_gauss_seidel(matrix, vector, tol, max_iter)

            iter_text = "Método de Gauss-Seidel:\n\n"
            for it, x_vals, err in iterations:
                iter_text += f"Iteración {it}: x = {[round(v, 6) for v in x_vals]}, error = {err:.6f}\n"

            sol_text = "Solución aproximada:\n"
            for i, val in enumerate(solution):
                sol_text += f"x[{i}] = {val}\n"

            self.controller.show_popup("Iteraciones Gauss-Seidel", iter_text)
            self.controller.show_popup("Solución Aproximada", sol_text, height=10)

            self.result_label.config(text=f"Iteraciones realizadas: {len(iterations)}")

        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
