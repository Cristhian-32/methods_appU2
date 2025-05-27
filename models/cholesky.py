def cholesky_decomposition(A, b):
    n = len(A)

    # Verificar si A es simétrica
    # for i in range(n):
    #     for j in range(n):
    #         if A[i][j] != A[j][i]:
    #             raise ValueError("La matriz A debe ser simétrica")

    # Inicializar L
    L = [[0.0] * n for _ in range(n)]

    # Descomposición Cholesky: A = L * Lᵗ
    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                value = A[i][i] - sum_k
                if value <= 0:
                    raise ValueError("La matriz no es definida positiva")
                L[i][j] = value ** 0.5
            else:
                L[i][j] = (A[i][j] - sum_k) / L[j][j]

    # Sustitución hacia adelante: Ly = b
    y = [0.0] * n
    for i in range(n):
        sum_j = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_j) / L[i][i]

    # Sustitución hacia atrás: Lᵗx = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_j = sum(L[j][i] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_j) / L[i][i]

    return L, x 
