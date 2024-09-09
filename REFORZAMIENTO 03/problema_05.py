
lista_desordenada = [5, "Banana", 2.5, "Manzana", 10, "Cereza", 3.14, "Durazno", 1]


print("Lista desordenada:")
print(lista_desordenada)


numeros = [item for item in lista_desordenada if isinstance(item, (int, float))]
numeros.sort()

cadenas = [item for item in lista_desordenada if isinstance(item, str)]
cadenas.sort()


lista_ordenada = numeros + cadenas

print("\nLista ordenada:")
print(lista_ordenada)