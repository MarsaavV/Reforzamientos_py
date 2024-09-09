
"""PROBLEMA 02"""

cursos = [
    "Lenguaje",
    "Microeconomia",
    "Matemática",
    "Investigacion academica",
    "Estadistica",
    "Macroeconomia"
]

cursos.append("Lenguaje")
cursos.append("Microeconomia")
cursos.append("Matemática")
cursos.append("Investigacion academica")

cursos.remove("Estadistica")
cursos.remove("Macroeconomia")

print("Lista final de cursos:")
for curso in cursos:
    print(f"- {curso}")

total_cursos = len(cursos)
print(f"\nCantidad total de cursos: {total_cursos}")