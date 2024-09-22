

def acceder_a_lista():
    lista = [2, 6, 10, 4, 5, 23, 1]

    try:
        valor = lista[10]

    except IndexError:
        print("Error: El índice que estás intentando acceder no existe en la lista.")
        print("Causa: La lista tiene solo 7 elementos (índices de 0 a 6), pero estás intentando acceder al índice 10.")
        print("Solución: Asegúrate de usar un índice válido dentro del rango de la lista.")

    except TypeError:
        print("Error: El índice debe ser un número entero.")
        print("Causa: Estás intentando acceder a la lista con un índice de tipo no entero.")
        print("Solución: Asegúrate de que el índice sea un número entero válido.")

    else:
        print("El valor en el índice 10 es: {}".format(valor))

acceder_a_lista()