from sympy import sympify, Symbol, lambdify
import math

def parabolic_interpolation_verbose(f_str, x0, x1, x2, tol=1e-5, max_iter=100):
    

    x = Symbol('x')
    try:
        expr = sympify(f_str)
        f = lambdify(x, expr, modules=["math"])
    except Exception as e:
        return None, None, f"Error al interpretar la función: {e}", []

    iteration = 1
    history = []

    while iteration <= max_iter:
        f0 = f(x0)
        f1 = f(x1)
        f2 = f(x2)

        numerator = (f0 * (x1**2 - x2**2) + f1 * (x2**2 - x0**2) + f2 * (x0**2 - x1**2))
        denominator = 2 * (f0 * (x1 - x2) + f1 * (x2 - x0) + f2 * (x0 - x1))

        if denominator == 0:
            break

        x3 = numerator / denominator
        f3 = f(x3)

        history.append({
            'i': iteration,
            'x0': x0, 'f0': f0,
            'x1': x1, 'f1': f1,
            'x2': x2, 'f2': f2,
            'x3': x3, 'f3': f3,
        })

        if abs(x3 - x1) < tol:
            break

        if f0 <= f1 and f0 <= f2:
            x0 = x3
        elif f1 <= f0 and f1 <= f2:
            x1 = x3
        else:
            x2 = x3

        iteration += 1

    output = f"{'i':<3} {'x₀':<8} {'f(x₀)':<10} {'x₁':<8} {'f(x₁)':<10} {'x₂':<8} {'f(x₂)':<10} {'x₃':<8} {'f(x₃)':<10}\n"
    for row in history:
        output += (f"{row['i']:<3} "
                   f"{row['x0']:<8.4f} {row['f0']:<10.4f} "
                   f"{row['x1']:<8.4f} {row['f1']:<10.4f} "
                   f"{row['x2']:<8.4f} {row['f2']:<10.4f} "
                   f"{row['x3']:<8.4f} {row['f3']:<10.4f}\n")

    output += f"\nMáximo aproximado en x = {x3:.5f}\nValor máximo f(x) = {f3:.5f}"

    return x3, f3, output, history
