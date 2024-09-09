while True:
    try:
        tamaño_lista = int(input("Ingrese el tamaño de la lista de nombres de alumnos: "))
        if tamaño_lista > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


nombres_alumnos = []


print(f"Ingrese los nombres de {tamaño_lista} alumnos:")
for i in range(tamaño_lista):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nombres_alumnos.append(nombre)


print(f"\nTamaño de la lista: {len(nombres_alumnos)}")
print("Nombres de los alumnos ingresados:")
for nombre in nombres_alumnos:
    print(f"- {nombre}")