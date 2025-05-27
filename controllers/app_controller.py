import tkinter as tk
from views.welcome_view import WelcomeView
from views.methods_view import MethodsView
from views.gauss_elimination_view import GaussView
from views.gauss_jordan_view import GaussJordanView
from views.lu_descomposition_view import LUView
from models.gauss_elimination import gauss_elimination
from models.gauss_jordan import gauss_jordan
from models.lu_descomposition import lu_decomposition

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplicación de Métodos Numéricos")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("800x600")
        self.current_view = None

    def run(self):
        self.show_welcome()
        self.root.mainloop()

    def show_welcome(self):
        self.clear_view()
        self.current_view = WelcomeView(self.root, self)

    def show_methods(self):
        self.clear_view()
        self.current_view = MethodsView(self.root, self)

    def clear_view(self):
        if self.current_view is not None:
            self.current_view.destroy()

    #Métodos

    #Métodos de Álgebra Lineal Numérica

    #Método de eliminación de Gauss
    def show_gauss_elimination(self):
        self.clear_view()
        self.current_view = GaussView(self.root, self)
    
    def solve_gauss(self, matrix, vector):
        return gauss_elimination(matrix, vector)

    def show_gauss_jordan(self):
        self.clear_view()
        self.current_view = GaussJordanView(self.root, self)

    def solve_gauss_jordan(self, matrix, vector):
        return gauss_jordan(matrix, vector)
    
    def show_lu_decomposition(self):
        self.clear_view()
        self.current_view = LUView(self.root, self)

    def solve_lu_decomposition(self, matrix, vector):
        return lu_decomposition(matrix, vector)
    
    def show_cholesky(self): print("Cholesky")
    def show_jacobi(self): print("Jacobi")
    def show_gauss_seidel(self): print("Gauss-Seidel")

    #Métodos de Optimización y Regresión
    def show_unidimensional_optimization(self): print("Optimización 1D")
    def show_multidimensional_optimization(self): print("Optimización MultiD")
    def show_constrained_optimization(self): print("Con restricciones")
    def show_linear_regression(self): print("Regresión lineal")
    def show_multiple_regression(self): print("Regresión múltiple")
    def show_nonlinear_regression(self): print("Regresión no lineal")

    #Extras
    def show_extra1(self): print("Extra 1")
    def show_extra2(self): print("Extra 2")
    def show_extra3(self): print("Extra 3")
    def show_extra4(self): print("Extra 4")
