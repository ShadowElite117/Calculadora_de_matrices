import numpy as np
import os
import Graficar_matrices

# Solicita al usuario un entero y lo retorna, en este caso para la operacion a realizar.
# Si el valor solicitado no es un entero se solicita nuevamente y se genera un mensaje de error.
def solicitar_entrada_operacion():
    while True:
        operacion = input("Introduzca la opción que desea: ")
        try:
            operacion = int (operacion)
            return operacion
        except ValueError:
            print ("Porfavor ingrese un número válido")

# Solicita al usuario un entero positivo y lo retorna, en este caso para el tamaño de las
# matrices. Si el valor solicitado no es un entero positivo, se solicita nuevamente y se genera
# un mensaje de error.
def solicitar_entrada_matrices():
    while True:
        n = input("Introduzca valor de n para las matrices: ")
        try:
            n = int (n)
            return n
        except ValueError:
            print ("Porfavor ingrese un número entero")

# Función para limpiar la consola siempre que sea necesario. Es independiente del S.O.
def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

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

        n = solicitar_entrada_matrices()

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
            print("8) Graficar matrices")
            print("9) Salir del programa")

            operacion = solicitar_entrada_operacion()

            borrar_pantalla()
            matriz_respuesta = np.zeros((n, n))

            if operacion == 1:
                print(suma_matrices(n, matriz_1, matriz_2, matriz_respuesta), "\n")

            if operacion == 2:
                print("1) Calcular matriz 1 - matriz 2")
                print("2) Calcular matriz 2 - matriz 1")
                op = int(input("Ingrese la operacion que desee realizar: "))

                print(resta_matrices(n, matriz_1, matriz_2, matriz_respuesta, op), "\n")

            if operacion == 3:
                print("1) Calcular matriz 1 x matriz 2")
                print("2) Calcular matriz 2 x matriz 1")
                op = int(input("Introduzca la opción que desea: "))

                print(multiplicacion_matrices(n, matriz_1, matriz_2, matriz_respuesta, op), "\n")

            if operacion == 4:
                print(transpuesta(n, matriz_1, matriz_respuesta), "\n")

            if operacion == 5:
                print(transpuesta(n, matriz_2, matriz_respuesta), "\n")

            if operacion == 6:
                menor = matriz_1[0, 0]
                mayor = matriz_1[0, 0]

                print("El número menor es %d y el número mayor es %d \n" %(numero_menor_mayor(n, matriz_1, menor, mayor)))

            if operacion == 7:
                menor = matriz_2[0, 0]
                mayor = matriz_2[0, 0]

                print("El número menor es %d y el número mayor es %d \n" %(numero_menor_mayor(n, matriz_2, menor, mayor)))

            if operacion == 8:
                Graficar_matrices.main(n, matriz_1, matriz_2)

main()
