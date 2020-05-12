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

    matrizr = np.zeros((n, n))

    if m == 1:
        for i in range(n):
            for j in range(n):
                matrizr[i, j] = matriz1[i, j] + matriz2[i, j]
        print(matrizr, "\n")

    if m == 2:
        print("1) Calcular matriz 1 - matriz 2")
        print("2) Calcular matriz 2 - matriz 1")

        op = int(input("Introduzca la opción que desea: "))

        for i in range(n):
            for j in range(n):
                if op == 1:
                    matrizr[i, j] = matriz1[i, j] - matriz2[i, j]
                if op == 2:
                    matrizr[i, j] = matriz2[i, j] - matriz1[i, j]
        print(matrizr, "\n")
