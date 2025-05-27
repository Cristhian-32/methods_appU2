import tkinter as tk

class WelcomeView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#121212")
        self.controller = controller
        self.pack(fill="both", expand=True)

        self.label = tk.Label(
            self,
            text="Bienvenido",
            font=("Helvetica", 18),
            bg="#121212",
            fg="#ffffff"
        )
        self.label.pack(pady=40)

        self.start_button = tk.Button(
            self,
            text="Empezar",
            command=controller.show_methods,
            font=("Helvetica", 14, "bold"),
            bg="#1F1F1F",
            fg="white",
            activebackground="#333333",
            activeforeground="white",
            bd=0,
            padx=20,
            pady=10
        )
        self.start_button.pack(pady=10)
