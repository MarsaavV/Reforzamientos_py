
"""PROBLEMA 01"""

cursos = [
    "Lenguaje",
    "Microeconomia",
    "Matemática",
    "Investigacion academica",
    "Estadistica",
    "Macroeconomia"
]

print("Lista de cursos:")
for curso in cursos:
    print(f"- {curso}")

cursos_invertidos = cursos[::-1]

print("\nLista de cursos invertida:")
for curso in cursos_invertidos:
    print(f"- {curso}")