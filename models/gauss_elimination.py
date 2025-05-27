def gauss_elimination(matrix, vector):
    n = len(matrix)
    # Eliminar hacia adelante
    for i in range(n):
        # Pivote
        if matrix[i][i] == 0:
            raise ValueError("División por cero detectada en el pivote.")
        for j in range(i+1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= ratio * matrix[i][k]
            vector[j] -= ratio * vector[i]

    # Sustitución regresiva
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        suma = sum(matrix[i][j] * x[j] for j in range(i+1, n))
        x[i] = (vector[i] - suma) / matrix[i][i]
    
    return x
