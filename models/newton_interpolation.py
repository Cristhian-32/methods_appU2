def divided_diff(x, y):
    n = len(x)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def newton_eval(x_data, coef, x):
    n = len(coef)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_data[i]) + coef[i]
    return result

def interpolate_newton(x_values, y_values, x_eval, max_order):
    results = {}
    n = len(x_values)
    
    # Elegir puntos base cercanos a x_eval para cada orden
    # Para simplificar, ordenamos x y y juntos, y seleccionamos primeros max_order+1 puntos con x más cercanos a x_eval
    points = list(zip(x_values, y_values))
    points.sort(key=lambda p: abs(p[0] - x_eval))
    
    for order in range(1, max_order + 1):
        subset = points[:order+1]
        xs, ys = zip(*sorted(subset, key=lambda p: p[0]))  # ordenar por x para interpolar
        coef = divided_diff(list(xs), list(ys))
        y_interp = newton_eval(list(xs), coef, x_eval)
        results[order] = y_interp
    return results
