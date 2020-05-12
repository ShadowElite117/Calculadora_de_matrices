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

    print("Calculadora de matrices \n", "Menú: \n")

    print("1) Sumar matriz 1 y matriz 2")
    print("2) Restar matriz 1 y matriz 2")
    print("3) Multiplicar matriz 1 y matriz 2")
    print("4) Transpuesta de la matriz 1")
    print("5) Transpuesta de la matriz 2")
    print("6) Número mayor y menor de la matriz 1")
    print("7) Número mayor y menor de la matriz 2")
    print("8) Salir del programa")

    m = int(input("Introduzca la opción que desea: "))
