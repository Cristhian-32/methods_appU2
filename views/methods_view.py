import tkinter as tk

class MethodsView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True, padx=20, pady=20)

        self.button_actions = {
            # Álgebra Lineal Numérica
            "Eliminación de Gauss": controller.show_gauss_elimination,
            "Método de Gauss-Jordan": controller.show_gauss_jordan,
            "Descomposición LU": controller.show_lu_decomposition,
            "Método de Cholesky": controller.show_cholesky,
            "Método Iterativo de Jacobi": controller.show_jacobi,
            "Método Iterativo de Gauss-Seidel": controller.show_gauss_seidel,

            # Optimización y Regresión
            "Optimización unidimensional sin restricciones": controller.show_golden_section,
            "Optimización multidimensional sin restricciones": controller.show_parabolic_interpolation,
            "Optimización con restricciones": controller.show_newton_maximum,
            "Recta de regresión lineal de mínimos cuadrados": controller.show_linear_regression,
            "Regresión lineal múltiple": controller.show_multiple_linear_regression,
            "Regresión no lineal": controller.show_nonlinear_regression,

            # Extras
            "Newton Interpolation": controller.show_newton_interpolation,
            "Botón 2": controller.show_extra2,
            "Botón 3": controller.show_extra3,
            "Botón 4": controller.show_extra4,
        }

        # Título principal
        title_label = tk.Label(
            self,
            text="Seleccione un Método",
            font=("Helvetica", 18, "bold"),
            bg="#121212",
            fg="white"
        )
        title_label.pack(pady=(10, 20))

        # Contenedor de columnas
        columns_frame = tk.Frame(self, bg="#121212")
        columns_frame.pack(anchor="center", pady=10)


        # Columnas
        self.create_column(columns_frame,
            "Métodos de Álgebra Lineal Numérica",
            [
                "Eliminación de Gauss",
                "Método de Gauss-Jordan",
                "Descomposición LU",
                "Método de Cholesky",
                "Método Iterativo de Jacobi",
                "Método Iterativo de Gauss-Seidel"
            ]
        ).grid(row=0, column=0, padx=10)

        self.create_column(columns_frame,
            "Métodos de Optimización y Regresión",
            [
                "Optimización unidimensional sin restricciones",
                "Optimización multidimensional sin restricciones",
                "Optimización con restricciones",
                "Recta de regresión lineal de mínimos cuadrados",
                "Regresión lineal múltiple",
                "Regresión no lineal"
            ]
        ).grid(row=0, column=1, padx=10)

        self.create_column(columns_frame,
            "Extras",
            ["Newton Interpolation", "Botón 2", "Botón 3", "Botón 4"]
        ).grid(row=0, column=2, padx=10)

        # Botón Atrás
        back_button = tk.Button(
            self,
            text="Atrás",
            command=controller.show_welcome,
            font=("Helvetica", 14, "bold"),
            bg="#1F1F1F",
            fg="white",
            activebackground="#333333",
            activeforeground="white",
            bd=0,
            padx=20,
            pady=10
        )
        back_button.pack(pady=20)

    def create_column(self, master, title, buttons):
        frame = tk.Frame(master, bg="#121212")

        title_label = tk.Label(
            frame,
            text=title,
            font=("Helvetica", 12, "bold"),
            bg="#121212",
            fg="white",
            wraplength=200,
            justify="center"
        )
        title_label.pack(pady=(0, 10))

        for text in buttons:
            action = self.button_actions.get(text, lambda: print(f"No implementado: {text}"))
            btn = tk.Button(
                frame,
                text=text,
                command=action,
                font=("Helvetica", 10, "bold"),
                bg="#1F1F1F",
                fg="white",
                activebackground="#333333",
                activeforeground="white",
                bd=0,
                padx=10,
                pady=6,
                wraplength=180,
                justify="center"
            )
            btn.pack(pady=4, fill="x")

        return frame
