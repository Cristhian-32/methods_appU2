from sympy import diff, sympify, Symbol
from sympy.utilities.lambdify import lambdify

def newton_maximum_verbose(f_str, x0, tol=1e-5, max_iter=100):

    x = Symbol('x')
    try:
        expr = sympify(f_str)
        f = lambdify(x, expr, modules=["math"])
        d_expr = expr.diff(x)
        dd_expr = d_expr.diff(x)
        df = lambdify(x, d_expr, modules=["math"])
        ddf = lambdify(x, dd_expr, modules=["math"])
    except Exception as e:
        return None, None, f"Error al interpretar la función: {e}", []

    iteration = 1
    history = []
    x_curr = x0

    header = "{:<3} {:<10} {:<12} {:<12} {:<12}\n".format("i", "x", "f(x)", "f'(x)", "f''(x)")
    output = header

    while iteration <= max_iter:
        fx = f(x_curr)
        dfx = df(x_curr)
        ddfx = ddf(x_curr)

        history.append({'i': iteration, 'x': x_curr, 'fx': fx, 'dfx': dfx, 'ddfx': ddfx})
        output += f"{iteration:<3} {x_curr:<10.6f} {fx:<12.6f} {dfx:<12.6f} {ddfx:<12.6f}\n"

        if abs(dfx) < tol or ddfx == 0:
            break

        x_next = x_curr - dfx / ddfx

        if abs(x_next - x_curr) < tol:
            x_curr = x_next
            break

        x_curr = x_next
        iteration += 1

    output += f"\nMáximo aproximado en x = {x_curr:.6f}\nValor máximo f(x) = {f(x_curr):.6f}"

    return x_curr, f(x_curr), output, history
