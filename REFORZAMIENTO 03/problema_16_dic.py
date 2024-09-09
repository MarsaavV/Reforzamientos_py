while True:
    try:
        cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        if cantidad_alumnos > 0:
            break
        else:
            print("La cantidad de alumnos debe ser un número entero positivo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


alumnos_notas = {}


for i in range(cantidad_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {nombre}: "))
            if 0 <= nota <= 20:
                break
            else:
                print("La nota debe estar entre 0 y 20. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido para la nota.")


    alumnos_notas[nombre] = nota


total_notas = sum(alumnos_notas.values())
media_notas = total_notas / cantidad_alumnos


print("\nInformación de los alumnos:")
for alumno, nota in alumnos_notas.items():
    print(f"{alumno} tiene la nota de {nota}")

print(f"\nLa media de todas las notas es: {media_notas:.2f}")