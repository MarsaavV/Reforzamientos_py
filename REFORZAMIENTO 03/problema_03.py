
"""PROBLEMA 03"""

cursos = [
    "Lenguaje",
    "Microeconomia",
    "Matemática",
    "Investigacion academica",
    "Estadistica",
    "Macroeconomia"
]


cursos.append("Lenguaje")

curso_a_contar = "Lenguaje"
cantidad_repeticiones = cursos.count(curso_a_contar)


print(f"El curso '{curso_a_contar}' se repite {cantidad_repeticiones} veces en la lista.")
del cursos[0]
print("\nLista final de cursos después de eliminar el primer ítem:")
for curso in cursos:
    print(f"- {curso}")
total_cursos = len(cursos)
print(f"\nCantidad total de cursos: {total_cursos}")