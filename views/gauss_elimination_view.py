import tkinter as tk
from tkinter import messagebox

class GaussView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self, text="Método de Eliminación de Gauss", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="white").pack(pady=10)

        tk.Label(self, text="Ingrese la matriz (filas separadas por ; y valores por ,):",
                 bg="#121212", fg="white").pack()
        self.matrix_entry = tk.Entry(self, width=60)
        self.matrix_entry.pack(pady=5)
        self.matrix_entry.insert(0 , "6,-1,0,-2,0,0,0,0,0; -1,6,-1,0,-2,0,0,0,0; 0,1,6,0,0,-2,0,0,0; -2,0,0,6,-1,0,-2,0,0; 0,-2,0,-1,6,-1,0,-2,0; 0,0,-2,0,-1,6,0,0,-2; 0,0,0,-2,0,0,6,-1,0; 0,0,0,0,-2,0,1,6,-1; 0,0,0,0,0,-2,0,-1,6")

        tk.Label(self, text="Ingrese el vector independiente (valores separados por ,):",
                 bg="#121212", fg="white").pack()
        self.vector_entry = tk.Entry(self, width=60)
        self.vector_entry.pack(pady=5)
        self.vector_entry.insert(0, "3,2,3,1,0,1,3,2,3")

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
            matrix = [list(map(float, row.split(','))) for row in matrix_input.split(';')]
            vector = list(map(float, vector_input.split(',')))
            result = self.controller.solve_gauss(matrix, vector)
            self.result_label.config(text=f"Resultado: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
