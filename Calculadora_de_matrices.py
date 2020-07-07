import numpy as np
import os
import Graficar_matrices

class Error(Exception):
    pass

class DimensionNoEsMayorACero(Error):
    pass

# Función para limpiar la consola siempre que sea necesario. Es independiente del S.O.
def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

# Función que imprime el menú y solicita la opción deseada a realizar.
def menu():
    while True:
        print("Calculadora de matrices \n", "Menú: \n")

        print("1) Sumar matriz 1 y matriz 2")
        print("2) Restar matriz 1 y matriz 2")
        print("3) Multiplicar matriz 1 y matriz 2")
        print("4) Transpuesta de la matriz 1")
        print("5) Transpuesta de la matriz 2")
        print("6) Número mayor y menor de la matriz 1")
        print("7) Número mayor y menor de la matriz 2")
        print("8) Graficar matrices")
        print("9) Salir del programa")

        try:
            opcion = int(input("Introduzca la opción que desea: "))
        except ValueError:
            borrar_pantalla()
            print("Por favor ingrese un número válido.")
        else:
            return opcion

def opciones_menu(opcion, n, matriz_1, matriz_2, matriz_respuesta):
    if opcion == 1:
        print(suma_matrices(n, matriz_1, matriz_2, matriz_respuesta), "\n")

    if opcion == 2:
        print("1) Calcular matriz 1 - matriz 2")
        print("2) Calcular matriz 2 - matriz 1")
        op = int(input("Ingrese la operacion que desee realizar: "))

        print(resta_matrices(n, matriz_1, matriz_2, matriz_respuesta, op), "\n")

    if opcion == 3:
        print("1) Calcular matriz 1 x matriz 2")
        print("2) Calcular matriz 2 x matriz 1")
        op = int(input("Introduzca la opción que desea: "))

        print(multiplicacion_matrices(n, matriz_1, matriz_2, matriz_respuesta, op), "\n")

    if opcion == 4:
        print(transpuesta(n, matriz_1, matriz_respuesta), "\n")

    if opcion == 5:
        print(transpuesta(n, matriz_2, matriz_respuesta), "\n")

    if opcion == 6:
        menor = matriz_1[0, 0]
        mayor = matriz_1[0, 0]

        print("El número menor es %d y el número mayor es %d \n" %(numero_menor_mayor(n, matriz_1, menor, mayor)))

    if opcion == 7:
        menor = matriz_2[0, 0]
        mayor = matriz_2[0, 0]

        print("El número menor es %d y el número mayor es %d \n" %(numero_menor_mayor(n, matriz_2, menor, mayor)))

    if opcion == 8:
        Graficar_matrices.main(n, matriz_1, matriz_2)

def dimensiones_matriz_1():
    dim_matriz_1 = [0, 0]

    while True:
        try:
            dim_matriz_1[0] = int(input("Introduzca valor de filas (i) para la matriz 1: "))
            if dim_matriz_1[0] <= 0:
                raise DimensionNoEsMayorACero
        except ValueError:
            borrar_pantalla()
            print("Por favor introduzca un número entero positivo mayor a cero.")
        except DimensionNoEsMayorACero:
            borrar_pantalla()
            print("Por favor introduzca un número entero positivo mayor a cero.")
        else:
            while True:
                try:
                    dim_matriz_1[1] = int(input("Introduzca valor de filas (j) para la matriz 1: "))
                    if dim_matriz_1[1] <= 0:
                        raise DimensionNoEsMayorACero
                except ValueError:
                    borrar_pantalla()
                    print("Por favor introduzca un número entero positivo mayor a cero.")
                except DimensionNoEsMayorACero:
                    borrar_pantalla()
                    print("Por favor introduzca un número entero positivo mayor a cero.")
                else:
                    break

            break

    return dim_matriz_1

def dimensiones_matriz_2():
    dim_matriz_2 = [0, 0]

    while True:
        try:
            dim_matriz_2[0] = int(input("Introduzca valor de filas (i) para la matriz 2: "))
            if dim_matriz_2[0] <= 0:
                raise DimensionNoEsMayorACero
        except ValueError:
            borrar_pantalla()
            print("Por favor introduzca un número entero positivo mayor a cero.")
        except DimensionNoEsMayorACero:
            borrar_pantalla()
            print("Por favor introduzca un número entero positivo mayor a cero.")
        else:
            while True:
                try:
                    dim_matriz_2[1] = int(input("Introduzca valor de filas (j) para la matriz 2: "))
                    if dim_matriz_2[1] <= 0:
                        raise DimensionNoEsMayorACero
                except ValueError:
                    borrar_pantalla()
                    print("Por favor introduzca un número entero positivo mayor a cero.")
                except DimensionNoEsMayorACero:
                    borrar_pantalla()
                    print("Por favor introduzca un número entero positivo mayor a cero.")
                else:
                    break

            break

    return dim_matriz_2

def crear_matrices(dim_matriz_1, dim_matriz_2):
    matriz_1 = np.zeros((dim_matriz_1[0], dim_matriz_1[1]))
    matriz_2 = np.zeros((dim_matriz_2[0], dim_matriz_2[1]))

    return matriz_1, matriz_2

def llenar_matriz(dim_matriz, matriz):     
    for i in range(dim_matriz[0]):
        for j in range(dim_matriz[1]):
            while True:
                try:
                    matriz[i, j] = float(input(f"Introduzca valor de la casilla ({i + 1}, {j + 1}) para la matriz: "))
                except ValueError:
                    continue
                else:
                    print(matriz)
                    break

    return matriz

# Se suman las matrices 1 y 2, y se retorna la matriz respuesta.
def suma_matrices(n, matriz_1, matriz_2, matriz_respuesta):
    for i in range(n):
        for j in range(n):
            matriz_respuesta[i, j] = matriz_1[i, j] + matriz_2[i, j]
    return matriz_respuesta

# Se restan las matrices 1 y 2 ó 2 y 1 dependiendo de la entrada dada por el usuario,
# y retorna una matriz respuesta, la cual se imprime después.
def resta_matrices(n, matriz_1, matriz_2, matriz_respuesta, op):
    if op == 1:
        for i in range(n):
            for j in range(n):
                matriz_respuesta[i, j] = matriz_1[i, j] - matriz_2[i, j]
    elif op == 2:
        for i in range(n):
            for j in range(n):
                matriz_respuesta[i, j] = matriz_2[i, j] - matriz_1[i, j]
    return matriz_respuesta

def multiplicacion_matrices(n, matriz_1, matriz_2, matriz_respuesta, op):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if op == 1:
                    matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_1[i, k] * matriz_2[k, j]
                elif op == 2:
                    matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_2[i, k] * matriz_1[k, j]
    return matriz_respuesta

# Función para hallar la matriz transpuesta de la matriz seleccionada.
def transpuesta(n, matriz, matriz_respuesta):
    for i in range(n):
        for j in range(n):
            matriz_respuesta[i, j] = matriz[j, i]
    return matriz_respuesta

def numero_menor_mayor(n, matriz, menor, mayor):
    for i in range(n):
        for j in range(n):
            if menor > matriz[i, j]:
                menor = matriz[i, j]
            if mayor < matriz[i, j]:
                mayor = matriz[i, j]

    return menor, mayor

def main():
    operacion = 0
    while operacion != 9:
        dim_matriz_1 = dimensiones_matriz_1()
        print(dim_matriz_1)
        dim_matriz_2 = dimensiones_matriz_2()
        print(dim_matriz_2)
        matriz_1, matriz_2 = crear_matrices(dim_matriz_1, dim_matriz_2)
        matriz_1 = llenar_matriz(dim_matriz_1, matriz_1)
        matriz_2 = llenar_matriz(dim_matriz_2, matriz_2)
        opcion = menu()

        borrar_pantalla()
        # matriz_respuesta = np.zeros((n, n))

        # opciones_menu(opcion, matriz_1, matriz_2, matriz_respuesta)

main()
