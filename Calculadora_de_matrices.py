import numpy as np
import os

def suma(n,matriz_1,matriz_2):
    matriz_respuesta=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            matriz_respuesta[i,j] = matriz_1[i,j] + matriz_2[i,j]
    return(matriz_respuesta)

def resta(n,matriz_1,matriz_2):
    matriz_respuesta=np.zeros((n,n))
    op=int(input("ingrese la operacion que desee realizar:"))
    if op==1:
        for i in range(n):
            for j in range(n):
                matriz_respuesta[i,j] = matriz_1[i,j] - matriz_2[i,j]
        print(matriz_respuesta)
    elif op==2:
        for i in range(n):
            for j in range(n):
                matriz_respuesta[i,j] = matriz_2[i,j] - matriz_1[i,j]
        print(matriz_respuesta)

def borrar_pantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def main():
    m = 0
    while m != 8:
        n = int(input("Introduzca valor de n para las matrices: "))

        borrar_pantalla()

        if n > 0:
            matriz_1 = np.zeros((n, n))
            matriz_2 = np.zeros((n, n))
            for h in range(2):        
                for i in range(n):
                    for j in range(n):
                        if h == 0:
                            matriz_1[i, j] = float(input(f"Introduzca valor de la casilla {i + 1}, {j + 1} para la matriz {h + 1}: "))
                            print(matriz_1)
                        else:
                            matriz_2[i, j] = float(input(f"Introduzca valor de la casilla {i + 1}, {j + 1} para la matriz {h + 1}: "))
                            print(matriz_2)

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

            borrar_pantalla()
            matriz_respuesta = np.zeros((n, n))

            if m == 1:
                borrar_pantalla()
                suma(n,matriz_1,matriz_2)
                print(matriz_respuesta, "\n")

            if m == 2:
                borrar_pantalla()
                print("1) Calcular matriz 1 - matriz 2")
                print("2) Calcular matriz 2 - matriz 1")
                resta(n,matriz_1,matriz_2)
                

            if m == 3:
                borrar_pantalla()
                print("1) Calcular matriz 1 x matriz 2")
                print("2) Calcular matriz 2 x matriz 1")
        
                op = int(input("Introduzca la opción que desea: "))

                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            if op == 1:
                                matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_1[i, k] * matriz_2[k, j]
                            if op == 2:
                                matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_2[i, k] * matriz_1[k, j]
                print(matriz_respuesta, "\n")

            if m == 4:
                borrar_pantalla()
                for i in range(n):
                    for j in range(n):
                        matriz_respuesta[i, j] = matriz_1[j, i]
                print(matriz_respuesta, "\n")

            if m == 5:
                borrar_pantalla()
                for i in range(n):
                    for j in range(n):
                        matriz_respuesta[i, j] = matriz_2[j, i]
                print(matriz_respuesta, "\n")

            if m == 6:
                borrar_pantalla()
                menor = matriz_1[0, 0]
                mayor = matriz_1[0, 0]

                for i in range(n):
                    for j in range(n):
                        if menor > matriz_1[i, j]:
                            menor = matriz_1[i, j]
                        if mayor < matriz_1[i, j]:
                            mayor = matriz_1[i, j]
                print("El número menor es", menor, "y el número mayor es", mayor, "\n")

            if m == 7:
                borrar_pantalla()
                menor = matriz_2[0, 0]
                mayor = matriz_2[0, 0]

                for i in range(n):
                    for j in range(n):
                        if menor > matriz_2[i, j]:
                            menor = matriz_2[i, j]
                        if mayor < matriz_2[i, j]:
                            mayor = matriz_2[i, j]
                print("El número menor es", menor, "y el número mayor es", mayor, "\n")

main()
