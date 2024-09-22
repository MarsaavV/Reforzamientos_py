
import random

def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(30)]
    print("Lista generada de números aleatorios:", numeros)
    return numeros

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)
    return lista_ordenada

def obtener_mayor(lista):
    mayor = max(lista)
    print(f"El número mayor de la lista es: {mayor}")
    return mayor
