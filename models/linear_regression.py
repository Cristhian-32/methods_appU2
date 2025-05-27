import numpy as np

def linear_regression_verbose(x_str, y_str):
    # Convertir strings a arrays float
    x = np.array([float(val.strip()) for val in x_str.split(',')])
    y = np.array([float(val.strip()) for val in y_str.split(',')])

    n = len(x)
    if n != len(y):
        raise ValueError("Los datos X e Y deben tener la misma longitud")

    # Cálculo pendiente y ordenada al origen
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    m = np.sum((x - x_mean)*(y - y_mean)) / np.sum((x - x_mean)**2)
    b = y_mean - m * x_mean

    # Predicciones
    y_pred = m * x + b

    # Error estándar de la estimación
    residuals = y - y_pred
    s = np.sqrt(np.sum(residuals**2) / (n - 2))

    # Coeficiente de correlación r
    r = np.corrcoef(x, y)[0,1]

    # Log detallado para mostrar al usuario
    log = (
        f"Pendiente (m): {m:.4f}\n"
        f"Intersección (b): {b:.4f}\n"
        f"Error estándar de la estimación (s): {s:.4f}\n"
        f"Coeficiente de correlación (r): {r:.4f}\n"
        f"Evaluación del ajuste:\n"
        f"- r cerca de ±1 indica buen ajuste.\n"
        f"- Error estándar pequeño indica buenas predicciones."
    )

    return m, b, s, r, log
