
def suma_con_excepcion():
    try:

        suma = 80 + "Hola Pythonista"

    except TypeError:

        print("Error: No se puede sumar un número entero con una cadena de texto.")
        print("Causa: Estás intentando sumar un entero (80) con una cadena ('Hola Pythonista').")
        print("Solución: Convierte ambos valores al mismo tipo de datos (por ejemplo, convierte el entero a cadena).")

    else:
        print("El resultado de la suma es: {}".format(suma))


suma_con_excepcion()