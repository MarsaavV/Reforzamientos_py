while True:
    try:
        tamaño_lista = int(input("Ingrese el tamaño de la lista de compañías: "))
        if tamaño_lista >= 5:
            break
        else:
            print("El tamaño mínimo de la lista debe ser 5.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

compañias = []

print(f"Ingrese los nombres de {tamaño_lista} compañías relacionadas con TI:")
for i in range(tamaño_lista):
    nombre_compañia = input(f"Ingrese el nombre de la compañía {i + 1}: ")
    compañias.append(nombre_compañia)

compañias_copia = compañias.copy()

print("\nAgregando nombres repetidos a la lista copia...")
for i in range(tamaño_lista // 2):
    nombre_repetido = compañias[i]
    compañias_copia.append(nombre_repetido)

compañias_sin_repetir = list(set(compañias_copia))

print("\nLista original de compañías:")
for compañia in compañias:
    print(f"- {compañia}")

print("\nLista de compañías sin nombres repetidos:")
for compañia in compañias_sin_repetir:
    print(f"- {compañia}")