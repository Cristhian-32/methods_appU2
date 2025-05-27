def gauss_jordan(matrix, vector):
    n = len(matrix)

    # Construir matriz aumentada
    for i in range(n):
        matrix[i].append(vector[i])

    # Gauss-Jordan
    for i in range(n):
        # Pivote
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("División por cero en el pivote.")
        
        # Normalizar la fila
        matrix[i] = [x / pivot for x in matrix[i]]

        # Hacer ceros en la columna i (excepto la fila i)
        for j in range(n):
            if j != i:
                ratio = matrix[j][i]
                matrix[j] = [a - ratio * b for a, b in zip(matrix[j], matrix[i])]

    # Solución
    return [row[-1] for row in matrix]
