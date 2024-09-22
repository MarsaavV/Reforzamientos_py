
import math

def cargar_valor():
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Error: Solo se permite ingresar valores enteros. Inténtelo de nuevo.")

def mostrar_raiz_cuadrada(valor):
    raiz = math.sqrt(valor)
    print("La raíz cuadrada de {} es: {}".format(valor, raiz))

def calcular_potencias(valor):
    potencias = {
        'cuadrado': valor ** 2,
        'cubo': valor ** 3
    }
    print("El valor {} elevado al cuadrado es: {}".format(valor, potencias['cuadrado']))
    print("El valor {} elevado al cubo es: {}".format(valor, potencias['cubo']))
    return potencias
