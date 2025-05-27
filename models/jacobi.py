def jacobi_method(A, b, tol, max_iterations):
    n = len(A)
    x_old = [0.0 for _ in range(n)]
    x_new = [0.0 for _ in range(n)]
    steps = ["Método de Jacobi:\n"]

    for iteration in range(1, max_iterations + 1):
        for i in range(n):
            sum_j = sum(A[i][j] * x_old[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_j) / A[i][i]

        # Calcular el error máximo
        error = max(abs(x_new[i] - x_old[i]) for i in range(n))

        # Guardar los valores actuales
        x_str = ', '.join(f"{x:.6f}" for x in x_new)
        steps.append(f"Iteración {iteration}: x = [{x_str}], error = {error:.6f}")

        if error < tol:
            break

        x_old = x_new.copy()

    # Agregar resultado final
    steps.append("\nSolución aproximada x:")
    for i, val in enumerate(x_new):
        steps.append(f"x[{i}] = {val}")

    return x_new, '\n'.join(steps)
