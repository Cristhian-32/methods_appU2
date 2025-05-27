from sympy import diff, sympify, Symbol
from sympy.utilities.lambdify import lambdify

def golden_section_max_verbose(f_str, a, b, tol=1e-5, max_iter=100):
    x = Symbol('x')
    try:
        expr = sympify(f_str)
        f = lambdify(x, expr, modules=["math"])
    except Exception as e:
        return None, None, f"Error al interpretar la función: {e}", []

    r = (5**0.5 - 1) / 2
    c = b - r * (b - a)
    d = a + r * (b - a)

    log_lines = []
    history = []
    i = 1

    # Encabezado tabulado
    header = f"{'i':<3} {'xₗ':>10} {'f(xₗ)':>10} {'x₁':>10} {'f(x₁)':>10} {'x₂':>10} {'f(x₂)':>10} {'xᵤ':>10} {'f(xᵤ)':>10} {'d':>10}"
    log_lines.append(header)
    log_lines.append("-" * len(header))

    while abs(b - a) > tol and i <= max_iter:
        fx_a = f(a)
        fx_b = f(b)
        fx_c = f(c)
        fx_d = f(d)
        d_width = abs(b - a)

        # Guardar línea formateada
        line = (f"{i:<3} "
                f"{a:10.4f} {fx_a:10.4f} "
                f"{c:10.4f} {fx_c:10.4f} "
                f"{d:10.4f} {fx_d:10.4f} "
                f"{b:10.4f} {fx_b:10.4f} "
                f"{d_width:10.4f}")
        log_lines.append(line)

        # Guardar para gráfica
        history.append((a, b, c, d, fx_c, fx_d))

        if fx_c > fx_d:
            b = d
            d = c
            c = b - r * (b - a)
        else:
            a = c
            c = d
            d = a + r * (b - a)

        i += 1

    x_max = (a + b) / 2
    fx_max = f(x_max)

    log_lines.append("")
    log_lines.append(f"Máximo aproximado en x = {x_max:.5f}")
    log_lines.append(f"Valor máximo f(x) = {fx_max:.5f}")

    return x_max, fx_max, "\n".join(log_lines), history
