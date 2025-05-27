def gauss_seidel_method(A, b, tol=1e-6, max_iterations=100):
    n = len(A)
    x = [0.0 for _ in range(n)]
    iterations = []
    
    for iteration in range(1, max_iterations + 1):
        x_new = x.copy()
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))       # valores ya actualizados en esta iteración
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))    # valores de la iteración anterior
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        # Calcular error (norma infinito del vector diferencia)
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        
        # Guardar el estado para mostrar iteraciones
        iterations.append((iteration, x_new.copy(), error))
        
        if error < tol:
            return x_new, iterations
        
        x = x_new
    
    return x, iterations
