import numpy as np
import os
import Graficar_matrices


def solicitar_entrada_operacion():

    """ Solicita al usuario un entero y lo retorna, en este caso para la operacion a realizar.
        Si el valor solicitado no es un entero vuelve a solicitarlo
        mandando un mensaje. """

    while True:
        operacion = input("Introduzca la opción que desea: ")
        try:
            operacion = int (operacion)
            return operacion
        except ValueError:
            print ("Porfavor ingrese un número válido")

def solicitar_entrada_matrices():

    """ Solicita al usuario un entero y lo retorna, en este caso para el valor de las matrices.
        Si el valor solicitado no es un entero vuelve a solicitarlo
        mandando un mensaje. """

    while True:
        n = input("Introduzca valor de n para las matrices: ")
        try:
            n = int (n)
            return n
        except ValueError:
            print ("Porfavor ingrese un número entero")

def borrar_pantalla():

    """Limpia la consola para tener una mejor apariencia a la hora
    de realizar operaciones con las matrices"""

    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def suma_de_matrices(n, matriz_1, matriz_2, matriz_respuesta):

    """suma las matrices 1 y 2 en ese orden, y retorna una matriz respuesta,
    la cual se imprime después"""

    for i in range(n):
        for j in range(n):
            matriz_respuesta[i, j] = matriz_1[i, j] + matriz_2[i, j]
    return matriz_respuesta

def resta_de_matrices(n, matriz_1, matriz_2, matriz_respuesta, op):

    """resta las matrices 1 y 2 o 2 y 1 dependiendo de la entrada dada por el usuario,
     y retorna una matriz respuesta, la cual se imprime después"""

    if op == 1:
        for i in range(n):
            for j in range(n):
                matriz_respuesta[i, j] = matriz_1[i, j] - matriz_2[i, j]
    elif op == 2:
        for i in range(n):
            for j in range(n):
                matriz_respuesta[i, j] = matriz_2[i, j] - matriz_1[i, j]
    return matriz_respuesta

def multiplicacion_de_matrices(n, matriz_1, matriz_2, matriz_respuesta, op):

    """utiliza el índice de la matriz respuesta que es cero al comienzo, y le suma el resultado dado
    al multiplicar la matriz 1 y matriz 2 en el orden dado por el usuario, posterior a esto
    retorna una matriz respuesta con el resultado"""

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if op == 1:
                    matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_1[i, k] * matriz_2[k, j]
                elif op == 2:
                    matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_2[i, k] * matriz_1[k, j]
    return matriz_respuesta

def transpuesta(n, matriz, matriz_respuesta):

    """realiza la transposición de la matriz 1 o 2 según la opción que el usuario
    haya digitado"""

    for i in range(n):
        for j in range(n):
            matriz_respuesta[i, j] = matriz[j, i]
    return matriz_respuesta

def main():
    operacion = 0
    while operacion != 8:

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
            print("8) Salir del programa")
            print("9) Graficar matrices")
            

            operacion = solicitar_entrada_operacion()

            borrar_pantalla()
            matriz_respuesta = np.zeros((n, n))

            if operacion == 1:
                print(suma_de_matrices(n, matriz_1, matriz_2, matriz_respuesta), "\n")
                
            
                    

            if operacion == 2:
                print("1) Calcular matriz 1 - matriz 2")
                print("2) Calcular matriz 2 - matriz 1")
                op = int(input("Ingrese la operacion que desee realizar: "))

                print(resta_de_matrices(n, matriz_1, matriz_2, matriz_respuesta, op), "\n")

            if operacion == 3:
                print("1) Calcular matriz 1 x matriz 2")
                print("2) Calcular matriz 2 x matriz 1")
                op = int(input("Introduzca la opción que desea: "))

                print(multiplicacion_de_matrices(n, matriz_1, matriz_2, matriz_respuesta, op), "\n")

            if operacion == 4:
                print(transpuesta(n, matriz_1, matriz_respuesta), "\n")

            if operacion == 5:
                print(transpuesta(n, matriz_2, matriz_respuesta), "\n")

            if operacion == 6:
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

            if operacion == 7:
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

            if operacion == 9:    
                Graficar_matrices.main(n, matriz_1, matriz_2)
            
main()
