import numpy as np
import os

def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

n = int(input("Introduzca valor de n para las matrices: "))

borrarPantalla()

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

    borrarPantalla()
    matrizr = np.zeros((n, n))

    if m == 1:
        borrarPantalla()
        for i in range(n):
            for j in range(n):
                matrizr[i, j] = matriz1[i, j] + matriz2[i, j]
        print(matrizr, "\n")

    if m == 2:
        borrarPantalla()
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

    if m == 3:
        borrarPantalla()
        print("1) Calcular matriz 1 x matriz 2")
        print("2) Calcular matriz 2 x matriz 1")
        
        op = int(input("Introduzca la opción que desea: "))

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if op == 1:
                        matrizr[i, j] = matrizr[i, j] + matriz1[i, k] * matriz2[k, j]
                    if op == 2:
                        matrizr[i, j] = matrizr[i, j] + matriz2[i, k] * matriz1[k, j]
        print(matrizr, "\n")

    if m == 4:
        borrarPantalla()
        for i in range(n):
            for j in range(n):
                matrizr[i, j] = matriz1[j, i]
        print(matrizr, "\n")

    if m == 5:
        borrarPantalla()
        for i in range(n):
            for j in range(n):
                matrizr[i, j] = matriz2[j, i]
        print(matrizr, "\n")
