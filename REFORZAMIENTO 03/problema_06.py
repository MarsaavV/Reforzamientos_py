
mi_lista = [3.14, 1.618, True, False, 2.71, True]


penultimo_valor = mi_lista[-2]
ultimo_valor = mi_lista[-1]

print(f"Penúltimo valor: {penultimo_valor}")
print(f"Último valor: {ultimo_valor}")


print("\nElementos y sus tipos en la lista:")
for item in mi_lista:
    print(f"Elemento: {item}, Tipo: {type(item)}")