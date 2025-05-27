import tkinter as tk
from views.welcome_view import WelcomeView
from views.methods_view import MethodsView
from views.gauss_elimination_view import GaussView
from views.gauss_jordan_view import GaussJordanView
from views.lu_descomposition_view import LUView
from views.cholesky_view import CholeskyView
from views.jacobi_view import JacobiView
from views.gauss_seidel_view import GaussSeidelView
from views.golden_secction_view import GoldenSectionView
from views.parabolic_interpolation_view import ParabolicInterpolationView
from views.newton_view import NewtonMaximumView
from views.linear_regression_view import LinearRegressionView
from views.multiple_linear_regression_view import MultipleLinearRegressionView
from views.newton_interpolation import NewtonInterpolationView
from models.gauss_elimination import gauss_elimination
from models.gauss_jordan import gauss_jordan
from models.lu_descomposition import lu_decomposition
from models.cholesky import cholesky_decomposition
from models.jacobi import jacobi_method
from models.gauss_seidel import gauss_seidel_method
from models.golden_section import golden_section_max_verbose
from models.parabolic_interpolation import parabolic_interpolation_verbose
from models.newton import newton_maximum_verbose
from models.linear_regression import linear_regression_verbose
from models.multiple_linear_regression import multiple_linear_regression
from models.newton_interpolation import interpolate_newton

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplicación de Métodos Numéricos")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("800x600")
        self.current_view = None
        self.popups = []

    def run(self):
        self.show_welcome()
        self.root.mainloop()

    def show_welcome(self):
        self.clear_view()
        self.current_view = WelcomeView(self.root, self)

    def show_methods(self):
        self.clear_view()
        self.close_all_popups()
        self.current_view = MethodsView(self.root, self)

    def clear_view(self):
        if self.current_view is not None:
            self.current_view.destroy()

    def show_popup(self, title, message, width=80, height=25):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.configure(bg="#121212")

        text_widget = tk.Text(popup, wrap="word", bg="#1E1E1E", fg="white",
                            font=("Consolas", 10), width=width, height=height)
        text_widget.insert("1.0", message)
        text_widget.config(state="disabled")
        text_widget.pack(padx=10, pady=10)

        self.popups.append(popup)  # Guardar la referencia

    def close_all_popups(self):
        for popup in self.popups:
            try:
                popup.destroy()
            except:
                pass
        self.popups.clear()


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
    
    def show_cholesky(self):
        self.clear_view()
        self.current_view = CholeskyView(self.root, self)

    def solve_cholesky(self, matrix, vector):
        return cholesky_decomposition(matrix, vector)
    
    def show_jacobi(self):
        self.clear_view()
        self.close_all_popups()
        self.current_view = JacobiView(self.root, self)

    def solve_jacobi(self, matrix, vector, tol, max_iter):
        solution, log = jacobi_method(matrix, vector, tol, max_iter)
        return log

    from models.gauss_seidel import gauss_seidel_method

    def show_gauss_seidel(self):
        self.clear_view()
        self.current_view = GaussSeidelView(self.root, self)

    def solve_gauss_seidel(self, matrix, vector, tol, max_iter):
        return gauss_seidel_method(matrix, vector, tol, max_iter)


    #Métodos de Optimización y Regresión
    def show_golden_section(self):
        self.clear_view()
        self.current_view = GoldenSectionView(self.root, self)

    def solve_golden_section(self, func, a, b, tol):
        return golden_section_max_verbose(func, a, b, tol)
    
    def show_parabolic_interpolation(self):
        self.clear_view()
        self.current_view = ParabolicInterpolationView(self.root, self)

    def solve_parabolic_interpolation(self, func_str, x0, x1, x2, tol, iterations):
        return parabolic_interpolation_verbose(func_str, x0, x1, x2, tol, iterations)

    def show_newton_maximum(self):
        self.clear_view()
        self.current_view = NewtonMaximumView(self.root, self)
    
    def solve_newton_maximum(self, func_str, x0, tol, max_iter):
        return newton_maximum_verbose(func_str, x0, tol, max_iter)


    def show_linear_regression(self):
        self.clear_view()
        self.current_view = LinearRegressionView(self.root, self)

    def solve_linear_regression(self, x_str, y_str):
        return linear_regression_verbose(x_str, y_str)

    def show_multiple_linear_regression(self):
        self.clear_view()
        self.current_view = MultipleLinearRegressionView(self.root, self)

    def solve_multiple_linear_regression(self, X, y):
        return multiple_linear_regression(X, y)

    def show_nonlinear_regression(self): print("Regresión no lineal")

    #Extras
    def show_newton_interpolation(self):
        self.clear_view()
        self.current_view = NewtonInterpolationView(self.root, self)

    def interpolate_newton(self, x_values, y_values, x_eval, max_order):
        return interpolate_newton(x_values, y_values, x_eval, max_order)
    def show_extra2(self): print("Extra 2")
    def show_extra3(self): print("Extra 3")
    def show_extra4(self): print("Extra 4")
