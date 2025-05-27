import numpy as np

def multiple_linear_regression(X, y):
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    
    # Agregar columna de unos para el término independiente
    ones = np.ones((X.shape[0], 1))
    X_b = np.hstack((ones, X))
    
    # Coeficientes: B = (XᵀX)⁻¹ Xᵀy
    B = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)

    # Predicciones
    y_pred = X_b @ B

    # Error estándar de la estimación
    residuals = y - y_pred
    SSE = np.sum(residuals ** 2)
    degrees_of_freedom = X.shape[0] - X.shape[1] - 1
    standard_error = np.sqrt(SSE / degrees_of_freedom)

    # Coeficiente de correlación
    r_numerator = np.sum((y - np.mean(y)) * (y_pred - np.mean(y_pred)))
    r_denominator = np.sqrt(np.sum((y - np.mean(y)) ** 2) * np.sum((y_pred - np.mean(y_pred)) ** 2))
    r = r_numerator / r_denominator

    return B.flatten(), standard_error, r
