import numpy as np
import os
import Graficar_matrices

def Crear_contrasenia(user):
    def numero_primo(numero):
        if numero == 1:
            primo = 0
        elif numero == 2:
            primo = 1
        elif numero % 2 == 0:
            primo = 0
        else:
            i = 3
            primo = 1
        while i < numero:
            if numero % i == 0:
                primo = 0
                break
            else:
                i = i + 2
        return primo

    def cadena_a_lista(cadena):
        return cadena.split()

    def eliminar_signos(lista_palabras, num_palabras):
        for i in range(num_palabras):
            longitud_palabra = len(lista_palabras[i])
            palabra = ""
            for j in range(longitud_palabra):
                cod_ASCII = ord(lista_palabras[i][j])
                if (cod_ASCII >= 65 and cod_ASCII <= 90) or (cod_ASCII >= 97 and cod_ASCII <= 122):
                    palabra += lista_palabras[i][j]
            lista_palabras[i] = palabra
        return lista_palabras

    def peso_palabra(palabra, semilla):
        peso = 0
        longitud_palabra = len(palabra)
        for i in range(longitud_palabra):
            peso += (ord(palabra[i]) * (i + 1)) % semilla
        return peso

    def calcular_checksum(lista_palabras, num_palabras, semilla, limite):
        checksum = 0
        for i in range(num_palabras):
            peso = peso_palabra(lista_palabras[i], semilla)
            checksum = (checksum + peso) * semilla
        if checksum > limite:
            checksum = checksum % limite
        return checksum

    def Crear(cadena):
        semilla = 1151
        limite = 12709007
        if numero_primo(semilla):
            lista_palabras = cadena_a_lista(cadena)
            lista_palabras = eliminar_signos(lista_palabras, len(lista_palabras))
            num_palabras = len(lista_palabras)
            return (calcular_checksum(lista_palabras, num_palabras, semilla, limite))


    creada = str(Crear(user))
    return creada

def solicitar_entrada_usuario():

    while True:
        opc = input("Ingrese la opción que desea realizar\n")
        try:
            opc = int (opc)
            return opc
        except ValueError:
            print ("Por favor ingrese un número entero\n")

def verificar_entrada():

    while True:
        opcion = input("Ingrese la opción que desea realizar\n")
        try:
            opcion = int (opcion)
            return opcion
        except ValueError:
            print ("Por favor ingrese un número entero\n")

def historial():

    while True:
        mostrar = input("Ingrese la opción que desea realizar\n")
        try:
            mostrar = str (mostrar)
            return mostrar
        except ValueError:
            print ("Por favor ingrese 'Si' o 'No'\n")

def imprimir_registro(user):
    f = open("user.txt","r")
    text = f.read()
    print(text)
    f.close()

def verificar_contrasenia(user, registro_contra):
    print ("Escriba su contraseña\n")
    contrasenia = input()
    if registro_contra == contrasenia:
        print ("¿Quiere ver el historial? (Si/No)")

        mostrar = historial()

        if mostrar == 'Si' or mostrar == 'si' or mostrar == 'SI':
            imprimir_registro(user)
            main()
        elif mostrar == 'No' or mostrar == 'no' or mostrar == 'NO':
            main()
        else:
            print ("Elija una de las opciones disponibles\n")
            verificar_contrasenia

def compr_usuario():

    while True:
        mostrar = input()
        try:
            mostrar = str (mostrar)
            return mostrar
        except ValueError:
            print ("Por favor ingrese una entrada válida")


def adicionar_registro(usuar, matriz_1, matriz_2, matriz_respuesta):
    f = open(usuar + ".txt","a+")
    f.write(matriz_1)
    f.write(matriz_2)
    f.write(matriz_respuesta)
    f.close()

def registrar_usuario(registro_contrasenia):
    print ("Escriba un nombre para su usuario")

    user = compr_usuario()

    if user in registro_contrasenia:
        print ("Escribe otro nombre de usuario")
        registrar_usuario(registro_contrasenia)
    else:
        print ("Esta es su contraseña:")
        creada = Crear_contrasenia(user)
        print (creada)
        print ("Su cuenta ha sido creada con éxito")
        registro_contrasenia[user] = creada
        adicionar_registro(user, '', '', '')
        llave = list(registro_contrasenia)
    registro = open("data.dat","w")
    registro.write(llave[0])
    registro.write(":")
    registro.write(creada)
    registro.close

def comprobar_usuario(registro_contrasenia):
    
    print ("Escriba su nombre de usuario")
    usuario = input()
    if usuario in registro_contrasenia:
        verificar_contrasenia(usuario, registro_contrasenia)
    else:
        print ("1) Escribir de nuevo el usuario")
        print ("2) Registrarse")

        opccion = verificar_entrada()

        if opccion == 1:
            comprobar_usuario(registro_contrasenia)
        
        elif opccion == 2:
            registrar_usuario(registro_contrasenia)
        else:
            print ("Elija una de las opciones disponibles")
            comprobar_usuario(registro_contrasenia)


def entrada_usuario():
    """Solo funciona para registrarse, esto se da correctamente, la opcion de logearse no funciona"""
    print ("1) Iniciar sesión")
    print ("2) Registrarse")

    opc = solicitar_entrada_usuario()

    if opc == 1:
        registro_contrasenia = {}
        registro = open("data.dat","r")
        comprobar_usuario(registro_contrasenia)
    
    elif opc == 2:
        registro_contrasenia = {}
        registrar_usuario(registro_contrasenia)
    
    else:
        print ("Elija una de las opciones disponibles")
        solicitar_entrada_usuario()

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

        print("1) Introducir matrices")
        print("2) Sumar matrices")
        print("3) Restar matrices")
        print("4) Multiplicar matrices")
        print("5) Transpuesta de la matriz")
        print("6) Número menor y mayor de la matriz")
        print("7) Salir del programa")

        try:
            opcion = int(input("Introduzca la opción que desea: "))
        except ValueError:
            borrar_pantalla()
            print("Por favor ingrese un número válido.")
        else:
            return opcion

def dimensiones_matriz(num_matriz):
    dim_matriz = [0, 0]

    while True:
        try:
            dim_matriz[0] = int(input(f"Introduzca valor de filas (i) para la matriz {num_matriz}: "))
            if dim_matriz[0] <= 0:
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
                    dim_matriz[1] = int(input(f"Introduzca valor de filas (j) para la matriz {num_matriz}: "))
                    if dim_matriz[1] <= 0:
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

    return dim_matriz

def crear_matriz(dim_matriz):
    matriz = np.zeros((dim_matriz[0], dim_matriz[1]))

    return matriz

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

def numero_matrices(matrices):
    while True:
        try:
            borrar_pantalla()
            print("Hay disponibles %d matrices." %(len(matrices)))
            num_matriz_1 = int(input("Seleccione matriz 1: "))
            num_matriz_2 = int(input("Seleccione matriz 2: "))
        except ValueError:
            continue
        else:
            break

    return num_matriz_1, num_matriz_2

# Se suman las matrices 1 y 2, y se retorna la matriz respuesta.
def suma_matrices(matriz_1, dim_matriz_1, matriz_2):
    matriz_respuesta = np.zeros((dim_matriz_1[0], dim_matriz_1[1]))

    for i in range(dim_matriz_1[0]):
        for j in range(dim_matriz_1[1]):
                matriz_respuesta[i, j] = matriz_1[i, j] + matriz_2[i, j]

    return matriz_respuesta

# Se restan las matrices 1 y 2 ó 2 y 1 dependiendo de la entrada dada por el usuario,
# y retorna una matriz respuesta, la cual se imprime después.
def resta_matrices(matriz_1, dim_matriz_1, matriz_2):
    matriz_respuesta = np.zeros((dim_matriz_1[0], dim_matriz_1[1]))

    for i in range(dim_matriz_1[0]):
        for j in range(dim_matriz_1[1]):
            matriz_respuesta[i, j] = matriz_1[i, j] - matriz_2[i, j]

    return matriz_respuesta

def multiplicacion_matrices(matriz_1, dim_matriz_1, matriz_2, dim_matriz_2):
    matriz_respuesta = np.zeros((dim_matriz_1[0], dim_matriz_2[1]))

    for i in range(dim_matriz_1[0]):
        for j in range(dim_matriz_2[1]):
            for k in range(dim_matriz_1[1]):
                    matriz_respuesta[i, j] = matriz_respuesta[i, j] + matriz_1[i, k] * matriz_2[k, j]

    return matriz_respuesta

# Función para hallar la matriz transpuesta de la matriz seleccionada.
def transpuesta(matriz, dim_matriz):
    matriz_respuesta = np.zeros((dim_matriz[1], dim_matriz[0]))

    for i in range(dim_matriz[1]):
        for j in range(dim_matriz[0]):
            matriz_respuesta[i, j] = matriz[j, i]

    return matriz_respuesta

def numero_menor_mayor(matriz, dim_matriz, menor, mayor):
    for i in range(dim_matriz[0]):
        for j in range(dim_matriz[1]):
            if menor > matriz[i, j]:
                menor = matriz[i, j]
            if mayor < matriz[i, j]:
                mayor = matriz[i, j]

    return menor, mayor

def opciones_menu(opcion, matrices, matriz_respuesta):
    borrar_pantalla()

    if opcion == 1:
        continuar = True
        num_matriz = 0

        while continuar == True:
            matrices[num_matriz].append(dimensiones_matriz(num_matriz + 1))
            matrices[num_matriz].append(crear_matriz(matrices[num_matriz][0]))

            matrices[num_matriz][1] = llenar_matriz(matrices[num_matriz][0], matrices[num_matriz][1])

            while True:
                op = str(input("¿Desea agregar otra matriz? (Si/No): "))

                if op == "SI" or op == "Si" or op == "si":
                    num_matriz += 1
                    matrices.append([])
                    break
                elif op == "NO" or op == "No" or op == "no":
                    continuar = False
                    break
                else:
                    continue

        return matrices, matriz_respuesta, True

    if opcion == 2:
        matriz_1, matriz_2 = numero_matrices(matrices)

        if matrices[matriz_1 - 1][0] == matrices[matriz_2 - 1][0]:
            matriz_respuesta = suma_matrices(matrices[matriz_1 - 1][1], matrices[matriz_1 - 1][0], matrices[matriz_2 - 1][1])
            print(matriz_respuesta, "\n")
            input("Presione Enter para continuar...")
        else:
            print("Las matrices 1 y 2 no se pueden sumar porque sus dimensiones son diferentes.")

        return matrices, matriz_respuesta, True

    if opcion == 3:
        matriz_1, matriz_2 = numero_matrices(matrices)

        if matrices[matriz_1 - 1][0] == matrices[matriz_2 - 1][0]:
            matriz_respuesta = resta_matrices(matrices[matriz_1 - 1][1], matrices[matriz_1 - 1][0], matrices[matriz_2 - 1][1])
            print(matriz_respuesta, "\n")
            input("Presione Enter para continuar...")
        else:
            print("Las matrices 1 y 2 no se pueden restar porque sus dimensiones son diferentes.")

        return matrices, matriz_respuesta, True

    if opcion == 4:
        matriz_1, matriz_2 = numero_matrices(matrices)

        if matrices[matriz_1 - 1][0][1] == matrices[matriz_2 - 1][0][0]:
            matriz_respuesta = multiplicacion_matrices(matrices[matriz_1 - 1][1], matrices[matriz_1 - 1][0], matrices[matriz_2 - 1][1], matrices[matriz_2 - 1][0])
            print(matriz_respuesta, "\n")
            input("Presione Enter para continuar...")
        else:
            print("Las matrices 1 y 2 no se pueden multiplicar porque el número de columnas")
            print("de la matriz 1 es diferente al número de filas de la matriz 2.")

        return matrices, matriz_respuesta, True

    if opcion == 5:
        while True:
            try:
                borrar_pantalla()
                print("Hay disponibles %d matrices." %(len(matrices)))
                num_matriz_1 = int(input("Seleccione matriz: "))
            except ValueError:
                continue
            else:
                break

        matriz_respuesta = transpuesta(matrices[num_matriz_1 - 1][1], matrices[num_matriz_1 - 1][0])
        print(matriz_respuesta, "\n")
        input("Presione Enter para continuar...")

        return matrices, matriz_respuesta, True

    if opcion == 6:
        while True:
            try:
                borrar_pantalla()
                print("Hay disponibles %d matrices." %(len(matrices)))
                num_matriz_1 = int(input("Seleccione matriz: "))
            except ValueError:
                continue
            else:
                break
        
        menor = matrices[num_matriz_1 - 1][1][0, 0]
        mayor = matrices[num_matriz_1 - 1][1][0, 0]

        menor, mayor = numero_menor_mayor(matrices[num_matriz_1 - 1][1], matrices[num_matriz_1 - 1][0], menor, mayor)
        print("El número menor es " + str(menor) + " y el número mayor es " + str(mayor) + "\n")
        input("Presione Enter para continuar...")

        return matrices, matriz_respuesta, True

    if opcion == 7:
        return matrices, matriz_respuesta, False

def main():
    matrices = [[]]
    matriz_respuesta = "No hay matriz respuesta."

    while True:
        borrar_pantalla()
        opcion = menu()
        matrices, matriz_respuesta, continuar = opciones_menu(opcion, matrices, matriz_respuesta)

        if continuar == False:
            break

main()
