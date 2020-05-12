import numpy as np

n = int(input("Introduzca valor de n para las matrices: "))

if n > 0:
    matriz1 = np.zeros((n, n))
    matriz2 = np.zeros((n, n))
    for h in range(2):        
        for i in range(n):
            for j in range(n):
                if h == 0:
                    matriz1[i, j] = float(input(f"Introduzca valor de la casilla {i + 1}, {j + 1} para la matriz {h + 1}: "))
                    print(matriz1)
                else:
                    matriz2[i, j] = float(input(f"Introduzca valor de la casilla {i + 1}, {j + 1} para la matriz {h + 1}: "))
                    print(matriz2)
